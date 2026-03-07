---
authors: Daniel Bazo Correa
description:
  Creación y gestión de entornos virtuales de Python con VENV, Anaconda y Poetry
title: Entornos
---

## Bibliografía

- [VENV Docs](https://docs.python.org/3/library/venv.html)
- [Poetry Docs](https://python-poetry.org/)
- [Anaconda Docs](https://docs.anaconda.com/)
- [uv Docs](https://docs.astral.sh/uv/)

## Introducción

Existen varias opciones para la gestión de paquetes en Python. Independientemente de la
que elijas, mi recomendación es optar siempre por la alternativa más simple y
minimalista, aunque también dependerá mucho del entorno de desarrollo que tengas en la
empresa o de a lo que estés acostumbrado. Recuerda que, al final, estas siguen siendo
herramientas que tienes que considerar y, si te aportan mejoras, implementarlas
gradualmente. Cuanto menor sea el número de dependencias y más ligero sea el entorno, más
fácil será llevarlo a producción (por ejemplo, en una imagen de Docker), compartirlo con
tu equipo o mantenerlo en el tiempo.

En la actualidad, las opciones que más recomiendo son **Poetry** y **uv**. Ambas
herramientas agilizan la creación y gestión de entornos, permiten mantener las
configuraciones del proyecto de forma organizada mediante un archivo `pyproject.toml` y,
sobre todo, favorecen la **reproducibilidad** de los proyectos.

### Anaconda

<p align="center">
  <img src="../../../assets/img/docs/logos/anaconda-logo.png" width="500"/>
  <br />
  <em>Logo de Anaconda</em>
</p>

**Anaconda** es una plataforma de código abierto diseñada para la creación y gestión de
entornos virtuales en Python, enfocada en proyectos de ciencia de datos y aprendizaje
automático. Proporciona una distribución de Python con numerosas bibliotecas
preinstaladas, un gestor de paquetes propio y herramientas como
[_Jupyter_](https://jupyter.org/).

La gestión de paquetes en Anaconda se realiza mediante
_[Conda](https://anaconda.org/anaconda/repo)_, aunque también es posible utilizar
_[PIP](https://pypi.org/)_. Sin embargo, no es recomendable mezclar ambos, ya que pueden
surgir errores en la compatibilidad de paquetes.

Durante años fue la plataforma más usada en ciencia de datos, ya que ofrecía un
ecosistema completo (Jupyter, Spyder, RStudio, etc.) de manera muy sencilla. Sin embargo,
con el tiempo ha presentado limitaciones como una **licencia más restrictiva** para
empresas y un **exceso de dependencias por defecto**.

Hoy en día existen alternativas más eficientes, modernas y ligeras, como **Poetry** y
**uv**, que utilizan el gestor de entornos virtuales de Python y evitan instalar paquetes
innecesarios.

### VENV

Por otro lado, [`VENV`](https://docs.python.org/3/library/venv.html) es una alternativa
más ligera para la creación de entornos virtuales sin las dependencias adicionales de
Anaconda, y que ya viene por defecto cuando instalamos Python. En este caso, la gestión
de paquetes se lleva a cabo con _[PIP](https://pypi.org/)_.

### Poetry

<p align="center">
  <img src="https://python-poetry.org/images/logo-origami.svg" width="100"/>
  <br />
  <em>Logo de Poetry</em>
</p>

[`Poetry`](https://python-poetry.org/) es otra herramienta de gestión de dependencias en
proyectos de Python.

Permite, entre otras cosas, administrar dependencias por grupos (_producción_, _pruebas_,
_documentación_, etc.), eliminando la necesidad de crear múltiples ficheros de requisitos
de dependencias (los `requirements.txt`) o de tener un único fichero.

También permite crear y manejar entornos virtuales automáticamente, y facilitar la
creación de _wheels_ para empaquetar proyectos y publicarlos en
_[PyPI](https://pypi.org/)_ o en tu repositorio de paquetes privado.

### uv

[`uv`](https://docs.astral.sh/uv/) es una de las herramientas más recientes y eficientes
para la gestión de entornos virtuales y dependencias en Python, y es la que personalmente
utilizo y recomiendo. Su objetivo principal es simplificar y acelerar tareas que
tradicionalmente requieren múltiples herramientas, como `pip`, `poetry` o `venv`.

Una de sus principales ventajas es la posibilidad de crear un entorno virtual por
proyecto. Esta es la mejor práctica, ya que así evitamos mezclar dependencias entre
proyectos, lo que puede llevar a conflictos entre versiones.

Lo que más me ha impresionado de `uv` es su velocidad, en parte gracias a que utiliza
Rust para instalar y resolver dependencias en milisegundos, superando a `pip` y `poetry`.
Además, permite crear un sistema similar a `cargo` de Rust, basado en archivos
`pyproject.toml`, donde podemos definir metadatos de nuestro proyecto, gestionar paquetes
con sus versiones, especificar la versión de Python requerida, así como configuraciones
específicas de proyectos que instalemos, como linters o similares.

Por otro lado, `uv` permite la **gestión automática de entornos**, no requiere
configuraciones adicionales para crear y mantener entornos virtuales, por lo que no
necesitas tener instalado Python en el sistema que estés utilizando, `uv` lo hace de
forma automática.

## Utilidades para la gestión de entornos

En el desarrollo de software con Python, la creación de un entorno virtual es una
práctica necesaria.

Este proceso consiste en generar una instancia aislada del intérprete de Python,
permitiendo que las dependencias de un proyecto específico no interfieran con las
bibliotecas globales del sistema ni con otros desarrollos simultáneos. Esta segmentación
garantiza la reproducibilidad del código y evita conflictos de versiones.

A continuación, se describen los procedimientos para la gestión de entornos según la
herramienta seleccionada:

=== "VENV"

      1.  **Preparación del repositorio**: Para acceder a versiones específicas de Python que
         pueden no estar presentes en los repositorios oficiales de la distribución, se añade
         el repositorio especializado:
         ```bash
         sudo add-apt-repository ppa:deadsnakes/ppa
         sudo apt update
         ```
      2.  **Instalación del entorno de ejecución**: Se procede a instalar la versión deseada
         de Python (por ejemplo, la 3.10) junto con los binarios de desarrollo y el gestor de
         paquetes `pip`:
         ```bash
         sudo apt install python3.10 python3.10-venv python3.10-dev python3-pip
         ```
      3.  **Despliegue y activación**: Se genera la estructura del entorno dentro del
         directorio del proyecto y se activa para que el intérprete actual apunte a dicha
         ubicación:
         ```bash
         python3.10 -m venv nombre_del_entorno
         source nombre_del_entorno/bin/activate
         ```

=== "Anaconda"

      1.  **Instalación inicial**: El proceso comienza con la descarga e instalación de la
         suite desde su portal oficial. En sistemas Windows, se recomienda el uso del
         _Anaconda Prompt_ para garantizar que las variables de entorno estén correctamente
         configuradas.
      2.  **Gestión de entornos con Conda**: A diferencia de otras herramientas, Conda permite
         definir la versión de Python de forma explícita durante la creación:
         ```bash
         conda create --name nombre_del_entorno python=3.10
         ```
      3.  **Activación e interoperabilidad**: Una vez activado el entorno, es posible integrar
         `pip` si una librería no se encuentra en los canales de Conda, aunque se debe
         proceder con cautela para evitar inconsistencias:
         ```bash
         conda activate nombre_del_entorno
         conda install pip
         pip install --upgrade pip
         ```

=== "Poetry"

      1.  **Configuración del entorno local**: Para facilitar la visibilidad y el
         mantenimiento, es recomendable configurar Poetry de modo que aloje los entornos
         virtuales dentro de la carpeta raíz del proyecto:
         ```bash
         pip install poetry
         poetry config virtualenvs.in-project true
         ```
      2.  **Inicialización y despliegue**: Al crear un nuevo proyecto, la herramienta genera
         automáticamente la estructura de archivos necesaria y, tras la instalación de
         dependencias, gestiona la creación del entorno virtual de forma transparente:
         ```bash
         poetry new nombre_del_proyecto
         cd nombre_del_proyecto
         poetry install
         ```

=== "uv"

      1.  **Instalación y configuración inicial**: Se instala mediante un script de ejecución
         rápida que configura el binario en el sistema:
         ```bash
         curl -LsSf https://astral.sh/uv/install.sh | sh
         ```
      2.  **Ciclo de vida del proyecto**: El flujo de trabajo con `uv` permite inicializar un
         proyecto y crear su entorno virtual correspondiente con una latencia mínima:
         ```bash
         uv init nombre_del_proyecto
         cd nombre_del_proyecto
         uv venv
         uv pip install nombre_del_paquete
         ```

### Gestión de la caché

En muchas ocasiones, estos gestores de entorno almacenan en caché la información de los
paquetes que instalan, lo que puede llevar a ocupar una gran cantidad de espacio en el
disco o incluso generar conflictos cuando tenemos paquetes corruptos. Para liberar
espacio o solucionar problemas con dependencias, se puede purgar/eliminar la caché con
los siguientes comandos:

=== "PIP"

      ```bash linenums="1"
      pip cache purge
      ```

=== "Anaconda"

      ```bash linenums="1"
      conda clean --all
      ```

=== "Poetry"

      ```bash linenums="1"
      poetry cache clear --all
      ```

=== "uv"

      ```bash linenums="1"
      uv cache clean
      ```

### Actualización de paquetes

El software evoluciona de forma continua. Los paquetes que se utilizan habitualmente
incorporan nuevas funcionalidades o corrigen errores y vulnerabilidades de seguridad en
versiones posteriores. Por lo tanto, mantener las dependencias actualizadas es clave para
el correcto funcionamiento del proyecto.

=== "PIP"

      1. Actualizar todos los paquetes

         Puedes utilizar el siguiente comando para actualizar todos los paquetes:

         ```bash linenums="1"
         pip freeze | grep -v "^\-e" | cut -d = -f 1 | xargs -n1 pip install -U
         ```

         Donde:

         - `pip freeze`: Genera una lista de los paquetes instalados.
         - `grep -v "^\-e"`: Excluye las instalaciones en modo editable.
         - `cut -d = -f 1`: Extrae solo los nombres de los paquetes, sin las versiones.
         - `xargs -n1 pip install -U`: Actualiza cada paquete.

      2. Actualizar un paquete específico

         Para actualizar un paquete específico:

         ```bash linenums="1"
         pip install --upgrade nombre_del_paquete
         ```

=== "Anaconda"

      1. Actualizar todos los paquetes

         Aunque Anaconda permite la instalación de paquetes con PIP, se recomienda evitar
         mezclar paquetes del repositorio de Anaconda y PIP, ya que esto podría causar
         conflictos. Si decides usar paquetes de Anaconda, puedes actualizar todos los
         paquetes con:

         ```bash linenums="1"
         conda update --all
         ```

      2. Actualizar un paquete específico

         Para actualizar un paquete específico:

         ```bash linenums="1"
         conda update nombre_del_paquete
         ```

=== "Poetry"

      1. Actualizar todos los paquetes

         ```bash linenums="1"
         poetry update
         ```

      2. Actualizar un paquete específico

         Para actualizar un paquete específico:

         ```bash linenums="1"
         poetry update nombre_del_paquete
         ```

=== "uv"

      1. Actualizar todos los paquetes

         ```bash linenums="1"
         uv pip install --upgrade $(uv pip list --format=freeze | cut -d = -f 1 | tr '\n' ' ')
         ```

      2. Actualizar un paquete específico

         ```bash linenums="1"
         uv pip install --upgrade nombre_del_paquete
         ```

### Instalación de paquetes desde un archivo de requisitos

Cuando un proyecto necesita dependencias específicas, es útil usar un archivo
`requirements.txt`. Aunque hoy en día, con sistemas como los que ofrecen los ficheros
`toml` en uv o Poetry, cada vez lo recomiendo menos, en el caso de que lo necesites, aquí
tienes los pasos a seguir:

1.  **Crear un archivo `requirements.txt`** con los paquetes y versiones deseadas:

    ```plaintext
    numpy==1.21.0
    pandas>=1.3.0
    requests
    ```

2.  **Instalar los paquetes desde el archivo**:

=== "PIP"

      ```bash
      pip install -r requirements.txt
      ```

=== "Poetry"

      ```bash
      poetry install
      ```

=== "uv"

      ```bash
      uv pip install -r requirements.txt
      ```

### Eliminar un entorno

=== "VENV, Poetry, uv"

      En la mayoría de los casos, los entornos creados con `VENV`, `Poetry` y `uv` se alojan
      dentro del propio directorio del proyecto. Por ello, si ya no los necesitas, basta con
      eliminar la carpeta correspondiente para borrar por completo el entorno junto con toda
      su información.

      ```bash
      rm -rf nombre_del_entorno
      ```

=== "Anaconda"

      1.  **Listar los entornos disponibles**:

         ```bash
         conda env list
         ```

      2.  **Eliminar un entorno**:

         ```bash
         conda env remove --name nombre_del_entorno
         ```

### Integración del entorno con Jupyter

Para utilizar un entorno virtual dentro de **Jupyter**, es necesario seguir estos pasos:

1.  **Instalar `ipykernel` en el entorno**: Primero, debes añadir `ipykernel` como
    dependencia dentro del entorno virtual. Para ello, instala el paquete utilizando el
    gestor de dependencias correspondiente (por ejemplo, `pip`, `poetry`, `uv` o
    `conda`).
2.  **Registrar el entorno en Jupyter**: Este paso es necesario únicamente cuando el
    entorno virtual se encuentra en un directorio diferente al del proyecto. En la
    mayoría de los entornos de desarrollo, como **VSCode**, si el entorno está dentro del
    directorio del proyecto, se detectará automáticamente y podrás seleccionar el kernel
    asociado sin pasos adicionales. En caso de que necesites registrar el entorno
    manualmente, ejecuta:

```bash linenums="1"
python -m ipykernel install --user --name=nombre_del_entorno
```

En el caso de utilizar `uv`, si has empleado el comando `uv venv`, por defecto `uv`
creará un entorno en la raíz del proyecto en la que te encuentras, con la versión de
Python especificada en el `pyproject.toml`. Con ello, al utilizar Jupyter Notebooks,
VSCode detectará directamente que el entorno se encuentra en la raíz del proyecto sin
necesidad de ejecutar los comandos anteriores.

### Eliminación de paquetes instalados

=== "PIP"

      Eliminar todos los paquetes

      ```bash
      pip list --format=freeze > installed.txt
      pip uninstall -r installed.txt -y
      ```

      Eliminar un paquete específico

      ```bash
      pip uninstall nombre_del_paquete
      ```

=== "Anaconda"

      ```bash
      conda remove nombre_del_paquete
      ```

=== "Poetry"

      ```bash
      poetry remove nombre_del_paquete
      ```

=== "uv"

      ```bash
      uv pip uninstall nombre_del_paquete
      ```
