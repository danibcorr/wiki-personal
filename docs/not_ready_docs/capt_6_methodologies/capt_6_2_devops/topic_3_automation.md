---

authors:
Daniel Bazo Correa
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

**GitHub** es una plataforma de desarrollo colaborativo diseñada para la gestión de
proyectos de software. Proporciona herramientas avanzadas para el control de versiones
mediante **Git**, así como funcionalidades para la integración y entrega continua
(_Continuous Integration_ - CI y _Continuous Deployment_ - CD, respectivamente).

Con el tiempo, GitHub se ha consolidado como una herramienta esencial para
desarrolladores y equipos de software. Entre sus características destacadas se
encuentran:

- **GitHub Actions**: Permite la automatización de flujos de trabajo directamente dentro
  de los repositorios, facilitando la integración con servicios externos y optimizando
  procesos de desarrollo.
- **GitHub Pages**: Ofrece una manera sencilla de publicar sitios web estáticos
  directamente desde un repositorio.

Una de las principales ventajas de utilizar **GitHub Actions** en lugar de herramientas
como **Jenkins**, u otras soluciones similares, es su integración nativa con GitHub.
Además, su **Marketplace** proporciona un amplio catálogo de acciones desarrolladas tanto
por GitHub como por terceros, lo que permite extender y personalizar los flujos de
trabajo de manera eficiente.

## CI/CD con GitHub Actions

La implementación de **CI/CD** permite automatizar procesos de desarrollo, mejorando la
eficiencia y reduciendo errores en la integración y despliegue de software.

- **CI (_Continuous Integration_)**: Se refiere a la automatización de la integración de
  código en un repositorio compartido, asegurando que los cambios sean validados
  continuamente mediante pruebas y compilaciones.
- **CD (_Continuous Deployment_)**: Automatiza el proceso de despliegue de código en
  entornos de producción, facilitando la entrega continua de nuevas versiones del
  software.

### GitHub Actions y su funcionamiento

**GitHub Actions** es una plataforma que permite la automatización de flujos de trabajo a
través de archivos de configuración en formato YAML.

Cada **workflow** está compuesto por una serie de pasos organizados en **jobs**, que
pueden ejecutarse en paralelo o en secuencia, dependiendo de las necesidades del
proyecto.

El **runner** de GitHub Actions es un servidor que ejecuta estos **workflows** en un
entorno definido, permitiendo:

- Compilación del código para distintos sistemas operativos.
- Ejecución de pruebas en paralelo.
- Validación de código con herramientas como linters y analizadores estáticos.
- Implementación de código en producción o entornos de staging.

Para definir un **workflow**, se crea un archivo `.yml` dentro de la carpeta
`.github/workflows/`, por ejemplo:

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
  <em>Logo de GitHub</em>  
</p>

Un **pipeline** típico en un **workflow** podría incluir pasos como:

1. Fusionar (merge) cambios en la rama principal.
2. Ejecutar pruebas.
3. Realizar un análisis de código (_linting_).
4. Generar una compilación (_build_).
5. Desplegar en producción o staging.

## Estructura de un Workflow en GitHub Actions

Un **workflow** en GitHub Actions está definido en un archivo de configuración YAML (por
ejemplo, `workflow.yml`). Este archivo contiene las instrucciones necesarias para
automatizar tareas dentro de un repositorio.

### Elementos clave de un workflow

- **Nombre del Workflow (`name`)**: El campo `name` define un nombre descriptivo para el
  workflow. Aunque es opcional, se recomienda utilizarlo para mejorar la identificación y
  reutilización de workflows dentro del repositorio.

  ```yaml
  name: Nombre del Workflow
  ```

- **Disparadores (`on`)**: Los disparadores (`on`) determinan cuándo debe ejecutarse el
  workflow. Pueden activarse mediante eventos como `push`, `pull_request` o ejecuciones
  programadas. También es posible definir **permisos** a nivel global o dentro de un
  **job** específico. Si varios jobs requieren los mismos permisos, es recomendable
  declararlos a nivel del workflow en lugar de repetirlos en cada job.

  ???+ example "Ejemplo"

  Definición de permisos a nivel de **workflow**

  ```yaml
  name: Nombre del Workflow

  on:
    push:
      branches: ["main"]
    workflow_call:

  permissions:
    contents: write
  ```

  Definición de permisos dentro de un **job**

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
      Checkout repository
          uses: actions/checkout@v4
  ```

- **Jobs (`jobs`)**: Los **jobs** representan las unidades de trabajo dentro de un
  workflow. Cada **job** se compone de una serie de **steps** que definen las acciones a
  ejecutar de manera secuencial. Por defecto, los **jobs** se ejecutan en paralelo a
  menos que uno dependa explícitamente de otro. Cada **job** se ejecuta en una nueva
  máquina virtual. Se debe especificar un sistema operativo con `runs-on`, permitiendo
  elegir entre Linux, macOS y Windows.

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

???+ example "Ejemplo" básico

El siguiente ejemplo muestra un workflow que se ejecuta cuando hay un `push` o un
`pull_request` en la rama `main`.

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
    Checkout repository
        uses: actions/checkout@v4
```

