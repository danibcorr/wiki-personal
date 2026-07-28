---
authors: Daniel Bazo Correa
description: Programación de kernels CUDA en C, gestión de memoria y patrones comunes.
title: CUDA en C
---

Este capítulo detalla la programación de kernels CUDA en C, incluyendo la gestión de
hilos y bloques, la asignación de memoria unificada y los patrones comunes de
paralelización.

## Bibliografía

- NVIDIA y Universidad de Málaga. (s.f.). _Deep Learning Institute - UMA_.
  <http://nvidiadli.uma.es/index.php/es/certificaciones-nvidia>

## Conceptos básicos

En CUDA, una función paralelizada se denomina _kernel_. Para conocer la GPU disponible y
sus características se puede utilizar el siguiente comando en la terminal:

```bash linenums="1"
nvidia-smi
```

!!! note "Requisitos previos"

    Es necesario disponer de una tarjeta gráfica de NVIDIA con los _drivers_ del sistema
    operativo instalados para poder utilizar estos comandos y programar con CUDA. En caso
    contrario, es posible acceder a plataformas de terceros que proporcionan este tipo de
    recursos, aunque pueden suponer un coste económico dependiendo del _hardware_
    seleccionado.

También es posible consultar las especificaciones de la GPU de forma programática desde
el propio código CUDA:

```c linenums="1"
#include <stdio.h>

int main(void)
{
    int deviceId;
    cudaGetDevice(&deviceId);

    cudaDeviceProp props;
    cudaGetDeviceProperties(&props, deviceId);

    printf("GPU: %s\n", props.name);
    printf("Tamaño del warp: %d\n", props.warpSize);
    printf("Hebras máximas por bloque: %d\n", props.maxThreadsPerBlock);
    printf("Número de SMs: %d\n", props.multiProcessorCount);

    return 0;
}
```

Durante la programación en CUDA, tanto la CPU como la GPU realizan operaciones
simultáneamente, por lo que resulta necesario sincronizar los tiempos de ejecución entre
ambos componentes.

<figure markdown="span">
  ![Interacción entre la CPU y la GPU](../../assets/img/docs/cuda/cuda-c-cpu-gpu-interaction.png)
  <figcaption>Interacción y sincronización entre la CPU y la GPU.</figcaption>
</figure>

!!! warning "Sentencias condicionales en la GPU"

    La sincronización entre la GPU y la CPU, así como entre diferentes hilos en la GPU,
    puede hacer que las sentencias condicionales como `if` resulten desfavorables para la
    ejecución en la GPU. Por tanto, se recomienda minimizar el uso de sentencias
    condicionales dentro de un _kernel_.

La programación en CUDA se realiza utilizando C/C++ y los archivos CUDA tienen la
extensión `.cu`. La compilación del código se lleva a cabo con el siguiente comando:

```bash linenums="1"
nvcc -arch=sm_70 -o resultado_nombre programa.cu -run
```

En este comando, `-arch=sm_70` especifica la arquitectura objetivo para la compilación,
`-o` indica el nombre del ejecutable generado y `-run` ejecuta el binario resultante una
vez finalizada la compilación.

!!! note "Prefijo `!` en Jupyter"

    Para compilar desde un _notebook_ de Jupyter se debe añadir el prefijo `!` al inicio
    del comando, es decir, `!nvcc -arch=sm_70 -o resultado_nombre programa.cu -run`. Dicho
    símbolo indica al _notebook_ que la instrucción debe ejecutarse en la _shell_ del
    sistema en lugar de interpretarse como código Python.

