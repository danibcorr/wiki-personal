---
authors: Daniel Bazo Correa
description: Aceleración de aplicaciones Python con Numba y CuPy en GPU.
title: CUDA en Python
---

El rendimiento de las aplicaciones científicas y de ingeniería en Python se puede
mejorar significativamente mediante el uso de herramientas como Numba y CuPy. Estas
tecnologías permiten la paralelización y aceleración del código, aprovechando la
potencia de procesamiento de las GPUs y superando las limitaciones del intérprete de
Python.

## Bibliografía

- CuPy. (s.f.). _CuPy: NumPy & SciPy for GPU_. <https://cupy.dev/>
- Numba. (s.f.). _Numba: A High Performance Python Compiler_.
  <https://numba.pydata.org/>

## Numba

### Fundamentos

Numba es un compilador JIT (_Just-In-Time_) utilizado para acelerar cálculo numérico en
Python tanto en CPU como en GPU. A diferencia de otros enfoques, Numba compila funciones
individuales de Python, no la aplicación al completo, por lo que no sustituye al
intérprete de Python.

La aceleración se consigue generando implementaciones específicas para el tipo de dato
que se utiliza, en lugar de emplear el _dynamic typing_ que es el comportamiento por
defecto de Python. Al ser _just-in-time_, la compilación se produce cuando la función se
invoca por primera vez, lo que permite al compilador conocer los argumentos que se van a
utilizar. Numba se centra principalmente en tipos de datos numéricos (enteros,
flotantes, números complejos) y ofrece el mejor soporte cuando se trabaja con _arrays_
de NumPy.