!!!note "Nota"

    Se recomienda incluir la acción `checkout` al inicio del workflow para asegurarse de que
    el código más reciente esté disponible antes de ejecutar cualquier otra tarea.

???+ example "Ejemplo" configuración de Python, Poetry y Flake8

En este ejemplo, el workflow configura Python, administra dependencias con Poetry y
valida el código con Flake8.

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
    Checkout repository
        uses: actions/checkout@v4

    Instalar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

    Instalar Poetry
        uses: snok/install-poetry@v1

    Instalar dependencias con Poetry
        run: poetry install

    Verificar código con Flake8
        run: poetry run flake8 src/
```

???+ example "Ejemplo" uso de caché para optimización de **workflows**

Para mejorar el rendimiento, es posible utilizar caché para almacenar dependencias y
evitar reinstalaciones innecesarias.

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
    Checkout repository
        uses: actions/checkout@v4

    Instalar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

    Instalar Poetry
        uses: snok/install-poetry@v1
        with:
          virtualenvs-in-project: true

    Cargar caché de dependencias
        uses: actions/cache@v4
        id: cached-poetry-dependencies
        with:
          path: .venv
          key: venv-${{ runner.os }}-${{ hashFiles('**/poetry.lock') }}

    Instalar dependencias con Poetry
        if: steps.cached-poetry-dependencies.outputs.cache-hit != 'true'
        run: poetry install
```

!!!note "Nota"

La clave de caché `key: venv-${{ runner.os }}-${{ hashFiles('**/poetry.lock') }}`
garantiza que el caché solo se actualice cuando cambie el archivo `poetry.lock`. Utilizar
caché reduce significativamente el tiempo de ejecución del workflow, pero es importante
monitorearlo para evitar el uso de dependencias obsoletas.

### Modularización de workflows y acciones

Para mejorar la reutilización y mantenimiento del código, se recomienda modularizar los
workflows mediante acciones personalizadas. Un ejemplo de la estructura del proyecto
podría ser la siguiente:

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

Donde dentro de la carpeta `build-application` podríamos tener un ejemplo de accion, la
cual ha de tener siempre el nombre `action.yml`, tal que así:

```yml
name: Build Application

runs:
  using: composite

  steps:
  Checkout repository
      uses: actions/checkout@v4

  Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.10.7"

  Instalar Poetry
      uses: snok/install-poetry@v1
      with:
        virtualenvs-in-project: true

  Cargar caché de dependencias
      uses: actions/cache@v4
      id: cached-poetry-dependencies
      with:
        path: .venv
        key: venv-${{ runner.os }}-${{ hashFiles('**/poetry.lock') }}

  Instalar dependencias con Poetry
      if: steps.cached-poetry-dependencies.outputs.cache-hit != 'true'
      run: poetry install
```

La modularización de workflows no solo mejora la reutilización, sino que también facilita
el mantenimiento del código y la integración de nuevas funcionalidades sin modificar los
workflows principales. Este enfoque modular permite dividir la complejidad de los
workflows, mejorar la eficiencia y permitir la reutilización de configuraciones a lo
largo del proyecto.

### Uso de estrategias con matrices

Las **matrices de estrategia** en GitHub Actions permiten ejecutar un mismo **workflow**
en múltiples combinaciones de entornos, lo que es útil para probar software en diferentes
sistemas operativos, versiones o configuraciones.

Por ejemplo, podemos crear una matriz para múltiples sistemas operativos y versiones:

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

GitHub genera automáticamente **todas las combinaciones posibles** de los valores
definidos en `matrix`. Todas las combinaciones generadas se reflejan en la siguiente
tabla:

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

Del mismo modo, se excluyen las siguientes estrategias:

| OS             | Versión | Entorno     |
| -------------- | ------- | ----------- |
| macos-latest   | 12      | production  |
| windows-latest | 16      | _Cualquier_ |

Gracias al bloque `exclude`, estas combinaciones **no se ejecutarán** en el workflow.

Los beneficios del uso de matrices son:

- **Eficiencia:** Permite probar múltiples entornos en paralelo.
- **Flexibilidad:** Se pueden excluir combinaciones no necesarias.
- **Automatización escalable:** Ideal para probar en distintos sistemas sin escribir
  múltiples workflows.

