---
authors: Daniel Bazo Correa
description: Automatiza tus procesos con Makefile.
title: Makefile
---

## Referencias

- [Makefile Tutorial](https://makefiletutorial.com/)

## Introducción

<figure markdown="span">
  ![Logo de Makefile](../../assets/img/docs/logos/makefile-logo.png){ width="300" }
  <figcaption>Logo de Makefile</figcaption>
</figure>

Un _Makefile_ es un archivo de configuración utilizado por la herramienta `make` que
permite automatizar procesos de compilación, ejecución y gestión de proyectos de
_software_. Se emplea de forma generalizada en entornos con sistemas operativos basados
en GNU/Linux y puede contener comandos escritos en [Bash](./section_1_bash.md).

## Sintaxis básica

### Estructura de una regla

Una regla en un _Makefile_ define el proceso de construcción de un objetivo (_target_) a
partir de sus prerrequisitos. La estructura básica es la siguiente:

```makefile linenums="1"
targets: prerequisites
	comando
	comando
	comando
```

El campo _targets_ contiene los nombres de los archivos o tareas que se generarán,
separados por espacios. Habitualmente se define un único _target_ por regla. Los
_prerequisites_ son los archivos o dependencias necesarios para generar el _target_,
también separados por espacios. Los comandos son las instrucciones que se ejecutan para
construir el _target_ y cada uno de ellos debe comenzar obligatoriamente con un carácter
de tabulación, no con espacios.

???+ example "Ejemplo sin prerrequisitos"

    ```makefile linenums="1"
    setup:
    	@echo "Installing dependencies..."
    	@uv sync --all-groups
    	@uv run pre-commit install
    	@echo "✅ Dependencies installed."
    ```

    En este ejemplo, `setup` es el *target* que representa la tarea a realizar.
    Al no tener prerrequisitos, se ejecuta siempre que se invoque. Los comandos
    precedidos por `@` se ejecutan sin mostrar la línea del comando en la salida,
    mostrando únicamente su resultado. Al ejecutar `make setup`, Make ejecuta los
    comandos de forma secuencial: sincroniza las dependencias con `uv` e instala
    los *hooks* de *pre-commit*.

???+ example "Ejemplo con prerrequisitos"

    ```makefile linenums="1"
    pipeline: setup clean_cache_temp_files clean_notebooks lint code_check security
    	@echo "✅ Pipeline complete."
    ```

    En este caso, `pipeline` depende de varios *targets* previos. Make ejecuta cada
    prerrequisito en orden antes de ejecutar el comando propio del *target*.

### Comentarios

Los comentarios en un _Makefile_ se escriben utilizando el símbolo `#`. No afectan a la
ejecución del archivo y sirven para documentar el propósito de las reglas o los
comandos.

???+ example "Ejemplo"

    ```makefile linenums="1"
    # Esta regla instala las dependencias del proyecto
    setup:
    	@uv sync --all-groups
    ```

### Variables

Las variables en _Makefiles_ permiten almacenar y reutilizar valores, lo que facilita la
personalización de comandos y rutas sin necesidad de repetir información.

???+ example "Ejemplo"

    ```makefile linenums="1"
    PATH_RESEARCH ?= src
    PATH_TESTS ?= tests
    PATH_PROJECT_ROOT ?= .

    lint:
    	@echo "Running lint checks..."
    	@uv run ruff format $(PATH_PROJECT_ROOT)
    	@uv run ruff check --fix $(PATH_PROJECT_ROOT)
    	@echo "✅ Linting complete."

    test:
    	@echo "Running tests..."
    	@uv run pytest -m training $(PATH_TESTS) --maxfail=1 --durations=0
    	@uv run pytest -m inference $(PATH_TESTS) --maxfail=1 --durations=0
    	@echo "✅ Tests complete."
    ```

    La sintaxis `?=` asigna un valor por defecto a la variable, permitiendo
    sobreescribirla en el momento de la invocación. En la regla `test`, el comando
    utiliza `$(PATH_TESTS)` para referenciar el directorio de pruebas. Para ejecutar
    con un directorio diferente basta con especificarlo en la llamada:

    ```sh linenums="1"
    make test PATH_TESTS=./tests/unit
    ```

#### Variables automáticas

Make proporciona variables automáticas que permiten referirse de manera dinámica a los
_targets_ y prerrequisitos sin necesidad de escribirlos explícitamente en cada regla.

| Variable | Descripción                                               |
| -------- | --------------------------------------------------------- |
| `$@`     | Nombre del _target_ actual.                               |
| `$<`     | Primer prerrequisito de la regla.                         |
| `$^`     | Todos los prerrequisitos de la regla.                     |
| `$*`     | Parte del nombre (_stem_) que coincide con el patrón `%`. |
| `$(@D)`  | Directorio del _target_ actual.                           |
| `$(@F)`  | Nombre del archivo del _target_ actual.                   |

???+ example "Ejemplo"

    ```makefile linenums="1"
    output.zip: processed_data/input1.csv processed_data/input2.csv
    	zip $@ $^
    ```

    En este caso, `$@` representa el *target* actual (`output.zip`) y `$^` contiene
    todos los prerrequisitos (`processed_data/input1.csv processed_data/input2.csv`).

#### Variables específicas de objetivo y patrones

Make permite definir variables que se aplican únicamente a determinados objetivos o
patrones de archivos, lo que posibilita configuraciones particulares sin afectar al
resto del proyecto.

???+ example "Ejemplo"

    ```makefile linenums="1"
    # Se agrega una opción de optimización para la generación de archivos intermedios
    %.txt: PYTHONFLAGS += --optimize

    # Definir la regla para procesar archivos .csv y convertirlos en .txt
    %.txt: %.csv
    	python3 process_data.py $< $@
    ```

    El patrón `%.txt` indica que cualquier archivo con extensión `.csv` se convertirá
    en un archivo `.txt`. La variable específica `PYTHONFLAGS += --optimize` se aplica
    exclusivamente cuando se genera un archivo `.txt`. En la regla, `$<` representa el
    archivo de entrada y `$@` el de salida.

## Funciones avanzadas

### Manipulación de cadenas de texto

Make ofrece un conjunto de funciones integradas que facilitan la manipulación de cadenas
de texto y listas, lo que resulta especialmente útil para transformar nombres de
archivos y gestionar dependencias de forma dinámica.

#### Función `subst`

La función `subst` reemplaza todas las ocurrencias de un texto por otro dentro de una
cadena.

!!!note "Sintaxis"

    ```makefile linenums="1"
    $(subst from,to,text)
    ```

    Donde `from` es el texto a reemplazar, `to` es el texto de reemplazo y `text` es la
    cadena sobre la que se realiza la búsqueda.

???+ example "Ejemplo"

    ```makefile linenums="1"
    SOURCES = file1.cpp file2.cpp file3.cpp
    OBJECTS = $(subst .cpp,.o,$(SOURCES))
    ```

    La función reemplaza `.cpp` por `.o` en la lista de archivos, generando
    `file1.o file2.o file3.o`.

#### Función `patsubst`

La función `patsubst` realiza sustituciones basadas en patrones, utilizando el comodín
`%` para mayor flexibilidad.

!!!note "Sintaxis"

    ```makefile linenums="1"
    $(patsubst pattern,replacement,text)
    ```

???+ example "Ejemplo"

    ```makefile linenums="1"
    SOURCES = file1.cpp file2.cpp file3.cpp
    OBJECTS = $(patsubst %.cpp,%.o,$(SOURCES))
    ```

    Este ejemplo produce el mismo resultado que `subst`, pero la sintaxis basada en
    patrones permite expresar transformaciones más complejas.

#### Funciones `filter` y `filter-out`

Estas funciones permiten filtrar listas de elementos. La función `filter` conserva
únicamente las palabras que coinciden con un patrón determinado, mientras que
`filter-out` elimina aquellas que coinciden.

!!!note "Sintaxis"

    ```makefile linenums="1"
    $(filter pattern...,text)
    $(filter-out pattern...,text)
    ```

???+ example "Ejemplo"

    ```makefile linenums="1"
    SOURCES = file1.c file2.cpp file3.h
    C_FILES = $(filter %.c,$(SOURCES))
    ```

    La función `filter` selecciona únicamente los archivos con extensión `.c`,
    resultando en `file1.c`.

#### Función `foreach`

La función `foreach` permite iterar sobre una lista y aplicar una transformación a cada
elemento.

!!!note "Sintaxis"

    ```makefile linenums="1"
    $(foreach var,list,text)
    ```

???+ example "Ejemplo"

    ```makefile linenums="1"
    DIRS = dir1 dir2 dir3
    CLEAN_DIRS = $(foreach dir,$(DIRS),$(dir)/clean)
    ```

    Este ejemplo genera la lista `dir1/clean dir2/clean dir3/clean`.

#### Función `if`

La función `if` permite evaluar una condición y devolver un valor u otro en función del
resultado.

!!!note "Sintaxis"

    ```makefile linenums="1"
    $(if condition,then-part[,else-part])
    ```

???+ example "Ejemplo"

    ```makefile linenums="1"
    USE_DEBUG = yes
    CFLAGS = $(if $(USE_DEBUG),-g,-O2)
    ```

    Si `USE_DEBUG` tiene un valor no vacío, se asigna `-g` para habilitar la
    depuración. En caso contrario, se utiliza `-O2` para optimización.

### Directivas

Las directivas en Make controlan el flujo de ejecución, la inclusión de archivos
externos y otras configuraciones avanzadas del proceso de construcción.

#### `include`

La directiva `include` permite incorporar el contenido de otros _Makefiles_ dentro de
uno principal, lo que facilita la organización modular de proyectos grandes.

???+ example "Ejemplo"

    ```makefile linenums="1"
    include config.mk
    ```

#### `VPATH`

La directiva `VPATH` especifica directorios adicionales donde Make buscará los archivos
necesarios cuando no los encuentre en el directorio actual.

???+ example "Ejemplo"

    ```makefile linenums="1"
    VPATH = src:include
    ```

    Make buscará primero en `src` y luego en `include` para localizar los archivos
    requeridos.

#### `.PHONY`

La directiva `.PHONY` declara objetivos que no corresponden a archivos reales en el
sistema de archivos. Esto evita conflictos en caso de que exista un archivo con el mismo
nombre que el _target_ y garantiza que la regla se ejecute siempre que se invoque.

???+ example "Ejemplo"

    ```makefile linenums="1"
    .PHONY: setup \
    	clean_cache_temp_files clean_notebooks \
    	lint code_check check_dead_code security \
    	test \
    	doc mlflow \
    	train_pipeline inference_pipeline \
    	profile_train profile_inference \
    	pipeline all
    ```

    Todos los *targets* se declaran como objetivos ficticios, ya que representan tareas
    y no archivos reales. Esto resulta especialmente importante en proyectos donde los
    nombres de los *targets* podrían coincidir con directorios existentes.

#### `.DEFAULT_GOAL`

La directiva `.DEFAULT_GOAL` define qué _target_ se ejecuta cuando se invoca `make` sin
argumentos.

???+ example "Ejemplo"

    ```makefile linenums="1"
    .DEFAULT_GOAL := pipeline
    ```

    Con esta configuración, ejecutar `make` sin argumentos equivale a ejecutar
    `make pipeline`.

#### `.DELETE_ON_ERROR`

La directiva `.DELETE_ON_ERROR` indica que Make debe eliminar el archivo de objetivo si
algún comando falla durante su ejecución, evitando así la presencia de archivos
incompletos o corruptos en el sistema.

!!!note "Sintaxis"

    ```makefile linenums="1"
    .DELETE_ON_ERROR:
    ```

### Condicionales

Los _Makefiles_ permiten el uso de estructuras condicionales para adaptar las reglas
según diferentes entornos o configuraciones del proyecto.

!!!note "Sintaxis"

    ```makefile linenums="1"
    ifeq (condición)
        acción
    else
        acción
    endif
    ```

???+ example "Ejemplo"

    ```makefile linenums="1"
    ifeq ($(USE_DEBUG),yes)
        CFLAGS = -g
    else
        CFLAGS = -O2
    endif
    ```

### Macros y funciones personalizadas

Make permite definir macros que agrupan varios comandos bajo un nombre reutilizable, lo
que mejora la legibilidad y reduce la duplicación de código en _Makefiles_ extensos.

!!!note "Sintaxis"

    ```makefile linenums="1"
    define nombre_de_macro
        comandos
    endef
    ```

???+ example "Ejemplo"

    ```makefile linenums="1"
    define compile_rule
        $(CC) $(CFLAGS) -c $< -o $@
    endef

    %.o: %.c
        $(call compile_rule)
    ```

## Buenas prácticas

El uso adecuado de _Makefiles_ mejora la legibilidad del proyecto y facilita su
mantenimiento a largo plazo. A continuación se describen las prácticas más
recomendables.

### Organización

Es conveniente estructurar el _Makefile_ de forma que resulte fácil de leer y mantener.
Las directivas y variables deben situarse al inicio del archivo, seguidas de comentarios
claros que expliquen el propósito de cada sección. En proyectos de gran tamaño, resulta
aconsejable dividir el _Makefile_ en módulos mediante la directiva `include`. Los
_targets_ relacionados deben agruparse de forma lógica y ordenarse de lo más general a
lo más específico.

???+ example "Ejemplo completo"

    ```makefile linenums="1"
    .PHONY: setup clean lint test pipeline all

    .DEFAULT_GOAL := pipeline

    # --- Variables ---
    PATH_RESEARCH ?= src
    PATH_TESTS ?= tests
    PATH_PROJECT_ROOT ?= .

    # --- Configuración ---
    setup:
    	@echo "Installing dependencies..."
    	@uv sync --all-groups
    	@uv run pre-commit install
    	@echo "✅ Dependencies installed."

    # --- Limpieza ---
    clean:
    	@echo "Cleaning cache and temporary files..."
    	@find . -type d -name __pycache__ -exec rm -rf {} +
    	@find . -type d -name .pytest_cache -exec rm -rf {} +
    	@find . -type d -name .mypy_cache -exec rm -rf {} +
    	@find . -type f \( -name '*.pyc' -o -name '*.pyo' \) -delete
    	@echo "✅ Clean complete."

    # --- Calidad de código ---
    lint:
    	@echo "Running lint checks..."
    	@uv run ruff format $(PATH_PROJECT_ROOT)
    	@uv run ruff check --fix $(PATH_PROJECT_ROOT)
    	@echo "✅ Linting complete."

    # --- Tests ---
    test:
    	@echo "Running tests..."
    	@uv run pytest $(PATH_TESTS) --maxfail=1 --durations=0
    	@echo "✅ Tests complete."

    # --- Pipelines ---
    pipeline: setup clean lint
    	@echo "✅ Pipeline complete."

    all: pipeline test
    	@echo "✅ All tasks complete."
    ```

### Depuración

Existen varias técnicas útiles para depurar _Makefiles_ cuando el comportamiento no es
el esperado. La ejecución en seco mediante la opción `-n` muestra qué comandos se
ejecutarían sin llevarlos a cabo realmente:

```sh linenums="1"
make -n
```

La opción `-d` proporciona una salida detallada sobre cómo Make procesa las reglas y
resuelve las dependencias:

```sh linenums="1"
make -d
```
