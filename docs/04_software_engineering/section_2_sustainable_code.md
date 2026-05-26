---
authors: Daniel Bazo Correa
description:
    Principios de diseño, código limpio, modularidad y gestión de la complejidad en
    software.
title: Diseño y código sostenible
---

de John Ousterhout.

## Principios de código limpio

El desarrollo de un proyecto debe realizarse bajo una estructura de código clara y
sostenible, utilizando herramientas y metodologías para garantizar su organización y
limpieza. Estas prácticas son fundamentales durante el desarrollo, puesta en producción
y evolución del proyecto, independientemente del lenguaje de programación utilizado.

El código limpio se rige por principios universales que favorecen la legibilidad, el
mantenimiento y la escalabilidad:

- **Separación de responsabilidades**: Cada parte del código debe tener una tarea
  específica. Una función, una única tarea.
- **Minimizar dependencias entre módulos**: Diseñar módulos como si fueran
  microservicios, con interfaces claras y acoplamiento mínimo.
- **Nomenclatura descriptiva**: Utilizar nombres de variables y funciones fáciles de
  interpretar, buscar y entender.
- **Evitar comentarios innecesarios**: Si el código necesita un comentario para
  explicarse, es preferible extraer una función o variable con un nombre descriptivo.
- **Principio de responsabilidad única**: No agrupar toda la lógica en clases cuando la
  programación funcional puede ser suficiente.
- **Validación cerca de los datos**: La validación debe estar siempre lo más cerca
  posible de la fuente de datos.

### Estructura del proyecto

Un proyecto debe estar organizado en dos partes principales:

1. **Directorio de la aplicación**: Contiene la lógica del código, la configuración de
   los modelos, los registros (_logs_) y demás componentes funcionales.
2. **Ajustes y configuraciones**: Incluye configuraciones y dependencias del proyecto,
   como archivos de gestión de dependencias, _Dockerfiles_, archivos de configuración
   `.yml` y similares.

Esta separación promueve un código modular, organizado y fácil de mantener.

### Convenciones de estilo

Cada lenguaje de programación dispone de guías de estilo que definen convenciones para
escribir código legible y consistente. Se recomienda adoptar la guía oficial del
lenguaje utilizado y emplear herramientas de formateo automático para garantizar su
cumplimiento.

| Elemento              | Convención                   | Ejemplo             |
| :-------------------- | :--------------------------- | :------------------ |
| Paquetes y módulos    | Minúsculas con guiones bajos | `mi_modulo`         |
| Clases                | _CamelCase_ (o _PascalCase_) | `MiClase`           |
| Funciones y variables | Minúsculas con guiones bajos | `mi_funcion`        |
| Constantes            | Mayúsculas con guiones bajos | `MI_CONSTANTE`      |
| Elementos no públicos | Prefijo con guion bajo       | `_variable_interna` |

