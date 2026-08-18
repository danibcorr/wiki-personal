---
authors: Daniel Bazo Correa
description: Crea tus propios scripts ejecutables con Bash.
title: Bash
---

Este capítulo presenta Bash como intérprete de comandos y lenguaje de scripting,
cubriendo su sintaxis básica, estructuras de control y técnicas de automatización.

## Bibliografía

- Pelado Nerd. (2021). _TODOS deberían aprender BASH - Bash PARTE 1_ \[Vídeo\]. YouTube.
  <https://www.youtube.com/watch?v=4_ub6614dwY>

## Introducción

<figure markdown="span">
  ![Logo de Bash](../../assets/img/docs/logos/bash-logo.png)
  <figcaption>Logo de Bash</figcaption>
</figure>

BASH (_Bourne Again Shell_) es un intérprete de comandos y un lenguaje de programación
ampliamente utilizado en sistemas basados en Unix. Fue desarrollado por Brian Fox para
el proyecto GNU y publicado en 1989 como una evolución del _Bourne Shell_ (`sh`).

## Sintaxis

### Estructura de un _script_

Todo programa en BASH comienza con la línea `#!/bin/bash`, conocida como _shebang_. Esta
directiva indica al sistema operativo qué intérprete debe utilizar para ejecutar los
comandos contenidos en el archivo, independientemente del entorno en el que se invoque.

Los _scripts_ de BASH emplean por convención la extensión `.sh`, lo que facilita su
identificación dentro del sistema de archivos.

A continuación del _shebang_ se añaden las instrucciones que definen las acciones a
realizar, como mostrar mensajes en la terminal, invocar otros _scripts_ o ejecutar
tareas específicas del sistema.

???+ example "Hola mundo"

    Para ilustrar el proceso, se crea un _script_ básico denominado `script.sh` que
    muestra un mensaje en la terminal:

    ```bash linenums="1"
    #!/bin/bash

    echo "Hola mundo"
    ```

En Linux, cada archivo posee un conjunto de **permisos** que determinan quién puede
leerlo, escribirlo o ejecutarlo. Al crear un _script_, este no dispone de permisos de
ejecución por defecto, lo que impide su invocación directa. Para que el sistema lo
reconozca como un programa ejecutable, es necesario otorgarle dichos permisos y
posteriormente invocarlo desde la terminal.

???+ example "Dar permisos de ejecución"

    El comando `chmod` modifica los permisos de un archivo. La opción `+x` añade el
    permiso de ejecución:

    ```bash linenums="1"
    chmod +x script.sh
    ```

    Una vez concedido el permiso, es posible ejecutar el _script_ directamente:

    ```bash linenums="1"
    ./script.sh
    ```

    !!! note "Conoce Linux"

        Si quieres conocer sobre estos comandos y lo básico sobre Linux, puedes dirigirte a
        este [apartado](../../01_operative_systems/01_linux/section_1_fundamentals.md).

### Argumentos

BASH permite pasar parámetros a un _script_ en el momento de su invocación. Dentro del
_script_, estos argumentos se referencian mediante el símbolo `$` seguido de un número
que indica su posición.

???+ example "Argumentos posicionales"

    ```bash linenums="1"
    #!/bin/bash

    echo "Hola $1"
    echo "Adiós $2"
    ```

    En este caso, `$1` corresponde al primer argumento proporcionado, `$2` al segundo,
    y así sucesivamente. Cabe destacar que `$0` siempre contiene el nombre del propio
    _script_.

### Variables

Las variables en BASH se asignan de forma directa, sin necesidad de declarar su tipo
previamente. El nombre de la variable se escribe seguido del signo `=` y el valor
deseado, sin espacios entre ellos.

???+ example "Declarar variables"

    ```bash linenums="1"
    #!/bin/bash

    nombre="Daniel"
    echo "Mi nombre es $nombre"
    ```

    También es posible almacenar el resultado de la ejecución de un comando del sistema
    en una variable mediante la sintaxis `$(comando)`:

    ```bash linenums="1"
    #!/bin/bash

    resultado=$(comando)
    ```

### Entrada del usuario

Para capturar datos introducidos por el usuario durante la ejecución de un _script_, se
utiliza el comando `read`. Este comando detiene la ejecución hasta que el usuario
proporciona un valor y pulsa la tecla _Enter_.

???+ example "Leer entrada del usuario"

    ```bash linenums="1"
    #!/bin/bash

    echo "¿Cuál es tu nombre?"
    read nombre
    echo "Tu nombre es $nombre"
    ```

### Operaciones aritméticas

Las operaciones aritméticas en BASH se evalúan dentro de la construcción `$(( ))`, que
permite realizar cálculos matemáticos básicos con números enteros.

???+ example "Operaciones aritméticas"

    ```bash linenums="1"
    #!/bin/bash

    echo $((5 + 5))
    ```

Los operadores aritméticos disponibles son:

- `+`: Suma.
- `-`: Resta.
- `*`: Multiplicación.
- `/`: División entera.
- `%`: Módulo (resto de la división).

### Condiciones

Las estructuras condicionales en BASH se construyen mediante el comando `if`, que evalúa
expresiones y ejecuta bloques de código en función del resultado. Las condiciones se
encierran entre corchetes `[ ]` y pueden combinarse mediante operadores lógicos.

???+ example "Condicional if-else"

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

Los operadores de comparación disponibles son:

- `==`: Igual a.
- `!=`: Distinto de.
- `>`: Mayor que.
- `<`: Menor que.
- `>=`: Mayor o igual que.
- `<=`: Menor o igual que.