???+ example "Código básico en CUDA"

    ```c linenums="1"
    #include <stdio.h>

    void hola_cpu(void)
    {
        printf("Esto es un saludo desde la CPU\n");
    }

    // Define una función de kernel que se ejecuta en la GPU
    __global__ void ejemplo_kernel(void)
    {
        printf("Hola, esto se está ejecutando de forma paralela en GPU\n");
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
invocada desde la CPU. El código ejecutado en la CPU se denomina _host_ y el código
ejecutado en la GPU se denomina _device_.

Las funciones `__global__` deben tener el tipo de retorno `void`. La invocación de una
función CUDA utiliza la **configuración de ejecución**, que adopta la forma
`nombre_funcion<<<x, y>>>`, donde `x` es el número de bloques e `y` es el número de
hilos por bloque. El número total de hilos se obtiene multiplicando `x` por `y`. Por
ejemplo, con 2 bloques y 4 hilos por bloque se obtienen 8 hilos en total. El número de
bloques y de hilos depende de las capacidades de _hardware_ de la GPU.

El código del _kernel_ se ejecuta en cada hilo de cada bloque configurado cuando se
lanza el _kernel_. Un _kernel_ con un solo bloque utilizará únicamente un
multiprocesador de la GPU. La función `cudaDeviceSynchronize()` asegura que la GPU
complete su tarea antes de que la CPU finalice el programa, funcionando como herramienta
de sincronización entre CPU y GPU.

???+ example "Control del orden de ejecución entre CPU y GPU"

    La posición de `cudaDeviceSynchronize()` determina el orden en que se completan las
    operaciones. En el siguiente ejemplo, la GPU ejecuta primero y la CPU después:

    ```c linenums="1"
    #include <stdio.h>

    void helloCPU(void)
    {
        printf("Hola desde la CPU.\n");
    }

    __global__ void helloGPU(void)
    {
        printf("Hola desde la GPU.\n");
    }

    int main(void)
    {
        helloGPU<<<1, 1>>>();
        cudaDeviceSynchronize();

        helloCPU();

        return 0;
    }
    ```

CUDA permite agilizar los bucles en la programación. Por ejemplo, para incrementar un
valor `b` a los `N` elementos de un vector en la CPU:

```c linenums="1"
#include <stdlib.h>

#define N (1 << 20)

void incremento_en_cpu(float *a, float b, int n)
{
    for (int idx = 0; idx < n; idx++)
    {
        a[idx] = a[idx] + b;
    }
}

int main(void)
{
    float *a = (float *)malloc(N * sizeof(float));
    float b = 2.0f;

    incremento_en_cpu(a, b, N);
    free(a);

    return 0;
}
```

Este bucle es adecuado para la paralelización, ya que cada índice es independiente y no
requiere un orden específico de ejecución (las hebras en un _warp_ se ejecutan de forma
desordenada).

## Identificación de hilos, bloques y mallas

CUDA proporciona variables integradas que describen los hilos, bloques y mallas
(_grid_):

| Variable      | Definición                                            |
| ------------- | ----------------------------------------------------- |
| `gridDim.x`   | Número total de bloques en la malla.                  |
| `blockIdx.x`  | Índice del bloque actual dentro de la malla.          |
| `blockDim.x`  | Número de hilos en un bloque dentro del _kernel_.     |
| `threadIdx.x` | Índice de un hilo dentro de un bloque en el _kernel_. |

Los bloques de un mismo _kernel_ no pueden comunicarse entre sí durante su ejecución, ya
que pueden ejecutarse en cualquier orden y de forma independiente. El _kernel_ debe
realizar el trabajo de una sola iteración del bucle, por lo que la configuración del
_kernel_ debe ajustarse al número de iteraciones, configurando adecuadamente tanto el
número de bloques como el número de hilos por bloque. A continuación se presenta el
código paralelizado del bucle anterior:

```c linenums="1"
#include <math.h>

#define N (1 << 20)

__global__ void incremento_en_gpu(float *a, float b, int n)
{
    int idx = blockIdx.x * blockDim.x + threadIdx.x;

    if (idx < n)
    {
        a[idx] = a[idx] + b;
    }
}

