---
authors: Daniel Bazo Correa
description: Control de versiones con Git.
title: Git
---

## Bibliografía

- [Git](https://git-scm.com/)
- [Git Hooks](https://githooks.com/)
- [Learning Git: A Hands-On and Visual Guide to the Basics of Git](https://www.oreilly.com/library/view/learning-git/9781098133900/)
- [Ship / Show / Ask, A modern branching strategy](https://martinfowler.com/articles/ship-show-ask.html)

## Introducción

<p align="center">  
  <img src="../../assets/img/docs/logos/git-logo.png"/>  
  <br />  
  <em>Logo de Git</em>  
</p>

**Git** es un sistema de control de versiones que permite gestionar el historial de
cambios en proyectos de software. Facilita la colaboración entre desarrolladores, el
seguimiento de modificaciones en el código y la administración de distintas versiones del
código a lo largo del tiempo. Al igual que el _kernel_ de Linux, fue desarrollado
inicialmente por Linus Torvalds.

Plataformas como **GitHub** o **GitLab** utilizan Git para facilitar la gestión de
proyectos y la colaboración en línea, ofreciendo interfaces gráficas y funcionalidades
adicionales como la integración continua.

## Control de versiones

El **control de versiones** es una herramienta que permite gestionar los cambios en
archivos a lo largo del tiempo, facilitando la recuperación de versiones anteriores
cuando sea necesario.

Puede entenderse como un sistema de **etiquetas de cambios**, cada vez que se guarda un
cambio mediante un _commit_ en Git, se genera un **identificador único** que registra el
estado exacto de los archivos en ese momento. Esto permite consultar, comparar o
restaurar versiones anteriores de manera segura y organizada.

### Terminología

- **Repositorio local**: Espacio en el ordenador donde se almacenan todos los archivos de
  un proyecto y sus versiones anteriores. Git permite hacer un seguimiento de los cambios
  en estos archivos sin necesidad de conexión a internet.

- **Repositorio remoto**: Copia del repositorio local almacenada en internet o en una red
  externa. Plataformas como GitHub, GitLab o Bitbucket permiten que varias personas
  trabajen en el mismo proyecto desde diferentes ubicaciones.

- **Histórico (_Log_)**: Registro que muestra todos los cambios realizados en el proyecto
  a lo largo del tiempo. Cada vez que se guarda un cambio en Git (un **_commit_**), queda
  registrado en este historial con información como la fecha, el autor del cambio y una
  descripción de lo modificado. También se conoce como **_Commit History_**, siendo el
  lugar donde se almacenan todos los **_commits_** realizados.

- **Conflicto**: Situación que ocurre cuando Git no puede combinar automáticamente los
  cambios de diferentes personas en un mismo archivo. Por ejemplo, si dos personas editan
  la misma línea de un archivo y luego intentan guardar sus cambios en el repositorio
  remoto, Git no puede determinar qué versión debe mantener y marca un conflicto. En ese
  caso, es necesario revisar y decidir manualmente qué cambios conservar.

### Áreas de trabajo

<p align="center">  
  <img src="../../assets/img/docs/git-stages.png"/>  
  <br />  
  <em>Áreas de trabajo en Git. [Link](https://ihcantabria.github.io/ApuntesGit/_images/comandos-workflow.png)</em>  
</p>

En Git existen dos partes esenciales para el manejo de repositorios: el repositorio
local, que se encuentra en tu ordenador, y el repositorio remoto, que se ubica en un
servidor externo como GitHub, GitLab o Bitbucket.

Dentro del sistema Git se distinguen diferentes áreas:

1. **_Working Directory_**: Es el directorio de trabajo donde se modifican los archivos.
   Cuando se añaden nuevos archivos en esta área, para Git están en estado _untracked_
   (sin seguimiento) hasta que se añadan explícitamente.

2. **_Staging Area_**: Funciona como un espacio de borrador donde se preparan los cambios
   para el siguiente _commit_. Se representa físicamente mediante un fichero llamado
   `index` dentro de la carpeta `.git` en la raíz del repositorio. Los archivos añadidos
   a esta área pasan a estar _tracked_ (con seguimiento).

3. **_Commit History_**: Área donde se almacenan todas las versiones confirmadas del
   proyecto.

4. **_Local Repository_**: Contiene toda la información del proyecto y su historial de
   cambios a nivel local.

El flujo de trabajo típico consiste en modificar archivos en el _Working Directory_,
añadirlos al _Staging Area_ mediante `git add`, confirmarlos al _Commit History_ con
`git commit` y finalmente subirlos al repositorio remoto con `git push`.

### Estados de un archivo

Durante el ciclo de vida en Git, un archivo puede pasar por diferentes estados:

1. **Sin seguimiento (_Untracked_)**: El archivo es nuevo y Git aún no lo está
   rastreando. No se guarda en el historial del repositorio hasta que se agregue
   manualmente con `git add`.

2. **Ignorado (_Ignored_)**: Archivos como configuraciones personales o temporales pueden
   estar en una lista especial llamada `.gitignore`. Git los omite y no los agrega al
   repositorio.

3. **Modificado (_Modified_)**: El archivo ha sido editado después de su última
   confirmación (_commit_), pero esos cambios aún no han sido registrados en Git.

4. **Preparado (_Staged_)**: Una vez que el archivo modificado se agrega con `git add`,
   entra en estado _staged_. Esto significa que está listo para ser guardado en la
   próxima confirmación.

5. **Confirmado (_Committed_)**: Cuando se ejecuta `git commit`, los cambios preparados
   se guardan en la base de datos de Git, registrándolos en el historial del repositorio
   de manera permanente.

## Git

### Comandos básicos para Git Bash

**Git Bash** es una interfaz de línea de comandos (también conocido como **CLI** de
_Command-line Interface_) que permite la interacción con Git mediante el uso de comandos
de Linux.

Si quieres conocer sobre estos comandos y lo básico sobre Linux, puedes dirigirte a este
[apartado](docs/capt_1_operative_systems/topic_1_linux.md).

### Configuración de Git

Antes de comenzar a trabajar con plataformas como GitHub o GitLab, es imprescindible
configurar correctamente el entorno local de Git. Esta configuración incluye, entre otros
aspectos, la identidad del autor de los _commits_ y ciertos parámetros de comportamiento
global.

Mediante el comando `git config --global --list` es posible consultar todas las variables
definidas en la configuración global de Git junto con sus valores. Esta configuración se
utiliza, entre otros fines, para establecer el nombre de usuario y la dirección de correo
electrónico que quedarán asociados a cada _commit_.

#### Configurar nombre de usuario y correo

Git utiliza el nombre y el correo configurados para identificar tus contribuciones.
Puedes configurarlos globalmente para que se apliquen a todos tus repositorios utilizando
los siguientes comandos:

```bash linenums="1"
git config --global user.name "Tu Nombre"
git config --global user.email "tu-correo@example.com"
```

Para verificar la configuración, puedes utilizar:

```bash linenums="1"
git config --global --list
```

Si deseas configurarlos solo para un repositorio específico, omite la opción `--global` y
ejecuta los comandos dentro del directorio del repositorio.

#### Configurar autenticación SSH para GitHub/GitLab

Configurar claves SSH simplifica la autenticación con GitHub/GitLab.

Para ello, genera una clave SSH si no tienes una, utilizando el siguiente comando:

```bash linenums="1"
ssh-keygen -t ed25519 -C "<EMAIL_ADDRESS>"
```

Si tu sistema no soporta `ed25519`, usa:

```bash linenums="1"
ssh-keygen -t rsa -b 4096 -C "<EMAIL_ADDRESS>"
```

Copia la clave pública generada:

```bash linenums="1"
cat ~/.ssh/id_ed25519.pub
```

Ve a tu cuenta de GitHub o GitLab, accede a **Settings** > **SSH and GPG keys** (o
similar), y añade la clave pública copiada.

Finalmente, puedes probar la conexión utilizando el siguiente comando:

```bash linenums="1"
ssh -T git@github.com
```

En el caso de utilizar GitLab puedes utilizar este otro comando:

```bash linenums="1"
ssh -T git@gitlab.com
```

#### Configurar autenticación con tokens personales

Si prefieres usar HTTPS en lugar de SSH, puedes crear un token personal de acceso en
GitHub/GitLab y usarlo como contraseña al clonar o realizar _push_. Para configurarlo:

1. Ve a **Settings** > **Developer Settings** > **Personal Access Tokens**.
2. Genera un token con los permisos necesarios.
3. Al realizar una operación que requiera autenticación, usa tu usuario como nombre de
   usuario y el token como contraseña.

### Comandos para el control de versiones

Un comando de Git se compone de tres elementos fundamentales: el programa principal
(`git`), el comando que define la acción concreta que se desea realizar y, de forma
opcional, una serie de opciones y argumentos que ajustan su comportamiento.

???+ example "Ejemplo"

    ```
    git commit -m "Esto es un commit"
    ```

    En este caso, `git commit` define la acción de confirmar cambios, `-m` es una opción que
    permite añadir un mensaje descriptivo y `"Esto es un commit"` es el argumento asociado a
    dicha opción.

A continuación se describen los comandos más relevantes para la gestión del control de
versiones en un repositorio Git a nivel local.

| Comando                | Función                                                                                                                                                                                                           | Ejemplo de uso                                                                                             |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **git init**           | Inicializa un repositorio Git en el directorio actual, creando la carpeta oculta `.git` que contiene toda la información necesaria para el control de versiones. Por defecto, la rama principal creada es `main`. | `git init` inicializa un repositorio en la carpeta actual.                                                 |
| **git remote**         | Gestiona las conexiones entre el repositorio local y uno o varios repositorios remotos. Permite añadir, eliminar o listar repositorios remotos.                                                                   | `git remote add origin url_repo` asocia el repositorio remoto con el alias `origin`.                       |
| **git clone**          | Crea una copia local completa de un repositorio existente, incluyendo su historial de commits y ramas.                                                                                                            | `git clone https://github.com/usuario/repositorio.git` clona el repositorio indicado.                      |
| **git add**            | Añade cambios al área de preparación (_staging area_). Git no mueve los archivos, sino que registra una instantánea de su estado actual.                                                                          | `git add archivo.txt` prepara el archivo para el próximo commit.                                           |
| **git commit**         | Registra de forma permanente los cambios preparados en el historial del repositorio local.                                                                                                                        | `git commit -m "Mensaje del commit"` crea un commit con un mensaje descriptivo.                            |
| **git commit --amend** | Modifica el último commit, permitiendo cambiar el mensaje o añadir nuevos cambios al mismo commit. Resulta útil para corregir errores recientes.                                                                  | `git commit --amend` reabre el último commit para modificarlo.                                             |
| **git reset HEAD**     | Revierte la preparación de archivos que habían sido añadidos al área de preparación, sin perder los cambios en el directorio de trabajo.                                                                          | `git reset HEAD archivo.txt` saca el archivo del área de preparación.                                      |
| **git status**         | Muestra el estado actual del repositorio, indicando qué archivos han sido modificados, cuáles están preparados y cuáles no están siendo seguidos.                                                                 | `git status` muestra un resumen del estado del repositorio.                                                |
| **git checkout**       | Permite cambiar entre ramas o restaurar archivos a su último estado confirmado. En versiones recientes de Git, se recomienda `git switch` para cambiar de rama.                                                   | `git checkout rama-nueva` cambia a otra rama.<br />`git checkout -- archivo.txt` descarta cambios locales. |
| **git branch**         | Gestiona las ramas locales, permitiendo listarlas, crearlas o eliminarlas.                                                                                                                                        | `git branch` lista las ramas.<br />`git branch rama-nueva` crea una nueva rama.                            |
| **git merge**          | Fusiona los cambios de una rama en la rama actual, integrando sus commits en el historial.                                                                                                                        | `git merge rama-nueva` fusiona `rama-nueva` en la rama actual.                                             |
| **git fetch**          | Descarga información actualizada del repositorio remoto sin modificar la rama local ni el directorio de trabajo. Permite inspeccionar cambios antes de integrarlos.                                               | `git fetch origin` descarga los cambios del remoto `origin`.                                               |
| **git fetch --prune**  | Descarga los cambios del repositorio remoto y elimina las referencias locales a ramas remotas que ya no existen. Es fundamental para evitar acumulación de ramas obsoletas.                                       | `git fetch --prune` limpia referencias a ramas remotas eliminadas.                                         |
| **git pull**           | Combina `git fetch` y `git merge` en un solo comando, descargando y fusionando los cambios del repositorio remoto con la rama actual.                                                                             | `git pull origin main` actualiza la rama local `main`.                                                     |
| **git push**           | Envía los commits locales al repositorio remoto, haciendo públicos los cambios confirmados.                                                                                                                       | `git push origin main` sube los commits a la rama `main` remota.                                           |
| **git log**            | Muestra el historial de commits del repositorio, permitiendo analizar la evolución del proyecto.                                                                                                                  | `git log` muestra el historial completo.<br />`git log --oneline` muestra un resumen compacto.             |
| **git diff**           | Muestra las diferencias entre archivos en distintos estados, como entre el directorio de trabajo y el último commit o entre commits concretos.                                                                    | `git diff` muestra los cambios no confirmados.                                                             |
| **git stash**          | Guarda temporalmente los cambios no confirmados y limpia el directorio de trabajo, permitiendo cambiar de contexto sin perder trabajo.                                                                            | `git stash` guarda los cambios.<br />`git stash pop` los recupera.                                         |
| **git rm**             | Elimina archivos del repositorio y del área de preparación, registrando la eliminación para el próximo commit.                                                                                                    | `git rm archivo.txt` elimina el archivo del control de versiones.                                          |
| **git rebase**         | Reaplica commits sobre una base distinta, manteniendo un historial lineal. Es especialmente útil para actualizar ramas con respecto a la rama principal.                                                          | `git rebase main` reaplica los commits actuales sobre `main`.                                              |
| **git clean**          | Elimina archivos no rastreados del directorio de trabajo. Debe usarse con precaución, ya que borra archivos de forma permanente.                                                                                  | `git clean -f` elimina archivos no rastreados.                                                             |

## Estrategias para el control de versiones

### Ramas

Las estrategias relacionadas con Git están estrechamente vinculadas con la forma en que
se crean, desarrollan y combinan las diferentes ramas dentro de un mismo repositorio. El
uso de ramas permite trabajar en un mismo proyecto de diferentes maneras y facilita que
distintas personas colaboren en un proyecto simultáneamente.

Una de las metodologías más básicas o estándares de Git consiste en utilizar una rama
principal conocida como `main` o `master`, que es la que se lleva a producción y debe
estar siempre disponible. Adicionalmente, se cuenta con una rama de desarrollo (`dev`)
que incorpora las nuevas características o funcionalidades que posteriormente se añadirán
a la rama principal. A partir de estas, es posible crear diferentes subramas que permiten
implementar cada característica por separado, aunque esto dependerá de la metodología de
trabajo utilizada.

En Git existe el concepto de `HEAD`, un puntero que indica la rama que se está utilizando
y apunta a un _commit_ específico. Es posible encontrarse en un _commit_ que no está
siendo apuntado por una rama, situación conocida como **_Detached HEAD State_**.

Tanto **_Trunk-Based Development_** como **_Git Flow_** son estrategias populares de
control de versiones, cada una con sus propias ventajas y casos de uso.

### _Merge_ y _pull requests_

Para combinar los cambios de una rama a otra se utilizan los _merges_ o _pull requests_
en los repositorios. En este proceso intervienen dos ramas: la rama "_source_" y la rama
"_target_". La rama _source_ contiene los cambios que se desean incorporar, mientras que
la _target_ es la rama donde se introducirán dichos cambios. Por ejemplo, la rama
_source_ puede ser la rama `dev` y la _target_ puede ser la rama `main` o `master`.

### _Trunk-Based Development_

<p align="center">
  <img src="../../assets/img/docs/trunk-based-git.png"/>
  <br />
  <em>Esquema de desarrollo Trunk-Based. [Link](https://statusneo.com/wp-content/uploads/2022/12/Beginners%20Guide%20to%20Trunk-Based%20Development.png)</em>
</p>

En esta estrategia, los desarrolladores fusionan frecuentemente pequeñas actualizaciones
en una única rama principal.

Las principales ventajas de esta estrategia son:

- **Facilita la Integración Continua (CI) y el Despliegue Continuo (CD)**: Esta
  metodología es ideal para entornos donde se practican CI/CD, permitiendo despliegues
  rápidos y frecuentes gracias a la fusión de cambios pequeños y frecuentes.
- **Fomenta la iteración rápida y la colaboración**: Los desarrolladores pueden trabajar
  en paralelo y fusionar sus cambios rápidamente, lo que acelera el ciclo de desarrollo.

Sin embargo, presenta las siguientes desventajas:

- **Gestión en equipos grandes**: Puede ser difícil de gestionar en equipos grandes sin
  una estricta disciplina y coordinación.
- **Rastreo de cambios individuales**: Es menos capaz de rastrear cambios individuales en
  comparación con Git Flow, lo que puede dificultar la identificación de problemas
  específicos.

### Git Flow

<p align="center">
  <img src="../../assets/img/docs/git-flow-git.png"/>
  <br />
  <em>Esquema de desarrollo Git Flow. [Link](https://images.edrawmax.com/what-is/gitflow-diagram/2-git-flow-model.png)</em>
</p>

Esta estrategia utiliza múltiples ramas para diferentes propósitos (por ejemplo, ramas de
características, ramas de lanzamiento, ramas de corrección).

Las principales ventajas de esta estrategia son:

- **Organización y estructura**: Git Flow es altamente organizado y estructurado, lo que
  facilita la gestión de proyectos complejos.
- **Seguimiento detallado de cambios**: Permite un seguimiento detallado de los cambios
  individuales, lo que es útil para auditorías y revisiones de código.
- **Adecuado para ciclos de lanzamiento largos**: Es ideal para proyectos con ciclos de
  lanzamiento más largos, donde se requiere una planificación y gestión detallada.

Sin embargo, presenta las siguientes desventajas:

- **Complejidad**: La gestión de múltiples ramas puede ser más compleja y requerir más
  esfuerzo y coordinación.
- **Ralentización del desarrollo**: Si no se gestiona correctamente, puede ralentizar el
  proceso de desarrollo debido a la necesidad de mantener y fusionar múltiples ramas.

### Cuándo usar Trunk-Based Development o Git Flow

- **Trunk-Based Development**: Es ideal para equipos que practican CI/CD, necesitan
  iteraciones rápidas y trabajan en proyectos con actualizaciones frecuentes. Es
  especialmente útil en entornos ágiles donde la velocidad y la flexibilidad son
  cruciales.
- **Git Flow**: Adecuado para proyectos con ciclos de lanzamiento más largos, que
  requieren un seguimiento detallado de los cambios, y para equipos que prefieren un
  enfoque más estructurado. Es ideal para proyectos donde la estabilidad y la
  planificación a largo plazo son prioritarias.

### _Ship / Show / Ask_

Uno de los problemas recurrentes en el desarrollo de software moderno reside en el
crecimiento progresivo de código, el aumento de su complejidad y la consiguiente pérdida
de visibilidad por parte del resto de los miembros del equipo. Esta situación provoca que
la incorporación de nuevas funcionalidades en las ramas de producción se vea limitada o,
en muchos casos, que la responsabilidad del control de calidad recaiga casi
exclusivamente en las herramientas de integración y despliegue continuo (CI/CD),
reduciendo la interacción humana en el proceso de revisión.

En este contexto surge la estrategia **_Ship / Show / Ask_**, una propuesta que redefine
la forma de trabajar con ramas y solicitudes de integración en Git. Este enfoque,
propuesto por Rouan Wilsenach, se articula en tres modalidades diferenciadas que buscan
equilibrar velocidad, calidad y comunicación dentro del equipo.

El enfoque **_Ship_** se basa en la realización de cambios pequeños, acotados y de bajo
riesgo que pueden integrarse directamente en la rama principal sin necesidad de abrir una
_Pull Request_ ni solicitar la revisión explícita de otros miembros del equipo. Resulta
especialmente adecuado cuando se añade una funcionalidad siguiendo un patrón existente,
se corrige un error menor y poco relevante, se actualiza documentación o se mejora el
código a partir de comentarios previos.

La modalidad **_Show_** introduce un punto intermedio entre la integración directa y la
revisión formal. En este caso, se crea una _Pull Request_ desde una rama distinta de la
principal, pero dicha solicitud no requiere aprobación obligatoria para ser integrada. El
cambio pasa por los mecanismos habituales de CI/CD y se incorpora rápidamente a la base
de código, pero al mismo tiempo se genera un espacio explícito para la revisión, el
aprendizaje y la conversación. El equipo es notificado de la existencia de la _Pull
Request_, lo que permite que otros desarrolladores revisen el enfoque adoptado, planteen
preguntas o sugieran mejoras. Este enfoque es especialmente útil cuando se busca
retroalimentación sobre cómo mejorar una solución, cuando se introduce un nuevo patrón,
se realiza una refactorización relevante o se corrige un error interesante desde el punto
de vista técnico. De este modo, se favorece el aprendizaje colectivo sin frenar el flujo
de entrega.

Por último, el enfoque **_Ask_** representa el modelo más tradicional y deliberativo.
Consiste en abrir una _Pull Request_ que sí requiere la aprobación explícita de uno o
varios miembros del equipo antes de ser integrada. Este modelo se reserva para
situaciones de mayor incertidumbre o riesgo, como propuestas experimentales, nuevos
enfoques arquitectónicos o soluciones que aún no están completamente maduras. En estos
casos, el objetivo principal es fomentar la discusión abierta, validar decisiones
técnicas y construir consenso. Resulta adecuado cuando se plantean dudas sobre la
viabilidad de una solución, se exploran alternativas, se solicita ayuda para mejorar una
implementación o simplemente se deja el trabajo pendiente de revisión para una
integración posterior.

Independientemente de la modalidad elegida, una de las reglas fundamentales que subyacen
a esta estrategia es que las ramas no deben tener una vida prolongada y deben mantenerse
alineadas con la rama principal mediante _rebases_ frecuentes. Las ramas que divergen
durante demasiado tiempo incrementan el riesgo de conflictos al integrarse, dificultan la
comprensión del estado real del proyecto y suelen generar frustración innecesaria en el
equipo.

El propio autor destaca que, cuando se entregan funcionalidades siguiendo patrones
consolidados y existe un alto nivel de confianza y estándares de calidad compartidos, el
equipo tenderá a utilizar más el enfoque **Ship**. En cambio, cuando los miembros aún se
están conociendo, el dominio del problema es nuevo o se están explorando soluciones
desconocidas, surge una mayor necesidad de comunicación, lo que incrementa el uso de
**Show** y **Ask**. Esto pone de manifiesto que la comunicación efectiva y el trabajo
colaborativo son pilares fundamentales de la ingeniería de software.

## Git Hooks

Los **Git Hooks** son una funcionalidad integrada en Git que permite automatizar tareas y
aplicar políticas a lo largo del flujo de trabajo. Gracias a ellos, Git puede ejecutar
acciones en momentos clave del proceso de desarrollo, asegurando la calidad del código y
el cumplimiento de políticas específicas del proyecto.

### Definición y uso de Git Hooks

Los Git Hooks son scripts que se ejecutan automáticamente en respuesta a eventos
específicos dentro de Git, como antes o después de realizar un _commit_, un _push_ o un
_merge_.

Para utilizar Git Hooks, es necesario crear scripts en el directorio `.git/hooks`,
ubicado en la raíz del repositorio Git. Por defecto, al crear un nuevo repositorio, Git
proporciona una serie de _hooks_ de ejemplo que pueden modificarse según las necesidades
del proyecto.

Estos scripts deben ser ejecutables y deben llevar el nombre del evento para el que se
activan, como `pre-commit`, `pre-push` o `post-merge`. Para asegurarse de que tienen los
permisos adecuados, se puede utilizar el siguiente comando:

```bash linenums="1"
chmod +x pre-commit
```

Una vez ubicados en el directorio correcto y con los permisos necesarios, Git ejecutará
automáticamente estos scripts cuando ocurra el evento correspondiente.

Al desarrollar y administrar Git Hooks, es esencial seguir ciertas pautas que aseguren su
eficacia y mantengan un flujo de trabajo ordenado.

En primer lugar, los hooks deben ser rápidos y confiables, de manera que su ejecución no
interfiera con la productividad del equipo ni genere demoras en los procesos habituales
de desarrollo. Asimismo, se recomienda evitar que los hooks realicen cambios automáticos
en el código sin la aprobación explícita del desarrollador, ya que estas modificaciones
pueden provocar conflictos, errores inesperados o dificultades en la integración del
código.

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

## Casos de uso prácticos

En el desarrollo con Git es habitual necesitar manipular la historia de commits o
sincronizar el repositorio local con el remoto. A continuación se presentan soluciones
claras y seguras para los escenarios más frecuentes.

### Gestionar commits no firmados

Para garantizar la autenticidad de los commits, se pueden adoptar varias estrategias.

Podemos volver a generar y firmar todos los commits. Si ya son válidos pero les falta la
firma, basta con recrearlos para que aparezcan firmados. Para ello utilizamos los
siguientes comandos:

```bash linenums="1"
git rebase --root --exec 'git commit --amend --no-edit -S'
git push --force-with-lease
```

Si el repositorio requiere firmas GPG y has añadido commits sin firmar, se producirá un
error al intentar subirlos. Para solucionarlo, puedes reescribir el historial y firmar
los commits existentes sin perder los cambios mediante los siguientes comandos:

```bash linenums="1"
git log --pretty="%h %G?"   # Identifica commits no firmados (N)
git checkout -b rama-limpia
git rebase -i --root        # Marca con 'drop' los commits N en el editor
git push --force-with-lease origin rama-limpia
```

Otra alternativa es restablecer la rama a un commit firmado determinado:

```bash linenums="1"
git reset --hard <commit_firmado>
git push --force-with-lease
```

### Sincronizar repositorio local con el remoto

Para sincronizar la rama local exactamente con la remota, descartando cualquier cambio
local y archivos sin seguimiento, utiliza el siguiente comando.

!!! warning "Advertencia"

    Esta operación es irreversible y eliminará cualquier trabajo que no haya sido subido al repositorio.

```bash linenums="1"
git fetch origin && git reset --hard origin/main && git clean -fd
```

Si prefieres eliminar y recrear la rama local por completo para asegurar una copia limpia
desde el servidor, puedes seguir estos pasos:

```bash linenums="1"
git checkout main
git branch -D nombre-rama
git checkout -b nombre-rama origin/nombre-rama
```

### Eliminar ramas locales que ya no existen en remoto

A veces el repositorio local acumula más ramas que el remoto (por ejemplo, tras borrar
ramas en el servidor). Esto puede volver la lista de ramas difícil de manejar. Para
limpiar tu entorno, puedes eliminar automáticamente las ramas locales cuyo remoto de
seguimiento ya no existe, utilizando el siguiente comando:

```bash linenums="1"
git fetch --prune && git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D
```

Donde:

- **`git fetch --prune`**: actualiza las referencias remotas y elimina las que ya no
  existen en el remoto (prunea ramas remotas eliminadas).
- **`git branch -vv`**: lista las ramas locales con información detallada, incluyendo si
  siguen a una rama remota (tracking).
- **`grep ': gone]'`**: filtra las ramas cuyo remoto de seguimiento ya no existe
  (aparecen marcadas como `gone`).
- **`awk '{print $1}'`**: extrae únicamente el nombre de la rama local.
- **`xargs git branch -D`**: elimina esas ramas localmente.

Ten en cuenta que `-D` fuerza el borrado aunque la rama no esté mergeada. Si prefieres un
borrado seguro (solo si está fusionada), usa `-d`:

```bash linenums="1"
git fetch --prune && git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -d
```

También, como recomendación, conviene revisar primero qué ramas se van a eliminar
ejecutando únicamente el siguiente comando antes de proceder al borrado:

```bash linenums="1"
git branch -vv | grep ': gone]'
```
