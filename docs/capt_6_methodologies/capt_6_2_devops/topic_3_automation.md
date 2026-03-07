---
authors: Daniel Bazo Correa
description: Herramientas necesarias para DevOps.
title: GitHub Actions
---

## Bibliografía

- [ML in Production: From Data Scientist to ML Engineer](https://www.udemy.com/course/ml-in-production/?couponCode=SKILLS4SALEA)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## Introducción

<p align="center">
  <img src="/assets/img/docs/logos/github-logo.png" width="500"/>
  <br />
  <em>Logo de GitHub</em>
</p>

GitHub es una plataforma de desarrollo colaborativo diseñada para la gestión de proyectos
de software. Proporciona herramientas avanzadas para el control de versiones mediante
Git, así como funcionalidades para la integración y entrega continua (_Continuous
Integration_ - CI y _Continuous Deployment_ - CD, respectivamente). Con el tiempo, GitHub
se ha consolidado como una herramienta esencial para desarrolladores y equipos de
software, destacando entre sus características GitHub Actions, que permite la
automatización de flujos de trabajo directamente dentro de los repositorios facilitando
la integración con servicios externos, y GitHub Pages, que ofrece una manera sencilla de
publicar sitios web estáticos directamente desde un repositorio.

Una de las principales ventajas de utilizar GitHub Actions en lugar de herramientas como
Jenkins u otras soluciones similares es su integración nativa con GitHub. Además, su
Marketplace proporciona un amplio catálogo de acciones desarrolladas tanto por GitHub
como por terceros, lo que permite extender y personalizar los flujos de trabajo de manera
eficiente.

## CI/CD con GitHub Actions

La implementación de CI/CD permite automatizar procesos de desarrollo, mejorando la
eficiencia y reduciendo errores en la integración y despliegue de software. La
integración continua (CI) se refiere a la automatización de la integración de código en
un repositorio compartido, asegurando que los cambios sean validados continuamente
mediante pruebas y compilaciones. El despliegue continuo (CD) automatiza el proceso de
despliegue de código en entornos de producción, facilitando la entrega continua de nuevas
versiones del software.

### GitHub Actions y su funcionamiento

GitHub Actions es una plataforma que permite la automatización de flujos de trabajo a
través de archivos de configuración en formato YAML. Cada _workflow_ está compuesto por
una serie de pasos organizados en _jobs_, que pueden ejecutarse en paralelo o en
secuencia dependiendo de las necesidades del proyecto.

El _runner_ de GitHub Actions es un servidor que ejecuta estos _workflows_ en un entorno
definido, permitiendo la compilación del código para distintos sistemas operativos, la
ejecución de pruebas en paralelo, la validación de código con herramientas como _linters_
y analizadores estáticos, y la implementación de código en producción o entornos de
_staging_.

Para definir un _workflow_, se crea un archivo `.yml` dentro de la carpeta
`.github/workflows/`:

```plaintext
src
│
.github
│   ├── workflows
│   │   ├── workflow_ejemplo.yml
```

<p align="center">
  <img src="/assets/img/docs/workflow-github-actions.png"/>
  <br />
  <em>Esquema de un workflow en GitHub Actions</em>
</p>

Un _pipeline_ típico en un _workflow_ podría incluir pasos como fusionar (_merge_)
cambios en la rama principal, ejecutar pruebas, realizar un análisis de código
(_linting_), generar una compilación (_build_) y desplegar en producción o _staging_.

## Estructura de un Workflow en GitHub Actions

Un _workflow_ en GitHub Actions está definido en un archivo de configuración YAML que
contiene las instrucciones necesarias para automatizar tareas dentro de un repositorio.

### Elementos clave de un workflow

El campo `name` define un nombre descriptivo para el _workflow_. Aunque es opcional, se
recomienda utilizarlo para mejorar la identificación y reutilización de _workflows_
dentro del repositorio:

```yaml
name: Nombre del Workflow
```

Los disparadores (`on`) determinan cuándo debe ejecutarse el _workflow_. Pueden activarse
mediante eventos como `push`, `pull_request` o ejecuciones programadas. También es
posible definir permisos a nivel global o dentro de un _job_ específico. Si varios _jobs_
requieren los mismos permisos, es recomendable declararlos a nivel del _workflow_ en
lugar de repetirlos en cada _job_.

???+ example "Ejemplo"

    Definición de permisos a nivel de _workflow_:

    ```yaml
    name: Nombre del Workflow

    on:
      push:
        branches: ["main"]
      workflow_call:

    permissions:
      contents: write
    ```

    Definición de permisos dentro de un _job_:

    ```yaml
    name: Nombre del Workflow

    on:
      push:
        branches: ["main"]
      workflow_call:

    jobs:
      build-mkdocs:
        name: Build MkDocs Wiki
        runs-on: ubuntu-latest
        needs: setup-lint-test

        permissions:
          contents: write

        steps:
          - name: Checkout repository
            uses: actions/checkout@v4
    ```

Los _jobs_ representan las unidades de trabajo dentro de un _workflow_. Cada _job_ se
compone de una serie de _steps_ que definen las acciones a ejecutar de manera secuencial.
Por defecto, los _jobs_ se ejecutan en paralelo a menos que uno dependa explícitamente de
otro mediante la directiva `needs`. Cada _job_ se ejecuta en una nueva máquina virtual, y
se debe especificar un sistema operativo con `runs-on`, permitiendo elegir entre Linux,
macOS y Windows:

???+ example "Ejemplo"

    ```yaml
    jobs:
      nombre-del-job:
        runs-on: ubuntu-latest
    ```

    !!!note "Nota"

        Consulta la documentación oficial sobre runners de GitHub
        [aquí](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/about-github-hosted-runners).

GitHub Actions permite integrar acciones predefinidas disponibles en
[GitHub Actions](https://github.com/actions) y el
[GitHub Marketplace](https://github.com/marketplace).

### Ejemplos de configuración de workflows

???+ example "Ejemplo básico"

    El siguiente ejemplo muestra un _workflow_ que se ejecuta cuando hay un `push` o un `pull_request` en la rama `main`:

    ```yaml
    name: Workflow básico

    on:
      push:
        branches: ["main"]
      pull_request:
        branches: ["main"]

    permissions:
      contents: read

    jobs:
      build:
        runs-on: ubuntu-latest

        steps:
          - name: Checkout repository
            uses: actions/checkout@v4
    ```

    !!!note "Nota"

        Se recomienda incluir la acción `checkout` al inicio del workflow para asegurarse de que
        el código más reciente esté disponible antes de ejecutar cualquier otra tarea.

???+ example "Ejemplo: Configuración de Python, Poetry y Flake8"

    En este ejemplo, el _workflow_ configura Python, administra dependencias con Poetry y valida el código con Flake8:

    ```yaml
    name: Verificación con Flake8

    on:
      push:
        branches: ["main"]
      pull_request:
        branches: ["main"]

    permissions:
      contents: read

    jobs:
      build:
        runs-on: ubuntu-latest

        steps:
          - name: Checkout repository
            uses: actions/checkout@v4

          - name: Instalar Python
            uses: actions/setup-python@v5
            with:
              python-version: "3.10"

          - name: Instalar Poetry
            uses: snok/install-poetry@v1

          - name: Instalar dependencias con Poetry
            run: poetry install

          - name: Verificar código con Flake8
            run: poetry run flake8 src/
    ```

???+ example "Ejemplo: Uso de caché para optimización de workflows"

    Para mejorar el rendimiento, es posible utilizar caché para almacenar dependencias y evitar reinstalaciones innecesarias:

    ```yaml
    name: Workflow con caché

    on:
      push:
        branches: ["main"]
      pull_request:
        branches: ["main"]

    permissions:
      contents: read

    jobs:
      build:
        runs-on: ubuntu-latest

        steps:
          - name: Checkout repository
            uses: actions/checkout@v4

          - name: Instalar Python
            uses: actions/setup-python@v5
            with:
              python-version: "3.10"

          - name: Instalar Poetry
            uses: snok/install-poetry@v1
            with:
              virtualenvs-in-project: true

          - name: Cargar caché de dependencias
            uses: actions/cache@v4
            id: cached-poetry-dependencies
            with:
              path: .venv
              key: venv-${{ runner.os }}-${{ hashFiles('**/poetry.lock') }}

          - name: Instalar dependencias con Poetry
            if: steps.cached-poetry-dependencies.outputs.cache-hit != 'true'
            run: poetry install
    ```

    !!!note "Nota"

        La clave de caché `key: venv-${{ runner.os }}-${{ hashFiles('**/poetry.lock') }}`
        garantiza que el caché solo se actualice cuando cambie el archivo `poetry.lock`. Utilizar
        caché reduce significativamente el tiempo de ejecución del workflow, pero es importante
        monitorearlo para evitar el uso de dependencias obsoletas.

### Modularización de workflows y acciones

Para mejorar la reutilización y el mantenimiento del código, se recomienda modularizar
los _workflows_ mediante acciones personalizadas. Un ejemplo de la estructura del
proyecto podría ser la siguiente:

```plaintext
src
│
.github
|   ├── actions
|       ├── build-application
|           ├── action.yml
|   ├── workflows
│       ├── lint.yml
```

Dentro de la carpeta `build-application` se define una acción, que siempre debe tener el
nombre `action.yml`:

```yml
name: Build Application

runs:
  using: composite

  steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.10.7"

    - name: Instalar Poetry
      uses: snok/install-poetry@v1
      with:
        virtualenvs-in-project: true

    - name: Cargar caché de dependencias
      uses: actions/cache@v4
      id: cached-poetry-dependencies
      with:
        path: .venv
        key: venv-${{ runner.os }}-${{ hashFiles('**/poetry.lock') }}

    - name: Instalar dependencias con Poetry
      if: steps.cached-poetry-dependencies.outputs.cache-hit != 'true'
      run: poetry install
```

La modularización de _workflows_ no solo mejora la reutilización, sino que también
facilita el mantenimiento del código y la integración de nuevas funcionalidades sin
modificar los _workflows_ principales. Este enfoque modular permite dividir la
complejidad, mejorar la eficiencia y permitir la reutilización de configuraciones a lo
largo del proyecto.

### Uso de estrategias con matrices

Las matrices de estrategia en GitHub Actions permiten ejecutar un mismo _workflow_ en
múltiples combinaciones de entornos, lo que resulta útil para probar software en
diferentes sistemas operativos, versiones o configuraciones. Por ejemplo:

```yml
name: Workflow

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

strategy:
  matrix:
    os: [macos-latest, windows-latest]
    version: [12, 14, 16]
    environment: [staging, production]
    exclude:
      - os: macos-latest
        version: 12
        environment: production
      - os: windows-latest
        version: 16
runs-on: ${{ matrix.os }}
```

GitHub genera automáticamente todas las combinaciones posibles de los valores definidos
en `matrix`. Las combinaciones resultantes se reflejan en la siguiente tabla:

| OS             | Versión | Entorno    |
| -------------- | ------- | ---------- |
| macos-latest   | 12      | staging    |
| macos-latest   | 14      | staging    |
| macos-latest   | 14      | production |
| macos-latest   | 16      | staging    |
| macos-latest   | 16      | production |
| windows-latest | 12      | staging    |
| windows-latest | 12      | production |
| windows-latest | 14      | staging    |
| windows-latest | 14      | production |

Gracias al bloque `exclude`, las siguientes combinaciones no se ejecutan en el
_workflow_:

| OS             | Versión | Entorno    |
| -------------- | ------- | ---------- |
| macos-latest   | 12      | production |
| windows-latest | 16      | Cualquiera |

Los beneficios del uso de matrices incluyen la eficiencia al probar múltiples entornos en
paralelo, la flexibilidad para excluir combinaciones no necesarias y la automatización
escalable, ideal para probar en distintos sistemas sin escribir múltiples _workflows_.
Este enfoque resulta especialmente útil en proyectos que requieren pruebas en múltiples
versiones de software, diferentes entornos (_staging_/producción) o compatibilidad con
varios sistemas operativos.

## Jenkins

Jenkins es una aplicación basada en servidor, de código abierto, que facilita la
integración continua y la automatización de la construcción, pruebas y despliegue de
software. Utiliza un sistema de _plugins_ para integrarse con servicios de terceros, como
proveedores de la nube, repositorios de código y herramientas de notificación. Su
funcionamiento se basa en la detección de cambios en el código fuente: cuando se producen
_commits_, Jenkins los compila y, si la construcción es correcta, procede al despliegue;
en caso contrario, genera alertas para que el equipo pueda actuar rápidamente.

Jenkins abarca las principales etapas del ciclo DevOps: control de versiones, integración
continua, monitorización continua, testeo continuo, gestión de la configuración y
despliegue continuo.

### Arquitectura maestro-esclavo

Jenkins se puede configurar en una arquitectura maestro-esclavo. El nodo maestro es el
servidor principal que gestiona la interfaz de usuario, la programación de trabajos y la
asignación de tareas a los nodos esclavos. Los nodos esclavos son máquinas adicionales,
locales o remotas, que ejecutan las tareas asignadas por el maestro. Esta arquitectura
ofrece ventajas significativas en cuanto a distribución de la carga, escalabilidad y
aislamiento de entornos de ejecución.

### Tipos de plugins

Los _plugins_ más destacados de Jenkins se agrupan en varias categorías: los de interfaz,
relacionados con la interfaz gráfica de Jenkins; los de plataforma, vinculados al sistema
operativo; los administrativos, destinados a la gestión de usuarios y permisos; los de
construcción, que permiten notificar el resultado de la compilación de una aplicación; y
los de gestión del código fuente, que facilitan la comunicación entre Jenkins y
repositorios como GitLab o GitHub.

### Creación de pipelines

Para crear un _pipeline_ en Jenkins, la práctica recomendada consiste en definir un
archivo conocido como `Jenkinsfile` en la raíz del proyecto. Cuando se realiza un _push_
al repositorio, Jenkins lo detecta y ejecuta automáticamente el _pipeline_ definido. Si
la variedad de entornos de ejecución es alta durante la fase de construcción, resulta
conveniente complementar Jenkins con herramientas de aprovisionamiento como Ansible.

### Integración con GitHub

Para conectar Jenkins con GitHub es necesario instalar el _plugin_ de GitHub en Jenkins,
crear un _personal access token_ desde los ajustes del perfil de GitHub y, a
continuación, configurar el enlace en la sección de configuración del sistema de Jenkins,
donde aparece la opción para establecer la conexión con GitHub mediante dicho token.
