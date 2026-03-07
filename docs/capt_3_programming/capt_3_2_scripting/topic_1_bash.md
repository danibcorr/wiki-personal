---
authors: Daniel Bazo Correa
description: Crea tus propios scripts ejecutables con Bash.
title: Bash
---

## Bibliografía

- [Pradumnasaraf/DevOps](https://github.com/Pradumnasaraf/DevOps)
- [TODOS deberían aprender BASH - Bash PARTE 1](https://www.youtube.com/watch?v=4_ub6614dwY)

## Introducción

<p align="center">
  <img src="../../../assets/img/docs/logos/bash-logo.png" width="500"/>
  <br />
  <em>Logo de Bash</em>
</p>

**BASH** (_Bourne Again Shell_) es un intérprete de comandos y un lenguaje de
programación utilizado en sistemas basados en Unix. Fue desarrollado por Brian Fox para
el Proyecto GNU y lanzado en 1989 como una versión mejorada del _Bourne shell_ (`sh`).

Se distingue por su eficiencia en la ejecución de comandos, su compatibilidad con
_scripts_ de _shell_ y su versatilidad para la automatización de tareas y la
administración de sistemas.

## Conceptos básicos

### Ejemplo de programa base

Un programa básico en BASH comienza con la línea `#!/bin/bash` (_shebang_), que indica al
sistema qué intérprete debe usar para ejecutar los comandos del script.

Es importante destacar que los scripts de BASH suelen tener la extensión `.sh`.

!!!note "Nota"

    El uso del shebang `#!/bin/bash` garantiza que el script se ejecute con el intérprete
    adecuado, independientemente del entorno en el que se ejecute.

A continuación, se añaden las líneas de comandos que definen las acciones a realizar,
como mostrar un mensaje en la terminal, ejecutar otros scripts o realizar tareas
específicas.

???+ example "Ejemplo"

    Supongamos que tenemos un script llamado `script.sh`. Para hacerlo ejecutable, primero
    debemos otorgarle permisos.

    Primero, crearemos un _script_ básico, con nombre `script.sh`, para mostrar en la
    terminal un `Hola mundo`:

    ```bash linenums="1"
    #!/bin/bash

    echo "Hola mundo"
    ```

En Linux, cada archivo tiene **permisos** que determinan quién puede leerlo, escribirlo o
ejecutarlo. Cuando creas un script (`script.sh`), normalmente **no tiene permisos de
ejecución por defecto**, lo que significa que no se puede ejecutar directamente. Para
permitir que el sistema lo ejecute como un programa, usamos:

```bash linenums="1"
chmod +x script.sh
```

**Qué hace este comando:**

- `chmod`: Cambia los **permisos** de un archivo.
- `+x`: Añade el permiso de **ejecución** al archivo.
- `script.sh`: El archivo al que le estamos dando permisos.

Después de ejecutar este comando, podrás ejecutar tu script desde la terminal
directamente así:

```bash linenums="1"
./script.sh
```

### Pasar parámetros como argumentos

En BASH, los parámetros se pasan al script mediante el uso de `$`, seguido del número que
representa la posición del argumento.

???+ example "Ejemplo"

    ```bash linenums="1"
    #!/bin/bash

    echo "Hola $1"
    echo "Adiós $2"
    ```

    En este caso, el primer argumento se pasa como `$1`, el segundo como `$2`, y así
    sucesivamente.

    !!!note "Nota"

        `$0` siempre contiene el nombre del script.

### Asignación de variables

En BASH, las variables se asignan de manera sencilla, sin necesidad de declarar su tipo
previamente.

???+ example "Ejemplo"

    ```bash linenums="1"
    #!/bin/bash

    nombre="Daniel"
    echo "Mi nombre es $nombre"
    ```

    También es posible almacenar el resultado de la ejecución de un comando del sistema en
    una variable:

    ```bash linenums="1"
    #!/bin/bash

    resultado=$(comando)
    ```

    El uso de `$(comando)` permite capturar la salida de un comando y almacenarla en una
    variable, lo cual resulta útil para automatizar tareas y procesar información.

### Introducción de entradas del usuario

Para capturar entradas del usuario, se utiliza el comando `read`.

???+ example "Ejemplo"

    ```bash linenums="1"
    #!/bin/bash

    echo "¿Cuál es tu nombre?"
    read nombre
    echo "Tu nombre es $nombre"
    ```

### Operaciones aritméticas

Las operaciones aritméticas en BASH se realizan dentro de `$(( ))`, lo que permite
evaluar expresiones matemáticas de manera sencilla.

???+ example "Ejemplo"

    ```bash linenums="1"
    #!/bin/bash

    echo $((5 + 5))
    ```

Operaciones disponibles:

- `+`: Suma.
- `-`: Resta.
- `*`: Multiplicación.
- `/`: División.
- `%`: Módulo (el resto de la división).

### Condiciones

En BASH, las condiciones se expresan utilizando el comando `if`, junto con los operadores
de comparación y lógicos.

???+ example "Ejemplo"

    ```bash linenums="1"
    #!/bin/bash

    if [ "$1" == "Dani" ] || [ "$1" == "Paco" ]; then
        echo "Hola $1"
    elif [ "$1" == "Jorge" ]; then
        echo "Bienvenido"
    else
        echo "Intruso"
    fi
    ```

Operadores de comparación:

- `==`: Igual a.
- `!=`: Distinto de.
- `>`: Mayor que.
- `<`: Menor que.
- `>=`: Mayor o igual que.
- `<=`: Menor o igual que.

Operadores booleanos:

- `-a` o `&&`: Y (AND).
- `-o` o `||`: O (OR).
- `!`: No (NOT).

Es importante recordar que `-a` y `-o` se usan dentro de corchetes, mientras que `&&` y
`||` se emplean fuera de ellos.

!!!note "Nota"

    Recuerda que los operadores `&&` y `||` son más comunes fuera de los corchetes, mientras
    que los operadores `-a` y `-o` se utilizan dentro de los corchetes en las condiciones del
    `if`.

### Bucles

BASH soporta varios tipos de bucles. Un bucle `for` se define de la siguiente manera:

???+ example "Ejemplo"

    ```bash linenums="1"
    #!/bin/bash

    for i in 1 2 3; do
        echo $i
    done
    ```

Un bucle `while` se usa cuando se necesita repetir una acción mientras se cumpla una
condición específica:

???+ example "Ejemplo"

    ```bash linenums="1"
    #!/bin/bash

    i=1
    while [ $i -le 5 ]; do
        echo $i
        (( i++ ))
    done
    ```

Comandos adicionales:

- `break`: Finaliza el bucle.
- `continue`: Salta a la siguiente iteración del bucle.

!!!note "Nota"

    Los bucles `for` son ideales cuando se conoce el número exacto de iteraciones, mientras que los bucles `while` se utilizan cuando la condición de salida depende de una variable o del resultado de una operación.

### Funciones

Las funciones en BASH permiten organizar y reutilizar el código de manera más eficiente.
Definir funciones ayuda a hacer el código más modular, legible y fácil de mantener,
facilitando además la reutilización de bloques de código sin tener que escribirlos varias
veces.

???+ example "Ejemplo"

    ```bash linenums="1"
    #!/bin/bash

    function funcion() {
        echo "Esta es una función de prueba"
    }

    funcion
    ```

## Ejemplos de automatización

En el desarrollo de proyectos en Python, la automatización de tareas mediante **Bash**
resulta fundamental para garantizar la reproducibilidad y eficiencia del entorno.

A continuación, se presenta un ejemplo de script que ilustra cómo preparar un entorno de
desarrollo, instalando herramientas necesarias y dependencias tanto del sistema como de
Python:

```bash linenums="1"
#!/bin/bash
set -e

# Verificación e instalación de la herramienta "uv"
echo "Checking for uv..."
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh > /dev/null 2>&1
    echo "✅ uv installed."
else
    echo "✅ uv already installed."
fi

# Instalación de dependencias del sistema
echo "Installing system dependencies..."
sudo apt-get update > /dev/null 2>&1
sudo apt-get install -y build-essential > /dev/null 2>&1
echo "✅ System dependencies installed."

# Instalación de dependencias de Python a través de Makefile
echo "Installing Python dependencies with Makefile..."
make install > /dev/null 2>&1

echo "✅ Devcontainer setup complete."
```

Este script ejecuta de manera secuencial y automatizada varias operaciones clave para
configurar un entorno de desarrollo.

Primero, verifica si la herramienta `uv` está instalada y, en caso contrario, procede a
su instalación de forma silenciosa. La ejecución silenciosa se logra mediante
`> /dev/null 2>&1`, que descarta tanto la salida estándar como los mensajes de error,
evitando que aparezcan en la terminal.

Posteriormente, el script actualiza el sistema e instala paquetes esenciales mediante
`apt-get`, también de manera silenciosa.

Finalmente, instala las dependencias de Python definidas en un archivo `Makefile`,
asegurando que el entorno de desarrollo quede completamente configurado.
