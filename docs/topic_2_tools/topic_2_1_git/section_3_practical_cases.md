---
authors: Daniel Bazo Correa
description: Automatización con Git Hooks y soluciones a escenarios frecuentes en Git.
title: Hooks y casos prácticos
---

## Referencias

- [Git Hooks](https://githooks.com/)

## Introducción

Más allá de las estrategias de ramificación, el uso eficaz de Git requiere conocer los
mecanismos que permiten automatizar tareas dentro del flujo de trabajo y resolver
situaciones habituales que surgen durante la gestión del historial de un repositorio.
Estos aspectos prácticos resultan fundamentales para mantener la calidad del código,
garantizar la coherencia del proyecto y facilitar la colaboración en equipos de
cualquier tamaño.

## Git Hooks

Los **Git Hooks** son una funcionalidad integrada en Git que permite automatizar tareas
y aplicar políticas a lo largo del flujo de trabajo. Gracias a ellos, Git puede ejecutar
acciones en momentos clave del proceso de desarrollo, asegurando la calidad del código y
el cumplimiento de políticas específicas del proyecto.

### Funcionamiento

Los Git Hooks son scripts que se ejecutan automáticamente en respuesta a eventos
específicos dentro de Git, como antes o después de realizar un _commit_, un _push_ o un
_merge_.

Para utilizar Git Hooks, es necesario crear scripts en el directorio `.git/hooks`,
ubicado en la raíz del repositorio Git. Por defecto, al crear un nuevo repositorio, Git
proporciona una serie de _hooks_ de ejemplo que pueden modificarse según las necesidades
del proyecto.

Estos scripts deben ser ejecutables y deben llevar el nombre del evento para el que se
activan, como `pre-commit`, `pre-push` o `post-merge`. Para asegurarse de que tienen los
permisos adecuados (permisos de ejecución), se puede utilizar el siguiente comando:

???+ example "Ejemplo"

    ```bash linenums="1"
    chmod +x pre-commit
    ```

Una vez ubicados en el directorio correcto y con los permisos necesarios, Git ejecutará
automáticamente estos scripts cuando ocurra el evento correspondiente.

Al desarrollar y administrar Git Hooks, es esencial seguir ciertas pautas que aseguren
su eficacia y mantengan un flujo de trabajo ordenado. En primer lugar, los hooks deben
ser rápidos y confiables, de manera que su ejecución no interfiera con la productividad
del equipo ni genere demoras en los procesos habituales de desarrollo. Asimismo, se
recomienda evitar que los hooks realicen cambios automáticos en el código sin la
aprobación explícita del desarrollador, ya que estas modificaciones pueden provocar
conflictos, errores inesperados o dificultades en la integración del código.

### Tipos de Git Hooks

A continuación se describen los tipos de hooks más comunes:

#### pre-commit

Se ejecuta antes de realizar un _commit_. Es útil para verificar el formato del código,
ejecutar pruebas unitarias, validar los mensajes de _commit_ o evitar errores
ortográficos.

???+ example "Ejemplo"

    Verificación de estilo con Black en la rama `main`.

    ```bash linenums="1"
    #!/bin/bash
    # Hook pre-commit para ejecutar Black solo en la rama main

    # Obtener la rama actual
    branch_name=$(git rev-parse --abbrev-ref HEAD)

    # Verificar si estamos en la rama main
    if [ "$branch_name" != "main" ]; then
        echo "No se ejecutará Black porque no estás en la rama 'main'."
        exit 0
    fi

    # Ejecutar Black en el directorio actual
    black . --check

    # Verificar el estado de la última operación
    if [ $? -ne 0 ]; then
        echo "Errores de estilo detectados. Bloqueando el commit."
        exit 1
    fi

    echo "El commit se ha completado con éxito."
    ```

#### pre-push

Se ejecuta antes de enviar cambios a un repositorio remoto. Se emplea para evitar
_pushes_ en ramas protegidas o para ejecutar pruebas antes de subir los cambios.

???+ example "Ejemplo"

    Instalación de dependencias y ejecución de pruebas con Poetry.

    ```bash linenums="1"
    #!/bin/bash
    # Hook pre-push para actualizar pip, instalar Poetry, instalar dependencias y ejecutar pruebas

    # Actualizar pip
    echo "Actualizando pip..."
    python -m pip install --upgrade pip

    # Instalar Poetry si no está instalado
    if ! command -v poetry &> /dev/null; then
        echo "Instalando Poetry..."
        pip install poetry
    fi

    # Verificar si Poetry se instaló correctamente
    if ! command -v poetry &> /dev/null; then
        echo "Error: Poetry no se pudo instalar."
        exit 1
    fi

    # Instalar dependencias de Poetry
    echo "Instalando dependencias de Poetry..."
    poetry install

    # Ejecutar pruebas con Pytest
    echo "Ejecutando pruebas con Pytest..."
    poetry run pytest -v ./tests

    # Verificar el estado de las pruebas
    if [ $? -ne 0 ]; then
        echo "Error: Las pruebas no han pasado. Bloqueando el push."
        exit 1
    fi

    echo "El push se ha completado con éxito."
    ```

#### post-commit

Se ejecuta después de realizar un _commit_. Puede utilizarse para enviar notificaciones
automáticas al equipo.

???+ example "Ejemplo"

    Notificación por correo tras un commit.

    ```bash linenums="1"
    #!/bin/bash
    # Hook post-commit para enviar una notificación por correo

    # Obtener el mensaje del último commit
    commit_message=$(git log -1 --pretty=%B)

    # Enviar un correo electrónico (usando sendmail como ejemplo)
    echo "Nuevo commit realizado: $commit_message" | sendmail -v equipo@example.com
    ```

#### post-merge

Se ejecuta después de completar un _merge_. Es útil para actualizar dependencias o
regenerar documentación.

???+ example "Ejemplo"

    Actualización de dependencias con Poetry.

    ```bash linenums="1"
    #!/bin/bash
    # Hook post-merge para actualizar dependencias con Poetry

    # Verificar si Poetry está instalado
    if ! command -v poetry &> /dev/null; then
        echo "Poetry no está instalado. Instalándolo..."
        pip install poetry
    fi

    # Actualizar las dependencias
    echo "Actualizando dependencias de Poetry..."
    poetry update

    # Ejecutar pruebas para verificar que todo funciona correctamente
    echo "Ejecutando pruebas con Pytest..."
    poetry run pytest -v ./tests

    # Verificar el estado de las pruebas
    if [ $? -ne 0 ]; then
        echo "Error: Las pruebas no han pasado. Verifica los errores."
        exit 1
    fi

    echo "El post-merge se ha completado con éxito."
    ```

#### pre-receive y post-receive

Estos _hooks_ se ejecutan en el servidor remoto al recibir cambios mediante _push_.

En el caso de **pre-receive**, se usa para validar que los _commits_ cumplan con las
políticas del proyecto antes de aceptarlos.

???+ example "Ejemplo"

    Bloquear _pushes_ con mensajes de _commit_ incorrectos.

    ```bash linenums="1"
    #!/bin/bash
    # Hook pre-receive para validar mensajes de commit

    while read oldrev newrev refname; do
        for commit in $(git rev-list $oldrev..$newrev); do
            commit_message=$(git log --format=%B -n 1 $commit)
            if ! [[ $commit_message =~ ^\[JIRA-[0-9]+\] ]]; then
                echo "El mensaje de commit '$commit_message' no cumple con el formato requerido."
                exit 1
            fi
        done
    done
    ```

Mientras que **post-receive**, se emplea para realizar despliegues automáticos en
producción.

???+ example "Ejemplo"

    Despliegue automático tras recibir un _push_.

    ```bash linenums="1"
    #!/bin/bash
    # Hook post-receive para desplegar automáticamente el código en producción

    echo "Desplegando cambios en producción..."

    # Cambiar al directorio de producción
    cd /var/www/mi-aplicacion

    # Obtener la última versión del código
    git pull origin main

    # Reiniciar el servidor web para aplicar cambios
    pm2 restart mi-aplicacion
    ```

## Escenarios frecuentes

En el desarrollo con Git es habitual necesitar manipular la historia de _commits_ o
sincronizar el repositorio local con el remoto. A continuación se presentan soluciones
claras y seguras para los escenarios más frecuentes.

### Gestionar _commits_ no firmados

Para garantizar la autenticidad de los _commits_, existen varias estrategias en función
de la situación del repositorio. Si los _commits_ existentes son válidos en cuanto a su
contenido pero carecen de firma criptográfica, es posible recrearlos de forma que
incorporen la firma sin alterar los cambios que contienen:

???+ example "Ejemplo: Firmar todos los _commits_"

    ```bash linenums="1"
    git rebase --root --exec 'git commit --amend --no-edit -S'
    git push --force-with-lease
    ```

Si el repositorio requiere firmas GPG y has añadido _commits_ sin firmar, se producirá
un error al intentar subirlos. Para solucionarlo, puedes reescribir el historial y
firmar los _commits_ existentes sin perder los cambios:

???+ example "Ejemplo: Reescribir historial eliminando _commits_ no firmados"

    ```bash linenums="1"
    git log --pretty="%h %G?"   # Identifica commits no firmados (N)
    git checkout -b rama-limpia
    git rebase -i --root        # Marca con 'drop' los commits N en el editor
    git push --force-with-lease origin rama-limpia
    ```

Otra alternativa es restablecer la rama a un _commit_ firmado determinado:

???+ example "Ejemplo: Restablecer a un _commit_ firmado"

    ```bash linenums="1"
    git reset --hard <commit_firmado>
    git push --force-with-lease
    ```

### Sincronizar repositorio local con el remoto

Para sincronizar la rama local exactamente con la remota, descartando cualquier cambio
local y archivos sin seguimiento, utiliza el siguiente comando.

!!! warning "Advertencia"

    Esta operación es irreversible y eliminará cualquier trabajo que no haya sido
    subido al repositorio.

???+ example "Ejemplo: Sincronizar con reset"

    ```bash linenums="1"
    git fetch origin && git reset --hard origin/main && git clean -fd
    ```

Si prefieres eliminar y recrear la rama local por completo para asegurar una copia
limpia desde el servidor, puedes seguir estos pasos:

???+ example "Ejemplo: Recrear rama local"

    ```bash linenums="1"
    git checkout main
    git branch -D nombre-rama
    git checkout -b nombre-rama origin/nombre-rama
    ```

### Eliminar ramas locales que ya no existen en remoto

Con el tiempo, el repositorio local tiende a acumular ramas que ya no existen en el
remoto, por ejemplo tras su eliminación en el servidor una vez completada la
integración. Esta acumulación dificulta la gestión del entorno local y puede generar
confusión sobre el estado real del proyecto. Para mantener un espacio de trabajo limpio,
es posible eliminar de forma automática todas las ramas locales cuyo remoto de
seguimiento ha dejado de existir:

???+ example "Ejemplo: Eliminar ramas locales obsoletas"

    ```bash linenums="1"
    git fetch --prune && git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D
    ```

    Donde:

    - **`git fetch --prune`**: Actualiza las referencias remotas y elimina las que ya no
      existen en el remoto.
    - **`git branch -vv`**: Lista las ramas locales con información detallada, incluyendo si
      siguen a una rama remota (tracking).
    - **`grep ': gone]'`**: Filtra las ramas cuyo remoto de seguimiento ya no existe
      (aparecen marcadas como `gone`).
    - **`awk '{print $1}'`**: Extrae únicamente el nombre de la rama local.
    - **`xargs git branch -D`**: Elimina esas ramas localmente.

Ten en cuenta que `-D` fuerza el borrado aunque la rama no esté mergeada. Si prefieres
un borrado seguro (solo si está fusionada), usa `-d`:

???+ example "Ejemplo: Borrado seguro"

    ```bash linenums="1"
    git fetch --prune && git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -d
    ```

También, como recomendación, conviene revisar primero qué ramas se van a eliminar
ejecutando únicamente el siguiente comando antes de proceder al borrado:

???+ example "Ejemplo: Revisar ramas a eliminar"

    ```bash linenums="1"
    git branch -vv | grep ': gone]'
    ```
