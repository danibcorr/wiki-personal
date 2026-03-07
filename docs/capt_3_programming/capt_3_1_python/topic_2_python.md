---
authors: Daniel Bazo Correa
description: Aprende todo lo necesario sobre el lenguaje de programación Python.
title: Python
---

## Bibliografía

- [Python Docs](https://docs.python.org/3/)
- [Python Bootcamps Udemy](https://www.udemy.com/course/complete-python-bootcamp/)

## Introducción

<p align="center">
  <img src="../../../assets/img/docs/logos/python-logo.png" height="250" width="250"/>
  <br />
  <em>Logo de Python</em>
</p>

**Python** es un lenguaje de programación de alto nivel, interpretado y de propósito
general, desarrollado por Guido van Rossum. Su principal ventaja reside en la rápida
adopción que ha experimentado en el sector tecnológico, impulsada en gran medida por el
auge de la inteligencia artificial. Además, presenta una curva de aprendizaje accesible
gracias a una sintaxis que se caracteriza por ser clara y legible.

Python cuenta con una amplia comunidad de desarrolladores y un ecosistema robusto de
bibliotecas y _frameworks_ que permiten abordar una gran diversidad de proyectos,
incluyendo aplicaciones web, análisis de datos, automatización de tareas y aprendizaje
automático.

### Creación y configuración del entorno

Antes de comenzar a programar en Python, es necesario disponer del intérprete instalado
en el sistema. En distribuciones Linux, suele venir preinstalada alguna versión de Python
3.x, por lo que no se requiere ninguna instalación adicional en un principio. En caso
contrario, siempre es posible visitar la
[página oficial de Python](https://www.python.org/) o buscar un tutorial específico para
el sistema operativo en cuestión.

Independientemente del sistema, resulta imprescindible crear un entorno virtual que
permita aislar la versión de Python y los paquetes específicos de cada proyecto. Un
entorno virtual puede entenderse como una parcela reservada para una versión concreta de
Python y un conjunto determinado de dependencias, logrando así un aislamiento completo
respecto al sistema y a otros proyectos. Esta práctica resulta muy útil para evitar
conflictos entre dependencias y garantizar la reproducibilidad del entorno de desarrollo.

Para obtener instrucciones detalladas sobre la configuración de entornos virtuales y la
gestión de paquetes en Python, se puede consultar la sección de entornos de esta misma
wiki, dentro del
[apartado de programación en Python](https://www.google.com/search?q=./topic_1_environments.md).

### Jupyter Notebooks

<p align="center">
  <img src="../../../assets/img/docs/jupyter-notebook.png"/>
  <br />
  <em>Ejemplo de un cuaderno Jupyter</em>
</p>

Existen dos formas principales de trabajar en Python. La primera es mediante ficheros con
extensión **.py**, que funcionan como archivos de texto plano que permiten al entorno de
desarrollo (por ejemplo, Visual Studio Code) ofrecer funcionalidades como autocompletado
y corrección de sintaxis. Esta es la forma de programar más recomendable y la que se
utiliza en el desarrollo profesional y en la puesta en producción del código.

Sin embargo, para explorar el lenguaje y para proyectos de ciencia de datos, se tiende a
utilizar **Jupyter Notebooks**, una herramienta interactiva que integra código, texto y
visualizaciones en un único documento. Entre sus principales ventajas destacan:

- **Interactividad**: Permite ejecutar bloques de código de manera independiente, lo que
  facilita la prueba de ideas y la depuración paso a paso.
- **Documentación integrada**: Soporta texto en formato Markdown, permitiendo incluir
  explicaciones y notas directamente junto al código.
- **Visualización**: Facilita la incorporación de gráficos y visualizaciones mediante
  bibliotecas como **Matplotlib** o **Seaborn**, mostrando los resultados de manera
  inmediata dentro del mismo documento.

La elección entre una u otra herramienta depende sobre todo de la facilidad para
organizar los proyectos y del enfoque de exploración y desarrollo que se adopte. También
influye la forma de trabajo del equipo. En cualquier caso, conviene explorar ambas
opciones sin descartar ninguna, ya que cada una tiene su momento y su utilidad.

## Conceptos básicos

Para dominar Python, es fundamental comprender primero los pilares que sostienen
cualquier programa: cómo se almacena la información, cómo se manipula y cómo se controla
el flujo de las instrucciones. En esta sección se exploran los elementos esenciales del
lenguaje, desde los tipos de datos básicos y las operaciones matemáticas hasta las
estructuras de control que permiten dotar de lógica al código.

### Tipos de datos

Python ofrece varios tipos de datos fundamentales que permiten definir, almacenar y
manipular información. A continuación se detallan los principales tipos de datos y sus
características:

| Tipo de datos                               | Palabra reservada | Ejemplos                         |
| ------------------------------------------- | ----------------- | -------------------------------- |
| **Números enteros**                         | `int`             | `3`                              |
| **Números flotantes**                       | `float`           | `2.3`                            |
| **Cadenas de texto**                        | `str`             | `"Hola"`                         |
| **Listas** (colección ordenada y mutable)   | `list`            | `[10, "hello", 200.3]`           |
| **Diccionarios** (pares clave-valor)        | `dict`            | `{"edad": 20, "nombre": "Dani"}` |
| **Tuplas** (secuencia ordenada e inmutable) | `tuple`           | `(10, "hello", 200.3)`           |
| **Sets** (colección única y desordenada)    | `set`             | `{"a", "b"}`                     |
| **Booleanos** (valores lógicos)             | `bool`            | `True`, `False`                  |

Las palabras reservadas son términos que Python utiliza internamente y que no pueden ser
empleados como nombres de variables o funciones. Son la forma que tiene el lenguaje de
interpretar cada tipo de dato como tal.

Python no requiere que se especifique el tipo de una variable de forma explícita. Sin
embargo, cada vez es más común (y constituye una buena práctica) utilizar lo que se
conoce como _typing_ para anotar los tipos. Por ejemplo:

```py linenums="1"
# Sin typing
valor_entero = 12

# Con typing
valor_entero: int = 12
lista_valores: list[int] = [1, 2, 3]
diccionario_valores: dict[str, list[int]] = {"esto_es_un_string": [1, 2, 3]}
```

### Operaciones con datos

Python permite realizar una amplia variedad de operaciones sobre datos numéricos y otros
tipos. Las principales operaciones matemáticas y funciones disponibles son:

| Operador/Función        | Descripción                                                            |
| ----------------------- | ---------------------------------------------------------------------- | --- | --- |
| `+`, `-`, `*`, `/`, `%` | Suma, resta, multiplicación, división y módulo (resto de la división). |
| `-x`                    | Cambia el signo de un número.                                          |
| `abs(x)`                | Devuelve el valor absoluto de $x$, es decir, $                         | x   | $.  |
| `pow(x, y)` o `x**y`    | Potencia de $x$ elevado a $y$, es decir, $x^y$.                        |
| `max(x, y)`             | Devuelve el valor máximo entre $x$ e $y$.                              |
| `min(x, y)`             | Devuelve el valor mínimo entre $x$ e $y$.                              |
| `round(x, n)`           | Redondea $x$ a $n$ decimales.                                          |
| `hex(x)`                | Convierte $x$ a hexadecimal.                                           |
| `bin(x)`                | Convierte $x$ a binario.                                               |

Es posible extender la funcionalidad utilizando librerías, que pueden ser estándar
(incluidas con la propia instalación de Python) o paquetes de terceros como NumPy, Pandas
o similares. Por ejemplo, la librería estándar `math` amplía las operaciones disponibles:

| Operador/Función | Descripción                                                                        |
| ---------------- | ---------------------------------------------------------------------------------- |
| `math.floor(x)`  | Redondea $x$ hacia abajo, es decir, $\lfloor x \rfloor$. Requiere importar `math`. |
| `math.ceil(x)`   | Redondea $x$ hacia arriba, es decir, $\lceil x \rceil$. Requiere importar `math`.  |
| `math.sqrt(x)`   | Devuelve la raíz cuadrada de $x$, es decir, $\sqrt{x}$. Requiere importar `math`.  |
| `math.pi`        | Devuelve el valor de la constante $\pi$. Requiere importar `math`.                 |

Para utilizar estas funciones, basta con importar la librería:

```py linenums="1"
import math

math.floor(3.1415)
```

### Operadores

Existen diferentes tipos de operadores en Python. Los **operadores de comparación**
permiten evaluar relaciones entre dos valores, devolviendo un resultado booleano (`True`
o `False`):

| Expresión | Descripción               |
| --------- | ------------------------- |
| `A == B`  | A es igual a B.           |
| `A != B`  | A es distinto de B.       |
| `A < B`   | A es menor que B.         |
| `A <= B`  | A es menor o igual que B. |
| `A > B`   | A es mayor que B.         |
| `A >= B`  | A es mayor o igual que B. |

Por otro lado, los **operadores lógicos** permiten combinar varias condiciones y
controlar el flujo de ejecución en función de los resultados:

| Operador | Descripción                                                  |
| -------- | ------------------------------------------------------------ |
| `and`    | Devuelve `True` si **todas** las condiciones son verdaderas. |
| `or`     | Devuelve `True` si **al menos una** condición es verdadera.  |
| `not`    | Invierte el valor lógico de la condición.                    |

Los operadores lógicos se utilizan principalmente en estructuras de control, como
condicionales y bucles, para determinar el flujo del programa en función de condiciones
lógicas. Estas estructuras se explican en secciones posteriores.

### Variables

Al crear variables en Python, se deben seguir ciertas reglas:

- Los nombres no deben comenzar con números.
- No se permiten espacios en los nombres.
- No se deben utilizar los siguientes símbolos:
  `: ' " < > / , ? | \ ( ) ! @ # $ % ^ & * ~ - +`.
- Se recomienda utilizar nombres de variables en minúsculas.

**Python es un lenguaje de tipificación dinámica**, por lo que no es necesario declarar
explícitamente el tipo de dato, ya que este se asigna automáticamente según el valor. Por
ejemplo:

```py linenums="1"
mis_perros = 2
mis_perros = ["Pixel", "One"]
```

Para conocer el tipo de una variable, se utiliza la función `type(variable)`.

### Mostrar datos por pantalla

Para mostrar datos en pantalla se utiliza la función `print()`:

```py linenums="1"
print("Esto es una prueba")
```

Es posible concatenar variables que contienen cadenas de texto o métodos que devuelvan un
valor utilizando el operador `+`:

```py linenums="1"
char_name = "Daniel"
char_age = 19

print("Yo me llamo " + char_name + " y tengo " + str(char_age) + " años.")
```

Este método puede resultar ineficiente. A partir de Python 3, es posible dar formato a la
función `print()` utilizando cadenas de formato con `f`, que permiten incluir variables o
expresiones dentro de llaves `{}`:

```py linenums="1"
char_name = "Daniel"
char_age = 19

print(f"Yo me llamo {char_name} y tengo {char_age} años")
```

Incluso es posible modificar la cantidad específica de decimales para un valor de tipo
`float` utilizando el formato `{valor_float:.precisiónf}`. Por ejemplo, para mostrar el
número $\pi$ con 5 decimales:

```py linenums="1"
import math

pi = math.pi
print(f"El número pi con 5 decimales es: {pi:.5f}")
```

### Introducción de datos

Python permite recibir información del usuario mediante la función `input(...)`. Esta
función siempre devuelve el valor ingresado como una cadena de texto (`string`), por lo
que es necesario realizar una conversión de tipo (**_casting_**) si se requiere un tipo
de dato diferente:

```py linenums="1"
nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")

print("\n\t- DATOS DEL USUARIO - \n")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
```

Para convertir un `input` a un número, es necesario hacer un _casting_, como en el
siguiente ejemplo, donde se convierte una entrada de tipo `string` a `float`:

```py linenums="1"
numero = float(input("Introduce un numero: "))
```

### Cadenas de texto

Una cadena de texto, o **_string_**, es una secuencia de caracteres que puede contener
letras, números, símbolos o espacios. A continuación se muestra un ejemplo básico de
`string` junto con el uso del indexado:

```py linenums="1"
frase = "Hola buenas"

# Muestra el carácter 'H'
print("El primer carácter de mi string es " + frase[0])

# Muestra el carácter 'b'
print("El sexto carácter de mi string es " + frase[5])
```

En este caso, el índice de un `string` comienza en `0`, por lo que `frase[0]` hace
referencia al primer carácter (`"H"`) y `frase[5]` al sexto carácter (`"b"`). El espacio
en blanco también cuenta como un carácter.

Python permite acceder a cualquier carácter de un `string` utilizando su posición o
**índice**. El primer carácter tiene el índice `0`, el segundo el índice `1`, y así
sucesivamente. También se pueden usar índices negativos para contar desde el final del
`string` hacia el principio. Por ejemplo, `frase[-1]` devuelve el último carácter `'s'`.

Los strings son **inmutables**, lo que significa que no es posible cambiar un carácter
específico en un `string` ya creado. Intentar modificar directamente un elemento produce
un error:

```py linenums="1"
frase = "Hola buenas"

# Intentar cambiar el primer carácter
frase[0] = "h"  # Esto producirá un error
```

Este código genera un error de tipo `TypeError`. Para modificar un `string`, es necesario
crear uno nuevo combinando partes del original:

```py linenums="1"
frase = "Hola buenas"

# Crear un nuevo string con la primera letra modificada
nueva_frase = "h" + frase[1:]

# Imprime: "hola buenas"
print(nueva_frase)
```

#### Métodos

Las variables de tipo `string` en Python disponen de varias funciones incorporadas para
manipular y analizar el contenido de la cadena:

| Función                                            | Definición                                                                                                     |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `str(variable_a_convertir_en_string)`              | Convierte una variable en una cadena de texto.                                                                 |
| `variable *= x`                                    | Duplica la cadena `variable` `x` veces, siendo `x` un número entero.                                           |
| `variable[índice:]`                                | Obtiene una subcadena desde el índice hasta el final de la cadena.                                             |
| `variable[::X]`                                    | Obtiene caracteres de la cadena con un paso de `X`, es decir, toma un carácter cada `X` caracteres.            |
| `variable[::-1]`                                   | Invierte la cadena.                                                                                            |
| `variable.lower()`                                 | Convierte toda la cadena a minúsculas.                                                                         |
| `variable.upper()`                                 | Convierte toda la cadena a mayúsculas.                                                                         |
| `variable.isupper()`                               | Devuelve `True` si toda la cadena está en mayúsculas, `False` en caso contrario.                               |
| `variable.upper().isupper()`                       | Convierte la cadena a mayúsculas y devuelve `True` si toda la cadena está en mayúsculas.                       |
| `variable.split()`                                 | Divide la cadena en una lista de subcadenas basadas en espacios. Puede especificarse un delimitador diferente. |
| `len(variable)`                                    | Devuelve el número de caracteres en la cadena.                                                                 |
| `variable.index("a")` o `variable.index("buenas")` | Devuelve el primer índice donde se encuentra el parámetro especificado.                                        |
| `variable.replace("buenas", "me llamo Daniel")`    | Reemplaza una subcadena dentro de la cadena por otra subcadena.                                                |
| `variable.count('x')`                              | Cuenta el número de veces que aparece el carácter especificado.                                                |
| `variable.find('x')`                               | Devuelve la primera posición en la que se encuentra el carácter especificado.                                  |
| `variable.isalnum()`                               | Devuelve `True` si todos los caracteres son alfanuméricos.                                                     |
| `variable.isalpha()`                               | Devuelve `True` si todos los caracteres son alfabéticos.                                                       |
| `variable.islower()`                               | Devuelve `True` si todos los caracteres están en minúsculas.                                                   |
| `variable.isspace()`                               | Devuelve `True` si todos los caracteres son espacios en blanco.                                                |
| `variable.istitle()`                               | Devuelve `True` si la primera letra de cada palabra está en mayúsculas.                                        |
| `variable.split('x')`                              | Divide la cadena en partes cuando encuentra el carácter `x`.                                                   |
| `variable.partition('x')`                          | Divide la cadena en dos partes en el primer encuentro del carácter `x`.                                        |
| `variable.strip()`                                 | Elimina los espacios al principio y al final de la cadena.                                                     |

### Declaraciones condicionales

Las declaraciones condicionales en Python (`if`, `elif` y `else`) permiten ejecutar
diferentes bloques de código según se cumplan o no ciertas condiciones. Esto resulta
fundamental para controlar el flujo de un programa y tomar decisiones en función de los
datos evaluados.

El condicional básico es la instrucción `if`, que ejecuta un bloque de código solo si la
condición especificada es verdadera:

```py linenums="1"
if condicion:
    # Código a ejecutar si la condición es verdadera
```

Si la condición es falsa, se puede usar una instrucción `else` para ejecutar un bloque
alternativo:

```py linenums="1"
if condicion:
    # Código a ejecutar si la condición es verdadera
else:
    # Código a ejecutar si la condición es falsa
```

Para manejar múltiples condiciones, se utiliza la instrucción `elif`, que permite evaluar
varias condiciones de forma secuencial:

```py linenums="1"
if primera_condicion:
    # Código a ejecutar si la primera condición es verdadera
elif segunda_condicion:
    # Código a ejecutar si la segunda condición es verdadera
else:
    # Código a ejecutar si ninguna de las condiciones anteriores es verdadera
```

???+ example "Ejemplo"

    En este ejemplo se utiliza un condicional `if` para verificar si una letra está presente en una palabra:

    ```py linenums="1"
    letra = 'y'
    palabra = "Laguna"

    if letra in palabra:
        print(f"La palabra {palabra} contiene la letra {letra}")
    else:
        print(f"La palabra {palabra} no contiene la letra {letra}")
    ```

    Si `letra` se encuentra en el `string` `palabra`, el programa imprime un mensaje indicando que la palabra contiene la letra. En caso contrario, se ejecuta el bloque `else`.

### Bucles

Los bucles en Python permiten ejecutar un bloque de código repetidamente, facilitando la
automatización de tareas repetitivas al recorrer secuencias de elementos o al evaluar una
condición.

#### Bucle `for`

El bucle `for` es ideal para iterar sobre secuencias como listas o strings. Su sintaxis
básica es:

```py linenums="1"
for variable in iterable:
    # Código a ejecutar para cada elemento en el iterable
```

???+ example "Recorrer un rango de números"

    La función `range(n, m, s)` genera una secuencia de números desde `n` hasta `m - 1`, con un paso de `s`. Por ejemplo, para mostrar números desde 0 hasta 10 en pasos de 2:

    ```py linenums="1"
    for numero in range(0, 11, 2):
        print(numero)
    ```

???+ example "Recorrer los caracteres de un `string`"

    Se puede utilizar `range()` y `len()` para iterar sobre los índices de un `string`:

    ```py linenums="1"
    mi_string = "Hola caracola"
    for letra in range(len(mi_string)):
        print(mi_string[letra])
    ```

    Alternativamente, se puede iterar directamente sobre los caracteres del `string`:

    ```py linenums="1"
    mi_string = "Hola caracola"
    for letra in mi_string:
        print(letra)
    ```

???+ example "Recorrer dos secuencias simultáneamente con `zip()`"

    `zip()` permite recorrer dos secuencias al mismo tiempo, emparejando sus elementos:

    ```py linenums="1"
    mi_lista1 = "Hola"
    mi_lista2 = "Yadi"

    for item in zip(mi_lista1, mi_lista2):
        print(item)
    ```

    En este ejemplo, solo se recorren los caracteres hasta el final del `string` más corto.

???+ example "Uso de `enumerate()` para obtener índices y valores"

    `enumerate()` permite obtener el índice y el valor de cada elemento en una secuencia:

    ```py linenums="1"
    word = "abcde"

    for idx, letra in enumerate(word):
        print(f"Índice {idx}: {letra}")
    ```

#### Bucle `while`

El bucle `while` continúa ejecutándose mientras una condición se mantenga verdadera. Su
sintaxis básica es:

```py linenums="1"
while condicion:
    # Código a ejecutar mientras la condición sea verdadera
```

???+ example "Crear un contador"

    Un bucle `while` puede usarse para incrementar un contador hasta que alcance un valor determinado:

    ```py linenums="1"
    contador = 0
    while contador < 5:
        print(contador)
        contador += 1
    ```

#### Control de flujo en bucles: `break`, `continue` y `pass`

La instrucción `break` termina el bucle inmediatamente, incluso si no ha terminado de
recorrer todos los elementos:

```py linenums="1"
mi_string = "Daniel"

for letra in mi_string:
    if letra == 'a':
        break
    print(letra)
```

En este ejemplo, el bucle se detiene al encontrar la letra `'a'` y no continúa con el
resto de las iteraciones.

Por otra parte, `continue` omite el resto del código en la iteración actual y pasa a la
siguiente:

```py linenums="1"
mi_string = "Daniel"

for letra in mi_string:
    if letra == 'a':
        continue
    print(letra)
```

Cuando el bucle encuentra la letra `'a'`, omite el `print()` y continúa con la siguiente
letra.

Finalmente, `pass` no realiza ninguna acción, pero se utiliza como marcador de posición
cuando se necesita un bloque de código vacío:

```py linenums="1"
for letra in 'Python':
    if letra == 'h':
        pass  # No realiza ninguna acción
        print('Esta es la letra h')
    print('Letra actual:', letra)
```

### Uso de `__name__` y la función `main`

En Python, la variable especial `__name__` se utiliza para determinar si un archivo se
está ejecutando directamente como un script o si está siendo importado como un módulo en
otro script. Comprender este comportamiento resulta útil para estructurar el código de
manera que ciertos bloques se ejecuten solo cuando el archivo se ejecuta directamente.

> Un script es un conjunto de instrucciones escritas en un lenguaje de programación que
> se ejecutan de manera secuencial. Los scripts se utilizan para automatizar tareas
> repetitivas, realizar operaciones complejas o interactuar con otros programas.

Cuando un archivo de Python se ejecuta directamente, Python asigna a la variable
`__name__` el valor `"__main__"`. Sin embargo, si el archivo es importado como un módulo
en otro script, `__name__` toma el nombre del archivo (sin la extensión `.py`).

#### Caso práctico

Consideremos dos archivos Python, `one79.py` y `two79.py`, que se importan mutuamente:

**Archivo `one79.py`**

```py linenums="1"
# one79.py
import two79

print(f"Archivo 1 __name__ establecido a: {__name__}")

if __name__ == "__main__":
    print("Archivo 1 ejecutado directamente")
else:
    print("Archivo 1 ejecutado como importado a otro módulo")
```

**Archivo `two79.py`**

```py linenums="1"
# two79.py
import one79 as t

print(f"Archivo 2 __name__ establecido a: {__name__}")

if __name__ == "__main__":
    print("Archivo 2 ejecutado directamente")
else:
    print("Archivo 2 ejecutado como importado a otro módulo")
```

Si se ejecuta el archivo `one79.py`, el resultado será:

```
Archivo 1 __name__ establecido a: __main__
Archivo 2 __name__ establecido a: two79
Archivo 2 ejecutado como importado a otro módulo
```

En este caso, `one79.py` muestra que `__name__` es `"__main__"` porque se está ejecutando
directamente, mientras que `two79.py`, al ser importado dentro de `one79.py`, muestra que
`__name__` es `"two79"`.

Es una buena práctica definir una función `main()` que contenga el código principal a
ejecutar. Esto hace que el código sea más organizado y facilita la reutilización:

```py linenums="1"
# one79.py
import two79

def main():
    print("Código principal de one79.py")

if __name__ == "__main__":
    main()
```

En este ejemplo, el código dentro de la función `main()` solo se ejecuta si `one79.py` es
ejecutado directamente. Si es importado, solo se ejecuta el código fuera de la función
`main()`, que podría ser útil para la inicialización de módulos o importaciones.

## Estructuras de datos

En Python, las estructuras de datos son fundamentales para almacenar y manipular datos de
manera eficiente. A continuación se exploran las estructuras de datos más comunes del
lenguaje.

### Listas

Las listas en Python son estructuras de datos que permiten almacenar secuencias ordenadas
y mutables de elementos. A diferencia de otros lenguajes, las listas en Python pueden
contener elementos de diferentes tipos. Su tamaño es dinámico, lo que significa que puede
cambiar durante la ejecución del programa. La indexación comienza en `0`, y los índices
negativos permiten acceder a los elementos desde el final de la lista.

Para definir una lista, basta con usar corchetes y separar los elementos por comas:

```py linenums="1"
lista_amigos = ["Jorge", "Fran", "Ricardo"]
```

También es posible inicializar una lista vacía:

```py linenums="1"
lista = []
```

El acceso a los elementos se realiza mediante el índice:

```py linenums="1"
lista_amigos = ["Jorge", "Fran", "Ricardo"]

# Accede al primer elemento
print(f"El primer amigo es {lista_amigos[0]}")

# Accede al último elemento
print(f"Mi amigo del pueblo es {lista_amigos[-1]}")

# Selecciona un rango de elementos
print(lista_amigos[0:2])

# Muestra la lista completa
print(lista_amigos)
```

#### Métodos

| Función                  | Definición                                                                      |
| ------------------------ | ------------------------------------------------------------------------------- |
| `lista[indice] = x`      | Cambia el elemento en el índice especificado por `x`.                           |
| `lista.extend(x)`        | Agrega los elementos de `x` al final de la lista actual.                        |
| `lista.append(x)`        | Añade un elemento `x` al final de la lista.                                     |
| `lista.insert(indice,x)` | Inserta `x` en el índice especificado.                                          |
| `lista.remove(x)`        | Elimina la primera aparición de `x` en la lista.                                |
| `lista.clear()`          | Vacía la lista.                                                                 |
| `lista.pop()`            | Elimina el último elemento de la lista o el elemento en el índice especificado. |
| `lista.index(x)`         | Devuelve el índice de la primera aparición de `x`.                              |
| `lista.count(x)`         | Devuelve el número de veces que `x` aparece en la lista.                        |
| `lista.sort()`           | Ordena la lista en orden ascendente.                                            |
| `lista.reverse()`        | Invierte el orden de los elementos en la lista.                                 |
| `lista2 = lista1.copy()` | Crea una copia de `lista1` en `lista2`.                                         |
| `max(lista)`             | Devuelve el valor máximo de la lista.                                           |
| `min(lista)`             | Devuelve el valor mínimo de la lista.                                           |
| `del lista[x]`           | Elimina el elemento en el índice `x` de la lista.                               |

#### Comprensión de listas

Los bucles `for` permiten iterar sobre los elementos de una lista de manera sencilla.
Además, Python permite utilizar **comprensión de listas** para crear nuevas listas
basadas en operaciones sobre una secuencia de elementos:

```py linenums="1"
# Crear una lista de caracteres de un string
mi_lista = [letra for letra in "Hola"]
print(mi_lista)

# Crear una lista de cuadrados de números
mi_lista = [numero ** 2 for numero in range(0, 20, 2)]
print(mi_lista)

# Convertir temperaturas de Celsius a Fahrenheit
celcius = [0, 10, 20, 34.5]
fahrenheit = [((9/5) * temp + 32) for temp in celcius]
print(fahrenheit)

# Crear una lista de números cuadrados solo si son pares
mi_lista = [numero ** 2 for numero in range(0, 15, 2) if numero % 2 == 0]
print(mi_lista)
```

#### Listas anidadas y matrices

Las listas en Python pueden contener otras listas, lo que permite la representación de
matrices o tablas de datos. Este tipo de estructura resulta útil para manejar información
en varias dimensiones:

```py linenums="1"
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# Acceder al elemento en la tercera fila y tercera columna
print(number_grid[2][2])
```

En este caso, `number_grid[2][2]` devuelve el valor `9`, que es el elemento ubicado en la
tercera fila y tercera columna.

### Tuplas

Las **tuplas** en Python son secuencias ordenadas e **inmutables**, lo que significa que,
a diferencia de las listas, sus elementos no pueden ser modificados después de su
creación. Las tuplas resultan útiles cuando se necesita garantizar que los datos no
cambien a lo largo del programa. Además, son más rápidas de procesar que las listas.

Para definir una tupla se utilizan paréntesis:

```py linenums="1"
coordenadas = (4, 5)

print(f"Coordenada completa {coordenadas}")
print(f"Primera coordenada {coordenadas[0]} y segunda coordenada {coordenadas[1]}")
```

También es posible combinar tuplas con otras estructuras de datos, como listas de tuplas:

```py linenums="1"
lista_tuplas = [(1, 2), (3, 4), (5, 6)]
print(f"Mi lista de tuplas es {lista_tuplas}")
```

#### Métodos

A pesar de ser inmutables, las tuplas disponen de algunos métodos útiles:

| Función          | Descripción                                                    |
| ---------------- | -------------------------------------------------------------- |
| `tupla.count(x)` | Devuelve el número de veces que `x` aparece en la tupla.       |
| `tupla.index(x)` | Devuelve el índice de la primera aparición de `x` en la tupla. |

### Sets

Los **sets** en Python son colecciones **desordenadas** de elementos únicos. A diferencia
de las listas y tuplas, los sets no permiten duplicados, lo que los convierte en una
herramienta útil para eliminar valores repetidos o para realizar operaciones matemáticas
como uniones e intersecciones.

Un set se puede definir usando llaves `{}` o con la función `set()`:

```py linenums="1"
# Inicializar un set vacío
mi_set = set()

# Añadir elementos
mi_set.add(1)
mi_set.add(1)  # No se añadirá, ya que el elemento es único

# Inicializar un set con elementos
mi_nuevo_set = {'a', 'b', 'c'}
```

#### Métodos

| Función                    | Definición                                                                             |
| -------------------------- | -------------------------------------------------------------------------------------- |
| `s.add(x)`                 | Añade un elemento `x` al set.                                                          |
| `s.clear()`                | Elimina todos los elementos del set.                                                   |
| `sc = s.copy()`            | Crea una copia del set.                                                                |
| `s1.difference(s2)`        | Devuelve los elementos en `s1` que no están en `s2`.                                   |
| `s1.difference_update(s2)` | Elimina los elementos en `s1` que están en `s2`.                                       |
| `s.discard(elem)`          | Elimina el elemento `elem` del set sin causar error si `elem` no está presente.        |
| `s1.intersection(s2)`      | Devuelve los elementos comunes a `s1` y `s2`.                                          |
| `s1.issubset(s2)`          | Verifica si todos los elementos de `s1` están en `s2`.                                 |
| `s1.union(s2)`             | Devuelve la unión de `s1` y `s2`, combinando todos los elementos únicos de ambos sets. |

### Diccionarios

Los **diccionarios** en Python son colecciones de datos que almacenan pares de
**clave-valor**. Las claves son únicas y se utilizan para acceder a los valores
correspondientes. Los diccionarios son mutables, por lo que se pueden modificar después
de su creación.

Un diccionario se define utilizando llaves `{}`, donde cada elemento es un par de
clave-valor:

```py linenums="1"
conversion_meses = {
    "Ene": "Enero",
    "Feb": "Febrero",
    "Mar": "Marzo"
}

# Acceso a valores
print(conversion_meses["Ene"])
print(conversion_meses.get("Ene"))

# Manejo de claves no encontradas
clave = "Daniel"
print(conversion_meses.get(clave, f"La clave {clave} no está en el diccionario"))
```

#### Métodos

| Función                | Definición                                                   |
| ---------------------- | ------------------------------------------------------------ |
| `diccionario.items()`  | Devuelve una vista de los pares clave-valor del diccionario. |
| `diccionario.keys()`   | Devuelve una vista de las claves del diccionario.            |
| `diccionario.values()` | Devuelve una vista de los valores del diccionario.           |

#### Casos prácticos

##### Diccionarios anidados

Es posible crear diccionarios dentro de otros diccionarios para representar estructuras
más complejas:

```py linenums="1"
diccionario = {"k3": {'insideKey': 100}}

# Acceder al valor de 'insideKey'
print(diccionario["k3"]['insideKey'])
```

##### Iteración sobre diccionarios

Se puede iterar sobre claves, valores o pares clave-valor en un diccionario:

```py linenums="1"
d = {'k1': 1, 'k2': 2}

for llave in d.keys():
    print(llave)

for valor in d.values():
    print(valor)

for elemento in d.items():
    print(elemento)
```

##### Listas de diccionarios

Es posible combinar listas y diccionarios para crear estructuras más elaboradas, como una
lista de clientes y sus animales:

```py linenums="1"
clientes = [
    {"nombre": "<nombre>", "animales": ["Pakito", "Pakon", "Pakonazo"]},
    {"nombre": "<nombre>", "animales": ["Rodolfo"]},
    {"nombre": "<nombre>"}
]

for cliente in clientes:
    print(f"{cliente['nombre']} tiene: {cliente.get('animales', 'No tiene animales')}")
```

## Métodos y funciones

En Python, los métodos y las funciones son herramientas esenciales para la programación
modular y la reutilización del código.

### Métodos

Los métodos son funciones que están asociadas a un objeto específico. Actúan sobre el
objeto y pueden modificar su estado o realizar alguna operación en él. Cada tipo de
objeto tiene un conjunto específico de métodos. Por ejemplo, los métodos para objetos de
tipo `str` permiten realizar operaciones como convertir a mayúsculas, dividir la cadena
en palabras o reemplazar subcadenas.

Para información más detallada y actualizada sobre los métodos en Python, se puede
visitar la documentación oficial en [https://docs.python.org/](https://docs.python.org/).

```py linenums="1"
texto = "hola mundo"

# Convertir a mayúsculas
print(texto.upper())  # Output: "HOLA MUNDO"

# Dividir en palabras
print(texto.split())  # Output: ['hola', 'mundo']

# Reemplazar una subcadena
print(texto.replace("mundo", "Python"))  # Output: "hola Python"
```

#### Obtener una lista de métodos disponibles

Para obtener una lista de todos los métodos disponibles para un tipo de objeto, se puede
usar la función `dir()`:

```py linenums="1"
# Muestra todos los métodos disponibles para objetos de tipo str
print(dir(str))
```

#### Obtener ayuda sobre un método específico

Es posible obtener información detallada sobre un método específico utilizando la función
`help()`:

```py linenums="1"
# Muestra la documentación para el método upper()
help(str.upper)
```

### Definición de funciones

Las funciones son bloques de código reutilizables que realizan una tarea específica y
pueden ser llamadas desde cualquier lugar del programa. A diferencia de los métodos, las
funciones no están vinculadas a ningún tipo de objeto en particular.

Para definir una función se utiliza la palabra clave `def`, seguida del nombre de la
función y paréntesis con posibles parámetros:

```py linenums="1"
def saludo(nombre):
    return f"Hola, {nombre}!"

print(saludo("Mundo"))
```

Las funciones pueden tomar cualquier número de parámetros, y estos pueden tener valores
predeterminados. Si un parámetro tiene un valor predeterminado, es posible omitirlo al
llamar a la función:

```py linenums="1"
def saludo(nombre="Mundo"):
    return f"Hola, {nombre}!"

print(saludo())
print(saludo("Python"))
```

En este ejemplo, `nombre` tiene un valor predeterminado de `"Mundo"`. Si se llama a
`saludo()` sin ningún argumento, se utiliza el valor predeterminado. Si se proporciona un
argumento, este reemplaza el valor predeterminado.

#### Casos prácticos

##### Función para comprobar una lista

Esta función toma una lista de números como entrada y separa los números pares e impares
en dos conjuntos diferentes:

```py linenums="1"
def comprobar_lista(lista):
    lista_par_devolver = set()
    lista_impar_devolver = set()

    for indice in lista:
        if indice % 2 == 0:
            lista_par_devolver.add(indice)
        else:
            lista_impar_devolver.add(indice)

    print(f"Lista de números pares de la lista principal: {lista_par_devolver}")
    print(f"Lista de números impares de la lista principal: {lista_impar_devolver}")

comprobar_lista([1, 1, 1, 1, 1, 1, 23, 56, 87, 918, 23, 12, 3, 2, 4, 6, 5])
```

##### Función con tuplas

Este ejemplo muestra una función que determina el trabajador con más horas trabajadas:

```py linenums="1"
horas_trabajadores = [("Daniel", 22), ("Kike", 20), ("Ricardo", 25)]

def mejor_trabajador(lista):
    maximo = 0
    mejor = ""

    for empleado, horas in lista:
        if horas > maximo:
            maximo = horas
            mejor = empleado

    return (mejor, maximo)

mejor, maximo = mejor_trabajador(horas_trabajadores)
print(f"El mejor trabajador es {mejor} que ha trabajado un total de {maximo} horas")
```

##### Funciones que llaman a otras funciones

En este ejemplo se muestra un juego simple donde las funciones interactúan entre sí. Se
utiliza la función `shuffle()` del módulo `random`, que reordena una lista de manera
aleatoria:

```py linenums="1"
from random import shuffle

# Lista de vasos donde 'O' representa la bolita
vasos = [' ', 'O', ' ']

def shuffle_list(mi_lista):
    shuffle(mi_lista)
    return mi_lista

def inicio():
    print("La bolita se encuentra en el vaso 2\n")
    print('vaso 1: ')
    print('vaso 2: O')
    print('vaso 3: ')
    print("\nMoviendo la bola por los diferentes vasos...\n")

def operar():
    resultado = int(input("¿En qué vaso está la bolita?: "))

    while resultado < 1 or resultado > 3:
        print("Este vaso no existe")
        resultado = int(input("¿En qué vaso está la bolita?: "))

    comprobar(resultado)

def comprobar(resultado):
    i = 1

    if vasos[resultado - 1] == 'O':
        print("\n¡Has acertado!\n")
        for vaso in vasos:
            print(f"vaso {i}: {vaso}")
            i += 1
    else:
        print("\nHas fallado :(\n")
        for vaso in vasos:
            print(f"vaso {i}: {vaso}")
            i += 1

inicio()
shuffle_list(vasos)
operar()
```

### Argumentos arbitrarios: `*args` y `**kwargs`

En Python, los términos **`*args`** y **`**kwargs`\*\* se utilizan en la definición de
funciones para permitir que estas acepten un número arbitrario de argumentos.

En el siguiente ejemplo, `a` y `b` son argumentos posicionales:

```py linenums="1"
def mifuncion(a, b):
    return sum((a, b)) * 0.05

mifuncion(40, 60)
```

Si se desea que la función pueda manejar más de dos números, una opción sería asignar un
valor predeterminado a los parámetros adicionales:

```py linenums="1"
def mifuncion(a, b, c=0):
    return sum((a, b, c)) * 0.05
```

#### Funciones con `*args`

**`*args`** permite configurar la función para aceptar un número arbitrario de argumentos
posicionales. Python toma todos los parámetros que se pasan y los agrupa como una tupla:

```py linenums="1"
def mifuncion(*args):
    return sum(args) * 0.05
```

#### Funciones con `**kwargs`

De manera similar, **`**kwargs`\*\* permite manejar un número arbitrario de argumentos de
palabras clave. En lugar de crear una tupla, crea un diccionario:

```py linenums="1"
def mifuncion(**kwargs):
    if 'fruta' in kwargs:
        print(f"Mi fruta favorita es la {kwargs['fruta']}")
    else:
        print("No se encontró la fruta")

    if 'verduras' in kwargs:
        print(f"Mi verdura favorita es la {kwargs['verduras']}")
    else:
        print("No se encontró la verdura")

mifuncion(fruta='manzana', verduras='zanahoria')
```

#### Combinando `*args` y `**kwargs`

También es posible combinar ambos en la misma función:

```py linenums="1"
def mifuncion(*args, **kwargs):
    print(f"Tengo {args[0]} coneja llamada {kwargs['animal']}")

mifuncion(1, 2, 3, 4, fruta="manzana", verdura="zanahoria", animal="Misifu")
```

En este caso, `args` es una tupla de los argumentos posicionales y `kwargs` es un
diccionario de los argumentos de palabras clave, lo que proporciona una gran flexibilidad
a la hora de definir funciones.

### Funciones anónimas (lambdas), `map` y `filter`

Las **expresiones lambda**, junto con las funciones **`map()`** y **`filter()`**, son
herramientas que permiten un procesamiento de datos conciso y eficiente.

Las **expresiones lambda** son una forma rápida de crear funciones anónimas, es decir,
funciones que se utilizan una sola vez:

```py linenums="1"
lambda num: pow(num, 2)
```

La función **`map()`** aplica una función a cada elemento de una lista, devolviendo una
nueva lista con los resultados:

```py linenums="1"
mis_nums = [1, 2, 3, 4, 5]
list(map(lambda num: pow(num, 2), mis_nums))
```

La función **`filter()`** filtra los elementos de una lista basándose en una función de
filtrado, devolviendo una nueva lista con los elementos que cumplen la condición:

```py linenums="1"
mis_nums = [1, 2, 3, 4, 5]
list(filter(lambda num: num % 2 == 0, mis_nums))
```

Las expresiones lambda se utilizan comúnmente junto con `map()` y `filter()`:

```py linenums="1"
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson',
          'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))
```

Es importante recordar que las expresiones lambda pueden tomar múltiples argumentos, lo
que aumenta su flexibilidad. Sin embargo, debido a su naturaleza anónima y de un solo
uso, son más adecuadas para operaciones simples y concisas. Para operaciones más
complejas, es recomendable definir una función completa.

### Decoradores

Los decoradores en Python permiten modificar el comportamiento de una función sin alterar
su código fuente. Esto resulta útil cuando se desea añadir funcionalidades a una función
existente sin modificar su definición.

Los decoradores tienen múltiples aplicaciones. Por ejemplo, se utilizan en el desarrollo
web con _frameworks_ como Flask para añadir comportamientos a las funciones de ruta, como
requerir autenticación para acceder a ciertas páginas. También se emplean para crear
_loggers_ que registran cuándo se llaman a ciertas funciones y con qué argumentos, lo
cual resulta útil para depurar y entender el flujo de ejecución de un programa.

En Python, las funciones son objetos de primera clase. Esto significa que pueden ser
asignadas a variables, almacenadas en estructuras de datos, pasadas como argumentos a
otras funciones e incluso retornadas como valores de otras funciones:

```py linenums="1"
def funcion_saludo():
    return "Hola"

copia = funcion_saludo
del funcion_saludo

print(copia())  # Imprime: Hola
```

Un decorador es una función que toma otra función y extiende su comportamiento sin
modificar explícitamente su código fuente:

```py linenums="1"
def nuevo_decorador(funcion_original):
    def funcion_nueva():
        print("Antes de la funcion original")
        funcion_original()
        print("Despues de la funcion original")
    return funcion_nueva

@nuevo_decorador
def funcion_necesita_decorador():
    print("Necesita un nuevo decorador")

funcion_necesita_decorador()
```

En este ejemplo, `nuevo_decorador` añade dos líneas de impresión antes y después de la
ejecución de la función original. La sintaxis `@nuevo_decorador` antes de la definición
de `funcion_necesita_decorador` es lo que aplica el decorador a la función.

### Generadores

Los generadores en Python son una forma eficiente de crear iteradores. A diferencia de
las funciones normales, los generadores utilizan la palabra clave `yield` en lugar de
`return`. Esto permite que produzcan valores de uno en uno, y solo cuando se necesitan,
en lugar de calcular todos los valores a la vez y almacenarlos en memoria.

Una función generadora devuelve un objeto generador que puede ser iterado para obtener
los valores generados por `yield`:

```py linenums="1"
def funcion_cubo_generador(n):
    for x in range(n):
        yield pow(x, 3)

print(list(funcion_cubo_generador(10)))  # Imprime: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
```

Los generadores son especialmente útiles cuando se trabaja con grandes cantidades de
datos que no caben en memoria. En lugar de generar todos los datos a la vez, los producen
de uno en uno, lo que puede mejorar significativamente el rendimiento del programa.

La función `iter()` convierte un objeto iterable en un iterador, lo que permite utilizar
la función `next()` para acceder a sus elementos uno a uno:

```py linenums="1"
s = "hello"
s_iterador = iter(s)
print(next(s_iterador))  # Imprime: h
```

### Cronometrar el tiempo de ejecución de una función

Para evaluar la eficiencia del código, es posible medir el tiempo que una función tarda
en ejecutar una acción específica:

```py linenums="1"
import time

def func_uno(n):
    return [str(num) for num in range(n)]

def func_dos(n):
    return list(map(str, range(n)))

# Paso 1: Registrar el tiempo de inicio
start_time = time.time()

# Paso 2: Ejecutar el código que queremos cronometrar
result = func_uno(1000000)

# Paso 3: Calcular el tiempo total de ejecución
end_time = time.time() - start_time
print(end_time)
```

Para mediciones más precisas, se puede utilizar la biblioteca `timeit`, que permite
realizar múltiples repeticiones:

```py linenums="1"
import timeit

setup = '''
def func_uno(n):
    return [str(num) for num in range(n)]
'''

stmt = 'func_uno(100)'
print(timeit.timeit(stmt, setup, number=100000))

setup2 = '''
def func_dos(n):
    return list(map(str, range(n)))
'''

stmt2 = 'func_dos(100)'
print(timeit.timeit(stmt2, setup2, number=100000))
```

En Jupyter Notebooks es posible utilizar **funciones mágicas** (se activan con dos signos
de porcentaje al comienzo del bloque de código), como la función `timeit`:

```py linenums="1"
%%timeit
func_uno(100)
```

### Alcance de las variables (Scope)

En Python, es crucial entender cómo se manejan las variables. Estas se almacenan en lo
que se conoce como un "alcance" o _scope_, que determina la visibilidad de la variable en
otras partes del código:

```py linenums="1"
x = 25

def printer():
    x = 50
    return x

print(x)  # Devuelve 25
print(printer())  # Devuelve 50
```

La reasignación de `x` dentro de la función `printer()` no afecta a la asignación global
de `x`. Esto se debe a la regla de alcance en Python, que sigue la regla **LEGB**:

- **L, Local**: Nombres asignados dentro de una función (`def` o `lambda`) y que no se
  declaran globales en esa función.
- **E, Enclosing function locals**: Nombres en el ámbito local de cualquier función de
  encierro (`def` o `lambda`), de interior a exterior.
- **G, Global (module)**: Nombres asignados en el nivel superior de un archivo de módulo,
  o declarados globales en un `def` dentro del archivo.
- **B, Built-in (Python)**: Nombres preasignados en el módulo de nombres incorporados:
  `open`, `range`, `SyntaxError`, etc.

Este es el orden en el que Python busca las variables:

```py linenums="1"
# VARIABLE GLOBAL
nombre = "Esto es un string global"

def prueba():
    # VARIABLE DE ENCIERRO LOCAL
    nombre = "Daniel"

    def hola():
        # VARIABLE LOCAL
        nombre = "Carlitos"
        print(f"Hola {nombre}")

    hola()

prueba()
```

En este ejemplo, la función `hola()` muestra primero la variable local `"Carlitos"`. Si
se comenta la asignación local, toma la variable de encierro local `"Daniel"`. Y si
también se comenta esa asignación, toma la variable global `"Esto es un string global"`.

Cuando se reasigna una variable global dentro de una función, por el alcance, el valor de
reasignación solo se mantiene dentro de la función. Para modificar la variable global
desde dentro de una función, se puede usar la palabra clave `global`:

```py linenums="1"
x = 50

def prueba():
    global x
    print(f"Valor de x antes {x}")
    x = 200
    print(f"Valor de x despues {x}")

prueba()
print(f"Valor de x fuera {x}")
```

Sin embargo, se recomienda evitar el uso de `global` a menos que sea absolutamente
necesario. Es más seguro devolver un objeto y luego asignarlo a la variable, evitando así
sobrescribir la variable global dentro de una función de forma inadvertida.

## Programación Orientada a Objetos

La **Programación Orientada a Objetos (POO)** es un paradigma que organiza el código en
torno a **objetos** en lugar de funciones y lógica. Estos objetos combinan **datos**
(atributos) y **funciones** (métodos) que actúan sobre los datos. Este enfoque permite la
reutilización, modularidad y escalabilidad del código.

### Clases y objetos

Una **clase** es un molde o plantilla para crear objetos, que son instancias de la clase.
Los objetos tienen **atributos** (características) y **métodos** (comportamientos):

```py linenums="1"
class NombreDeClase():

    def __init__(self, parametro1, parametro2):
        self.parametro1 = parametro1
        self.parametro2 = parametro2

    def algun_metodo(self):
        print("Este es un método dentro de la clase")
```

Cuando se define una función dentro de una clase, se le llama **método**. El método
especial `__init__` es un **constructor** que se ejecuta automáticamente al crear una
nueva instancia de la clase. El primer argumento de cualquier método en una clase es
`self`, que se refiere a la instancia del objeto.

```py linenums="1"
class Coche():

    def __init__(self, marca, modelo, mejorado, acceso_coche):
        self.marca = marca
        self.modelo = modelo
        self.mejorado = mejorado
        self.acceso_coche = acceso_coche

mi_coche = Coche("Toyota", "Corolla", True, ["Juan", "Maria"])
print(f"Mi coche es un {mi_coche.marca} {mi_coche.modelo}")
```

### Métodos y atributos

Los **atributos** son características del objeto, y los **métodos** son acciones que
puede realizar. Algunos atributos son comunes a todas las instancias (atributos de
clase), mientras que otros son específicos para cada objeto (atributos de instancia):

```py linenums="1"
class Perro():

    # Atributo de clase (común para todas las instancias)
    especie = "mamífero"

    def __init__(self, raza, nombre, edad):
        # Atributos de instancia
        self.raza = raza
        self.nombre = nombre
        self.edad = edad

    def sonido(self):
        return "Woof!"

    def informacion(self):
        print(f"Nombre: {self.nombre}, Raza: {self.raza}, Edad: {self.edad}, Especie: {self.especie}")

if __name__ == '__main__':
    mi_perro = Perro("Labrador", "Fido", 3)
    mi_perro.informacion()
```

En este ejemplo, `especie` es un atributo de clase compartido por todas las instancias de
`Perro`, mientras que `raza`, `nombre` y `edad` son atributos únicos para cada instancia.

### Herencia y polimorfismo

#### Herencia

La **herencia** permite crear nuevas clases a partir de clases ya existentes. La nueva
clase (subclase) hereda los atributos y métodos de la clase padre, pero también puede
tener sus propios atributos y métodos o sobrescribir los heredados:

```py linenums="1"
class Animal():

    def __init__(self, nombre):
        self.nombre = nombre

    def quien_soy(self):
        print("Soy un animal")

    def comer(self):
        print("Estoy comiendo")

class Perro(Animal):

    def quien_soy(self):
        print(f"Soy un perro llamado {self.nombre}")

mi_perro = Perro("Fido")
mi_perro.quien_soy()  # Imprime: Soy un perro llamado Fido
mi_perro.comer()  # Imprime: Estoy comiendo
```

En este caso, `Perro` hereda de `Animal`, por lo que puede usar el método `comer`.
Además, la subclase `Perro` sobrescribe el método `quien_soy` de la clase `Animal`.

#### Polimorfismo

El **polimorfismo** permite usar el mismo nombre de método en diferentes clases. Aunque
el método tenga el mismo nombre, cada clase puede implementarlo de manera diferente:

```py linenums="1"
class Perro():

    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        print(f"El perro {self.nombre} ladra")

class Gato():

    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        print(f"El gato {self.nombre} maulla")

mi_perro = Perro("Fido")
mi_gato = Gato("Miau")

mi_perro.sonido()  # Imprime: El perro Fido ladra
mi_gato.sonido()  # Imprime: El gato Miau maulla
```

### Clases abstractas

Una **clase abstracta** es aquella que no se espera que se instancie directamente. Solo
sirve como base para otras clases que implementen sus métodos:

```py linenums="1"
class Animal():

    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        raise NotImplementedError("Subclase debe implementar este método")

class Perro(Animal):

    def sonido(self):
        return f"{self.nombre} hace woof!"

mi_perro = Perro("Fido")
print(mi_perro.sonido())  # Imprime: Fido hace woof!
```

Si no se implementa el método en la subclase, se genera un error al intentar invocarlo.

## Módulos y paquetes

### Importación de módulos

En Python, los **módulos** son archivos que contienen definiciones y declaraciones,
mientras que los **paquetes** son colecciones de módulos. Un gestor de paquetes muy
utilizado es **PIP**, que permite instalar y administrar bibliotecas externas.

PIP se utiliza junto con **PyPI** (Python Package Index), un repositorio que contiene
numerosos paquetes de terceros. Para instalar un paquete, se ejecuta el comando
`pip install` en la terminal:

```bash linenums="1"
pip install colorama
```

```py linenums="1"
from colorama import init, Fore

init()

# Texto en rojo
print(Fore.RED + "Texto de prueba")
```

### Uso de paquetes y librerías externas

Un **módulo** es simplemente un archivo `.py` que contiene funciones, variables y clases.
Un **paquete** es una colección de módulos organizados en una carpeta. El paquete debe
contener un archivo `__init__.py`, el cual puede estar vacío, pero es necesario para que
Python trate el directorio como un paquete.

Ejemplo de cómo estructurar un proyecto con módulos y submódulos:

```py linenums="1"
# main.py
from paquete78 import some_main_script as p
from paquete78.Subpaquetes import mysubscript as s

p.main_report()
s.sub_report()
```

```py linenums="1"
# paquete78/some_main_script.py
def main_report():
    print("Hola, soy una función dentro de mi script principal.")
```

```py linenums="1"
# paquete78/Subpaquetes/mysubscript.py
def sub_report():
    print("Hola, soy una función dentro de mi subscript.")
```

### Módulos avanzados de Python

#### Módulos de colección

El módulo `collections` proporciona tipos de datos especializados como `Counter`,
`defaultdict` y `namedtuple`, que son alternativas más eficientes a los contenedores
generales de Python (`dict`, `list`, `set` y `tuple`).

##### Counter

`Counter` es una subclase de diccionario para contar elementos de manera rápida. Almacena
los elementos como claves y su recuento como valores:

```py linenums="1"
from collections import Counter

lista = [1, 1, 1, 2, 2, 3, 'a', 'adios']
cuenta = Counter(lista)

print(cuenta.most_common())  # Devuelve los elementos más comunes
```

##### defaultdict

`defaultdict` es una subclase de `dict` que devuelve un valor predeterminado si la clave
no existe, evitando errores:

```py linenums="1"
from collections import defaultdict

d = defaultdict(lambda: 0)
print(d["inexistente"])  # Imprime: 0
```

##### namedtuple

`namedtuple` es una subclase de tupla que permite acceder a sus elementos por nombre en
lugar de por índice:

```py linenums="1"
from collections import namedtuple

Conejo = namedtuple("Conejo", ["Edad", "Color", "Nombre"])
misifu = Conejo(Edad=2, Color="Blanco", Nombre="Misifu")

print(misifu.Edad)  # Imprime: 2
```

### Módulo de fecha y hora

El módulo `datetime` permite trabajar con fechas y horas en Python. Es posible crear
objetos de fecha, realizar cálculos y extraer información como el año, mes o día:

```py linenums="1"
import datetime
from datetime import date

# Crear un objeto de tiempo
mi_tiempo = datetime.time(2, 20)
print(mi_tiempo.minute)  # Imprime: 20
print(mi_tiempo)  # Imprime: 02:20:00

# Obtener la fecha actual
hoy = datetime.date.today()
print(hoy)

# Extraer día, mes y año
print(f"Día: {hoy.day}, Mes: {hoy.month}, Año: {hoy.year}")

# Operaciones con fechas
fecha1 = date(2021, 11, 3)
fecha2 = date(2020, 11, 2)
print(fecha1 - fecha2)  # Imprime: 366 days, 0:00:00
```

### Módulo `math` y `random`

#### Módulo `math`

El módulo `math` proporciona funciones matemáticas comunes, como el valor de $\pi$,
logaritmos y funciones trigonométricas:

```py linenums="1"
import math

# Valor de pi y e
print(math.pi)  # Imprime: 3.141592653589793
print(math.e)   # Imprime: 2.718281828459045

# Logaritmo en base 2 de 100
print(math.log(100, 2))  # Imprime: 6.643856189774724

# Funciones trigonométricas
print(math.sin(math.radians(90)))  # Imprime: 1.0
print(math.degrees(math.pi / 2))  # Imprime: 90.0
```

#### Módulo `random`

El módulo `random` genera números pseudoaleatorios y ofrece varias funciones para elegir
elementos aleatoriamente o barajar listas:

```py linenums="1"
import random

# Número aleatorio entre 0 y 100
print(random.randint(0, 100))

# Semilla para números aleatorios reproducibles
random.seed(101)

# Lista de números del 0 al 9
lista = list(range(10))
print(lista)

# Elegir un número aleatorio de la lista
print(random.choice(lista))

# Elegir varios números aleatorios (pueden repetirse)
print(random.choices(lista, k=5))

# Elegir varios números aleatorios sin repetición
print(random.sample(lista, k=4))

# Barajar la lista de forma aleatoria
random.shuffle(lista)
print(lista)
```

## Manejo de errores y excepciones

### Validación de datos

Cuando se crean funciones que toman valores de entrada del usuario, es importante
verificar esas entradas para asegurarse de que son correctas. Esto se conoce como
validación de datos.

La función `input()` en Python puede resultar problemática porque espera la interacción
del usuario. Si se ejecuta accidentalmente dos veces, el programa puede quedarse
esperando una respuesta que no llega. En Jupyter, en ese caso, sería necesario reiniciar
el kernel, teniendo en cuenta que todas las variables anteriores se borrarán y habrá que
ejecutarlas de nuevo.

Una forma cómoda de validar datos es utilizar bucles `while` para pedir al usuario que
introduzca un valor repetidamente cuando este no es válido:

```py linenums="1"
def limite(eleccion):
    return int(eleccion) >= 1 and int(eleccion) <= 10

def eleccion_usuario():
    eleccion = input("Numero de 1-10: ")

    while not eleccion.isdigit() or not limite(eleccion):
        eleccion = input("Numero de 1-10: ")

        if not eleccion.isdigit():
            print("El valor introducido no es un numero")

        if eleccion.isdigit() and not limite(eleccion):
            print("El numero introducido supero el limite")

    return int(eleccion)

eleccion_usuario()
```

Para limpiar la consola cuando el usuario introduce valores incorrectos en un cuaderno
Jupyter, se puede importar y usar la función `clear_output()` de la biblioteca
`IPython.display`:

```py linenums="1"
from IPython.display import clear_output
```

Esta función borra la salida de la celda actual en un cuaderno Jupyter, lo que puede ser
útil para mantener la interfaz limpia. Sin embargo, solo funciona en cuadernos Jupyter y
no en otros entornos de Python.

### Manejo de excepciones

El manejo de errores es una estrategia que permite planificar y gestionar posibles
errores que puedan surgir en el código. Por ejemplo, si un usuario intenta escribir en un
archivo que se ha abierto en modo de solo lectura y no existe ninguna declaración de
error en el código, el programa entero se detendrá. Para evitar esto, se utiliza el
manejo de excepciones, que permite continuar con el programa, notificar el error y seguir
con la ejecución.

Existen tres palabras clave para el manejo de errores en Python:

- `try`: Bloque de código que se intenta ejecutar (puede producir un error).
- `except`: Bloque de código que se ejecuta en caso de que haya un error en el bloque
  `try`.
- `finally`: Bloque final de código que se ejecuta independientemente de si hubo un error
  o no.

```py linenums="1"
try:
    f.open("fichero", 'w')
    f.write("Linea de prueba")
except TypeError:
    print("Hubo un problema con el tipo")
except OSError:
    print("Hubo un error de OSError")
except:
    print("Hubo un fallo en otro tipo de excepciones")
finally:
    print("De todos modos seguí ejecutando el código")
```

En este otro ejemplo, se pide constantemente un dato al usuario hasta que introduzca un
valor adecuado:

```py linenums="1"
def introducir_entero():
    while True:
        try:
            valor = int(input("Introduce un número entero: "))
        except:
            print("El valor introducido no es un número")
        else:
            print(f"El valor {valor} es un valor correcto")
            break

introducir_entero()
```

Python tiene más excepciones implementadas que se pueden consultar en la documentación
oficial, en el apartado "Library → Exceptions".

### Depurador de Python

El depurador o **debugger** se emplea para identificar y corregir errores en el código.
En lugar de utilizar `print()` para inspeccionar el estado del programa, se puede usar el
depurador de Python, `pdb`:

```py linenums="1"
import pdb

x = [1, 2, 3]
z = 2
y = 1

resultado1 = z + y

# Al añadir este depurador, se pueden introducir las variables declaradas
# para ver su tipo e incluso realizar operaciones con ellas,
# comprobando si el resultado es el esperado o no.
# Una vez revisados los posibles casos y fallos, se pulsa "q" para salir del depurador.
pdb.set_trace()

resultado2 = y + x  # ERROR
```

### Pruebas unitarias con Pylint

Las pruebas unitarias son esenciales a medida que se expanden los proyectos con varios
archivos o se comienza a trabajar en equipo. Al realizar cualquier cambio o actualización
en el código, se pueden ejecutar archivos de prueba para asegurarse de que el código
anterior sigue funcionando de la manera esperada.

Existen diferentes herramientas para probar el código, entre las que destacan:

- **Pylint**: Biblioteca que analiza el código e informa de posibles problemas.
- **Unittest**: Biblioteca incorporada que permite probar programas y comprobar que se
  obtienen los resultados deseados.

Para usar Pylint, se ejecuta el siguiente comando en la terminal:

```bash linenums="1"
pylint nombre_fichero.py -r y
```

### Pruebas con Unittest

Con `unittest` se puede implementar un script en Python que analice los resultados
devueltos por el código y compruebe si son los esperados.

`cap85a.py`:

```py linenums="1"
def prueba(texto):
    return texto.capitalize()
```

`cap85b.py`:

```py linenums="1"
import cap85a
import unittest

class Test(unittest.TestCase):

    def test_1(self):
        texto = 'python'
        resultado = cap85a.prueba(texto)
        self.assertEqual(resultado, 'Python')

if __name__ == '__main__':
    unittest.main()
```

Si el resultado es el esperado, la prueba pasa. Si no, la prueba falla y se muestra un
mensaje de error.

## Trabajo con archivos y directorios

### Lectura y escritura de archivos

Es posible abrir un fichero usando la función `open()`:

```py linenums="1"
file = open(dirección_del_fichero)
```

Python permite asignar diferentes permisos (escritura, lectura o ambas) al fichero:

| Permiso | Definición                                                               |
| ------- | ------------------------------------------------------------------------ |
| `r`     | Solo lectura.                                                            |
| `w`     | Solo escritura, reescribe los archivos existentes o crea uno nuevo.      |
| `a`     | Para añadir información al final del archivo.                            |
| `r+`    | Lectura y escritura.                                                     |
| `w+`    | Escritura y lectura, reescribe los archivos existentes o crea uno nuevo. |
| `wb`    | Modo archivo, escritura y binario.                                       |

Para leer un fichero se pueden utilizar las siguientes funciones:

| Función       | Definición                                                        |
| ------------- | ----------------------------------------------------------------- |
| `readable()`  | Devuelve un booleano para saber si se puede leer o no el fichero. |
| `read()`      | Muestra toda la información del fichero.                          |
| `readline()`  | Lee la primera línea del fichero.                                 |
| `readlines()` | Lee todas las líneas del fichero y las inserta en una lista.      |

```py linenums="1"
nombre_fic = input("Nombre del fichero: ")

fichero = open(nombre_fic, "r")

if fichero.readable():
    lista = fichero.readlines()
```

También es posible iterar directamente sobre las líneas del fichero:

```py linenums="1"
for empleado in empleado_fic:
    print(empleado)

# Es recomendable cerrar el fichero después de trabajar con él
empleado_fic.close()
```

Si se lee un archivo directamente con métodos como `read()`, al leer de nuevo el fichero
no aparecerá nada. Para solucionarlo se utiliza `nombre_fichero.seek(0)`, que permite
poner el cursor al principio del fichero.

Otra forma de abrir un fichero y operar con él es mediante el gestor de contexto `with`,
que cierra automáticamente el archivo al finalizar el bloque:

```py linenums="1"
with open('myfile.txt', mode='w') as my_new_file:
    contents = my_new_file.read()

print(contents)
```

Un ejemplo de cómo escribir en un fichero:

```py linenums="1"
nombre_fic = input("Nombre del fichero: ")

fichero = open(nombre_fic, "a")

nuevo_empleado = input("Nombre del nuevo empleado: ")
funcion_empleado = input(f"Puesto del empleado {nuevo_empleado}: ")

fichero.write("\\n" + nuevo_empleado + " - " + funcion_empleado)
fichero.close()
```

### Manejo de archivos y directorios

En Python se utilizan varios módulos para la apertura, lectura y manipulación de archivos
y directorios en el sistema operativo. Los módulos principales son `shutil` y `os`, que
permiten realizar operaciones como navegar por los directorios, mover y eliminar
archivos, entre otras:

```py linenums="1"
import os
import shutil
import send2trash

# Creación de un archivo de prueba
f = open("Prueba.txt", 'w+')
f.write("Esto es una prueba de escritura en un archivo")
f.close()

# Obtención del directorio de trabajo actual
print(os.getcwd())

# Listado de los elementos en el directorio de trabajo
print(os.listdir())

# Listado de los elementos en un directorio específico
print(os.listdir('/home/usuario/'))

# Movimiento de archivos entre directorios
shutil.move("Prueba.txt", '/home/daniel/')

# Eliminación segura de archivos con send2trash
send2trash.send2trash("Prueba.txt")
```

Python también permite listar todos los archivos de un directorio, incluyendo carpetas,
subcarpetas y ficheros:

```py linenums="1"
import os

directorio = '/home/daniel/Desktop'

for carpeta, sub_carpetas, archivos in os.walk(directorio):
    print(f"Estamos en la carpeta: {carpeta}")
    print("Las subcarpetas son: ")

    for sub_carpeta in sub_carpetas:
        print(f"\t{sub_carpeta}")

    print("Los archivos son: ")

    for archivo in archivos:
        print(f"\t{archivo}")
```

### Manipulación de archivos CSV y JSON

Los archivos CSV (Comma Separated Values) son un formato utilizado por Excel y otros
programas de bases de datos. Son útiles para la manipulación de datos, aunque solo
contienen el contenido en crudo, sin imágenes, macros ni formato visual.

En Python se trabaja con el módulo `csv` incluido en la biblioteca estándar. Otras
bibliotecas a considerar para la manipulación de datos son Pandas, Openpyxl o la API de
Google Sheets para Python.

```py linenums="1"
import csv

# Abrimos el fichero
datos = open('example.csv', encoding='utf-8')

# csv.reader
csv_datos = csv.reader(datos)

# Convertimos los datos a una lista
lineas_datos = list(csv_datos)

correos = []

for linea in lineas_datos[1:]:
    if linea[3] not in correos:
        correos.append(linea[3])

for numero, correo in enumerate(correos):
    print(f"{numero} : {correo}")
```

Para escribir en un archivo CSV:

```py linenums="1"
import csv

# Creamos un archivo CSV
archivo_salida = open('fichero_prueba.csv', mode='w', newline='')

# "delimiter" es un delimitador que separa una columna de otra
csv_escribir = csv.writer(archivo_salida, delimiter=',')

csv_escribir.writerow(['a', 'b', 'c'])
csv_escribir.writerows([['1', '2', '3'], ['4', '5', '6']])

archivo_salida.close()

# Añadimos información al final del archivo
f = open('fichero_prueba.csv', mode='a', newline='')
csv_writer = csv.writer(f)

csv_writer.writerow(['Nombre', 'Apellido', 'Correo'])
csv_writer.writerows([['Daniel', 'BC', '<email>'],
                      ['Clara', 'RA', '<email>']])

f.close()
```

Para trabajar con ficheros JSON se importa la biblioteca `json`:

```py linenums="1"
import json

json_string = '{"Nombre":"Antonio", "Apellidos":"Adrian"}'
obj = json.loads(json_string)

print(f"Nombre: {obj['Nombre']} \nApellidos: {obj['Apellidos']}")
```

Python también permite cargar ficheros JSON directamente desde una URL:

```py linenums="1"
import requests

r = requests.get("url")
print(r.json())
```

### Comprimir y descomprimir archivos

```py linenums="1"
import zipfile

# Creación de archivos de prueba
f = open("nuevo_archivo.txt", 'w+')
f.write("Esto es solo un ejemplo de introducción de texto")
f.close()

f = open("nuevo_archivo2.txt", 'w+')
f.write("Un poquito más de texto")
f.close()

# Creación del archivo zip
archivo_comprimido = zipfile.ZipFile('comprimido_1.zip', 'w')

# Añadir archivos al zip
archivo_comprimido.write("nuevo_archivo.txt", compress_type=zipfile.ZIP_DEFLATED)
archivo_comprimido.write('nuevo_archivo2.txt', compress_type=zipfile.ZIP_DEFLATED)

archivo_comprimido.close()

# Extraer archivos de un archivo zip
zip_obj = zipfile.ZipFile('comprimido_1.zip', 'r')
zip_obj.extractall("contenido_extraido")
```

## Expresiones regulares

Las expresiones regulares en Python permiten manipular y buscar patrones en texto de
forma eficiente mediante el módulo `re`.

### Búsqueda y manipulación de patrones

```py linenums="1"
import re

texto = "El número del agente es 111-111-1111"
patron = "número"

# Localiza la palabra y muestra el índice desde donde empieza hasta donde acaba
busqueda = re.search(patron, texto)

# Muestra el índice de inicio de la palabra
print(busqueda.start())

# Muestra el índice de finalización de la palabra
print(busqueda.end())

# Si queremos encontrar todas las coincidencias, utilizamos findall
texto2 = "Mi número favorito es el número 8"
busqueda2 = re.findall("número", texto2)

# Para ver en qué índice se encuentra la palabra repetida
print("La palabra 'número' está en los siguientes índices:")

for palabra in re.finditer('número', texto2):
    print(f"\t{palabra.span()}")

# Para mostrar la palabra junto con el índice
print("\nLa palabra 'número' está en los siguientes índices:")

for palabra in re.finditer('número', texto2):
    print(f"\t{palabra.group()} -> {palabra.span()}")
```

### Patrones generales

```py linenums="1"
import re

texto = "Mi número de teléfono es 11 11 11 111"

# Importante usar la 'r' para indicar a Python que es un patrón raw
numero = re.search(r"\d{2} \d{2} \d{2} \d{3}", texto)
print(numero.group())

# Para extraer áreas concretas del patrón, se pueden utilizar grupos
numero_grupos = re.compile(r"(\d{2}) (\d{2}) (\d{2}) (\d{3})")
resultado = re.search(numero_grupos, texto)

# Acceder a un índice específico del grupo
print(resultado.group(4))
```

### Patrones de palabras

```py linenums="1"
import re

texto = "Tengo una coneja que se llama Misifu"

busq1 = re.search(r'coneja|perro', texto)
print(busq1.group())

texto2 = "Tengo un perro que se llama Tom"

busq2 = re.search(r'coneja|perro', texto2)
print(busq2.group())

texto3 = "The cat in the hat sat there"

# Encontrar palabras que terminen con 'at'
terminadas_at = re.findall(r'.at', texto3)
print(terminadas_at)

# Exclusión de caracteres específicos
phrase = "there are 3 numbers 34 inside 5 this sentence."
print(re.findall(r'[^\d]+', phrase))

# Eliminar signos de puntuación
test_phrase = """This is a string! But it has punctuation. How can we remove it?"""
clean = ' '.join(re.findall('[^!.? ]+', test_phrase))
print(clean)

# Encontrar palabras que comienzan con ciertos patrones
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
re.search(r'cat(fish|nap|claw)', text)
re.search(r'cat(fish|nap|claw)', texttwo)
```

## Expresiones regulares avanzadas

Esta sección profundiza en técnicas más avanzadas de expresiones regulares que resultan
esenciales para la limpieza y manipulación de datos en aplicaciones reales.

### Patrones y clases de caracteres

Las clases de caracteres permiten definir conjuntos de caracteres que se desea buscar. Se
delimitan con corchetes `[]` y admiten rangos, negaciones y combinaciones:

```python linenums="1"
import re

grades = "ACAAAABCBCBAA"

# Buscar todas las calificaciones B
re.findall("B", grades)

# Buscar calificaciones A o B
re.findall("[AB]", grades)

# Buscar combinaciones AB o AC
re.findall("[A][B-C]", grades)

# Equivalente con operador lógico
re.findall("AB|AC", grades)

# Negar un conjunto: todo lo que no sea A
re.findall("[^A]", grades)

# Cuidado con la combinación de ^ dentro y fuera de corchetes
re.findall("^[^A]", grades)
# Lista vacía: busca al inicio de la cadena un carácter que no sea A,
# pero la cadena comienza con A
```

### Cuantificadores

Los cuantificadores especifican cuántas veces debe aparecer un patrón para considerarse
una coincidencia. La sintaxis básica es `e{m,n}`, donde `e` es la expresión, `m` el
mínimo de repeticiones y `n` el máximo:

```python linenums="1"
import re

grades = "ACAAAABCBCBAA"

re.findall("A{2,10}", grades)  # Secuencias de 2 a 10 letras A consecutivas

re.findall("A{1,1}A{1,1}", grades)  # Pares de A consecutivas

# Sin cuantificador, el valor predeterminado es 1
re.findall("A{2}", grades)  # Exactamente 2 letras A consecutivas
```

Es importante tener en cuenta que no se deben incluir espacios dentro de las llaves del
cuantificador, ya que `"A{2, 2}"` devuelve un resultado vacío.

El metacarácter `\w` representa cualquier letra o dígito, y el asterisco `*` indica cero
o más repeticiones. El siguiente ejemplo extrae los encabezados de un artículo de
Wikipedia donde cada encabezado va seguido de `[edit]`:

```python linenums="1"
import re

with open("datasets/ferpa.txt", "r") as file:
    wiki = file.read()

# Buscar palabras seguidas de [edit] con límite de caracteres
re.findall("[\\w]{1,100}\\[edit\\]", wiki)

# Equivalente sin límite superior usando *
re.findall("[\\w]*\\[edit\\]", wiki)

# Extraer solo los títulos sin la etiqueta [edit]
for title in re.findall("[\\w ]*\\[edit\\]", wiki):
    print(re.split("[\\[]", title)[0])
```

### Grupos

Los grupos permiten hacer coincidir diferentes patrones simultáneamente y referirse a
ellos de forma independiente. Se definen con paréntesis:

```python linenums="1"
import re

# Agrupar título y etiqueta [edit] por separado
re.findall("([\\w ]*)(\\[edit\\])", wiki)

# Iterar sobre los resultados con finditer
for item in re.finditer("([\\w ]*)(\\[edit\\])", wiki):
    print(item.groups())

# Acceder a un grupo específico (grupo 0 es la coincidencia completa)
for item in re.finditer("([\\w ]*)(\\[edit\\])", wiki):
    print(item.group(1))
```

Los grupos pueden etiquetarse con nombres mediante la sintaxis `(?P<nombre>...)`, lo que
permite acceder a los resultados como un diccionario:

```python linenums="1"
for item in re.finditer("(?P<title>[\\w ]*)(?P<edit_link>\\[edit\\])", wiki):
    print(item.groupdict()['title'])
```

### _Look-ahead_ y _look-behind_

Estas técnicas permiten hacer coincidir un patrón sin capturarlo en el resultado. El
_look-ahead_ utiliza la sintaxis `(?=...)`:

```python linenums="1"
import re

for item in re.finditer("(?P<title>[\\w ]+)(?=\\[edit\\])", wiki):
    print(item)
```

También es posible crear patrones multilínea utilizando la bandera `re.VERBOSE`:

```python linenums="1"
patron = """
(?P<title>.*)           # Nombre de la universidad
(–\\ located\\ in\\ )  # Indicación de localización
(?P<city>\\w*)          # Ciudad
(,\\ )                  # Separador
(?P<state>\\w*)         # Estado
"""

for item in re.finditer(patron, wiki, re.VERBOSE):
    print(item.groupdict())
```

Para más información sobre expresiones regulares, se puede consultar la
[documentación oficial](https://docs.python.org/3/library/re.html) y utilizar
herramientas como [regex101](https://regex101.com/) para depurar patrones.

## Calidad y rendimiento del código

### Calidad del código

El código de alta calidad puede definirse de varias maneras: puede ser el código que se
ejecuta más rápido, el que resulta más fácil de leer o el que es más sencillo de
mantener. Un aspecto crucial para mantener la calidad del código es la
**modularización**, que consiste en dividir un programa en subprogramas más pequeños o
módulos, cada uno de los cuales realiza una tarea específica. Esto mejora la legibilidad
y facilita el mantenimiento, ya que es esperable que el código cambie a medida que
evoluciona el proyecto.

### Estrategias de optimización del rendimiento

Existen diversas estrategias para mejorar el rendimiento del código en Python:

- **Elección del algoritmo**: Las decisiones algorítmicas pueden marcar una gran
  diferencia en el rendimiento.
- **Elección de la estructura de datos**: Diferentes estructuras de datos presentan
  distintas compensaciones según la tarea a realizar.
- **Uso de funciones incorporadas**: Las funciones nativas de Python suelen ser más
  eficientes que las implementaciones propias, ya que muchas están implementadas en C.
- **Compilación de Python**: Herramientas como Cython, Numba y PyPy permiten compilar
  Python a un lenguaje de nivel inferior. Numba contiene un subconjunto de Python; Cython
  es un superconjunto con opciones adicionales en C; y PyPy es una reimplementación de
  Python con compilación _just-in-time_.
- **Código asíncrono**: Permite ejecutar operaciones de entrada/salida de forma no
  bloqueante.
- **Computación paralela y distribuida**: Aprovecha múltiples núcleos o máquinas para
  acelerar el procesamiento.

### Perfilado de código

El perfilado de código permite medir el rendimiento de diferentes partes de un programa e
identificar cuellos de botella. `cProfile` es el perfilador incorporado de Python:

```python linenums="1"
import numpy as np
from collections import Counter

def mode_using_counter(n_integers):
    random_integers = np.random.randint(1, 100_000, n_integers)
    c = Counter(random_integers)
    return c.most_common(1)[0][0]
```

En un cuaderno Jupyter, se puede ejecutar el perfilador con:

```python linenums="1"
%%prun
mode_using_counter(10_000_000)
```

La columna `tottime` en la salida muestra dónde se invierte la mayor parte del tiempo.
Para obtener una visualización gráfica de los resultados, se puede utilizar **SnakeViz**:

```bash
pip install snakeviz
```

```python linenums="1"
%load_ext snakeviz

%%snakeviz
mode_using_counter(10_000_000)
```

Para el perfilado de memoria, **Memray** es una herramienta desarrollada por Bloomberg
que genera informes detallados sobre el uso de memoria:

```bash
pip install memray
memray run script.py
```

### Optimización de memoria

A diferencia de las listas nativas de Python, que son dinámicas, los arrays de NumPy no
reservan espacio extra al asignarse. Esto significa que añadir elementos a un array de
NumPy requiere mover todo el array a una nueva ubicación de memoria, con una complejidad
$O(n)$. Por ello, conviene inicializar el array con el tamaño correcto desde el principio
utilizando funciones como `np.zeros`:

```python linenums="1"
import numpy as np

array_to_fill = np.zeros(1000)
```

Otro método eficaz para reducir el consumo de memoria consiste en utilizar valores de
precisión acordes al rango necesario. Tanto Pandas como NumPy procesan los datos en punto
flotante de 64 bits por defecto, pero en muchos casos es posible trabajar con 32, 16 o
incluso menos bits de información sin pérdida significativa de precisión.

## Buenas prácticas para código en producción

### Precisión decimal

Cuando se trabaja con valores monetarios o cálculos que requieren precisión decimal
exacta, es recomendable utilizar el módulo `Decimal` en lugar de `float`, ya que este
último puede introducir errores de redondeo inherentes a la representación en punto
flotante:

```python linenums="1"
from decimal import Decimal

RATES = {
    ("USD", "EUR"): Decimal("0.91")
}
```

### Rutas de archivos con `pathlib`

El módulo `pathlib` proporciona una interfaz orientada a objetos para trabajar con rutas
del sistema de archivos. Su uso resulta más limpio que la manipulación de cadenas de
texto y es multiplataforma, lo que garantiza la compatibilidad entre sistemas operativos:

```python linenums="1"
from pathlib import Path

ruta = Path("datos") / "archivo.csv"
```

### _Dataclasses_

En Python, cuando se necesita crear una clase cuya función principal es almacenar datos,
el código tiende a volverse repetitivo: es necesario escribir el método `__init__` para
asignar cada atributo, `__repr__` para obtener una representación legible del objeto y
`__eq__` para poder comparar instancias. El decorador `@dataclass`, disponible en el
módulo `dataclasses` desde Python 3.7, genera automáticamente todos estos métodos a
partir de las anotaciones de tipo de los atributos, lo que reduce significativamente el
código _boilerplate_.

#### Uso básico

Para definir una _dataclass_, basta con decorar la clase con `@dataclass` y declarar los
atributos con sus tipos:

```python linenums="1"
from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int = 0

p1 = Producto("Teclado", 49.99, 10)
p2 = Producto("Teclado", 49.99, 10)

print(p1)            # Producto(nombre='Teclado', precio=49.99, cantidad=10)
print(p1 == p2)      # True (compara por valor de los atributos)
print(p1.precio)     # 49.99
```

En este ejemplo, Python genera automáticamente el constructor, la representación en texto
y la comparación por igualdad. El atributo `cantidad` tiene un valor predeterminado de
`0`, por lo que es opcional al crear una instancia.

#### Parámetros del decorador

El decorador `@dataclass` acepta varios parámetros que modifican el comportamiento de la
clase:

```python linenums="1"
from dataclasses import dataclass

@dataclass(frozen=True, order=True, slots=True)
class User:
    name: str
    age: int

u1 = User("alice", 30)
u2 = User("bob", 25)

print(u1 < u2)   # True (compara por orden de los atributos: primero name, luego age)
# u1.name = "otro"  # Error: FrozenInstanceError, la instancia es inmutable
```

Cada parámetro cumple una función específica:

- `frozen=True`: Hace que las instancias sean inmutables. Cualquier intento de modificar
  un atributo después de la creación del objeto lanza un `FrozenInstanceError`. Esto
  resulta útil cuando se necesita garantizar la integridad de los datos o utilizar las
  instancias como claves de diccionarios o elementos de sets, ya que las hace
  _hashables_.
- `order=True`: Genera automáticamente los métodos de comparación (`__lt__`, `__le__`,
  `__gt__`, `__ge__`), permitiendo ordenar instancias. La comparación se realiza por el
  orden en que se declaran los atributos, de forma similar a como se comparan las tuplas.
- `slots=True` (disponible desde Python 3.10): Sustituye el diccionario interno
  `__dict__` por _slots_, lo que reduce el consumo de memoria por instancia y mejora
  ligeramente la velocidad de acceso a los atributos. Como contrapartida, no es posible
  crear atributos que no hayan sido declarados previamente en la clase.

#### Post-inicialización con `__post_init__`

El método `__post_init__` se ejecuta automáticamente después del `__init__` generado por
la _dataclass_. Resulta útil para realizar validaciones o transformaciones sobre los
atributos una vez asignados:

```python linenums="1"
from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str

    def __post_init__(self):
        # En una dataclass frozen, se usa object.__setattr__ para modificar atributos
        object.__setattr__(self, "name", self.name.strip().lower())

u = User("  Alice  ")
print(u.name)  # alice
```

Cuando la _dataclass_ es inmutable (`frozen=True`), no es posible reasignar atributos
directamente con `self.name = ...` dentro de `__post_init__`, ya que esto lanzaría un
error. En su lugar, se utiliza `object.__setattr__` para sortear la restricción de
inmutabilidad exclusivamente durante la fase de inicialización.

#### Valores predeterminados con `field`

Cuando un atributo necesita un valor predeterminado mutable (como una lista o un
diccionario), no se puede asignar directamente, ya que todas las instancias compartirían
la misma referencia. Para estos casos se utiliza la función `field` con
`default_factory`:

```python linenums="1"
from dataclasses import dataclass, field

@dataclass
class Inventario:
    nombre: str
    items: list[str] = field(default_factory=list)
    metadata: dict[str, str] = field(default_factory=dict, repr=False)

inv = Inventario("Almacén A")
inv.items.append("Tornillo")
print(inv)  # Inventario(nombre='Almacén A', items=['Tornillo'])
# metadata no aparece en repr porque se configuró repr=False
```

El parámetro `repr=False` en `field` permite excluir un atributo de la representación en
texto del objeto, lo cual resulta útil para atributos internos o de gran tamaño que no
aportan claridad al inspeccionar la instancia.

#### Herencia con _dataclasses_

Las _dataclasses_ soportan herencia de forma natural. La subclase hereda los atributos de
la clase padre y puede añadir los suyos propios. También es posible combinar
_dataclasses_ con clases abstractas del módulo `abc` para definir interfaces que las
subclases deben implementar:

```python linenums="1"
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Vehiculo(ABC):
    marca: str
    modelo: str

    @abstractmethod
    def tipo(self) -> str:
        ...

@dataclass
class Coche(Vehiculo):
    num_puertas: int = 4

    def tipo(self) -> str:
        return "Turismo"

c = Coche("Toyota", "Corolla")
print(c)         # Coche(marca='Toyota', modelo='Corolla', num_puertas=4)
print(c.tipo())  # Turismo
```

### Anotación de tipo `Self`

Cuando un método de una clase devuelve una instancia del mismo tipo, se puede utilizar la
anotación `Self` del módulo `typing` para indicarlo de forma clara:

```python linenums="1"
from typing import Self

class User:
    def metodo(self) -> Self:
        return User()
```

### Notas en excepciones

A partir de Python 3.11, es posible añadir notas adicionales a las excepciones capturadas
mediante el método `add_note`, lo que facilita la depuración al proporcionar contexto
extra sobre el error:

```python linenums="1"
try:
    ...
except Exception as e:
    e.add_note("Contexto adicional sobre el error")
    raise
```
