---
authors: Daniel Bazo Correa
description: Arquitectura y conceptos fundamentales de la plataforma CUDA de NVIDIA.
title: Fundamentos
---

<figure markdown="span">
  ![Logo de Nvidia CUDA](../../assets/img/docs/logos/cuda-logo.png)
  <figcaption>Logo de Nvidia CUDA</figcaption>
</figure>

**CUDA** (_Compute Unified Device Architecture_) es una plataforma de computación
paralela y una interfaz de programación de aplicaciones desarrollada por NVIDIA. Permite
el uso de unidades de procesamiento gráfico (_Graphics Processing Unit_, GPU) para
realizar cálculos complejos con mayor eficiencia. Su aplicación abarca áreas como la
inteligencia artificial, las simulaciones científicas y la renderización de gráficos,
donde la capacidad de procesamiento masivo en paralelo resulta determinante.

## Bibliografía

- NVIDIA. (s.f.). _NVIDIA Developer_. <https://www.nvidia.com/>
- NVIDIA y Universidad de Málaga. (s.f.). _Deep Learning Institute - UMA_.
  <http://nvidiadli.uma.es/index.php/es/certificaciones-nvidia>

## Arquitectura de la GPU

<figure markdown="span">
  ![Ecosistema de CUDA](../../assets/img/docs/cuda/cuda-fundamentals-ecosystem.png)
  <figcaption>Ecosistema de la plataforma CUDA.</figcaption>
</figure>

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

### Warps

<figure markdown="span">
  ![Organización de bloques de hilos en warps](../../assets/img/docs/cuda/cuda-fundamentals-warps.png)
  <figcaption>Organización de los bloques de hilos en <em>warps</em> dentro de la GPU. <a href="https://www.centron.de/en/tutorial/the-role-of-warps-in-parallel-processing-gpu-efficiency-explained/">Referencia</a></figcaption>
</figure>

El concepto clave en CUDA es el _warp_. En el nivel de _hardware_, un bloque de hilos se
divide en _warps_, que son grupos de 32 hilos que ejecutan instrucciones en paralelo.
Estos _warps_ permanecen en el multiprocesador hasta completar su ejecución. Un nuevo
bloque de hilos no se lanza hasta que se liberan suficientes registros y memoria
compartida para los _warps_ del nuevo bloque.

### Modelo CPU-GPU

Aunque CUDA ofrece ventajas significativas, resulta crucial equilibrar la carga de
trabajo entre la GPU y la CPU, un enfoque conocido como computación heterogénea.

La GPU se orienta al procesamiento intensivo en datos y paralelismo fino, mientras que
la CPU resulta más adecuada para operaciones con saltos y bifurcaciones, así como para
paralelismo grueso. Identificar qué partes del código se benefician de la paralelización
en la GPU y cuáles deben procesarse secuencialmente en la CPU es fundamental para
obtener el máximo rendimiento. Se observa, por tanto, que el paralelismo en el que CUDA
destaca es el **paralelismo de datos** (_data parallelism_).

<figure markdown="span">
  ![Comparación entre CPU y GPU](../../assets/img/docs/cuda/cuda-fundamentals-cpu-vs-gpu.jpeg)
  <figcaption>Comparación entre la arquitectura de una CPU y la de una GPU.</figcaption>
</figure>

### Jerarquía de memoria

Una GPU se compone de $N$ multiprocesadores, cada uno de los cuales contiene $M$
núcleos. La siguiente imagen muestra algunas de las familias de GPU de la serie Tesla de
NVIDIA.

<figure markdown="span">
  ![Familias de GPU de la serie Tesla de NVIDIA](../../assets/img/docs/cuda/cuda-fundamentals-gpu-families.png)
  <figcaption>Familias de GPU de la serie Tesla de NVIDIA.</figcaption>
</figure>

Cada multiprocesador dispone de su propio banco de registros, memoria compartida, una
caché de constantes y una caché de texturas (ambas de solo lectura). Además, la GPU
cuenta con una memoria global de tipo GDDR, que es aproximadamente tres veces más rápida
que la memoria principal de la CPU, aunque considerablemente más lenta que la memoria
compartida de tipo SRAM. Los bloques de hilos en CUDA pueden asignarse a cualquier
multiprocesador para su ejecución.

<figure markdown="span">
  ![Estructura interna de una GPU](../../assets/img/docs/cuda/cuda-fundamentals-gpu-architecture.png)
  <figcaption>Estructura interna de una GPU.</figcaption>
</figure>

A modo de ejemplo, la generación Volta, concretamente la GPU GV100, cuenta con 84
multiprocesadores (SMs) y 8 controladores de memoria de 512 bits. En la arquitectura
Volta, cada multiprocesador dispone de 64 núcleos para operaciones de tipo _int32_, 64
núcleos para _float32_, 32 núcleos para _float64_ y 8 unidades tensoriales.

<figure markdown="span">
  ![Multiprocesador de la arquitectura Volta](../../assets/img/docs/cuda/cuda-fundamentals-volta-sm.png)
  <figcaption>Multiprocesador (SM) de la arquitectura Volta (GPU GV100).</figcaption>
</figure>

De la imagen anterior se observa que el diseño de un bloque se utiliza como base para
crear diseños más complejos al replicarlo.

<figure markdown="span">
  ![Replicación de multiprocesadores en una GPU](../../assets/img/docs/cuda/cuda-fundamentals-sm-replication.png)
  <figcaption>Replicación de multiprocesadores a partir de un diseño de bloque base.</figcaption>
</figure>

### Núcleos tensoriales

En la última década, los núcleos tensoriales han adquirido un protagonismo notable. Son
la principal unidad de cómputo utilizada por bibliotecas de aprendizaje profundo. Estos
componentes están diseñados para realizar operaciones matriciales a alta velocidad, lo
que resulta crucial en el entrenamiento de modelos de inteligencia artificial y en
procesos que implican operaciones matriciales extensivas. El siguiente diagrama ilustra
el proceso de operación de cada núcleo tensorial por ciclo de reloj.

<figure markdown="span">
  ![Operación de un núcleo tensorial](../../assets/img/docs/cuda/cuda-fundamentals-tensor-core-operation.png)
  <figcaption>Operación de un núcleo tensorial por ciclo de reloj.</figcaption>
</figure>

### Precisión numérica

La precisión de los datos influye directamente en la tasa de transferencia
(_throughput_) del sistema. Reducir la precisión, por ejemplo de enteros de 32 bits a
enteros de 16 bits, permite realizar un mayor número de operaciones por unidad de
tiempo, aunque con una precisión menor en los resultados. Dependiendo de la aplicación,
esta reducción de precisión puede ser perfectamente aceptable.

<figure markdown="span">
  ![Throughput según la precisión numérica](../../assets/img/docs/cuda/cuda-fundamentals-precision-throughput.png)
  <figcaption>Throughput para diferentes precisiones numéricas en arquitecturas de GPU modernas.</figcaption>
</figure>