Los operadores lógicos permiten combinar múltiples condiciones:

- `-a` o `&&`: Conjunción lógica (AND).
- `-o` o `||`: Disyunción lógica (OR).
- `!`: Negación lógica (NOT).

!!! note "Operadores lógicos"

    Los operadores `-a` y `-o` se utilizan dentro de los corchetes de una expresión
    condicional, mientras que `&&` y `||` se emplean fuera de ellos para encadenar
    múltiples evaluaciones independientes.

### Bucles

BASH ofrece varias estructuras de repetición. El bucle `for` resulta adecuado cuando se
conoce de antemano el conjunto de valores sobre los que iterar.

???+ example "Bucle for"

    ```bash linenums="1"
    #!/bin/bash

    for i in 1 2 3; do
        echo $i
    done
    ```

El bucle `while` se emplea cuando la repetición debe continuar mientras se cumpla una
condición determinada, lo que lo hace idóneo para situaciones en las que el número de
iteraciones depende de una variable o del resultado de una operación.

???+ example "Bucle while"

    ```bash linenums="1"
    #!/bin/bash

    i=1
    while [ $i -le 5 ]; do
        echo $i
        (( i++ ))
    done
    ```

Dentro de cualquier bucle, el comando `break` permite finalizar la ejecución del bucle
de forma inmediata, mientras que `continue` salta directamente a la siguiente iteración
sin ejecutar el resto del cuerpo del bucle.

???+ example "Uso de break y continue"

    ```bash linenums="1"
    #!/bin/bash

    i=0
    max_value=5

    while [ $i -le $max_value ]; do
        if [ $(( i % 2)) -eq 0 ]; then
        echo "Valor par $i encontrado, continúo."
        (( i++ ))
        continue
        else
            echo "Valor impar $i encontrado, termino."
            break
        fi
    done
    ```

### Funciones

Las funciones en BASH permiten encapsular bloques de código reutilizables, lo que
favorece la modularidad, la legibilidad y el mantenimiento de los _scripts_. Una vez
definida, una función se invoca simplemente escribiendo su nombre.

???+ example "Definir una función"

    ```bash linenums="1"
    #!/bin/bash

    function funcion() {
        echo "Esta es una función de prueba"
    }

    funcion
    ```

### Control de errores

Por defecto, un _script_ de BASH continúa su ejecución aunque uno de sus comandos falle,
lo que puede provocar que se realicen operaciones sobre un estado inconsistente.

La opción `set -e` modifica este comportamiento y hace que el _script_ finalice de forma
inmediata en cuanto cualquier comando devuelve un código de salida distinto de cero, es
decir, en cuanto falla. De este modo, la ejecución se detiene en el primer error en
lugar de propagarlo a las instrucciones posteriores.

???+ example "Detención ante el primer error"

    ```bash linenums="1"
    #!/bin/bash
    set -e

    # Este comando falla y detiene el script en este punto
    cp archivo_inexistente.txt /tmp/
    echo "Esto nunca se ejecuta"
    ```

Existen situaciones en las que `set -e` no detiene el _script_ aunque un comando falle.
Los comandos evaluados dentro de una condición `if` o `while` no interrumpen la
ejecución, ya que su código de salida forma parte de la propia evaluación de la
condición. Tampoco lo hacen los comandos encadenados mediante los operadores `||` o
`&&`, puesto que el fallo se contempla dentro de la lógica de la expresión. Del mismo
modo, un comando ejecutado en una _subshell_ no detiene el _script_ principal cuando el
error se gestiona de forma externa.

En la práctica, `set -e` suele combinarse con otras opciones que refuerzan la robustez
del _script_:

```bash linenums="1"
#!/bin/bash
set -euo pipefail
```

Donde:

- `-e`: Finaliza el _script_ ante cualquier error.
- `-u`: Genera un error si se utiliza una variable no definida.
- `-o pipefail`: Propaga el fallo de cualquier comando de un _pipeline_ al conjunto del
  mismo. Sin esta opción, únicamente se considera el código de salida del último
  comando.

## Automatización

Combinando las estructuras anteriores (variables, condiciones, bucles y funciones), BASH
permite automatizar tareas complejas. En el desarrollo de proyectos, esta automatización
resulta fundamental para garantizar la reproducibilidad y la eficiencia del entorno de
trabajo.

???+ example "Script de configuración de entorno"

    A continuación se presenta un ejemplo de _script_ que ilustra cómo preparar un
    entorno de desarrollo completo, verificando e instalando herramientas necesarias y
    gestionando dependencias tanto del sistema como de Python:

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

    # Instalación de dependencias de Python
    echo "Installing Python dependencies with uv..."
    uv sync > /dev/null 2>&1
    echo "✅ Python dependencies installed."
    ```

    Este _script_ ejecuta de manera secuencial varias operaciones clave para configurar
    un entorno de desarrollo. En primer lugar, verifica si la herramienta `uv` se
    encuentra instalada en el sistema y, en caso contrario, procede a su instalación de
    forma silenciosa.

    La redirección `> /dev/null 2>&1` descarta tanto la salida estándar como los
    mensajes de error, evitando que aparezcan en la terminal durante la ejecución.

    Posteriormente, el _script_ actualiza los repositorios del sistema e instala los
    paquetes de compilación esenciales mediante `apt-get`, también de manera
    silenciosa. Finalmente, invoca al gestor de dependencias `uv` para instalar
    las dependencias de Python, asegurando que el entorno de desarrollo quede
    completamente operativo.
