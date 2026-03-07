---
authors: Daniel Bazo Correa
description: Procesamiento de arrays en Python.
title: Arrays
---

## Bibliografía

- [NumPy](https://numpy.org)
- [Dask](https://docs.dask.org).

## Librería numérica de Python, NumPy

NumPy es una biblioteca de Python que añade soporte para grandes matrices y conjuntos
multidimensionales, junto con una amplia colección de funciones matemáticas de alto nivel
para operar sobre ellos. Constituye la base de gran parte del ecosistema científico de
Python y resulta imprescindible para cualquier tarea que implique cálculo numérico
eficiente.

### Creación de arrays con NumPy

Para comenzar a trabajar con NumPy es necesario importar la biblioteca. La convención
habitual es utilizar el alias `np`:

```python
import numpy as np
import math

a = np.array([1, 2, 3])
print(a)
```

El atributo `ndim` permite consultar el número de dimensiones del array. Si se pasa una
lista de listas a `np.array`, se crea una matriz (array bidimensional):

```python
b = np.array([[1, 2, 3], [4, 5, 6]])
```

Entre los atributos más útiles de un array se encuentran `shape`, que devuelve el orden
de la matriz; `dtype`, que indica el tipo de los elementos del array; y `dtype.name`, que
devuelve únicamente el nombre del tipo.

Cuando se mezclan números enteros y números con coma flotante, NumPy convierte
automáticamente los enteros en flotantes, ya que no existe pérdida de precisión. En
general, NumPy asigna el tipo de datos más adecuado para mantener la homogeneidad del
array.

En ocasiones resulta necesario crear una matriz sin conocer de antemano los valores que
contendrá. NumPy ofrece funciones para este propósito, permitiendo rellenar matrices con
ceros, unos o cualquier valor arbitrario:

```python
d = np.zeros((2, 3))
print(d)

e = np.ones((2, 3))
print(e)

a = np.arange(1, 2, 0.1).reshape(5, 2)
print(a)

np.full(imagen_array.shape, 255)
```

La función `np.random.rand(i, j)` genera un array con números aleatorios de orden
$i \times j$. Si no se especifica `j`, se crea un array unidimensional. Otras funciones
de creación habituales son `np.arange(a, b, x)`, que genera una secuencia de números
desde `a` hasta `b` (sin incluir) con un tamaño de paso `x`, y `np.linspace(a, b, x)`,
que genera `x` números equiespaciados desde `a` hasta `b`, ambos inclusive:

```python
a1 = np.random.rand(4)
a2 = np.random.rand(4, 1)
a3 = np.array([[1, 2, 3, 4]])
a4 = np.arange(1, 4, 1)
a5 = np.linspace(1, 4, 4)

a1.shape == a2.shape  # Devuelve False
a5.shape == a1.shape  # Devuelve True
```

### Operaciones con arrays

NumPy permite realizar operaciones aritméticas elemento a elemento entre arrays de forma
directa. Partiendo de dos arrays:

```python
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])
```

La resta y la multiplicación elemento a elemento se realizan con los operadores
habituales:

```python
c = a - b
print(c)

d = a * b
print(d)
```

Como ejemplo práctico, supongamos que se dispone de un array con temperaturas en
Fahrenheit y se desea convertirlas a Celsius mediante la fórmula
$C = (F - 32) \times \frac{5}{9}$:

```python
fahrenheit = np.array([0, -10, -5, -15, 0])
celsius = (fahrenheit - 32) * (5 / 9)
print(celsius)
```

Un concepto muy útil es el **array booleano**: al aplicar un operador de comparación
sobre un array, NumPy itera sobre cada elemento y devuelve `True` o `False` según se
cumpla la condición. Por ejemplo, para comprobar qué temperaturas en Celsius son mayores
a -20:

```python
celsius > -20
# Devuelve: array([ True, False, False, False, True])
```

NumPy también admite la manipulación de matrices. Partiendo de dos matrices:

```python
A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
```

El operador `*` realiza la multiplicación elemento a elemento, mientras que el operador
`@` calcula el producto matricial (producto punto):

```python
print(A * B)  # Producto elemento a elemento
print(A @ B)  # Producto matricial
```

Al operar con matrices de diferentes tipos (por ejemplo, una de enteros y otra de
flotantes), el tipo de la matriz resultante corresponde al más general de los dos. Este
comportamiento se denomina **upcasting**.

Los arrays de NumPy disponen de métodos muy útiles para el análisis de datos: `sum()`
devuelve la suma de todos los elementos, `max()` el valor máximo, `min()` el valor mínimo
y `mean()` la media aritmética.

Es habitual pensar en un array multidimensional como una matriz con filas y columnas,
pero también se puede concebir como una lista ordenada de números donde el número de
filas y columnas es una abstracción para un propósito particular. Este es precisamente el
modo en que se almacenan las imágenes digitales. El siguiente ejemplo muestra cómo
trabajar con imágenes utilizando NumPy y la librería PIL:

```python
from PIL import Image
from IPython.display import display

imagen = Image.open('nombre_imagen.extension')
display(imagen)
```

Para convertir una imagen en un array de NumPy:

```python
imagen_array = np.array(imagen)
print(f"Tamaño del array de la imagen: {imagen_array.shape}")
imagen_array
```

Al imprimir el array, al final aparece el atributo `dtype`. En el caso de una imagen en
blanco y negro, el tipo suele ser `uint8`, que indica enteros sin signo de 8 bits. Cada
valor puede oscilar entre 0 y 255 ($2^8 = 256$ valores posibles, comenzando desde 0). En
imágenes en blanco y negro, el valor 0 representa el negro y el 255 el blanco.

Una vez obtenido el array de la imagen, se puede realizar cualquier operación sobre él
(como invertir los colores) y posteriormente renderizar el resultado utilizando la
función `fromarray()` de PIL:

```python
display(Image.fromarray(array_imagen))
```

### Indexación, corte e iteración

Estas operaciones resultan fundamentales para la manipulación y el análisis de datos, ya
que permiten seleccionar datos en función de condiciones específicas, así como copiar o
actualizar valores.

#### Indexación

Un array unidimensional funciona de manera similar a una lista de Python, por lo que se
accede a sus elementos mediante índices:

```python
a = np.array([1, 2, 3])
print(a[2])  # Muestra 3 (el índice inicial es 0)
```

Para un array multidimensional (matriz), se especifica el índice de la fila y de la
columna:

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
a[1][1]  # Devuelve 5
```

También es posible crear un array unidimensional que almacene varios elementos
seleccionados de un array multidimensional:

```python
valores = np.array([a[0, 1], a[0, 2], a[1, 1]])
```

#### Indexación booleana

La indexación booleana permite seleccionar elementos de forma arbitraria en función de
condiciones:

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
valores = np.array([a[0, 1], a[0, 2], a[1, 1]])
print(valores >= 3)
# Devuelve: [False  True  True]
```

#### Corte (_slicing_)

El corte permite crear una submatriz basada en la matriz original, de forma similar a
como se trabaja con listas:

```python
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a[:3])  # Elementos desde el inicio hasta el índice 3 (sin incluir)
```

También se pueden seleccionar rangos específicos:

```python
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = a[2:4]
print(b)  # Devuelve [3 4]
```

Para las matrices, el primer índice selecciona las filas y el segundo las columnas. Si
solo se proporciona un parámetro, se devuelve la fila completa:

```python
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)

a[:2]        # Filas hasta la segunda (sin incluir)
a[:2, 1:3]   # Filas hasta la segunda, columnas de la 1 a la 3 (sin incluir)
```

Es importante tener en cuenta que un segmento de una matriz es una **vista** sobre los
mismos datos (paso por referencia). Esto significa que la modificación de la submatriz
modificará en consecuencia la matriz original.

### Uso de NumPy con conjuntos de datos

Para cargar un conjunto de datos en NumPy se puede utilizar la función `genfromtxt()`,
especificando el nombre del archivo, el delimitador (el carácter que separa las columnas,
por ejemplo `;`) y el número de filas de encabezado a omitir. El parámetro `dtype`
permite especificar los tipos de datos para cada columna.

Supongamos un archivo CSV llamado `winequality-red.csv` con información sobre vinos:

```python
vinos = np.genfromtxt(
    "datasets/winequality-red.csv",
    delimiter=";",
    skip_header=1
)
vinos
```

Para seleccionar varias columnas no consecutivas, se pasan los índices deseados como una
lista:

```python
vinos[:, [0, 2, 4]]
```

Como ejemplo de análisis, para calcular la calidad media del vino tinto (última columna
del conjunto de datos):

```python
vinos[:, -1].mean()
```

Otro ejemplo práctico consiste en analizar datos de admisión universitaria. La función
`genfromtxt()` permite especificar nombres de campos al cargar los datos:

```python
admision_graduados = np.genfromtxt(
    'datasets/Admission_Predict.csv',
    dtype=None,
    delimiter=',',
    skip_header=1,
    names=(
        'Serial No', 'GRE Score', 'TOEFL Score',
        'University Rating', 'SOP',
        'LOR', 'CGPA', 'Research', 'Chance of Admit'
    )
)
admision_graduados
```

El resultado es un array unidimensional de 400 tuplas. Para recuperar una columna
específica:

```python
admision_graduados['GRE_Score'][:5]
```

Mediante indexación booleana se puede, por ejemplo, averiguar cuántos estudiantes tienen
experiencia en investigación (valor 1 en la columna `Research`):

```python
len(admision_graduados[admision_graduados['Research'] == 1])
```

## Operaciones de array con Dask

Cuando las estrategias de optimización con NumPy resultan insuficientes, la biblioteca
Dask ofrece una alternativa muy interesante. Dask permite realizar operaciones de array
en paralelo, lo que acelera la computación y posibilita el trabajo con datos que no caben
en la memoria del sistema. Su interfaz es muy similar a la de NumPy, aunque añade cierta
complejidad adicional, por lo que su uso se justifica cuando se necesita un aumento
significativo de rendimiento.

Dask funciona dividiendo un array en fragmentos (_chunks_), ejecutando los cálculos sobre
uno o varios fragmentos simultáneamente y combinando los resultados. Por ejemplo, para
encontrar el valor máximo de un array muy grande, Dask divide el array en fragmentos,
calcula el máximo de cada uno y luego obtiene el máximo global. No todas las operaciones
pueden paralelizarse de esta manera, pero cuando es posible, la mejora de rendimiento
puede ser muy notable. Además, dado que no todos los fragmentos se cargan en memoria a la
vez, Dask permite trabajar con conjuntos de datos que superan la capacidad de la memoria
RAM.

La instalación se realiza con el siguiente comando:

```bash
pip install "dask[complete]"
```

A continuación se muestra un ejemplo comparativo entre NumPy y Dask para encontrar el
valor máximo de un array de mil millones de enteros:

```python
import numpy as np

large_np_array = np.random.randint(1, 100000, 1000000000)

%%timeit -r1 -n7
np.max(large_np_array)
# 30.7s ± 0ns per loop (mean ± std. dev. of 1 run, 7 loops each)
```

El mismo cálculo con Dask:

```python
import dask.array as da

large_dask_array = da.random.randint(1, 100_000, 1_000_000_000)

%%timeit -r1 -n7
array_max = large_dask_array.max()
array_max.compute()
# 1.51s ± 0ns per loop (mean ± std. dev. of 1 run, 7 loops each)
```

También es posible crear un array de Dask a partir de un array de NumPy existente:

```python
large_dask_array = da.from_array(large_np_array)
```

La diferencia principal respecto a NumPy es que en Dask las operaciones se inicializan
primero (evaluación perezosa) y se ejecutan explícitamente con el método `.compute()`. En
este ejemplo, encontrar el máximo con Dask resulta aproximadamente 20 veces más rápido
que con NumPy.

Para distribuir los cálculos entre varios núcleos o máquinas, Dask proporciona el módulo
`dask.distributed`. Basta con crear un objeto `Client` especificando el número de
trabajadores:

```python
from dask.distributed import Client

client = Client(n_workers=4)
client
```

Una vez creado el cliente, los arrays de Dask se utilizan de la misma forma que antes, y
los cálculos se distribuyen automáticamente entre los trabajadores especificados. Para
más información, se puede consultar la
[documentación oficial de Dask](https://docs.dask.org).