Este enfoque es útil en proyectos que requieren pruebas en múltiples versiones de
software, diferentes entornos (staging/producción) o compatibilidad con varios sistemas
operativos.

# Otras

- GitHub Actions (Integración GitHub).

- Podemos utilizar múltiples S.O. (Linux, Mac, Windows) → Matrix.

- Wondflow → pipeline múltiples pasos (Example: Wondflow → Merge → Test → ... → build →
  Deploy).

- gitHub → Wondflow → Wondflow → Wondflow → Wondflow → Wondflow → WondFlow → WondFlow →
  WondFlow → WondFlow → WondFlow → Wondflow → WondFlow → WondFlow → WondFlow → Wondflow →
  Wondflow → WondFlow → WondFlow → Wondflow → WondFlow → Wondflow → WondFlow → WondFlow →
  Wondflow → Wondflow → Wondflow → Wondflow → WondFlwo → WondFlow → WondFlow → WondFlow →
  WondFlow → WondFlwo → WondFlow → WondFlow → WondFlow → WundFlow → WondFlow → WondFlow →
  WondFlow → WondFlow → WundFlow → WondFlwo → WondFlow → WondFlow → WondFlow → WondFlow →
  WondFlow → WondFlow → WondFlow → WondFlow.

- name: number project.
- para cuando "nacemos un trigger" del Wondflow.
- trabajo a realizar.

- Deudo de los jobs el run - ou es la máquina donde ejecutan el job (mirar
  documentación).
- Deudo de los jobs tenemos los steps.
- Deudo de los steps tenemos los uses para definir acciones ya existentes (mirar docu de
  cada acción).
- o crear nuestra propia acción.

- Al final cada job es ejecuto desde la raíz del rep (1).

- Permisos es mejor dentro de cada acción job.
- Cada job en un Wondflow se ejecuta en una máquina virtual.
- En la que por defecto funciona un paralelo.
- Salvo de otro (needs).

Para probar múltiples estrategias podemos utilizar:

- **stratégia**:  
  matrix

- **os**: [Ubuntu latest, Windows - Latest]

En un job, ahora variamos:

- **fun - ou**:  
  $$\frac{1}{2} \matrix{ \matrix{ \matrix{ \matrix{ \matrix{ \matrix{ \matrix{ \dots } } } } } } $$

## Jenkins

Jenkins permita escalar proyectos para llevarlos a producción de manera automática.
Jenkins es una aplicación basada en servidor que simplifiques facilita la integración y
la construcción. Utiliza plugins para utilizar servicios de terceros como proveedores de
la nube lo que hace Jenkins por ejemplo es comprobar los cómics del código cuando se
producen cambios y sean detectados. Jenkins los compila. Un besito construcción correcta
se inicia uno se levanta un Flack y si y si la construcción es correcta pues se despliega
Jenkins al final facilita el centro de de box que es construir el control de versiones,
la monitorización continua. El testeo continuo, la gestión de la configuración y el
despliegue continuo.

Jenkins se puede configurar de diferentes maneras teniendo configuración maestro esclavo
tenemos un Jenkins maestro que es el servidor principal que gestiona la interfaz el UVI y
los trabajos y asignación de tareas a los nuevos esclavos y luego tenemos los nuevos
esclavos que son máquinas adicionales que ejecutan las tareas asignadas por el Master que
pueden ser locales o remotos. La ventaja es una distribución de la carga escalabilidad y
aislamiento. Los tipos de plugin que son los más destacados son el de interfaz en July,
que son relacionados con la interfaz gráfica de Jenkins. Luego tenemos de plataformas
está relacionado con el sistema operativo administrativo que son para la gestión de
usuarios, permisos, etc. para la construcción pues por ejemplo para notificar el correcto
construcción de una aplicación o si hay fallos. Luego también tenemos para la gestión del
código fuente, que es para la comunicación entre Jenkins y el repositorio por ejemplo de
gitlab.

Para crear un Pipeline de Jenkins, lo mejor es crear un archivo conocido como Jenkins
Fire en la raíz del proyecto y cuando se hace un Puig lo detecta y hace un Trigger del
proceso silabario si la variedad es alta en cuanto a los tipos de equipos durante el
Bill, pues lo mejor será utilizar Ansible. Por ejemplo, si queremos conectar Jenkins con
Gisla, pues tenemos que instalar el plugin de iCloud crear un personal toquen desde los
ajustes del perfil de WhatsApp y luego ir a Jenkins a gestionar Jenkins y luego en la
parte de configuración del sistema pues aparecerá una opción para crear un enlace con
GitHub
