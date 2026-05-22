---
authors: Daniel Bazo Correa
description: Conoce las claves esenciales para crear código sostenible.
title: Código sostenible
---

## Principios

El desarrollo de un proyecto debe realizarse bajo una estructura de código clara y
sostenible, utilizando herramientas y metodologías para garantizar su organización y
limpieza. Estas prácticas son fundamentales durante el desarrollo, puesta en producción
y evolución del proyecto.

### Estructura del proyecto

Un proyecto debe estar organizado en dos partes principales:

1. **Directorio de la aplicación:** Contiene la lógica del código, la configuración de
   los modelos, los registros (_logs_), entre otros componentes.
2. **Ajustes y configuraciones:** Incluye configuraciones y dependencias del proyecto,
   como los archivos de gestión de dependencias (Poetry), Dockerfiles, archivos de
   configuración `.yml`, etc.

Esta separación promueve un código modular, organizado y fácil de mantener. Facilita la
colaboración entre miembros del equipo, simplifica el proceso de actualización y mejora
la comprensión de la estructura del proyecto por parte de nuevos desarrolladores.

Ejemplo de estructura de proyecto:

```plaintext linenums="1"
src (o nombre del proyecto)
│
├── config
│   ├── config.py
│   ├── .env
├── db
├── logs
├── model
│   ├── models
│   ├── pipeline
│   ├── inference.py
├── main.py
```

### Código limpio

