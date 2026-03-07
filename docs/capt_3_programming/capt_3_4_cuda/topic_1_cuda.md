---
authors: Daniel Bazo Correa
description: Conoce la plataforma de CUDA de NVIDIA para sus GPUs.
title: CUDA
---

## Bibliografía

- [NVIDIA](https://www.nvidia.com/)
- [DLI (Deep Learning Institute) - UMA](http://nvidiadli.uma.es/index.php/es/certificaciones-nvidia)
- [CuPy: NumPy & SciPy for GPU](https://cupy.dev/)
- [Numba: A High Performance Python Compiler](https://numba.pydata.org/)

## Introducción

<p align="center">
  <img src="../../../assets/img/docs/logos/cuda-logo.png" height="200"/>
  <br />
  <em>Logo de Nvidia CUDA</em>
</p>

**CUDA** (_Compute Unified Device Architecture_) es una plataforma de computación
paralela y una interfaz de programación de aplicaciones (API) desarrollada por NVIDIA.
Permite el uso de unidades de procesamiento gráfico (GPU) para realizar cálculos
complejos con mayor eficiencia en comparación con las unidades de procesamiento central
(CPU). Su aplicación abarca áreas como la inteligencia artificial, las simulaciones
científicas y la renderización de gráficos, donde la capacidad de procesamiento masivo en
paralelo resulta determinante.

## Conceptos fundamentales de CUDA

La plataforma de computación CUDA ofrece un amplio ecosistema de herramientas y
bibliotecas. En las primeras secciones se aborda el uso de CUDA en combinación con el
lenguaje de programación C, mientras que en secciones posteriores se exploran otras
bibliotecas y aplicaciones de CUDA en Python.

<p align="center">
  <img src="../../../assets/img/docs/B0FF9827-9E32-46F2-8365-FA0E686C649D.png"/>
  <br />
</p>

CUDA se sustenta en tres cualidades fundamentales que destacan la capacidad de la GPU
para el procesamiento paralelo:

- **Simplicidad**: La GPU organiza los hilos en grupos de 32, conocidos como _warps_.
  Todos los hilos de un _warp_ ejecutan la misma instrucción simultáneamente, lo que
  simplifica la gestión del paralelismo.
- **Escalabilidad**: La plataforma permite la creación de modelos de paralelización
  sostenible gracias a la abundancia de datos, especialmente en aplicaciones a gran
  escala. Utiliza el modelo _Single Instruction Multiple Threads_ (SIMT) para manejar
  grandes volúmenes de datos de manera eficiente.
- **Productividad**: CUDA permite que los hilos que enfrentan latencias oculten este
  tiempo mediante la conmutación con otros hilos, manteniendo una alta eficiencia en el
  procesamiento.

### Los _warps_ en CUDA

El concepto clave en CUDA es el **_warp_**. En el nivel de hardware, un bloque de hilos
se divide en _warps_, que son grupos de 32 hilos que ejecutan instrucciones en paralelo.
Estos _warps_ permanecen en el multiprocesador hasta completar su ejecución. Un nuevo
bloque de hilos no se lanza hasta que se liberan suficientes registros y memoria
compartida para los _warps_ del nuevo bloque. La conmutación inmediata entre los hilos
dentro de un _warp_ contribuye a una ejecución eficiente.

CUDA combina software, firmware y hardware para ofrecer una plataforma de computación
paralela robusta:

- **Software**: Proporciona extensiones SIMD que permiten la programación eficiente de la
  GPU, facilitando la ejecución paralela y escalable.
- **Firmware**: Incluye drivers para la programación GPU, que soportan tareas como
  renderizado, manejo de APIs y gestión de memoria.
- **Hardware**: Habilita el paralelismo general de la GPU, optimizando la capacidad de
  procesamiento paralelo.

### Computación heterogénea

Aunque CUDA ofrece ventajas significativas, resulta crucial equilibrar la carga de
trabajo entre la GPU y la CPU, un enfoque conocido como computación heterogénea. La GPU
se orienta al procesamiento intensivo en datos y paralelismo fino, mientras que la CPU
resulta más adecuada para operaciones con saltos y bifurcaciones, así como para
paralelismo grueso. Identificar qué partes del código se benefician de la paralelización
en la GPU y cuáles deben procesarse secuencialmente en la CPU es fundamental para obtener
el máximo rendimiento.

<p align="center">
  <img src="../../../assets/img/docs/EEA7EE5C-1D79-4B88-8DF7-37E17BF0D2FF.jpeg"/>
  <br />
</p>

Se observa, por tanto, que el paralelismo en el que CUDA destaca es el **paralelismo de
datos** (_data parallelism_).

### Hardware

Una GPU se compone de $N$ multiprocesadores, cada uno de los cuales contiene $M$ núcleos.
La siguiente imagen muestra algunas de las familias de GPU de la serie Tesla de NVIDIA.

<p align="center">
  <img src="../../../assets/img/docs/Untitled (1).png"/>
  <br />
</p>

Cada multiprocesador dispone de su propio banco de registros, memoria compartida, una
caché de constantes y una caché de texturas (ambas de solo lectura). Además, la GPU
cuenta con una memoria global de tipo GDDR, que es aproximadamente tres veces más rápida
que la memoria principal de la CPU, aunque considerablemente más lenta que la memoria
compartida de tipo SRAM. Los bloques de hilos en CUDA pueden asignarse a cualquier
multiprocesador para su ejecución. La siguiente imagen ilustra la estructura interna de
una GPU.

<p align="center">
  <img src="../../../assets/img/docs/Untitled 1 (1).png"/>
  <br />
</p>

A modo de ejemplo, la generación Volta, concretamente la GPU GV100, cuenta con 84
multiprocesadores (SMs) y 8 controladores de memoria de 512 bits. En la arquitectura
Volta, cada multiprocesador dispone de 64 núcleos para operaciones de tipo int32, 64
núcleos para float32, 32 núcleos para float64 y 8 unidades tensoriales.

<p align="center">
  <img src="../../../assets/img/docs/Untitled 2.png"/>
  <br />
</p>

De la imagen anterior se observa que el diseño de un bloque se utiliza como base para
crear diseños más complejos al replicarlo.

<p align="center">
  <img src="../../../assets/img/docs/Untitled 3.png"/>
  <br />
</p>

### Núcleos tensoriales

En la última década, los núcleos tensoriales han adquirido un protagonismo notable. Estos
componentes están diseñados para realizar operaciones matriciales a alta velocidad, lo
que resulta crucial en el entrenamiento de modelos de inteligencia artificial y en
procesos que implican operaciones matriciales extensivas. El siguiente diagrama ilustra
el proceso de operación de cada núcleo tensorial por ciclo de reloj.

<p align="center">
  <img src="../../../assets/img/docs/Untitled 4 (2).png"/>
  <br />
</p>

### Precisión numérica

La precisión de los datos influye directamente en la tasa de transferencia (_throughput_)
del sistema. Reducir la precisión, por ejemplo de enteros de 32 bits a enteros de 16
bits, permite realizar un mayor número de operaciones por unidad de tiempo, aunque con
una precisión menor en los resultados. Dependiendo de la aplicación, esta reducción de
precisión puede ser perfectamente aceptable. La siguiente imagen muestra el _throughput_
para diferentes precisiones de datos en arquitecturas de GPU modernas.

<p align="center">
  <img src="../../../assets/img/docs/Untitled 5 (2).png"/>
  <br />
</p>

## Programación con CUDA en C

### Conceptos básicos

En CUDA, una función paralelizada se denomina **kernel**. Para conocer la GPU disponible
y sus características se puede utilizar el siguiente comando en la terminal:

```bash linenums="1"
nvidia-smi
```

Durante la programación en CUDA, tanto la CPU como la GPU realizan operaciones
simultáneamente, por lo que resulta necesario sincronizar los tiempos de ejecución entre
ambos componentes.

<p align="center">
  <img src="../../../assets/img/docs/Untitled 6 (2).png"/>
  <br />
</p>

La sincronización entre la GPU y la CPU, así como entre diferentes hilos en la GPU, puede
hacer que las sentencias condicionales como `if` resulten desfavorables para la ejecución
en la GPU. Por tanto, se recomienda minimizar el uso de sentencias condicionales dentro
de un kernel.

La programación en CUDA se realiza utilizando C/C++ y los archivos CUDA tienen la
extensión `.cu`. La compilación del código se lleva a cabo con el siguiente comando:

```bash linenums="1"
!nvcc -arch=sm_70 -o resultado_nombre programa.cu -run
```

En este comando, `-arch=sm_70` especifica la arquitectura objetivo para la compilación. A
continuación se presenta un ejemplo básico de código en CUDA:

```c linenums="1"
#include <iostream>

using namespace std;

void hola_cpu(void)
{
    printf("Esto es un saludo desde la CPU");
}

// Define una función de kernel que se ejecuta en la GPU
__global__ void ejemplo_kernel(void)
{
    printf("Hola, esto se está ejecutando de forma paralela en GPU");
}

int main(void)
{
    hola_cpu();

    // Lanza el kernel en la GPU con una sola instancia de un solo hilo
    ejemplo_kernel<<<1, 1>>>();

    // Espera a que todos los hilos en la GPU terminen antes de continuar
    cudaDeviceSynchronize();

    return 0;
}
```

La palabra clave `__global__` indica que la función se ejecuta en la GPU y puede ser
invocada desde la CPU. El código ejecutado en la CPU se denomina **_host_** y el código
ejecutado en la GPU se denomina **_device_**. Las funciones `__global__` deben tener el
tipo de retorno `void`. La invocación de una función CUDA utiliza la **configuración de
ejecución**, que adopta la forma `nombre_funcion<<<x, y>>>`, donde `x` es el número de
bloques (debe ser menor a 2048) e `y` es el número de hilos por bloque (debe ser menor a
1024). El número total de hilos se obtiene multiplicando `x` por `y`. Por ejemplo, con 2
bloques y 4 hilos por bloque se obtienen 8 hilos en total. El número de bloques y de
hilos depende de las capacidades de hardware de la GPU.

El código del kernel se ejecuta en cada hilo de cada bloque configurado cuando se lanza
el kernel. Un kernel con un solo bloque utilizará únicamente un multiprocesador de la
GPU. La función `cudaDeviceSynchronize()` asegura que la GPU complete su tarea antes de
que la CPU finalice el programa, funcionando como herramienta de sincronización entre CPU
y GPU.

CUDA permite agilizar los bucles en la programación. Por ejemplo, para incrementar un
valor `b` a los `N` elementos de un vector en la CPU:

```c linenums="1"
void incremento_en_cpu(float *a, float b, int N)
{
    for (int idx = 0; idx < N; idx++)
    {
        a[idx] = a[idx] + b;
    }
}

void main()
{
    incremento_en_cpu(a, b, N);
}
```

Este bucle es adecuado para la paralelización, ya que cada índice es independiente y no
requiere un orden específico de ejecución (las hebras en un _warp_ se ejecutan de forma
desordenada).

### Identificación de hilos, bloques y mallas en un kernel

CUDA proporciona variables integradas que describen los hilos, bloques y mallas (_grid_):

| Variable      | Definición                                          |
| ------------- | --------------------------------------------------- |
| `gridDim.x`   | Número total de bloques en la malla.                |
| `blockIdx.x`  | Índice del bloque actual dentro de la malla.        |
| `blockDim.x`  | Número de hilos en un bloque dentro del kernel.     |
| `threadIdx.x` | Índice de un hilo dentro de un bloque en el kernel. |

Los bloques de un mismo kernel no pueden comunicarse entre sí durante su ejecución, ya
que pueden ejecutarse en cualquier orden y de forma independiente. El kernel debe
realizar el trabajo de una sola iteración del bucle, por lo que la configuración del
kernel debe ajustarse al número de iteraciones, configurando adecuadamente tanto el
número de bloques como el número de hilos por bloque. A continuación se presenta el
código paralelizado del bucle anterior:

```c linenums="1"
__global__ void incremento_en_gpu(float *a, float b, int N)
{
    int idx = blockIdx.x * blockDim.x + threadIdx.x;

    if (idx < N)
    {
        a[idx] = a[idx] + b;
    }
}

void main()
{
    dim3 dimBlock(blocksize);
    dim3 dimGrid(ceil(N / (float)blocksize));

    incremento_en_gpu<<<dimGrid, dimBlock>>>(a, b, N);
}
```

Cada hilo realiza una iteración del bucle. La fórmula para mapear cada hilo a un índice
del bucle es:

$$
i_{x} = (blockIdx.x \cdot blockDim.x) + threadIdx.x
$$

<p align="center">
  <img src="../../../assets/img/docs/Untitled 7 (1).png"/>
  <br />
</p>

Es importante que `blockDim.x` sea mayor o igual a 32, que es el tamaño del _warp_. En
casos donde el número de hilos excede el número de tareas, se debe asegurar que el índice
obtenido $i_{x}$ sea menor que el número total de datos.

<p align="center">
  <img src="../../../assets/img/docs/Untitled 8 (1).png"/>
  <br />
</p>

### Asignación de memoria en GPU

La asignación y liberación de memoria se realiza de forma diferente en la CPU y en la
GPU. En la CPU se utilizan las funciones `malloc()` y `free()`, mientras que en la GPU se
emplean `cudaMallocManaged()` y `cudaFree()`. El siguiente ejemplo muestra ambos
enfoques:

```c linenums="1"
// Asignación en CPU
int N = 2 << 20;
size_t size = N * sizeof(int);
int *a;
a = (int *)malloc(size);
free(a);

// Asignación en GPU con memoria unificada
int N = 2 << 20;
size_t size = N * sizeof(int);
int *a;
cudaMallocManaged(&a, size);
cudaFree(a);
```

Gracias a los avances en hardware, se ha logrado mejorar la tasa de transferencia entre
la CPU y la GPU. Las versiones recientes de CUDA permiten el uso de **memoria
unificada**, que facilita el intercambio de datos entre ambos componentes.

<p align="center">
  <img src="../../../assets/img/docs/Untitled 9.png"/>
  <br />
</p>

La memoria unificada ofrece varias ventajas: proporciona un único puntero a los datos
accesible tanto desde la CPU como desde la GPU, elimina la necesidad de usar
`cudaMemcpy()`, facilita la portabilidad del código y mejora el rendimiento en la
transferencia de datos asegurando la coherencia global. También permite la optimización
manual con `cudaMemcpyAsync()`.

Los tipos de memoria en CUDA se pueden observar en la siguiente imagen:

<p align="center">
  <img src="../../../assets/img/docs/Untitled 10 (1).png"/>
  <br />
</p>

La memoria unificada presenta algunas consideraciones importantes: su capacidad máxima
está limitada por la menor cantidad de memoria disponible entre las GPUs; la memoria
unificada utilizada por la CPU debe migrar de nuevo a la GPU antes de lanzar un kernel;
la CPU no puede acceder a la memoria unificada mientras la GPU ejecuta un kernel (se debe
llamar a `cudaDeviceSynchronize()` previamente); y la GPU tiene acceso exclusivo a la
memoria unificada mientras ejecuta un kernel, incluso si este no la utiliza directamente.

<p align="center">
  <img src="../../../assets/img/docs/AB407146-6A59-4476-A97F-B0D7BF2AA8CC.png"/>
  <br />
</p>

#### Ejemplos de uso de memoria unificada

El siguiente ejemplo muestra un uso **incorrecto** de la memoria unificada, donde la CPU
accede a una variable mientras la GPU puede estar ejecutándose:

```c linenums="1"
__device__ __managed__ int x, y = 2;

__global__ void mykernel()
{
    x = 10;
}

int main()
{
    mykernel <<<1, 1>>> ();

    // ERROR: Acceso concurrente desde la CPU mientras la GPU puede estar usando la variable 'y'
    y = 20;

    return 0;
}
```

La versión **correcta** incluye la sincronización antes de que la CPU acceda a la
variable:

```c linenums="1"
__device__ __managed__ int x, y = 2;

__global__ void mykernel()
{
    x = 10;
}

int main()
{
    mykernel <<<1, 1>>> ();

    // Sincronización antes de que la CPU acceda a la memoria unificada
    cudaDeviceSynchronize();

    y = 20;

    return 0;
}
```

### Kernels con gran tamaño de datos

Cuando la cantidad de datos excede el número máximo de hebras disponibles, es necesario
dividir los datos en bloques más pequeños que se ajusten al número de hebras. Tras
completar el procesamiento de una división, se pasa a la siguiente utilizando un
desplazamiento de $blockDim.x \cdot gridDim.x$. El siguiente bucle ilustra esta técnica:

```c linenums="1"
__global__ void kernel(int *a, int N)
{
    int indexWithinTheGrid = (blockIdx.x * blockDim.x) + threadIdx.x;
    int gridStride = blockDim.x * gridDim.x;

    for (int i = indexWithinTheGrid; i < N; i += gridStride)
    {
        // Código para procesar los datos
    }
}
```

### Manejo de errores

Las funciones de CUDA devuelven un valor de tipo `cudaError_t` que indica si se ha
producido un error. A continuación se muestra cómo gestionar errores al reservar memoria:

```c linenums="1"
cudaError_t err;
err = cudaMallocManaged(&a, N);

if (err != cudaSuccess)
{
    printf("Error: %s\n", cudaGetErrorString(err));
}
```

Para la gestión de errores al lanzar un kernel, se utiliza `cudaGetLastError()`:

```c linenums="1"
someKernel<<<1, -1>>>(); // -1 no es un valor válido para el número de hebras por bloque

cudaError_t err;
err = cudaGetLastError();

if (err != cudaSuccess)
{
    printf("Error: %s\n", cudaGetErrorString(err));
}
```

También se puede emplear una función auxiliar para verificar errores de forma
centralizada:

```c linenums="1"
#include <stdio.h>
#include <assert.h>

inline cudaError_t checkCuda(cudaError_t result)
{
    if (result != cudaSuccess)
    {
        fprintf(stderr, "CUDA Runtime Error: %s\n", cudaGetErrorString(result));
        assert(result == cudaSuccess);
    }

    return result;
}

int main()
{
    checkCuda(todas_las_funciones_a_gestionar_errores);
}
```

### Patrones comunes de kernels

<p align="center">
  <img src="../../../assets/img/docs/Untitled 12.png"/>
  <br />
</p>

Antes de explorar los distintos patrones, conviene definir el concepto de **bucle
_forall_**: se trata de un bucle `for` sin dependencias entre iteraciones, lo que permite
que el resultado no se vea alterado independientemente del índice de inicio. Los patrones
más comunes son los siguientes:

- **Operadores streaming**: Representan la forma más simple de un bucle _forall_. CUDA
  puede utilizar todos los hilos necesarios para procesar cada elemento de manera
  independiente:

  ```c linenums="1"
  #define N 1920 * 1080

  float r[N], g[N], b[N], luminancia[N];

  for(int i = 0; i < N; i++)
  {
      luminancia[i] = 255 * (0.2999 * r[i] + 0.587 * g[i] + 0.114 * b[i]);
  }
  ```

- **Operadores sobre vectores**: Cada iteración del bucle puede asignarse a un hilo CUDA
  para maximizar el paralelismo y la escalabilidad:

  ```c linenums="1"
  #define N (1 << 30)

  float a[N], b[N], c[N];

  for(int i = 0; i < N; i++)
  {
      c[i] = a[i] + b[i];
  }
  ```

- **Operadores patrón (_stencil operators_)**: Las iteraciones externas deben
  serializarse debido a dependencias, pero se puede aprovechar el paralelismo en cada
  partícula. La carga computacional depende del número de iteraciones:

  ```c linenums="1"
  int i, j, iter, N, Niters;
  float in[N][N], out[N][N];

  for (iter = 0; iter < Niters; iter++)
  {
      for (i = 1; i < N - 1; i++)
      {
          for (j = 1; j < N - 1; j++)
          {
              out[i][j] = 0.2 * (in[i][j] + in[i-1][j] + in[i+1][j] + in[i][j-1] + in[i][j+1]);
          }
      }

      for (i = 1; i < N - 1; i++)
      {
          for (j = 1; j < N - 1; j++)
          {
              in[i][j] = out[i][j];
          }
      }
  }
  ```

  El paralelismo en este caso está determinado por el tamaño de la matriz 2D ($N^2$).

- **Operadores de reducción**: Aunque el código presenta dependencias entre iteraciones,
  el paralelismo puede desplegarse mediante una estructura en árbol binario, resultando
  en $\log(N)$ pasos que reducen el grado de paralelismo hasta llegar a un solo hilo. Es
  fundamental usar un patrón de acceso a memoria que optimice la jerarquía de memoria de
  la GPU:

  ```c linenums="1"
  float sum, x[N];
  sum = 0;

  for (int i = 0; i < N; i++)
  {
      sum += x[i];
  }
  ```

- **Histogramas**: Representan un patrón donde los bucles presentan dependencias, pero
  las lecturas pueden realizarse en paralelo si se asignan a hilos CUDA. CUDA proporciona
  operaciones atómicas (`atomicInc(histo[image[i][j]])`) para manejar accesos
  concurrentes y prevenir condiciones de carrera:

  ```c linenums="1"
  int histo[Nbins], image[N][N];

  for (int i = 0; i < Nbins; i++)
  {
      histo[i] = 0;
  }

  for (int i = 0; i < N; i++)
  {
      for (int j = 0; j < N; j++)
      {
          histo[image[i][j]]++;
      }
  }
  ```

Como análisis final, el operador streaming es el más eficiente en GPU, el operador patrón
aprovecha mejor la memoria compartida, el operador de reducción requiere una mayor
intervención del programador y el histograma es el más desafiante de implementar.

## Aceleración de aplicaciones con CUDA en Python

El rendimiento de las aplicaciones científicas y de ingeniería en Python se puede mejorar
significativamente mediante el uso de herramientas como Numba y CuPy. Estas tecnologías
permiten la paralelización y aceleración del código, aprovechando la potencia de
procesamiento de las GPUs y superando las limitaciones del intérprete de Python.

### Numba

#### Fundamentos

Numba es un compilador JIT (_Just-In-Time_) y de especialización de tipos para acelerar
cálculo numérico en Python tanto en CPU como en GPU. A diferencia de otros enfoques,
Numba compila funciones individuales de Python, no la aplicación al completo, por lo que
no sustituye al intérprete de Python. La aceleración se consigue generando
implementaciones específicas para el tipo de dato que se utiliza, en lugar de emplear el
_dynamic typing_ que es el comportamiento por defecto de Python. Al ser _just-in-time_,
la compilación se produce cuando la función se invoca por primera vez, lo que permite al
compilador conocer los argumentos que se van a utilizar y facilita la ejecución
interactiva en cuadernos Jupyter. Numba se centra principalmente en tipos de datos
numéricos (enteros, flotantes, números complejos) y ofrece el mejor soporte cuando se
trabaja con arrays de NumPy.

Sin embargo, Numba presenta ciertas limitaciones: no es compatible con Pandas, por lo que
se recomienda convertir los DataFrames a matrices de NumPy o CuPy antes de utilizarlo.
Para más información, se puede consultar la
[página oficial de Numba](https://numba.pydata.org/).

#### Alternativas a Numba

Existen varias alternativas para la programación con CUDA, cada una con sus propias
ventajas. **CUDA C/C++** es la opción más común, con mayor rendimiento y flexibilidad, y
acelera aplicaciones escritas en C/C++. **pyCUDA** expone la totalidad de la API de CUDA
C/C++ y es la opción más eficiente disponible para Python, aunque requiere escribir
código C dentro de Python y, en general, modificaciones sustanciales del código.
**Numba**, por su parte, ofrece el mejor equilibrio entre tiempo de desarrollo y
beneficio: aunque potencialmente menos eficiente que pyCUDA y sin exponer aún la
totalidad de la API de CUDA C/C++, permite aceleraciones masivas con muy pocas
modificaciones del código, escribiendo directamente en Python, y también optimiza código
para la CPU.

#### Funcionamiento interno

Cuando se invoca una función decorada con `@jit` o `@njit`, el compilador de Numba
convierte el código Python a código máquina para el tipo específico de los datos que se
están utilizando. Numba también conserva la función original de Python en el atributo
`.py_func`, lo que permite llamar a la función con dicho atributo para comparar
resultados:

```python linenums="1"
from numba import jit
import math

@jit
def hypot(x, y):
    x = abs(x)
    y = abs(y)
    t = min(x, y)
    x = max(x, y)
    t = t / x
    return x * math.sqrt(1 + t * t)

# Ejecución compilada con Numba
hypot(3.0, 4.0)

# Ejecución con la función original de Python
hypot.py_func(3.0, 4.0)
```

No obstante, si existen versiones ya implementadas y optimizadas en Python para una
operación concreta, estas suelen ser más rápidas que Numba, ya que Numba introduce una
pequeña sobrecarga en la compilación inicial.

El proceso interno de compilación se puede visualizar de la siguiente manera:

![image.png](Numba/image.png)

Para inspeccionar el resultado de la inferencia de tipos, se puede utilizar el método
`.inspect_types()`, que imprime el código fuente anotado con los tipos inferidos:

```python linenums="1"
hypot.inspect_types()
```

#### Decoradores

Numba ofrece varios decoradores para la compilación y optimización de funciones:

| Decorador                       | Definición                                                                                                                                                                                                                     |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `@jit`                          | Compila en modo objeto. Numba compila los bucles optimizables a código máquina y el resto de la función se ejecuta con el intérprete de Python.                                                                                |
| `@njit` = `@jit(nopython=True)` | Compila sin el intérprete de Python, obteniendo el mejor rendimiento. Puede fallar si los parámetros no son compatibles; si falla, se recomienda utilizar `@jit`. Este es el decorador preferido para la mayoría de los casos. |
| `@njit(parallel=True)`          | Compila el código para ejecutarse en múltiples hilos, aprovechando la paralelización cuando las operaciones lo permiten.                                                                                                       |
| `@njit(fastmath=True)`          | Habilita cálculos matemáticos rápidos a costa de reducir la precisión numérica, acelerando aún más el rendimiento.                                                                                                             |

Los decoradores pueden combinarse para optimizar el rendimiento. Por ejemplo,
`@njit(parallel=True, fastmath=True)` evita el intérprete de Python, paraleliza el código
y permite una menor precisión numérica para maximizar la velocidad de ejecución.

El decorador `@njit` es la versión recomendada y más eficiente, ya que fuerza a mostrar
los errores de las estructuras o funciones que no son directamente compatibles con Numba
y que no se pueden compilar, evitando el _object mode_ (donde se utiliza el tipo de
variable original de Python sin especializar el tipo en Numba).

##### Ejemplo

```python linenums="1"
from numba import njit
import numpy as np

@njit()
def bucle(lista1, lista2, num_filas):
    lista3 = []

    for fila in range(num_filas):
        if (lista1[fila] >= 1) and (lista2[fila] <= 5):
            lista3.append(np.mean([lista1[fila], lista2[fila]]))

    return lista3

lista1 = np.array([1, 2, 3])
lista2 = np.array([4, 5, 6])
result = bucle(lista1, lista2, len(lista1))
print(result)
```

En este ejemplo, el decorador `@njit()` compila la función para ejecutarse sin el
intérprete de Python, mejorando notablemente el rendimiento.

#### Vectorización con Numba para operaciones elemento a elemento en GPU

El hardware de la GPU está diseñado para la paralelización de datos, por lo que se
obtiene el máximo _throughput_ cuando la GPU calcula la misma operación para diferentes
elementos al mismo tiempo. Las funciones universales de NumPy (_ufuncs_) realizan la
misma operación en cada elemento de un array, lo que las hace naturalmente paralelizables
y las ajusta muy bien a la naturaleza de la GPU. En realidad, las _ufuncs_ son funciones
que pueden tomar arrays de NumPy de cualquier dimensión o escalares y operar elemento a
elemento.

Un ejemplo para la CPU:

```python linenums="1"
from numba import vectorize
import numpy as np

@vectorize
def add_ten(num):
    return num + 10

nums = np.arange(10)
add_ten(nums)
```

Un ejemplo para la GPU:

```python linenums="1"
@vectorize(['int64(int64, int64)'], target='cuda')
def add_ufunc(x, y):
    return x + y

add_ufunc(a, b)
```

En el caso de la GPU se especifica el _target_ como `'cuda'`, así como el _typing_
específico de las variables (lo que aparece dentro de los paréntesis) y el tipo de
retorno de la función (lo que aparece fuera del paréntesis). En este caso, la función
toma como argumentos dos parámetros de tipo entero de 64 bits y devuelve el mismo tipo.

Internamente, Numba compila un kernel CUDA para ejecutar la operación _ufunc_ en paralelo
sobre todos los elementos de entrada, reserva memoria en la GPU para las entradas y la
salida, copia los datos de entrada a la GPU, ejecuta el kernel CUDA con las dimensiones
adecuadas según el tamaño de las entradas, copia el resultado de vuelta a la CPU y lo
devuelve como un array de NumPy en el _host_.

Existen algunas consideraciones importantes para obtener un rendimiento óptimo en la GPU:
las entradas deben ser suficientemente grandes para mantener la GPU ocupada (miles de
elementos como mínimo); el cálculo debe tener suficiente intensidad aritmética para
compensar la sobrecarga de enviar datos a la GPU; conviene ejecutar varias operaciones en
secuencia en la GPU para amortizar el coste de la copia de datos; y los tipos de datos
deben ser los más pequeños posibles, ya que las operaciones en punto flotante de 64 bits
pueden ser entre 2x y 24x más lentas que las de 32 bits dependiendo de la arquitectura de
la GPU. NumPy utiliza tipos de 64 bits por defecto, por lo que es importante establecer
el atributo `dtype` o usar `ndarray.astype()` para seleccionar tipos de 32 bits cuando
sea apropiado.

El siguiente ejemplo muestra una operación con mayor intensidad aritmética, sobre una
entrada mucho más grande y con tipos de datos de 32 bits:

```python linenums="1"
import math
import numpy as np
from numba import vectorize

SQRT_2PI = np.float32((2 * math.pi) ** 0.5)

@vectorize(['float32(float32, float32, float32)'], target='cuda')
def gaussian_pdf(x, mean, sigma):
    return math.exp(-0.5 * ((x - mean) / sigma) ** 2) / (sigma * SQRT_2PI)

x = np.random.uniform(-3, 3, size=1000000).astype(np.float32)
mean = np.float32(0.0)
sigma = np.float32(1.0)

gaussian_pdf(x[0], 0.0, 1.0)

import scipy.stats
norm_pdf = scipy.stats.norm
%timeit norm_pdf.pdf(x, loc=mean, scale=sigma)

%timeit gaussian_pdf(x, mean, sigma)

@vectorize
def cpu_gaussian_pdf(x, mean, sigma):
    return math.exp(-0.5 * ((x - mean) / sigma) ** 2) / (sigma * SQRT_2PI)

%timeit cpu_gaussian_pdf(x, mean, sigma)
```

Para operaciones como el coseno, el seno o la exponencial, las versiones de NumPy no son
compatibles con el _target_ CUDA, por lo que se debe utilizar la biblioteca `math` de
Python.

#### Diferencias entre `@vectorize` y `@njit`

El decorador `@njit` compila funciones de Python en código máquina eliminando la
sobrecarga del intérprete, y resulta adecuado para funciones que contienen bucles y
cálculos numéricos intensivos. No paraleliza automáticamente el código, aunque se puede
habilitar la paralelización con el argumento `parallel=True`. Por su parte, `@vectorize`
permite definir funciones que operan elemento a elemento sobre arrays de NumPy, de forma
similar a las _ufuncs_. Con `@vectorize` se puede especificar el tipo de datos de entrada
y salida, y Numba genera una función que aplica la operación a cada elemento del array de
manera eficiente. Se puede usar el argumento `target='parallel'` para habilitar la
paralelización automática en CPU, o `target='cuda'` para ejecutar en GPU.

#### Funciones de dispositivo para operaciones no elemento a elemento

Para funciones que no son estrictamente elemento a elemento, se utiliza `@cuda.jit`. El
parámetro `device=True` indica que la función solo puede ser invocada desde otra función
que se ejecuta en la GPU, no desde el _host_:

```python linenums="1"
from numba import cuda, vectorize
import math

@cuda.jit(device=True)
def polar_to_cartesian(rho, theta):
    x = rho * math.cos(theta)
    y = rho * math.sin(theta)
    return x, y

@vectorize(['float32(float32, float32, float32, float32)'], target='cuda')
def polar_distance(rho1, theta1, rho2, theta2):
    x1, y1 = polar_to_cartesian(rho1, theta1)
    x2, y2 = polar_to_cartesian(rho2, theta2)
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

n = 1000000
rho1 = np.random.uniform(0.5, 1.5, size=n).astype(np.float32)
theta1 = np.random.uniform(-np.pi, np.pi, size=n).astype(np.float32)
rho2 = np.random.uniform(0.5, 1.5, size=n).astype(np.float32)
theta2 = np.random.uniform(-np.pi, np.pi, size=n).astype(np.float32)

polar_distance(rho1, theta1, rho2, theta2)
```

#### Operaciones soportadas en la GPU

Las operaciones soportadas por Numba en la GPU incluyen sentencias `if`/`elif`/`else`,
bucles `while` y `for`, operadores matemáticos básicos, funciones seleccionadas de los
módulos `math` y `cmath`, y tuplas.

#### Ejemplo completo: capa oculta de una red neuronal en GPU

El siguiente ejemplo muestra cómo implementar una capa oculta de una red neuronal
utilizando `@vectorize` con _target_ CUDA, incluyendo la gestión explícita de la memoria
de la GPU para optimizar las transferencias de datos:

```python linenums="1"
import numpy as np
from numba import cuda, vectorize
from math import exp

n = 1000000

greyscales = np.floor(np.random.uniform(0, 255, n).astype(np.float32))
weights = np.random.normal(.5, .1, n).astype(np.float32)

@vectorize(['float32(float32)'], target='cuda')
def normalize(grayscales):
    return grayscales / 255

@vectorize(['float32(float32, float32)'], target='cuda')
def weigh(values, weights):
    return values * weights

@vectorize(['float32(float32)'], target='cuda')
def activate(values):
    return (exp(values) - exp(-values)) / (exp(values) + exp(-values))

def create_hidden_layer(n, greyscales, weights, exp, normalize, weigh, activate):
    # Transferencia de datos de CPU a GPU
    greyscales_device = cuda.to_device(greyscales)
    weights_device = cuda.to_device(weights)

    # Reserva de buffers en la GPU sin inicializar datos (similar a malloc en C)
    normalized_out_device = cuda.device_array(shape=(n,), dtype=np.float32)
    weighted_out_device = cuda.device_array(shape=(n,), dtype=np.float32)
    activated_out_device = cuda.device_array(shape=(n,), dtype=np.float32)

    # Ejecución de las operaciones en la GPU
    normalize(greyscales_device, out=normalized_out_device)
    weigh(normalized_out_device, weights_device, out=weighted_out_device)
    activate(weighted_out_device, out=activated_out_device)

    # Copia del resultado de vuelta a la CPU
    return activated_out_device.copy_to_host()

arguments = {
    "n": n,
    "greyscales": greyscales,
    "weights": weights,
    "exp": exp,
    "normalize": normalize,
    "weigh": weigh,
    "activate": activate
}

a = create_hidden_layer(**arguments)
print(a)
```

En este ejemplo, `cuda.to_device()` transfiere una variable de la CPU (almacenada en la
memoria RAM) a la GPU, reservando memoria para dicha variable. En el caso de un array de
NumPy, se obtiene una variable de la clase `DeviceNDArray`. Por su parte,
`cuda.device_array()` crea un array vacío en la memoria de la GPU sin copiar datos desde
la CPU, lo que permite crear buffers para almacenar resultados de cálculos intermedios
sin inicializar los datos.

### Kernels CUDA personalizados en Python con Numba

La jerarquía de ejecución en CUDA se organiza de la siguiente manera: las hebras se
agrupan en bloques de hebras, y los bloques de hebras conforman una malla (_grid_). Para
escribir kernels personalizados se utiliza el decorador `@cuda.jit`, que a diferencia de
`@vectorize` no devuelve valores, sino que utiliza un argumento de salida:

```python linenums="1"
from numba import cuda
import numpy as np

@cuda.jit
def add_kernel(x, y, out):
    idx = cuda.grid(1)  # Índice único del hilo en una malla unidimensional
    # Equivalente a: cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x
    out[idx] = x[idx] + y[idx]

n = 4096
x = np.arange(n).astype(np.int32)
y = np.ones_like(x)

d_x = cuda.to_device(x)
d_y = cuda.to_device(y)
d_out = cuda.device_array_like(d_x)

threads_per_block = 128
blocks_per_grid = 32

add_kernel[blocks_per_grid, threads_per_block](d_x, d_y, d_out)
cuda.synchronize()
print(d_out.copy_to_host())
```

Se pueden consultar las especificaciones de la GPU utilizada con el siguiente código:

```python linenums="1"
gpu = cuda.get_current_device()

print(f"Nombre de la GPU: {gpu.name}")
print(f"Número de multiprocesadores: {gpu.MULTIPROCESSOR_COUNT}")
print(f"Máximo de hilos por bloque: {gpu.MAX_THREADS_PER_BLOCK}")
print(f"Máximo de bloques en cada dimensión: {gpu.MAX_GRID_DIM_X}, {gpu.MAX_GRID_DIM_Y}, {gpu.MAX_GRID_DIM_Z}")
print(f"Máximo de hilos por dimensión de bloque: {gpu.MAX_BLOCK_DIM_X}, {gpu.MAX_BLOCK_DIM_Y}, {gpu.MAX_BLOCK_DIM_Z}")
print(f"Máximo de memoria compartida por bloque: {gpu.MAX_SHARED_MEMORY_PER_BLOCK} bytes")
```

La latencia de las operaciones puede ocultarse por los SMs con otro trabajo útil siempre
que exista trabajo pendiente. Para ello, conviene proporcionar a los SMs un número
suficiente de _warps_, lo que se consigue ejecutando kernels con dimensiones de malla y
bloque suficientemente grandes.

A la hora de elegir el tamaño óptimo de la malla de hilos CUDA, se pueden seguir estas
heurísticas como punto de partida: el tamaño de un bloque debe ser múltiplo de 32 hilos
(el tamaño de un _warp_), con tamaños típicos entre 128 y 512 hilos por bloque; el tamaño
de la malla debe asegurar la utilización completa de la GPU, siendo un buen punto de
partida lanzar entre 2x y 4x el número de SMs de la GPU (generalmente entre 20 y 100
bloques); y para entradas muy grandes, no conviene lanzar una malla donde el número de
hilos iguale al número de elementos de entrada, ya que esto generaría un número excesivo
de bloques con una sobrecarga significativa.

#### _Grid stride loop_

El patrón _grid stride loop_ permite trabajar con conjuntos de datos más grandes que el
número total de hilos, al tiempo que se beneficia de la **coalescencia de memoria
global**, que permite a los hilos paralelos acceder a la memoria en bloques contiguos,
reduciendo el número total de operaciones de memoria:

```python linenums="1"
from numba import cuda

@cuda.jit
def add_kernel(x, y, out):
    start = cuda.grid(1)
    stride = cuda.gridsize(1)  # Número total de hilos en la malla
    # Equivalente a: cuda.blockDim.x * cuda.gridDim.x

    for i in range(start, x.shape[0], stride):
        out[i] = x[i] + y[i]

import numpy as np

n = 100000
x = np.arange(n).astype(np.int32)
y = np.ones_like(x)

d_x = cuda.to_device(x)
d_y = cuda.to_device(y)
d_out = cuda.device_array_like(d_x)

threads_per_block = 128
blocks_per_grid = 30

add_kernel[blocks_per_grid, threads_per_block](d_x, d_y, d_out)
print(d_out.copy_to_host())
```

#### Diferencias entre `@vectorize` y `@cuda.jit`

El decorador `@vectorize` opera a un nivel más alto de abstracción y está pensado para
operaciones elemento a elemento, donde Numba gestiona la paralelización de forma
automática. Se puede usar tanto en CPU (`target='cpu'`) como en GPU (`target='cuda'`):

```python linenums="1"
from numba import vectorize
import numpy as np

@vectorize(['float32(float32, float32)'], target='cuda')
def suma_elementwise(x, y):
    return x + y

a = np.array([1, 2, 3, 4, 5], dtype=np.float32)
b = np.array([10, 20, 30, 40, 50], dtype=np.float32)

c = suma_elementwise(a, b)
print(c)  # [11. 22. 33. 44. 55.]
```

Por su parte, `@cuda.jit` opera a un nivel más bajo, similar a la programación con CUDA
en C. El programador controla explícitamente los bloques e hilos, lo que ofrece mayor
flexibilidad, incluyendo acceso a memoria compartida y sincronización de hilos:

```python linenums="1"
from numba import cuda
import numpy as np

@cuda.jit
def suma_kernel(x, y, out):
    idx = cuda.grid(1)
    if idx < x.size:
        out[idx] = x[idx] + y[idx]

a = np.array([1, 2, 3, 4, 5], dtype=np.float32)
b = np.array([10, 20, 30, 40, 50], dtype=np.float32)
c = np.zeros_like(a)

d_a = cuda.to_device(a)
d_b = cuda.to_device(b)
d_c = cuda.device_array_like(c)

threads_per_block = 32
blocks_per_grid = (a.size + (threads_per_block - 1)) // threads_per_block

suma_kernel[blocks_per_grid, threads_per_block](d_a, d_b, d_c)

c = d_c.copy_to_host()
print(c)  # [11. 22. 33. 44. 55.]
```

### Operaciones atómicas y condiciones de carrera

Una **condición de carrera** (_race condition_) ocurre cuando múltiples hilos acceden a
la misma ubicación de memoria y, debido a la falta de sincronización, el resultado puede
ser inesperado o incorrecto. Los dos tipos más comunes en CUDA son el _read-after-write_
(RAW), donde un hilo intenta leer un valor que otro hilo podría estar modificando
simultáneamente, y el _write-after-write_ (WAW), donde dos hilos intentan escribir en la
misma dirección de memoria al mismo tiempo.

Para evitar condiciones de carrera, cada hilo debe escribir en una ubicación de memoria
única, no se debe usar el mismo array como entrada y salida en la misma llamada al kernel
(en su lugar se puede emplear _double buffering_), y se deben utilizar operaciones
atómicas cuando sea necesario. Una operación atómica asegura que solo un hilo a la vez
pueda modificar una variable compartida.

El siguiente ejemplo muestra un código **incorrecto** sin operaciones atómicas, donde
varios hilos pueden leer el mismo valor del contador antes de que otro lo actualice:

```python linenums="1"
from numba import cuda
import numpy as np

@cuda.jit
def contador_global(counter):
    idx = cuda.grid(1)
    counter[0] += 1  # Condición de carrera
```

La versión **correcta** utiliza `cuda.atomic.add()` para garantizar la seguridad de la
operación:

```python linenums="1"
from numba import cuda
import numpy as np

@cuda.jit
def contador_global_atomic(counter):
    idx = cuda.grid(1)
    cuda.atomic.add(counter, 0, 1)  # Operación atómica

contador = np.zeros(1, dtype=np.int32)
d_contador = cuda.to_device(contador)

threads_per_block = 128
blocks_per_grid = 4

contador_global_atomic[blocks_per_grid, threads_per_block](d_contador)

resultado = d_contador.copy_to_host()
print("Valor final del contador:", resultado[0])  # Esperado: 128 * 4 = 512
```

### Uso eficiente del subsistema de memoria

La coalescencia de memoria (_memory coalescing_) es un factor determinante en el
rendimiento de los kernels CUDA. Los bloques de hebras se dividen en _warps_ de 32
hebras, y las instrucciones se ejecutan en paralelo a nivel de _warp_. El subsistema de
memoria intenta minimizar el número de líneas de caché requeridas para completar las
lecturas o escrituras solicitadas por el _warp_.

Cuanto más contiguos sean los datos asignados a cada hebra del _warp_, mayor es la
eficiencia en el uso de la memoria y menor la pérdida de rendimiento. Conforme la memoria
requerida se vuelve menos contigua, se necesitan más líneas de caché para satisfacer las
necesidades de los _warps_, y más datos transferidos no se utilizan.

![image.png](Numba/image%201.png)

![image.png](Numba/image%202.png)

![image.png](Numba/image%203.png)

El siguiente ejemplo ilustra la diferencia entre un patrón de acceso coalescente y uno no
coalescente:

```python linenums="1"
@cuda.jit
def add_experiment(a, b, out, stride, coalesced):
    i = cuda.grid(1)

    if coalesced == True:
        out[i] = a[i] + b[i]
    else:
        out[i] = a[stride * i] + b[stride * i]
```

Un ejemplo práctico de suma por columnas de una matriz, que aprovecha el acceso
coalescente:

```python linenums="1"
@cuda.jit
def col_sums(a, sums, ds):
    idx = cuda.grid(1)
    sum = 0.0

    for i in range(n):
        sum += a[i][idx]

    sums[idx] = sum

n = 16384
threads_per_block = 256
blocks = int(n / threads_per_block)

a = np.ones(n * n).reshape(n, n).astype(np.float32)
a[:, 3] = 9
sums = np.zeros(n).astype(np.float32)

d_a = cuda.to_device(a)
d_sums = cuda.to_device(sums)

%timeit col_sums[blocks, threads_per_block](d_a, d_sums, n); cuda.synchronize()
result = d_sums.copy_to_host()
truth = a.sum(axis=0)
```

#### Trabajo con matrices en 2D

CUDA permite trabajar con mallas bidimensionales de hilos, lo que resulta natural para
operaciones sobre matrices. Se utiliza `cuda.grid(2)` para obtener las coordenadas únicas
de cada hilo en la malla 2D:

```python linenums="1"
import numpy as np
from numba import cuda

A = np.zeros((4, 4))
d_A = cuda.to_device(A)

blocks = (2, 2)
threads_per_block = (2, 2)

@cuda.jit
def get_2D_indices(A):
    x, y = cuda.grid(2)
    # Equivalente a:
    # x = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x
    # y = cuda.blockIdx.y * cuda.blockDim.y + cuda.threadIdx.y
    A[x][y] = x + y / 10

get_2D_indices[blocks, threads_per_block](d_A)
result = d_A.copy_to_host()
result
```

En la suma de matrices, el acceso coalescente se consigue recorriendo por columnas
(`out[y][x]`), mientras que el acceso no coalescente recorre por filas (`out[x][y]`):

```python linenums="1"
@cuda.jit
def matrix_add(a, b, out, coalesced):
    x, y = cuda.grid(2)

    if coalesced == True:
        out[y][x] = a[y][x] + b[y][x]  # Acceso coalescente (por columna)
    else:
        out[x][y] = a[x][y] + b[x][y]  # Acceso no coalescente (por fila)
```

### Memoria compartida con Numba

La memoria utilizada hasta ahora es la **memoria global** (_global memory_), accesible
por cualquier hilo o bloque del dispositivo, con una vida útil que puede extenderse
durante toda la ejecución de la aplicación y con una capacidad relativamente grande. Sin
embargo, su latencia es elevada en comparación con otros tipos de memoria disponibles en
la GPU.

La **memoria compartida** (_shared memory_) reside en un área de memoria _on-chip_ del
dispositivo. Su tamaño es limitado y
[depende de la GPU utilizada](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#compute-capabilities).
Es compartida entre todos los hilos de un mismo bloque, no puede ser accedida por hilos
de otros bloques y no persiste una vez que el kernel termina su ejecución. A cambio,
ofrece un ancho de banda significativamente mayor que la memoria global, lo que la
convierte en una herramienta muy eficaz para optimizar el rendimiento de los kernels.

Los casos de uso más habituales de la memoria compartida son: almacenar en caché datos
leídos desde la memoria global que necesitan ser accedidos múltiples veces dentro de un
mismo bloque; acumular la salida de varios hilos para escribirla de forma coalescente en
la memoria global; y preparar datos para operaciones de dispersión y recopilación
(_scatter/gather_) dentro de un bloque.

En Numba, la memoria compartida se reserva mediante `cuda.shared.array` y la
sincronización entre hilos se realiza con `cuda.syncthreads()`, que garantiza que todos
los hilos del bloque hayan completado sus operaciones antes de continuar.

El siguiente ejemplo muestra cómo intercambiar los elementos de un vector utilizando
memoria compartida como buffer intermedio:

```python linenums="1"
from numba import cuda, types
import numpy as np

@cuda.jit
def swap_with_shared(vector, swapped):
    temp = cuda.shared.array(4, dtype=types.int32)

    idx = cuda.grid(1)

    temp[idx] = vector[idx]

    cuda.syncthreads()

    swapped[idx] = temp[3 - cuda.threadIdx.x]

vector = np.arange(4).astype(np.int32)
swapped = np.zeros_like(vector)

d_vector = cuda.to_device(vector)
d_swapped = cuda.to_device(swapped)

swap_with_shared[1, 4](d_vector, d_swapped)
```

Un caso más avanzado es la transposición de matrices mediante _tiling_, una técnica que
aprovecha la memoria compartida para realizar accesos coalescentes tanto en lectura como
en escritura, mejorando notablemente el rendimiento respecto a una transposición directa
sobre memoria global:

```python linenums="1"
from numba import cuda, types as numba_types
import numpy as np

@cuda.jit
def tile_transpose(a, transposed):
    # Asume un bloque de 32x32 hilos y dimensiones de `a` múltiplos de 32

    tile = cuda.shared.array((32, 32), numba_types.float32)

    # Índices globales de lectura (acceso coalescente)
    a_col = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x
    a_row = cuda.blockIdx.y * cuda.blockDim.y + cuda.threadIdx.y

    # Lectura coalescente de memoria global a memoria compartida
    tile[cuda.threadIdx.y, cuda.threadIdx.x] = a[a_row, a_col]

    cuda.syncthreads()

    # Índices transpuestos para escritura coalescente en memoria global
    t_col = cuda.blockIdx.y * cuda.blockDim.y + cuda.threadIdx.x
    t_row = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.y

    # Escritura desde memoria compartida (índices locales transpuestos) a memoria global
    transposed[t_row, t_col] = tile[cuda.threadIdx.x, cuda.threadIdx.y]
```

### CuPy

CuPy es una biblioteca de Python diseñada para acelerar cálculos numéricos mediante la
ejecución de código en GPUs. Ofrece una API similar a NumPy, lo que permite realizar
operaciones aprovechando la arquitectura de CUDA para mejorar el rendimiento. Resulta
especialmente útil en tareas que involucran grandes volúmenes de datos o cálculos
intensivos. Para más información, se puede consultar la
[página oficial de CuPy](https://cupy.dev/).

```python linenums="1"
import cupy as cp

a = cp.array([1, 2, 3, 4, 5])
b = cp.array([6, 7, 8, 9, 10])

c = a + b

c_numpy = cp.asnumpy(c)
print(c_numpy)  # Resultado: [ 7  9 11 13 15]
```

### Comparación entre Numba y CuPy

**Numba** resulta ideal para acelerar funciones específicas y bucles en Python. Permite
compilación JIT para CPU y GPU, y se integra bien con código existente de NumPy. Se
recomienda para optimizar algoritmos matemáticos complejos y simulaciones con estructuras
de bucles que pueden beneficiarse de la compilación JIT. **CuPy**, por su parte, es más
adecuado para trabajar con matrices y realizar operaciones a gran escala en GPUs. Ofrece
una API similar a NumPy, facilitando la migración de código y aprovechando el hardware de
CUDA. Resulta especialmente apropiado para tareas que involucren cálculos matriciales
intensivos, como el entrenamiento de modelos de _machine learning_, procesamiento de
imágenes y simulaciones con alta densidad de datos.