No obstante, Numba presenta ciertas limitaciones, entre las que destaca la falta de
compatibilidad con Pandas. Para más información, se puede consultar la
[página oficial de Numba](https://numba.pydata.org/).

### Funcionamiento interno

Cuando se invoca una función decorada con `@jit` o `@njit`, el compilador de Numba
convierte el código Python a código máquina para el tipo específico de los datos que se
están utilizando. Numba también conserva la función original de Python en el atributo
`.py_func`, lo que permite llamar a la función con dicho atributo para comparar
resultados:

```python linenums="1"
import math

from numba import jit

@jit
def hypot(x: float, y: float) -> float:
    """
    Calcula la hipotenusa de un triángulo rectángulo evitando
    desbordamientos.

    Args:
        x: Longitud del primer cateto.
        y: Longitud del segundo cateto.

    Returns:
        La longitud de la hipotenusa.
    """

    x = abs(x)
    y = abs(y)
    t = min(x, y)
    x = max(x, y)
    t = t / x

    return x * math.sqrt(1 + t * t)

# Ejecución de la versión compilada con Numba
hypot(3.0, 4.0)

# Ejecución de la función original de Python
hypot.py_func(3.0, 4.0)
```

No obstante, si existen versiones ya implementadas y optimizadas en Python para una
operación concreta, estas suelen ser más rápidas que Numba, ya que Numba introduce una
pequeña sobrecarga en la compilación inicial.

El proceso interno de compilación se puede visualizar de la siguiente manera:

<figure markdown="span">
  ![Proceso de compilación de Numba](../../assets/img/docs/cuda/cuda-python-numba-compilation.png)
  <figcaption>Proceso interno de compilación de una función con Numba.</figcaption>
</figure>

Para inspeccionar el resultado de la inferencia de tipos, se puede utilizar el método
`.inspect_types()`, que imprime el código fuente anotado con los tipos inferidos:

```python linenums="1"
hypot.inspect_types()
```

### Decoradores

Numba ofrece varios decoradores para la compilación y optimización de funciones:

| Decorador                       | Definición                                                                                                                                                                            |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `@jit`                          | Compila en modo objeto. Numba compila los bucles optimizables a código máquina y el resto de la función se ejecuta con el intérprete de Python.                                       |
| `@njit` = `@jit(nopython=True)` | Compila sin el intérprete de Python, obteniendo el mejor rendimiento. Puede fallar si los parámetros no son compatibles. Este es el decorador preferido para la mayoría de los casos. |
| `@njit(parallel=True)`          | Compila el código para ejecutarse en múltiples hilos, aprovechando la paralelización cuando las operaciones lo permiten.                                                              |
| `@njit(fastmath=True)`          | Habilita cálculos matemáticos rápidos a costa de reducir la precisión numérica, acelerando aún más el rendimiento.                                                                    |

Los decoradores pueden combinarse para optimizar el rendimiento. Por ejemplo,
`@njit(parallel=True, fastmath=True)` evita el intérprete de Python, paraleliza el
código y permite una menor precisión numérica para maximizar la velocidad de ejecución.

El decorador `@njit` es la versión recomendada y más eficiente, ya que fuerza a mostrar
los errores de las estructuras o funciones que no son directamente compatibles con Numba
y que no se pueden compilar, evitando el _object mode_ (donde se utiliza el tipo de
variable original de Python sin especializar el tipo en Numba).

???+ example "Compilación JIT con @njit"

    ```python linenums="1"
    import numpy as np
    from numba import njit

    @njit
    def bucle(lista1: np.ndarray, lista2: np.ndarray, num_filas: int) -> list[float]:
        """
        Calcula la media de los pares de valores que cumplen un rango
        determinado.

        Args:
            lista1: Primer vector de valores.
            lista2: Segundo vector de valores.
            num_filas: Número de posiciones que se desean recorrer.

        Returns:
            Las medias de los pares que satisfacen las condiciones
                establecidas.
        """

        lista3 = []

        for fila in range(num_filas):
            if (lista1[fila] >= 1) and (lista2[fila] <= 5):
                lista3.append(np.mean([lista1[fila], lista2[fila]]))

        return lista3

    lista1: np.ndarray = np.array([1, 2, 3])
    lista2: np.ndarray = np.array([4, 5, 6])
    resultado: list[float] = bucle(lista1, lista2, len(lista1))
    print(resultado)
    ```

### Vectorización para GPU

El _hardware_ de la GPU está diseñado para la paralelización de datos, por lo que se
obtiene el máximo _throughput_ cuando la GPU calcula la misma operación para diferentes
elementos al mismo tiempo. Las funciones universales de NumPy (_ufuncs_) realizan la
misma operación en cada elemento de un _array_, lo que las hace naturalmente
paralelizables y las ajusta muy bien a la naturaleza de la GPU.

???+ example "Para CPU"

    ```python linenums="1"
    import numpy as np
    from numba import vectorize

    @vectorize
    def add_ten(num: int) -> int:
        """
        Suma diez al elemento recibido.

        Args:
            num: Valor sobre el que se aplica la operación.

        Returns:
            El valor incrementado en diez unidades.
        """

        return num + 10

    nums: np.ndarray = np.arange(10)
    resultado: np.ndarray = add_ten(nums)
    print(resultado)
    ```

???+ example "Para GPU"

    ```python linenums="1"
    import numpy as np
    from numba import vectorize

    @vectorize(["int64(int64, int64)"], target="cuda")
    def add_ufunc(x: int, y: int) -> int:
        """
        Suma elemento a elemento los dos valores recibidos.

        Args:
            x: Primer operando.
            y: Segundo operando.

        Returns:
            La suma de ambos operandos.
        """

        return x + y

    a: np.ndarray = np.array([1, 2, 3, 4, 5])
    b: np.ndarray = np.array([10, 20, 30, 40, 50])
    resultado: np.ndarray = add_ufunc(a, b)
    print(resultado)
    ```

En el caso de la GPU se especifica el _target_ como `"cuda"`, junto con la firma de
tipos de la función, donde los tipos indicados entre paréntesis corresponden a los
argumentos y el que aparece fuera de ellos al valor de retorno.

Internamente, Numba compila un _kernel_ CUDA para ejecutar la operación _ufunc_ en
paralelo sobre todos los elementos de entrada, reserva memoria en la GPU para las
entradas y la salida, copia los datos de entrada a la GPU, ejecuta el _kernel_ CUDA con
las dimensiones adecuadas según el tamaño de las entradas, copia el resultado de vuelta
a la CPU y lo devuelve como un _array_ de NumPy en el _host_.

Para obtener un rendimiento óptimo en la GPU conviene tener presentes varias
consideraciones:

- **Tamaño de las entradas**: Los _arrays_ deben ser suficientemente grandes, del orden
  de miles de elementos como mínimo, para que el paralelismo compense la sobrecarga de
  la transferencia.
- **Intensidad aritmética**: El cálculo debe realizar suficiente trabajo por elemento
  para justificar el envío de los datos a la GPU.
- **Encadenamiento de operaciones**: Ejecutar varias operaciones consecutivas en la GPU
  permite amortizar el coste de la copia de datos.
- **Tipos de datos**: Conviene emplear los tipos más pequeños que resulten suficientes.
  NumPy utiliza 64 bits por defecto, por lo que el parámetro `dtype` o el método
  `ndarray.astype()` permiten reducir la precisión a 32 bits cuando resulta apropiado.

### Funciones de dispositivo

Para funciones que no son estrictamente elemento a elemento, se utiliza `@cuda.jit`. El
parámetro `device=True` indica que la función solo puede ser invocada desde otra función
que se ejecuta en la GPU:

```python linenums="1"
import math

from numba import cuda, vectorize

@cuda.jit(device=True)
def polar_to_cartesian(rho: float, theta: float) -> tuple[float, float]:
    """
    Convierte unas coordenadas polares en coordenadas cartesianas.

    Args:
        rho: Radio de la coordenada polar.
        theta: Ángulo de la coordenada polar en radianes.

    Returns:
        Las componentes x e y de la coordenada cartesiana equivalente.
    """

    x = rho * math.cos(theta)
    y = rho * math.sin(theta)

    return x, y

@vectorize(["float32(float32, float32, float32, float32)"], target="cuda")
def polar_distance(
    rho1: float, theta1: float, rho2: float, theta2: float
) -> float:
    """
    Calcula la distancia euclídea entre dos puntos expresados en
    coordenadas polares.

    Args:
        rho1: Radio del primer punto.
        theta1: Ángulo del primer punto en radianes.
        rho2: Radio del segundo punto.
        theta2: Ángulo del segundo punto en radianes.

    Returns:
        La distancia euclídea entre ambos puntos.
    """

    x1, y1 = polar_to_cartesian(rho1, theta1)
    x2, y2 = polar_to_cartesian(rho2, theta2)

    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
```

## _Kernels_ personalizados

La jerarquía de ejecución en CUDA se organiza de la siguiente manera: las hebras se
agrupan en bloques de hebras, y los bloques de hebras conforman una malla (_grid_). Para
escribir _kernels_ personalizados se utiliza el decorador `@cuda.jit`, que a diferencia
de `@vectorize` no devuelve valores, sino que utiliza un argumento de salida:

```python linenums="1"
import numpy as np
from numba import cuda

@cuda.jit
def add_kernel(x: np.ndarray, y: np.ndarray, out: np.ndarray) -> None:
    """
    Suma elemento a elemento dos vectores y escribe el resultado en el
    vector de salida.

    Args:
        x: Primer vector de entrada.
        y: Segundo vector de entrada.
        out: Vector de salida donde se almacena el resultado.
    """

    idx = cuda.grid(1)
    out[idx] = x[idx] + y[idx]

n: int = 4096
x: np.ndarray = np.arange(n).astype(np.int32)
y: np.ndarray = np.ones_like(x)

# Copia de los datos al dispositivo y reserva del vector de salida
d_x = cuda.to_device(x)
d_y = cuda.to_device(y)
d_out = cuda.device_array_like(d_x)

hilos_por_bloque: int = 128
bloques_por_malla: int = 32

add_kernel[bloques_por_malla, hilos_por_bloque](d_x, d_y, d_out)
cuda.synchronize()
print(d_out.copy_to_host())
```

A la hora de elegir el tamaño óptimo de la malla, el tamaño de un bloque debe ser
múltiplo de 32 hilos (el tamaño de un _warp_), con tamaños típicos entre 128 y 512. El
tamaño de la malla debe asegurar la utilización completa de la GPU, siendo un buen punto
de partida lanzar entre 2x y 4x el número de SMs.

### _Grid stride loop_

El patrón _grid stride loop_ permite trabajar con conjuntos de datos más grandes que el
número total de hilos, al tiempo que se beneficia de la **coalescencia de memoria
global**:

```python linenums="1"
import numpy as np
from numba import cuda

@cuda.jit
def add_kernel(x: np.ndarray, y: np.ndarray, out: np.ndarray) -> None:
    """
    Suma dos vectores recorriendo los datos con el patrón grid stride
    loop.

    Args:
        x: Primer vector de entrada.
        y: Segundo vector de entrada.
        out: Vector de salida donde se almacena el resultado.
    """

    start = cuda.grid(1)
    stride = cuda.gridsize(1)

    for i in range(start, x.shape[0], stride):
        out[i] = x[i] + y[i]
```

## Operaciones atómicas y condiciones de carrera

Una **condición de carrera** ocurre cuando múltiples hilos acceden a la misma ubicación
de memoria sin sincronización. Para evitarlas, cada hilo debe escribir en una ubicación
única, no usar el mismo _array_ como entrada y salida, y utilizar operaciones atómicas
cuando sea necesario.

???+ example "Con operación atómica"

    ```python linenums="1"
    import numpy as np
    from numba import cuda

    @cuda.jit
    def contador_global_atomic(counter: np.ndarray) -> None:
        """
        Incrementa de forma atómica un contador compartido por todos
        los hilos.

        Args:
            counter: Vector de un único elemento que almacena el
                contador global.
        """

        cuda.atomic.add(counter, 0, 1)

    contador: np.ndarray = np.zeros(1, dtype=np.int32)
    d_contador = cuda.to_device(contador)

    # Se lanzan 4 bloques de 128 hilos, por lo que el valor esperado es 512
    contador_global_atomic[4, 128](d_contador)

    resultado: np.ndarray = d_contador.copy_to_host()
    print(f"Valor final del contador: {resultado[0]}")
    ```

## Coalescencia de memoria

La coalescencia de memoria es un factor determinante en el rendimiento. Los bloques de
hebras se dividen en _warps_ de 32 hebras, y el subsistema de memoria intenta minimizar
el número de líneas de caché requeridas. Cuanto más contiguos sean los datos asignados a
cada hebra del _warp_, mayor es la eficiencia.

<figure markdown="span">
  ![Acceso coalescente a memoria global](../../assets/img/docs/cuda/cuda-python-numba-coalescing-1.png)
  <figcaption>Patrón de acceso coalescente a memoria global (I).</figcaption>
</figure>

<figure markdown="span">
  ![Acceso coalescente a memoria global](../../assets/img/docs/cuda/cuda-python-numba-coalescing-2.png)
  <figcaption>Patrón de acceso coalescente a memoria global (II).</figcaption>
</figure>

<figure markdown="span">
  ![Acceso coalescente a memoria global](../../assets/img/docs/cuda/cuda-python-numba-coalescing-3.png)
  <figcaption>Patrón de acceso coalescente a memoria global (III).</figcaption>
</figure>

### Trabajo con matrices en 2D

CUDA permite trabajar con mallas bidimensionales de hilos usando `cuda.grid(2)`:

```python linenums="1"
import numpy as np
from numba import cuda

@cuda.jit
def get_2d_indices(matriz: np.ndarray) -> None:
    """
    Escribe en cada posición de la matriz un valor derivado de sus
    índices 2D.

    Args:
        matriz: Matriz de salida sobre la que escribe cada hilo.
    """

    x, y = cuda.grid(2)
    matriz[x][y] = x + y / 10

matriz: np.ndarray = np.zeros((4, 4))
d_matriz = cuda.to_device(matriz)
get_2d_indices[(2, 2), (2, 2)](d_matriz)
resultado: np.ndarray = d_matriz.copy_to_host()
print(resultado)
```

## Memoria compartida

La **memoria compartida** reside en un área _on-chip_ del dispositivo. Su tamaño es
limitado pero ofrece un ancho de banda significativamente mayor que la memoria global.
Es compartida entre todos los hilos de un mismo bloque y no persiste una vez que el
_kernel_ termina.

Los casos de uso habituales incluyen almacenar en caché datos que se leen múltiples
veces, acumular resultados para realizar una escritura coalescente y preparar datos para
operaciones de dispersión o recopilación.

En Numba, la memoria compartida se reserva mediante `cuda.shared.array` y la
sincronización entre los hilos de un bloque se realiza con `cuda.syncthreads()`:

???+ example "Intercambio de elementos"

    ```python linenums="1"
    import numpy as np
    from numba import cuda, types

    @cuda.jit
    def swap_with_shared(vector: np.ndarray, swapped: np.ndarray) -> None:
        """
        Invierte el orden de un vector de cuatro elementos usando
        memoria compartida.

        Args:
            vector: Vector de entrada con los valores originales.
            swapped: Vector de salida donde se escriben los valores
                invertidos.
        """

        temp = cuda.shared.array(4, dtype=types.int32)
        idx = cuda.grid(1)

        temp[idx] = vector[idx]

        # Se espera a que todos los hilos del bloque hayan escrito en memoria compartida
        cuda.syncthreads()

        swapped[idx] = temp[3 - cuda.threadIdx.x]

    vector: np.ndarray = np.arange(4).astype(np.int32)
    swapped: np.ndarray = np.zeros_like(vector)
    d_vector = cuda.to_device(vector)
    d_swapped = cuda.to_device(swapped)
    swap_with_shared[1, 4](d_vector, d_swapped)
    print(d_swapped.copy_to_host())
    ```

???+ example "Transposición con _tiling_"

    ```python linenums="1"
    import numpy as np
    from numba import cuda
    from numba import types as numba_types

    @cuda.jit
    def tile_transpose(a: np.ndarray, transposed: np.ndarray) -> None:
        """
        Transpone una matriz por bloques apoyándose en memoria
        compartida.

        Args:
            a: Matriz de entrada que se desea transponer.
            transposed: Matriz de salida donde se escribe el
                resultado.
        """

        tile = cuda.shared.array((32, 32), numba_types.float32)

        a_col = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x
        a_row = cuda.blockIdx.y * cuda.blockDim.y + cuda.threadIdx.y

        # Carga coalescente del bloque de datos en memoria compartida
        tile[cuda.threadIdx.y, cuda.threadIdx.x] = a[a_row, a_col]
        cuda.syncthreads()

        t_col = cuda.blockIdx.y * cuda.blockDim.y + cuda.threadIdx.x
        t_row = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.y

        # Escritura coalescente leyendo el bloque transpuesto desde memoria compartida
        transposed[t_row, t_col] = tile[cuda.threadIdx.x, cuda.threadIdx.y]
    ```

## CuPy

CuPy es una biblioteca de Python diseñada para acelerar cálculos numéricos mediante la
ejecución de código en GPUs. Ofrece una API similar a NumPy, lo que permite realizar
operaciones aprovechando la arquitectura de CUDA. Para más información, se puede
consultar la [página oficial de CuPy](https://cupy.dev/).

```python linenums="1"
import cupy as cp
import numpy as np

a: cp.ndarray = cp.array([1, 2, 3, 4, 5])
b: cp.ndarray = cp.array([6, 7, 8, 9, 10])

# La suma se calcula en la GPU y el resultado se transfiere después a la CPU
c: cp.ndarray = a + b
c_numpy: np.ndarray = cp.asnumpy(c)

# Imprime: [ 7  9 11 13 15]
print(c_numpy)
```

En comparación con Numba, CuPy es más adecuado para trabajar con matrices y realizar
operaciones a gran escala en GPUs, ya que ofrece una API similar a NumPy que facilita la
migración de código. Numba, por su parte, resulta ideal para acelerar funciones
específicas y bucles mediante compilación JIT, tanto en CPU como en GPU, y se integra
bien con código existente de NumPy.