La guía de estilo [PEP 8](https://pep8.org/) define convenciones para escribir código
Python que sea legible y consistente. A continuación, se destacan sus principales
recomendaciones. Además, se sugieren herramientas como
[Black](https://pypi.org/project/black/) y [Ruff](https://docs.astral.sh/ruff/) para
aplicar estas convenciones automáticamente en los proyectos.

#### Diseño del código

- Se debe utilizar una indentación de 4 espacios, sin mezclar espacios y tabuladores.
- La longitud máxima de las líneas es de 79 caracteres; para comentarios y docstrings,
  es de 72 caracteres.
- Las líneas largas deben dividirse usando paréntesis, corchetes o llaves para mejorar
  la legibilidad.

Ejemplo:

```py linenums="1"
def funcion_larga(parametro1, parametro2,
                  parametro3, parametro4):
    return parametro1 + parametro2 + parametro3 + parametro4
```

#### Codificación de archivos y cadenas

- Los archivos fuente deben utilizar codificación UTF-8.
- Se pueden emplear comillas simples o dobles para las cadenas, pero es importante
  mantener la consistencia.
- Para cadenas multilínea, se prefieren las comillas dobles.

```py linenums="1"
cadena_simple = 'Hola mundo'
cadena_doble = "Hola mundo"
cadena_multilinea = """
    Esta es una cadena
    que ocupa varias líneas
"""
```

#### Importaciones

Las importaciones deben estar ubicadas al principio del archivo y organizadas en el
siguiente orden:

1. Biblioteca estándar de Python.
2. Bibliotecas de terceros.
3. Importaciones locales.

Se recomienda utilizar importaciones absolutas.

```py linenums="1"
import os
import sys

from external_lib import some_function

from local_module import local_function
```

#### Espacios en blanco

- No se deben añadir espacios adicionales alrededor de paréntesis, corchetes, llaves,
  comas o dos puntos.
- Se debe agregar un espacio alrededor de operadores de asignación, comparación y
  booleanos.

```py linenums="1"
x = 5
y = x + 1
if x == y:
    print(f"x:{x}, y:{y}")
```

#### Comentarios y docstrings

- Los comentarios deben ser claros y concisos, utilizando oraciones completas para
  describir el propósito del código.
- Los **docstrings** son obligatorios para módulos, funciones, clases y métodos
  públicos, describiendo su funcionalidad y parámetros.

```py linenums="1"
def suma(a, b):
    """
    Suma dos números y devuelve el resultado.

    Args:
        a (int): Primer número.
        b (int): Segundo número.

    Returns:
        int: La suma de a y b.
    """
    return a + b
```

#### Convenciones de nomenclatura

- **Paquetes y módulos:** Se deben escribir en minúsculas, sin espacios (ej.
  `mi_modulo`).
- **Clases:** Usar el estilo CapWords, también conocido como CamelCase (ej. `MiClase`).
- **Funciones y variables:** Utilizar minúsculas con guiones bajos (ej. `mi_funcion`).
- **Constantes:** Escribir en mayúsculas con guiones bajos (ej. `MI_CONSTANTE`).
- **Métodos y variables de instancia:** Como las funciones, con un guion bajo inicial
  para los elementos no públicos (ej. `_variable_interna`).

```py linenums="1"
class MiClase:
    MI_CONSTANTE = 42

    def __init__(self):
        self._variable_interna = 10

    def metodo_publico(self):
        return self._variable_interna
```

### Principios de código limpio

Más allá de las convenciones de estilo, el código limpio se rige por principios que
favorecen la legibilidad, el mantenimiento y la escalabilidad:

- **Separación de responsabilidades**: Cada parte del código debe tener una tarea
  específica. Una función, una única tarea.
- **Minimizar dependencias entre módulos**: Diseñar módulos como si fueran
  microservicios, con interfaces claras y acoplamiento mínimo.
- **_Naming_ descriptivo**: Utilizar nombres de variables y funciones fáciles de
  interpretar, buscar y entender.
- **Evitar comentarios innecesarios**: Si el código necesita un comentario para
  explicarse, es preferible extraer una función o variable con un nombre descriptivo.
- **Principio de responsabilidad única**: No agrupar toda la lógica en clases cuando la
  programación funcional puede ser suficiente.
- **Validación cerca de los datos**: La validación debe estar siempre lo más cerca
  posible de la fuente de datos.

### _Clean Architecture_

_Clean Architecture_ propone una separación clara entre la **lógica de negocio**
(aquello que no está limitado por la tecnología) y la **lógica de la aplicación** (que
depende de la tecnología utilizada). El objetivo es que el código sea elegante, robusto,
mantenible, escalable y funcional.

La arquitectura se organiza en capas concéntricas con dependencias que apuntan siempre
hacia el interior:

| Capa (de interior a exterior) | Responsabilidad                                                               |
| :---------------------------- | :---------------------------------------------------------------------------- |
| **Dominio**                   | Entidades y reglas de negocio puras. No conoce las capas exteriores.          |
| **Casos de uso (Aplicación)** | Orquesta la lógica de negocio. El dominio no sabe de los casos de uso.        |
| **Adaptadores**               | Convierte datos entre el formato de los casos de uso y el del mundo exterior. |
| **Externo (Infraestructura)** | _Frameworks_, bases de datos, UI, navegador, APIs externas.                   |

Un flujo típico sería: el usuario accede a la capa de **presentación** (externa), que
invoca la capa de **aplicación**, la cual se comunica con la **infraestructura** (base
de datos) y opera sobre el **dominio**. Esta estructura de capas se refleja directamente
en la organización de carpetas del proyecto, lo que facilita una división clara de la
lógica y la aplicación de buenas prácticas.

## Versionado semántico (SemVer)

El versionado semántico (_Semantic Versioning_) es un sistema estandarizado para
controlar las versiones del software, representado mediante el formato `X.Y.Z`:

| Componente    | Significado   | Se incrementa cuando...                                    |
| :------------ | :------------ | :--------------------------------------------------------- |
| **X** (Major) | Versión mayor | Un cambio rompe la compatibilidad con versiones anteriores |
| **Y** (Minor) | Versión menor | Se añade funcionalidad compatible con lo existente         |
| **Z** (Patch) | Parche        | Se corrigen errores sin alterar la compatibilidad          |

Un proyecto comienza en la versión `0.1.0` durante su desarrollo inicial. A partir de la
versión `1.0.0`, se considera estable y se aplican las reglas de incremento de forma
estricta.

Es posible añadir etiquetas adicionales como _pre-release_ (por ejemplo,
`3.1.4-alpha.1`), que siempre tienen menor precedencia que la versión estable
correspondiente (`3.1.4 > 3.1.4-alpha.1`).

## Desarrollo guiado por pruebas (TDD)

El _Test-Driven Development_ (TDD) propone escribir las pruebas antes del código de
producción. El ciclo fundamental se resume en la secuencia _Red-Green-Refactor_:

1. **Red**: Escribir una prueba que falla (la funcionalidad aún no existe).
2. **Green**: Implementar el código mínimo necesario para que la prueba pase.
3. **Refactor**: Mejorar la calidad interna del código sin alterar su comportamiento.

Este proceso contribuye a mantener un diseño limpio, facilita la detección temprana de
errores y reduce el riesgo de regresiones.

## Desarrollo guiado por comportamiento (BDD)

El _Behavior-Driven Development_ (BDD) extiende TDD centrándose en el comportamiento del
sistema desde la perspectiva del usuario final. En lugar de pruebas unitarias aisladas,
BDD describe escenarios de alto nivel en un lenguaje cercano al dominio del problema.

Este enfoque facilita la comunicación entre desarrolladores y responsables de negocio,
ya que las pruebas se expresan de forma comprensible para todos los actores. BDD valida
que el software cumple con los requisitos funcionales y no funcionales definidos a nivel
de negocio.