int main(void)
{
    float *a;
    float b = 2.0f;
    int blocksize = 256;

    cudaMallocManaged(&a, N * sizeof(float));

    // Configuración de la malla a partir del número de datos y del tamaño de bloque
    dim3 dimBlock(blocksize);
    dim3 dimGrid(ceil(N / (float)blocksize));

    incremento_en_gpu<<<dimGrid, dimBlock>>>(a, b, N);
    cudaDeviceSynchronize();
    cudaFree(a);

    return 0;
}
```

Cada hilo realiza una iteración del bucle. La fórmula que asocia cada hilo a un índice
del bucle es la siguiente:

$$i_{x} = (\text{blockIdx.x} \cdot \text{blockDim.x}) + \text{threadIdx.x}$$

En esta expresión, $i_{x}$ representa el índice global del hilo dentro de la malla,
`blockIdx.x` identifica el bloque al que pertenece el hilo, `blockDim.x` indica cuántos
hilos contiene cada bloque y `threadIdx.x` señala la posición del hilo dentro de su
bloque.

<figure markdown="span">
  ![Indexación de hilos en CUDA](../../assets/img/docs/cuda/cuda-c-thread-indexing.png)
  <figcaption>Mapeo de cada hilo a un índice del bucle en CUDA.</figcaption>
</figure>

!!! tip "Tamaño mínimo de bloque"

    Es importante que `blockDim.x` sea mayor o igual a 32, que es el tamaño del _warp_.
    En casos donde el número de hilos excede el número de tareas, se debe asegurar que el
    índice obtenido $i_{x}$ sea menor que el número total de datos.

<figure markdown="span">
  ![Comprobación de límites de índice en CUDA](../../assets/img/docs/cuda/cuda-c-bounds-checking.png)
  <figcaption>Comprobación de límites cuando el número de hilos supera al de tareas.</figcaption>
</figure>

## Asignación de memoria

La asignación y liberación de memoria se realiza de forma diferente en la CPU y en la
GPU. En la CPU se utilizan las funciones `malloc()` y `free()`:

```c linenums="1"
#include <stdlib.h>

void reserva_en_cpu(void)
{
    int N = 2 << 20;
    size_t size = N * sizeof(int);

    int *a = (int *)malloc(size);

    free(a);
}
```

En la GPU se emplean `cudaMallocManaged()` y `cudaFree()`, que reservan y liberan
memoria unificada accesible desde ambos dispositivos:

```c linenums="1"
void reserva_en_gpu(void)
{
    int N = 2 << 20;
    size_t size = N * sizeof(int);

    int *a;
    cudaMallocManaged(&a, size);

    cudaFree(a);
}
```

Gracias a los avances en _hardware_, se ha logrado mejorar la tasa de transferencia
entre la CPU y la GPU. Las versiones recientes de CUDA permiten el uso de **memoria
unificada**, que facilita el intercambio de datos entre ambos componentes.

<figure markdown="span">
  ![Memoria unificada en CUDA](../../assets/img/docs/cuda/cuda-c-unified-memory.png)
  <figcaption>Memoria unificada compartida entre la CPU y la GPU.</figcaption>
</figure>

La memoria unificada ofrece varias ventajas: proporciona un único puntero a los datos
accesible tanto desde la CPU como desde la GPU, elimina la necesidad de usar
`cudaMemcpy()`, facilita la portabilidad del código y mejora el rendimiento en la
transferencia de datos asegurando la coherencia global. También permite la optimización
manual con `cudaMemcpyAsync()`.

Los tipos de memoria en CUDA se pueden observar en la siguiente imagen:

<figure markdown="span">
  ![Tipos de memoria en CUDA](../../assets/img/docs/cuda/cuda-c-memory-types.png)
  <figcaption>Tipos de memoria disponibles en CUDA.</figcaption>
</figure>

!!! warning "Consideraciones de la memoria unificada"

    La capacidad máxima está limitada por la menor cantidad de memoria disponible entre
    las GPUs. La memoria unificada utilizada por la CPU debe migrar de nuevo a la GPU
    antes de lanzar un _kernel_. La CPU no puede acceder a la memoria unificada mientras
    la GPU ejecuta un _kernel_ (se debe llamar a `cudaDeviceSynchronize()` previamente).
    Además, la GPU tiene acceso exclusivo a la memoria unificada mientras ejecuta un
    _kernel_, incluso si este no la utiliza directamente.

<figure markdown="span">
  ![Jerarquía de memoria en CUDA](../../assets/img/docs/cuda/cuda-c-memory-hierarchy.png)
  <figcaption>Jerarquía de memoria en CUDA.</figcaption>
</figure>

### Ejemplos de uso de memoria unificada

???+ danger "Uso incorrecto de memoria unificada"

    En este ejemplo, la CPU accede a una variable mientras la GPU puede estar
    ejecutándose:

    ```c linenums="1"
    __device__ __managed__ int x, y = 2;

    __global__ void mykernel()
    {
        x = 10;
    }

    int main(void)
    {
        mykernel<<<1, 1>>>();

        // ERROR: la CPU accede a la variable 'y' mientras la GPU puede estar
        // utilizando la memoria unificada
        y = 20;

        return 0;
    }
    ```

???+ example "Uso correcto de memoria unificada"

    La versión correcta incluye la sincronización antes de que la CPU acceda a la
    variable:

    ```c linenums="1"
    __device__ __managed__ int x, y = 2;

    __global__ void mykernel()
    {
        x = 10;
    }

    int main(void)
    {
        mykernel<<<1, 1>>>();

        // Sincronización antes de que la CPU acceda a la memoria unificada
        cudaDeviceSynchronize();

        y = 20;

        return 0;
    }
    ```

## _Kernels_ con gran volumen de datos

Cuando la cantidad de datos excede el número máximo de hebras disponibles, es necesario
dividir el trabajo en porciones que se ajusten al número de hebras lanzadas. Tras
procesar una porción, cada hilo avanza a la siguiente aplicando un desplazamiento igual
al número total de hilos de la malla, es decir,
$\text{blockDim.x} \cdot \text{gridDim.x}$. Este patrón se conoce como _grid stride
loop_:

```c linenums="1"
__global__ void kernel(int *a, int N)
{
    int indexWithinTheGrid = (blockIdx.x * blockDim.x) + threadIdx.x;
    int gridStride = blockDim.x * gridDim.x;

    for (int i = indexWithinTheGrid; i < N; i += gridStride)
    {
        // Código para procesar el elemento situado en la posición i
        a[i] = a[i] * 2;
    }
}
```

## Manejo de errores

Las funciones de CUDA devuelven un valor de tipo `cudaError_t` que indica si se ha
producido un error. A continuación se muestra cómo gestionar errores al reservar
memoria:

```c linenums="1"
#include <stdio.h>