???+ example "En Python"

    En Python, la guía de estilo oficial es [PEP 8](https://pep8.org/). Herramientas
    como [Ruff](https://docs.astral.sh/ruff/) permiten aplicar estas convenciones
    automáticamente.

    ```python linenums="1"
    import os
    import sys

    from external_lib import some_function
    from local_module import local_function

    class MiClase:
        MI_CONSTANTE: int = 42

        def __init__(self) -> None:
            self._variable_interna: int = 10

        def metodo_publico(self) -> int:
            return self._variable_interna

    def suma(a: int, b: int) -> int:
        """Suma dos números y devuelve el resultado."""
        return a + b
    ```

## Complejidad

El problema más fundamental en la ciencia de la computación es la **descomposición de
problemas**. A medida que un programa evoluciona y adquiere más funcionalidades, se
vuelve complejo, con dependencias sutiles entre sus componentes. Con el tiempo, la
complejidad se acumula y resulta cada vez más difícil para los programadores mantener
todos los factores relevantes en mente al modificar el sistema. Esto ralentiza el
desarrollo y conduce a errores.

???+ warning "Mentalidad táctica vs. estratégica"

    Muchas organizaciones fomentan una mentalidad táctica, centrada en hacer que las
    funcionalidades estén operativas lo más rápido posible. Sin embargo, las
    complejidades se acumulan rápidamente cuando todos programan de forma táctica. El
    código funcional no es suficiente: el objetivo principal debe ser producir un gran
    diseño que además funcione. Se recomienda invertir entre un 10-20% del tiempo total
    de desarrollo en mejoras de diseño.

### Síntomas de la complejidad

La complejidad se manifiesta de tres formas generales:

1. **Amplificación de cambios**: Un cambio aparentemente simple requiere modificaciones
   en muchos lugares diferentes del código.
2. **Carga cognitiva**: Se refiere a cuánto necesita saber un desarrollador para
   completar una tarea. Surge de APIs con muchos métodos, variables globales,
   inconsistencias y dependencias entre módulos.
3. **Incógnitas desconocidas**: No resulta obvio qué piezas de código deben modificarse
   para completar una tarea, ni qué información necesita el desarrollador. Este es el
   peor de los tres síntomas.

### Causas de la complejidad

La complejidad tiene dos causas fundamentales:

- **Dependencias**: Cada vez que se crea una nueva clase, se generan dependencias
  alrededor de su API.
- **Oscuridad**: Ocurre cuando información importante no es evidente. La inconsistencia
  es un contribuyente importante a la oscuridad.

La necesidad de documentación extensa suele ser una señal de que el diseño no es del
todo correcto. La mejor forma de reducir la oscuridad es simplificando el diseño del
sistema.

## Diseño modular

Una de las técnicas más importantes para gestionar la complejidad del _software_ es
diseñar sistemas de modo que los desarrolladores solo necesiten enfrentarse a una
pequeña fracción de la complejidad total en cada momento. En el diseño modular, un
sistema se descompone en una colección de módulos relativamente independientes que
pueden adoptar muchas formas: clases, subsistemas o servicios.

### Interfaces

La interfaz de un módulo contiene dos tipos de información:

- **Formal**: Especificada explícitamente en el código (firmas de métodos, tipos de
  parámetros, valores de retorno, excepciones).
- **Informal**: Restricciones de uso, orden de llamadas, precondiciones. Si un
  desarrollador necesita conocer una pieza de información para usar un módulo, esa
  información forma parte de su interfaz.

### Módulos profundos

Los mejores módulos son aquellos que proporcionan funcionalidad potente con interfaces
simples. La cuestión más importante al diseñar clases y módulos es hacerlos
**profundos**: interfaces simples para los casos de uso comunes, pero con funcionalidad
significativa detrás.

???+ example "Módulo profundo vs. superficial en Python"

    Un módulo **superficial** expone demasiados detalles internos:

    ```python linenums="1"
    class GestorArchivos:
        def abrir_archivo(self, ruta: str) -> int: ...
        def leer_bytes(self, fd: int, n: int) -> bytes: ...
        def cerrar_archivo(self, fd: int) -> None: ...
        def verificar_permisos(self, ruta: str) -> bool: ...
        def obtener_tamaño(self, ruta: str) -> int: ...
    ```

    Un módulo **profundo** oculta la complejidad tras una interfaz simple:

    ```python linenums="1"
    class GestorArchivos:
        def leer(self, ruta: str) -> str:
            """Lee el contenido completo de un archivo."""
            ...
    ```

### Ocultación de información

Cada módulo debe encapsular piezas de conocimiento que representan decisiones de diseño.
La **ocultación de información** reduce la complejidad de dos formas: simplifica la
interfaz del módulo y facilita la evolución del sistema al limitar el impacto de los
cambios.

???+ example "Ocultación de información en Python"

    El usuario de la clase no necesita saber cómo se almacenan los datos internamente:

    ```python linenums="1"
    class Carrito:
        def __init__(self) -> None:
            self._items: dict[str, float] = {}

        def agregar(self, producto: str, precio: float) -> None:
            self._items[producto] = precio

        def total(self) -> float:
            return sum(self._items.values())
    ```

    Si en el futuro se cambia el diccionario por una base de datos, la interfaz pública
    (`agregar`, `total`) no cambia.

### Fugas de información

Lo opuesto a la ocultación de información es la **fuga de información**, que ocurre
cuando una decisión de diseño se refleja en múltiples módulos, creando dependencias
entre ellos.

???+ example "Fuga de información en Python"

    Si el formato de serialización se filtra a múltiples módulos, un cambio de JSON a
    YAML requiere modificar todos ellos:

    ```python linenums="1"
    # Fuga: ambos módulos conocen el formato JSON
    import json

    class Exportador:
        def exportar(self, datos: dict) -> str:
            return json.dumps(datos)

    class Importador:
        def importar(self, texto: str) -> dict:
            return json.loads(texto)
    ```

    La solución es encapsular la decisión de formato en un único módulo:

    ```python linenums="1"
    # Correcto: un solo módulo conoce el formato
    class Serializador:
        def serializar(self, datos: dict) -> str:
            return json.dumps(datos)

        def deserializar(self, texto: str) -> dict:
            return json.loads(texto)
    ```

???+ warning "Descomposición temporal"

    Un error común es la descomposición temporal, donde la estructura del sistema
    corresponde al orden temporal de las operaciones. Al diseñar módulos, hay que
    centrarse en el conocimiento necesario para cada tarea, no en el orden en que
    ocurren las tareas.

### Generalidad vs. especialización

La sobre-especialización puede ser la mayor causa de complejidad en _software_. El
código más general es más simple, limpio y fácil de entender. El código especializado
debe separarse limpiamente del código de propósito general, y los casos especiales deben
eliminarse siempre que sea posible.

### Cuándo dividir o unir código

La decisión de dividir o unir módulos debe basarse en la complejidad. La longitud por sí
sola rara vez es buena razón para dividir un método. Cada método debe hacer una cosa y
hacerla completamente. Es más importante que un módulo tenga una interfaz simple que una
implementación simple.

## Gestión de excepciones

El manejo de excepciones puede representar una fracción significativa de todo el código
de un sistema y es una fuente importante de complejidad. La lección clave es **reducir
el número de lugares donde deben manejarse las excepciones**.

Las técnicas principales para reducir esta complejidad son:

1. **Definir los errores fuera de existencia**: Diseñar las APIs de modo que las
   condiciones de error simplemente no puedan ocurrir.
2. **Enmascaramiento de excepciones**: Manejar la excepción en un nivel bajo sin
   propagarla hacia arriba.
3. **Agregación de excepciones**: Manejar muchas excepciones con un único fragmento de
   código.
4. **Terminar la aplicación**: Para ciertos errores que no vale la pena intentar
   manejar, simplemente dejar que la aplicación falle.

???+ example "Definir errores fuera de existencia en Python"

    En lugar de lanzar una excepción cuando la clave no existe:

    ```python linenums="1"
    # Diseño que genera excepciones innecesarias
    class Configuracion:
        def obtener(self, clave: str) -> str:
            if clave not in self._datos:
                raise KeyError(f"Clave '{clave}' no encontrada")
            return self._datos[clave]
    ```

    Se puede diseñar la API para que el error no exista:

    ```python linenums="1"
    # Diseño que elimina la condición de error
    class Configuracion:
        def obtener(self, clave: str, por_defecto: str = "") -> str:
            return self._datos.get(clave, por_defecto)
    ```

???+ warning "Antipatrón"

    Los programadores agravan los problemas definiendo excepciones innecesarias. Las
    excepciones lanzadas por una clase son parte de su interfaz: clases con muchas
    excepciones tienen interfaces complejas y son más superficiales.

## Documentación y nombres

### Comentarios

Los comentarios deben describir cosas que no son obvias a partir del código. El acto de
escribir comentarios permite evaluar las decisiones de diseño tempranamente. Si resulta
difícil escribir un comentario simple y completo para un método o variable, es un
indicador de que puede haber un problema con el diseño.

Buenas prácticas:

- Escribir el comentario de interfaz de cada método antes de su cuerpo.
- Posicionar los comentarios cerca del código que describen.
- No redocumentar las decisiones de diseño de un módulo en otro módulo.
- Si la información ya está documentada en otro lugar externo, referenciarla en lugar de
  repetirla.

### Nombres

Los buenos nombres tienen dos propiedades:

- **Precisión**: Si alguien ve este nombre aislado, sin ver su declaración ni
  documentación, ¿podrá adivinar a qué se refiere?
- **Consistencia**: Para cada uso común, elegir un nombre y usarlo en todas partes.
  Nunca usar ese nombre para otro propósito.

???+ example "Buenos vs. malos nombres en Python"

    ```python linenums="1"
    # Nombres vagos que no transmiten intención
    def proc(d: list[dict]) -> list[dict]:
        r = []
        for x in d:
            if x["a"] > 0:
                r.append(x)
        return r

    # Nombres descriptivos que documentan el código
    def filtrar_transacciones_positivas(
        transacciones: list[dict[str, float]]
    ) -> list[dict[str, float]]:
        positivas: list[dict[str, float]] = []
        for transaccion in transacciones:
            if transaccion["monto"] > 0:
                positivas.append(transaccion)
        return positivas
    ```

## Consistencia y claridad

La consistencia es una herramienta poderosa para reducir la complejidad. Si un sistema
es consistente, las cosas similares se hacen de formas similares y las cosas diferentes
se hacen de formas diferentes.

Para mantener la consistencia: documentar las convenciones más importantes, escribir
herramientas que verifiquen violaciones, y resistir la tentación de "mejorar"
convenciones establecidas. El _software_ debe diseñarse para facilitar la lectura, no la
escritura.

## Arquitectura de _software_

La arquitectura de _software_ se distingue del diseño en que la primera aborda
decisiones estructurales difíciles de revertir, mientras que el diseño se centra en
aspectos más fácilmente modificables. El verdadero trabajo de un arquitecto reside en su
capacidad para evaluar objetivamente los _trade-offs_ a ambos lados de una decisión
consecuente y resolverla de la mejor manera posible.

### _Clean Architecture_

_Clean Architecture_ propone una separación clara entre la **lógica de negocio**
(aquello que no está limitado por la tecnología) y la **lógica de la aplicación** (que
depende de la tecnología utilizada).

La arquitectura se organiza en capas concéntricas con dependencias que apuntan siempre
hacia el interior:

| Capa (de interior a exterior) | Responsabilidad                                                               |
| :---------------------------- | :---------------------------------------------------------------------------- |
| **Dominio**                   | Entidades y reglas de negocio puras. No conoce las capas exteriores.          |
| **Casos de uso (Aplicación)** | Orquesta la lógica de negocio. El dominio no sabe de los casos de uso.        |
| **Adaptadores**               | Convierte datos entre el formato de los casos de uso y el del mundo exterior. |
| **Externo (Infraestructura)** | _Frameworks_, bases de datos, UI, navegador, APIs externas.                   |

???+ example "Estructura de carpetas siguiendo _Clean Architecture_"

    ```plaintext linenums="1"
    mi_proyecto/
    ├── dominio/
    │   ├── entidades.py        # Modelos puros del negocio
    │   └── repositorios.py     # Interfaces abstractas (protocolos)
    ├── aplicacion/
    │   └── casos_de_uso.py     # Orquestación de la lógica de negocio
    ├── adaptadores/
    │   ├── api.py              # Controladores HTTP
    │   └── persistencia.py     # Implementación concreta del repositorio
    └── main.py                 # Punto de entrada y configuración
    ```

    ```python linenums="1"
    # dominio/repositorios.py
    from typing import Protocol
    from dominio.entidades import Usuario

    class RepositorioUsuarios(Protocol):
        def obtener_por_id(self, id: int) -> Usuario | None: ...
        def guardar(self, usuario: Usuario) -> None: ...
    ```

    ```python linenums="1"
    # aplicacion/casos_de_uso.py
    from dominio.entidades import Usuario
    from dominio.repositorios import RepositorioUsuarios

    class RegistrarUsuario:
        def __init__(self, repositorio: RepositorioUsuarios) -> None:
            self._repositorio = repositorio

        def ejecutar(self, nombre: str, email: str) -> Usuario:
            usuario = Usuario(nombre=nombre, email=email)
            self._repositorio.guardar(usuario)
            return usuario
    ```

### Registros de decisiones arquitectónicas (ADRs)

Una de las formas más efectivas de documentar decisiones de arquitectura es mediante los
_Architectural Decision Records_ (ADRs). Un ADR consiste en un archivo de texto breve
que describe una decisión arquitectónica específica, su contexto y sus consecuencias.

## Señales de alerta

La presencia de cualquiera de estos síntomas sugiere un problema con el diseño:

| Señal de alerta           | Descripción                                                                              |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| Fuga de información       | Una decisión de diseño se refleja en múltiples módulos                                   |
| Método de paso            | Un método no hace casi nada excepto pasar sus argumentos a otro método con firma similar |
| Repetición                | Un fragmento de código no trivial se repite una y otra vez                               |
| Métodos acoplados         | Dos métodos tienen tantas dependencias que es difícil entender uno sin entender el otro  |
| Nombre vago               | El nombre de una variable o método es tan impreciso que no transmite información útil    |
| Dificultad para nombrar   | Es difícil encontrar un nombre preciso e intuitivo para una entidad                      |
| Dificultad para describir | La documentación de una variable o método debe ser extensa para ser completa             |
| Código no obvio           | El comportamiento o significado de un fragmento de código no puede entenderse fácilmente |

## Versionado semántico

El versionado semántico (_Semantic Versioning_ o SemVer) es un sistema estandarizado
para controlar las versiones del _software_, representado mediante el formato `X.Y.Z`:

| Componente    | Significado   | Se incrementa cuando...                                    |
| :------------ | :------------ | :--------------------------------------------------------- |
| **X** (Major) | Versión mayor | Un cambio rompe la compatibilidad con versiones anteriores |
| **Y** (Minor) | Versión menor | Se añade funcionalidad compatible con lo existente         |
| **Z** (Patch) | Parche        | Se corrigen errores sin alterar la compatibilidad          |

Un proyecto comienza en la versión `0.1.0` durante su desarrollo inicial. A partir de la
versión `1.0.0`, se considera estable y se aplican las reglas de incremento de forma
estricta.

## Desarrollo guiado por pruebas (TDD)

El _Test-Driven Development_ (TDD) propone escribir las pruebas antes del código de
producción. El ciclo fundamental se resume en la secuencia _Red-Green-Refactor_:

1. **Red**: Escribir una prueba que falla (la funcionalidad aún no existe).
2. **Green**: Implementar el código mínimo necesario para que la prueba pase.
3. **Refactor**: Mejorar la calidad interna del código sin alterar su comportamiento.

???+ example "En Python con pytest"

    ```python linenums="1"
    # test_suma.py
    from mi_modulo import suma

    def test_suma_positivos() -> None:
        assert suma(2, 3) == 5

    def test_suma_negativos() -> None:
        assert suma(-1, -1) == -2
    ```

    ```python linenums="1"
    # mi_modulo.py
    def suma(a: int, b: int) -> int:
        return a + b
    ```

## Desarrollo guiado por comportamiento (BDD)

El _Behavior-Driven Development_ (BDD) extiende TDD centrándose en el comportamiento del
sistema desde la perspectiva del usuario final. En lugar de pruebas unitarias aisladas,
BDD describe escenarios de alto nivel en un lenguaje cercano al dominio del problema.

???+ example "Escenario BDD"

    ```gherkin linenums="1"
    Feature: Suma de números
      Scenario: Sumar dos números positivos
        Given el número 2
        And el número 3
        When se realiza la suma
        Then el resultado es 5
    ```

## Rendimiento

Las intuiciones de los programadores sobre el rendimiento no son fiables. Antes de hacer
cambios, hay que medir el comportamiento existente del sistema para identificar dónde
tendrá mayor impacto la optimización. La mejor forma de mejorar el rendimiento es con
cambios fundamentales como introducir una caché o usar un enfoque algorítmico diferente.
El código limpio y simple tiende a ser suficientemente rápido.
