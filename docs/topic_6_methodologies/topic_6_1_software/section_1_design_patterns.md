---
authors: Daniel Bazo Correa
description: Principios de diseño, modularidad y gestión de la complejidad en software.
title: Diseño de software
---

## Referencias

- [A Philosophy of Software Design, 2nd Edition](https://amzn.eu/d/0dCD1uib) de John
  Ousterhout.

## Arquitectura de software

La arquitectura de software se distingue del diseño en que la primera aborda decisiones
estructurales difíciles de revertir, mientras que el diseño se centra en aspectos más
fácilmente modificables. Existen clases enteras de problemas en arquitectura que no
tienen una solución óptima universal, sino que presentan conjuntos de **trade-offs**
entre los que hay que elegir.

El verdadero trabajo de un arquitecto reside en su capacidad para evaluar objetivamente
los trade-offs a ambos lados de una decisión consecuente y resolverla de la mejor manera
posible. No se trata de buscar el mejor diseño, sino la combinación menos mala de
compromisos.

Los arquitectos deben comprender los principios subyacentes de la arquitectura para
tomar decisiones efectivas. Antes de entender cómo implementar soluciones, deben
entender por qué una opción tiene mejores trade-offs que otra.

### Registros de decisiones arquitectónicas (ADRs)

Una de las formas más efectivas de documentar decisiones de arquitectura es mediante los
**Architectural Decision Records (ADRs)**. Un ADR consiste en un archivo de texto breve
(normalmente una o dos páginas) que describe una decisión arquitectónica específica, su
contexto y sus consecuencias.

### Gobernanza arquitectónica

Una vez que un arquitecto ha identificado las relaciones entre componentes y las ha
codificado en un diseño, necesita asegurar que los implementadores se adhieran a ese
diseño. Este proceso se conoce como **gobernanza arquitectónica** y es un área de
esfuerzo constante para mantener la arquitectura y el diseño como actividades separadas
pero relacionadas.

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

1. **Amplificación de cambios**: un cambio aparentemente simple requiere modificaciones
   en muchos lugares diferentes del código. Un buen diseño reduce la cantidad de código
   afectado por cada decisión de diseño.

2. **Carga cognitiva**: se refiere a cuánto necesita saber un desarrollador para
   completar una tarea. Surge de APIs con muchos métodos, variables globales,
   inconsistencias y dependencias entre módulos. A veces un enfoque que requiere más
   líneas de código es más simple porque reduce la carga cognitiva.

3. **Incógnitas desconocidas**: no resulta obvio qué piezas de código deben modificarse
   para completar una tarea, ni qué información necesita el desarrollador. Este es el
   peor de los tres síntomas.

### Causas de la complejidad

La complejidad tiene dos causas fundamentales:

- **Dependencias**: cada vez que se crea una nueva clase, se generan dependencias
  alrededor de su API.
- **Oscuridad**: ocurre cuando información importante no es evidente. La inconsistencia
  es un contribuyente importante a la oscuridad.

La necesidad de documentación extensa suele ser una señal de que el diseño no es del
todo correcto. La mejor forma de reducir la oscuridad es simplificando el diseño del
sistema.

## Diseño modular

Una de las técnicas más importantes para gestionar la complejidad del software es
diseñar sistemas de modo que los desarrolladores solo necesiten enfrentarse a una
pequeña fracción de la complejidad total en cada momento. Este enfoque se denomina
**diseño modular**.

En el diseño modular, un sistema se descompone en una colección de módulos relativamente
independientes. Los módulos pueden adoptar muchas formas: clases, subsistemas o
servicios.

### Interfaces

La interfaz de un módulo contiene dos tipos de información:

- **Formal**: especificada explícitamente en el código (firmas de métodos, tipos de
  parámetros, valores de retorno, excepciones).
- **Informal**: restricciones de uso, orden de llamadas, precondiciones. Si un
  desarrollador necesita conocer una pieza de información para usar un módulo, esa
  información forma parte de su interfaz.

La clave para diseñar abstracciones es comprender qué es importante y buscar diseños que
minimicen la cantidad de información relevante.

### Módulos profundos

Los mejores módulos son aquellos que proporcionan funcionalidad potente con interfaces
simples. La cuestión más importante al diseñar clases y módulos es hacerlos
**profundos**: interfaces simples para los casos de uso comunes, pero con funcionalidad
significativa detrás.

???+ example "Analogía"

    Un microondas tiene una implementación interna compleja, pero los usuarios ven una
    abstracción mucho más simple: unos pocos botones para controlar el tiempo y la
    intensidad.

### Ocultación de información

Cada módulo debe encapsular piezas de conocimiento que representan decisiones de diseño.
La **ocultación de información** es una de las técnicas más importantes para lograr
módulos profundos.

Ejemplos de información que puede ocultarse dentro de un módulo:

- Cómo implementar el protocolo de red TCP.
- Cómo parsear documentos JSON.
- Estructuras de datos y algoritmos relacionados con un mecanismo.

La ocultación de información reduce la complejidad de dos formas: simplifica la interfaz
del módulo y facilita la evolución del sistema al limitar el impacto de los cambios.

### Fugas de información

Lo opuesto a la ocultación de información es la **fuga de información**, que ocurre
cuando una decisión de diseño se refleja en múltiples módulos, creando dependencias
entre ellos.

???+ warning "Descomposición temporal"

    Un error común es la descomposición temporal, donde la estructura del sistema
    corresponde al orden temporal de las operaciones. Si el mismo conocimiento se usa en
    diferentes puntos de ejecución, se codifica en múltiples lugares. Al diseñar
    módulos, hay que centrarse en el conocimiento necesario para cada tarea, no en el
    orden en que ocurren las tareas.

### Generalidad vs. especialización

La sobre-especialización puede ser la mayor causa de complejidad en software. El código
más general es más simple, limpio y fácil de entender.

Preguntas útiles para encontrar el equilibrio:

- ¿Cuál es la interfaz más simple que cubrirá todas mis necesidades actuales?
- ¿En cuántas situaciones se usará este método?
- ¿Es fácil de usar esta API para mis necesidades actuales?

El código especializado debe separarse limpiamente del código de propósito general. Los
casos especiales deben eliminarse siempre que sea posible, diseñando el caso normal de
forma que maneje automáticamente las condiciones límite.

### Métodos de paso (pass-through)

Un método de paso es aquel que no hace más que invocar otro método con una firma similar
o idéntica. Esto indica que no hay una división limpia de responsabilidades entre las
clases. La solución es refactorizar para que cada clase tenga un conjunto distinto y
coherente de responsabilidades.

### Cuándo dividir o unir código

La decisión de dividir o unir módulos debe basarse en la complejidad. La longitud por sí
sola rara vez es buena razón para dividir un método. Cada método debe hacer una cosa y
hacerla completamente. Dividir un método solo tiene sentido si resulta en abstracciones
más limpias. Es más importante que un módulo tenga una interfaz simple que una
implementación simple.

## Gestión de excepciones

El manejo de excepciones puede representar una fracción significativa de todo el código
de un sistema y es una fuente importante de complejidad. La lección clave es **reducir
el número de lugares donde deben manejarse las excepciones**.

### Técnicas para reducir la complejidad de excepciones

1. **Definir los errores fuera de existencia**: diseñar las APIs de modo que las
   condiciones de error simplemente no puedan ocurrir. Redefinir la semántica para que
   el caso problemático se maneje de forma natural.

2. **Enmascaramiento de excepciones**: manejar la excepción en un nivel bajo sin
   propagarla hacia arriba.

3. **Agregación de excepciones**: manejar muchas excepciones con un único fragmento de
   código en lugar de escribir manejadores distintos para cada excepción individual.

4. **Terminar la aplicación**: para ciertos errores que no vale la pena intentar
   manejar, simplemente dejar que la aplicación falle.

???+ warning "Antipatrón"

    Los programadores agravan los problemas definiendo excepciones innecesarias. En
    lugar de buscar una forma limpia de manejar una situación, lanzan una excepción y
    trasladan el problema al llamador. Las excepciones lanzadas por una clase son parte
    de su interfaz: clases con muchas excepciones tienen interfaces complejas y son más
    superficiales.

## Documentación y nombres

### Comentarios

La idea general detrás de los comentarios es capturar información que estaba en la mente
del diseñador pero que no pudo representarse en el código. El principio guía es que los
comentarios deben describir cosas que no son obvias a partir del código.

Buenas prácticas para comentarios:

- Escribir el comentario de interfaz de cada método antes de su cuerpo, para centrarse
  en la abstracción sin distraerse con la implementación.
- Posicionar los comentarios cerca del código que describen.
- No redocumentar las decisiones de diseño de un módulo en otro módulo.
- Si la información ya está documentada en otro lugar externo, referenciarla en lugar de
  repetirla.
- Si no hay un lugar obvio para documentar algo, crear un archivo `designNotes`.

El acto de escribir comentarios permite evaluar las decisiones de diseño tempranamente y
descubrir problemas. Si resulta difícil escribir un comentario simple y completo para un
método o variable, es un indicador de que puede haber un problema con el diseño.

### Nombres

Elegir nombres para variables, métodos y otras entidades es uno de los aspectos más
infravalorados del diseño de software. Los buenos nombres son una forma de
documentación.

Los buenos nombres tienen dos propiedades:

- **Precisión**: el problema más común es que los nombres son demasiado genéricos o
  vagos. Al considerar un nombre, pregúntate: si alguien ve este nombre aislado, sin ver
  su declaración ni documentación, ¿podrá adivinar a qué se refiere?
- **Consistencia**: para cada uso común, elegir un nombre y usarlo en todas partes.
  Nunca usar ese nombre para otro propósito, y asegurar que el propósito sea lo
  suficientemente estrecho para que todas las variables con ese nombre tengan el mismo
  comportamiento.

## Consistencia y claridad

La consistencia es una herramienta poderosa para reducir la complejidad de un sistema y
hacer su comportamiento más evidente. Si un sistema es consistente, las cosas similares
se hacen de formas similares y las cosas diferentes se hacen de formas diferentes.

### Niveles de consistencia

- **Nombres**: usar convenciones uniformes.
- **Estilo de código**: las guías de estilo modernas abordan indentación, colocación de
  llaves, orden de declaraciones, nomenclatura y comentarios.
- **Interfaces**: interfaces similares para funcionalidades similares.
- **Patrones de diseño**: aplicar patrones reconocidos de forma consistente.

### Mantener la consistencia

- **Documentar**: crear un documento que liste las convenciones más importantes.
- **Hacer cumplir**: escribir herramientas que verifiquen violaciones y no permitir
  commits que no pasen las verificaciones.
- **No cambiar convenciones existentes**: resistir la tentación de "mejorar"
  convenciones establecidas. Tener una "mejor idea" no es excusa suficiente para
  introducir inconsistencias.

### Claridad del código

El software debe diseñarse para facilitar la lectura, no la escritura. Si el significado
y comportamiento del código no pueden entenderse con una lectura rápida, es una señal de
alerta. Los nombres bien elegidos ayudan a que el código sea obvio: la primera
suposición de alguien sobre el comportamiento de una variable debería ser correcta.

## Principios generales

### Principios clave

- Realizar inversiones continuas y pequeñas para mejorar el diseño del sistema.
- Los módulos deben ser profundos.
- Las interfaces deben diseñarse para que el uso más común sea lo más simple posible.
- Es más importante que un módulo tenga una interfaz simple que una implementación
  simple.
- Los módulos de propósito general son más profundos.
- Separar el código de propósito general del código especializado.
- Definir los errores fuera de existencia.
- Los comentarios deben describir lo que no es obvio a partir del código.
- El software debe diseñarse para facilitar la lectura, no la escritura.

### Señales de alerta (red flags)

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

### Rendimiento

Las intuiciones de los programadores sobre el rendimiento no son fiables. Antes de hacer
cambios, hay que medir el comportamiento existente del sistema para identificar dónde
tendrá mayor impacto la optimización. La mejor forma de mejorar el rendimiento es con
cambios fundamentales como introducir una caché o usar un enfoque algorítmico diferente.
El código limpio y simple tiende a ser suficientemente rápido.