void reserva_con_control_de_errores(int *a, size_t size)
{
    cudaError_t err = cudaMallocManaged(&a, size);

    if (err != cudaSuccess)
    {
        printf("Error: %s\n", cudaGetErrorString(err));
    }
}
```

Para la gestión de errores al lanzar un _kernel_, se utiliza `cudaGetLastError()`, que
devuelve el último error registrado por el _runtime_:

```c linenums="1"
#include <stdio.h>

void lanza_kernel_con_control_de_errores(void)
{
    // El valor -1 no es válido para el número de hebras por bloque
    someKernel<<<1, -1>>>();

    cudaError_t err = cudaGetLastError();

    if (err != cudaSuccess)
    {
        printf("Error: %s\n", cudaGetErrorString(err));
    }
}
```

???+ tip "Función auxiliar para verificar errores"

    Se puede emplear una función auxiliar para verificar errores de forma centralizada,
    envolviendo con ella cada llamada a la API de CUDA:

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

    int main(void)
    {
        int *a;
        size_t size = 1024 * sizeof(int);

        checkCuda(cudaMallocManaged(&a, size));
        checkCuda(cudaDeviceSynchronize());
        checkCuda(cudaFree(a));

        return 0;
    }
    ```

## Patrones comunes de _kernels_

<figure markdown="span">
  ![Patrones comunes de kernels en CUDA](../../assets/img/docs/cuda/cuda-c-kernel-patterns.png)
  <figcaption>Patrones comunes de kernels en CUDA.</figcaption>
</figure>

Antes de explorar los distintos patrones, conviene definir el concepto de **bucle
_forall_**, que designa un bucle `for` sin dependencias entre iteraciones, de modo que
el resultado no varía en función del orden ni del índice de inicio. Sobre esta base se
construyen los patrones descritos a continuación.

### Operadores _streaming_

Representan la forma más simple de un bucle _forall_. CUDA puede utilizar todos los
hilos necesarios para procesar cada elemento de manera independiente, como ocurre al
calcular la luminancia de una imagen a partir de sus tres canales de color:

```c linenums="1"
#define N (1920 * 1080)

float r[N], g[N], b[N], luminancia[N];

void calcula_luminancia(void)
{
    for (int i = 0; i < N; i++)
    {
        luminancia[i] = 255 * (0.2999 * r[i] + 0.587 * g[i] + 0.114 * b[i]);
    }
}
```

### Operadores sobre vectores

Cada iteración del bucle puede asignarse a un hilo CUDA distinto, lo que maximiza el
paralelismo y la escalabilidad al no existir comunicación entre iteraciones:

```c linenums="1"
#define N (1 << 30)

float a[N], b[N], c[N];

void suma_vectores(void)
{
    for (int i = 0; i < N; i++)
    {
        c[i] = a[i] + b[i];
    }
}
```

### Operadores patrón

Los operadores patrón (_stencil operators_) calculan cada elemento a partir de sus
vecinos. Las iteraciones externas deben serializarse debido a las dependencias entre
pasos temporales, pero el cálculo de cada elemento dentro de un mismo paso sí puede
paralelizarse. La carga computacional depende del número de iteraciones:

```c linenums="1"
#define N 1024
#define NITERS 100

float in[N][N], out[N][N];

void aplica_stencil(void)
{
    for (int iter = 0; iter < NITERS; iter++)
    {
        for (int i = 1; i < N - 1; i++)
        {
            for (int j = 1; j < N - 1; j++)
            {
                out[i][j] = 0.2 * (in[i][j] + in[i - 1][j] + in[i + 1][j] +
                                   in[i][j - 1] + in[i][j + 1]);
            }
        }

        for (int i = 1; i < N - 1; i++)
        {
            for (int j = 1; j < N - 1; j++)
            {
                in[i][j] = out[i][j];
            }
        }
    }
}
```

El grado de paralelismo en este caso está determinado por el tamaño de la matriz
bidimensional, es decir, $N^2$.

### Operadores de reducción

Aunque el código presenta dependencias entre iteraciones, el paralelismo puede
desplegarse mediante una estructura en árbol binario, lo que da lugar a $\log(N)$ pasos
en los que el grado de paralelismo se reduce progresivamente hasta llegar a un solo
hilo. Resulta fundamental emplear un patrón de acceso a memoria que aproveche la
jerarquía de memoria de la GPU:

```c linenums="1"
#define N (1 << 20)

float x[N];

float reduce_suma(void)
{
    float sum = 0;

    for (int i = 0; i < N; i++)
    {
        sum += x[i];
    }

    return sum;
}
```

### Histogramas

Los histogramas constituyen un patrón donde los bucles presentan dependencias en la
escritura, ya que varios hilos pueden incrementar la misma posición del histograma. Las
lecturas, en cambio, pueden realizarse en paralelo si se asignan a hilos CUDA distintos.
Para gestionar los accesos concurrentes y prevenir condiciones de carrera, CUDA
proporciona operaciones atómicas como `atomicInc(histo[image[i][j]])`:

```c linenums="1"
#define N 1024
#define NBINS 256

int histo[NBINS], image[N][N];

void calcula_histograma(void)
{
    for (int i = 0; i < NBINS; i++)
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
}
```

Como análisis final, el operador _streaming_ es el más eficiente en GPU, el operador
patrón aprovecha mejor la memoria compartida, el operador de reducción requiere una
mayor intervención del programador y el histograma es el más desafiante de implementar.

## Multiplicación de matrices 2D

Un caso de uso habitual en CUDA es la multiplicación de matrices, donde se aprovecha la
malla bidimensional de hilos para mapear cada elemento de la matriz resultado a un hilo
independiente.

<figure markdown="span">
  ![Multiplicación de matrices en CUDA](../../assets/img/docs/cuda/cuda-matrix.jpg)
  <figcaption>Multiplicación de matrices sobre una malla bidimensional de hilos.</figcaption>
</figure>

La clave consiste en calcular los índices de fila y columna a partir de las coordenadas
del hilo en la malla 2D. Cada hilo calcula un único elemento de la matriz resultado
acumulando el producto escalar de la fila correspondiente de la primera matriz con la
columna correspondiente de la segunda:

```c linenums="1"
#include <stdio.h>

#define N 64

__global__ void matrixMulGPU(int *a, int *b, int *c)
{
    int val = 0;

    int fila = (blockDim.x * blockIdx.x) + threadIdx.x;
    int col = (blockDim.y * blockIdx.y) + threadIdx.y;

    if (fila < N && col < N)
    {
        for (int k = 0; k < N; ++k)
        {
            val += a[fila * N + k] * b[k * N + col];
        }

        c[fila * N + col] = val;
    }
}

int main(void)
{
    int *a, *b, *c;
    size_t size = N * N * sizeof(int);

    cudaMallocManaged(&a, size);
    cudaMallocManaged(&b, size);
    cudaMallocManaged(&c, size);

    // Inicializar matrices
    for (int fila = 0; fila < N; ++fila)
    {
        for (int col = 0; col < N; ++col)
        {
            a[fila * N + col] = fila;
            b[fila * N + col] = col + 2;
            c[fila * N + col] = 0;
        }
    }

    // Configuración 2D: N/2 hilos por dimensión en cada bloque, 2 bloques por dimensión
    dim3 hilos_por_bloque(N / 2, N / 2, 1);
    dim3 numero_de_bloques(2, 2, 1);

    matrixMulGPU<<<numero_de_bloques, hilos_por_bloque>>>(a, b, c);
    cudaDeviceSynchronize();

    cudaFree(a);
    cudaFree(b);
    cudaFree(c);

    return 0;
}
```

!!! tip "Distribución de hilos en bloques multidimensionales"

    Al utilizar bloques multidimensionales, el producto de todas las dimensiones no debe
    superar el máximo de hilos por bloque (típicamente 1024). Por ejemplo,
    `dim3(32, 32, 1)` es válido (1024 hilos), pero `dim3(256, 3, 2)` no lo es (1536
    hilos).

## Precarga de memoria

La función `cudaMemPrefetchAsync()` permite migrar datos a la memoria de la GPU (o de
vuelta a la CPU) de forma anticipada, reduciendo las transferencias bajo demanda (_page
faults_) y mejorando el rendimiento del _kernel_:

```c linenums="1"
void procesa_con_precarga(float *datos, size_t size, int N, int bloques, int hilos)
{
    int deviceId;
    cudaGetDevice(&deviceId);

    // Precarga de datos hacia la GPU antes de lanzar el kernel
    cudaMemPrefetchAsync(datos, size, deviceId);

    mi_kernel<<<bloques, hilos>>>(datos, N);
    cudaDeviceSynchronize();

    // Precarga de resultados hacia la CPU antes de acceder desde el host
    cudaMemPrefetchAsync(datos, size, cudaCpuDeviceId);
}
```

Al utilizar precarga de memoria se obtienen menos transferencias pero con mayor volumen
de datos por transferencia, lo que resulta en una reducción significativa del tiempo de
ejecución del _kernel_.

## Perfilado de aplicaciones

El perfilador `nsys` (_NVIDIA Nsight Systems_) permite analizar el rendimiento de las
aplicaciones CUDA. Se ejecuta con el siguiente comando:

```bash linenums="1"
nsys profile --stats=true ./nombre_del_ejecutable
```

Entre la información proporcionada se encuentra el tiempo medio de ejecución del
_kernel_, lo que resulta útil para evaluar diferentes configuraciones de bloques y
hebras y determinar la distribución óptima para un problema concreto.

!!! tip "Optimización de la configuración de ejecución"

    Para datos de tamaño $2^{25}$, se pueden utilizar como máximo 1024 hebras por bloque,
    lo que requiere $2^{25} / 1024 = 32768$ bloques para cubrir todos los elementos. La
    combinación de `cudaDeviceProp` para consultar los SMs disponibles junto con el
    perfilado con `nsys` permite encontrar la configuración óptima de forma empírica.
