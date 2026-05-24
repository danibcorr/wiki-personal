---
authors: Daniel Bazo Correa
description: Fundamentos matemáticos del aprendizaje profundo.
title: Fundamentos matemáticos
---

## Fundamentos matemáticos

### Tensores como estructura fundamental

En el ámbito del aprendizaje profundo, los **tensores** constituyen la estructura de
datos esencial sobre la cual se construye y ejecuta la totalidad del proceso de cómputo.
Un tensor puede definirse formalmente como una colección ordenada de elementos numéricos
organizados en un espacio de $N$ dimensiones, que permite representar, almacenar y
manipular información de manera eficiente dentro de un modelo de red neuronal.

Su principal ventaja radica en su compatibilidad con sistemas de cómputo masivamente
paralelos, como las unidades de procesamiento gráfico (GPU) o las unidades de
procesamiento tensorial (TPU). Estas arquitecturas están diseñadas para ejecutar de
forma simultánea miles de operaciones matemáticas, lo cual resulta indispensable para el
entrenamiento y la inferencia en redes neuronales de gran escala, donde la eficiencia
computacional y el manejo óptimo de los recursos son factores determinantes.

Cada tensor se describe a partir de dos componentes fundamentales: el tipo de datos que
contiene y la precisión numérica empleada en los cálculos. Los valores almacenados
suelen ser numéricos, representados comúnmente como enteros o números en coma flotante.
En la práctica, los modelos de aprendizaje profundo suelen utilizar tensores de 32 bits
(precisión simple), aunque es frecuente aplicar técnicas de **cuantización** que reducen
la precisión a 16, 8 o incluso 4 bits, especialmente una vez completada la fase de
entrenamiento. Estas reducciones, sin embargo, dependen de las capacidades del hardware,
ya que no todas las arquitecturas soportan operaciones de baja precisión con la misma
eficiencia o estabilidad numérica.

Bibliotecas especializadas como **PyTorch**, **TensorFlow** o **Keras** facilitan estos
procesos mediante instrucciones de alto nivel. La elección del nivel de precisión
implica un compromiso entre exactitud y eficiencia. En aplicaciones donde los errores
mínimos son tolerables, como la clasificación de imágenes comunes, puede optarse por una
menor precisión para reducir el consumo energético y acelerar el entrenamiento. En
cambio, en entornos donde la seguridad y la fiabilidad son críticas, se requiere una
precisión numérica más alta que garantice la estabilidad y exactitud de los resultados.
Por tanto, existe una relación directa entre la precisión numérica, el error acumulado y
el coste computacional, de modo que optimizar este equilibrio constituye uno de los
aspectos clave del diseño de modelos eficientes. El uso de **precisión mixta**, que
combina tipos de punto flotante de 16 y 32 bits durante el entrenamiento, permite
acelerar la ejecución y reducir el consumo de memoria manteniendo la estabilidad
numérica en las operaciones críticas.

Desde el punto de vista operativo, los tensores funcionan de manera análoga a los
**_arrays_** de los lenguajes de programación tradicionales, permitiendo realizar
operaciones como indexación, segmentación o extracción de subconjuntos de datos. Estas
operaciones son esenciales, ya que posibilitan el procesamiento de partes específicas de
un conjunto de información sin necesidad de manipular el tensor completo.

La dimensionalidad es una de las características más importantes de los tensores, pues
determina la forma en que los datos se estructuran internamente. Según su número de
dimensiones, pueden clasificarse del siguiente modo:

- Un **escalar** corresponde a un tensor de dimensión cero y representa un único valor
  numérico.
- Un **vector** es un tensor unidimensional que almacena una secuencia ordenada de
  valores.
- Una **matriz** constituye un tensor bidimensional que organiza los datos en filas y
  columnas.
- Los **tensores de orden superior**, con tres o más dimensiones, permiten representar
  estructuras de datos más complejas, como secuencias temporales, imágenes, vídeos o
  volúmenes tridimensionales.

Un ejemplo ilustrativo lo constituye una imagen en color de 84 × 84 píxeles con tres
canales (rojo, verde y azul) procesada en lotes durante el entrenamiento. En este caso,
la representación corresponde a un tensor de rango 4, cuyas dimensiones reflejan: el
número de ejemplos en el lote, la altura y la anchura de la imagen, y el número de
canales de color.

En el ámbito del aprendizaje profundo, el tensor constituye la unidad de procesamiento
fundamental dentro de las bibliotecas de cálculo numérico. La mayoría de los modelos se
construyen mediante la composición de funciones elementales, tales como sumas,
multiplicaciones y transformaciones no lineales. Estas operaciones permiten representar
relaciones complejas entre los datos y, por tanto, son esenciales para el funcionamiento
de los modelos de inteligencia artificial.

Para ilustrar estos conceptos se emplea **PyTorch**, una biblioteca de código abierto
para _Deep Learning_ reconocida por su flexibilidad, su ecosistema de herramientas
complementarias y su amplia adopción tanto en el ámbito académico como en el industrial.
PyTorch permite definir, entrenar y desplegar modelos de redes neuronales de manera
eficiente, ofreciendo una interfaz altamente integrada con el lenguaje de programación
Python, lo que la hace especialmente accesible para investigadores y desarrolladores.

Aunque existen otras alternativas consolidadas, como **TensorFlow**, **JAX** y
**Keras**, PyTorch destaca por su creciente popularidad y por su estrecha vinculación
con la Linux Foundation, lo que garantiza un desarrollo sostenido y un soporte
comunitario cada vez mayor. Además, múltiples proyectos de terceros, como **Ray**,
utilizado para la creación de sistemas distribuidos de entrenamiento de modelos, también
forman parte del ecosistema de la Linux Foundation. Este entorno colaborativo impulsa la
innovación y asegura un soporte activo tanto por parte de empresas tecnológicas
reconocidas como de la comunidad de código abierto.

Una de las principales ventajas de PyTorch es su sintaxis intuitiva y expresiva, que
sigue de forma natural los principios del estilo "**pythónico**", es decir, un diseño
limpio y legible que favorece la comprensión del código.

Independientemente de la biblioteca elegida, los principios matemáticos y conceptuales
que sustentan el aprendizaje profundo son los mismos. Las diferencias radican
principalmente en la sintaxis y en las implementaciones específicas de cada entorno,
pero la base teórica y las operaciones fundamentales definidas sobre tensores permanecen
invariantes.

### Operaciones vectoriales

Los vectores constituyen tensores unidimensionales, habitualmente representados como
$x \sim (d)$, donde $d$ indica la dimensión del tensor. En el contexto del álgebra
lineal, y también en el ámbito de la inteligencia artificial, resulta fundamental
distinguir entre vectores columna y vectores fila, denotados respectivamente por $x$ y
$x^\top$. En esta notación, el superíndice del segundo símbolo representa la
**transpuesta** del vector, operación que intercambia filas por columnas. Un vector
columna puede considerarse como un tensor bidimensional de forma $(d, 1)$, mientras que
un vector fila posee forma $(1, d)$.

Esta distinción es particularmente relevante en entornos de programación, donde las
operaciones entre tensores deben cumplir las reglas de **_broadcasting_**, las cuales
determinan cómo se alinean las dimensiones durante las operaciones aritméticas. En
PyTorch, cuando las dimensiones de los tensores son incompatibles, puede ser necesario
utilizar funciones como `squeeze()`, `unsqueeze()` o `view()` para ajustar su
estructura. Dado que la biblioteca se actualiza con frecuencia, se recomienda consultar
la documentación oficial para obtener información actualizada sobre las funciones
disponibles.

Si se disponen dos vectores del mismo tamaño, $x$ y $y$, es posible combinarlos
linealmente mediante coeficientes escalares $a$ y $b$, generando un nuevo vector $z$,
tal que:

$$
z = a x + b y.
$$

Desde una perspectiva geométrica, en un espacio euclidiano bidimensional, la suma de
vectores puede interpretarse como la **diagonal del paralelogramo** definido por ambos
vectores. La magnitud o longitud de un vector se mide mediante la **norma euclidiana** o
**norma $L_2$**, definida como:

$$
||x|| = \sqrt{\sum_i x_i^2}.
$$

Esta norma representa la distancia del vector al origen del sistema de coordenadas y
constituye una medida fundamental en la evaluación de magnitudes y distancias.

Otra operación esencial es el **producto escalar** (o **producto punto**), definido
como:

$$
x \cdot y = \sum_i x_i \cdot y_i,
$$

cuyo resultado es un escalar con una interpretación geométrica directa: permite
determinar el **ángulo entre dos vectores** y, en consecuencia, su **similitud
direccional**. Esta relación se expresa mediante la siguiente ecuación:

$$
\cos(\theta) = \frac{x \cdot y}{||x|| \, ||y||}.
$$

De acuerdo con este principio:

- Si $\cos(\theta) = 1$, los vectores apuntan en la misma dirección.
- Si $\cos(\theta) = 0$, los vectores son ortogonales, es decir, forman un ángulo de 90
  grados entre sí.
- Si $\cos(\theta) = -1$, los vectores son opuestos, con un ángulo de 180 grados entre
  ambos.

Esta medida se conoce como **similitud del coseno** y desempeña un papel fundamental en
tareas de **agrupamiento (_clustering_)**, búsqueda semántica y **representaciones
latentes**.

Este principio tiene una aplicación directa en los **_word embeddings_**,
representaciones vectoriales del lenguaje en las que cada palabra se codifica como un
punto dentro de un espacio semántico de alta dimensionalidad. Modelos como GPT-2 y GPT-3
utilizan representaciones de entre 768 y más de 12000 dimensiones, lo que permite
capturar relaciones semánticas y sintácticas a través de simples operaciones
vectoriales.

A continuación, se presenta un ejemplo de implementación de la similitud del coseno
utilizando Python con la biblioteca **NumPy**:

```py linenums="1"
import numpy as np

def normalizar_matriz(matriz: np.ndarray) -> np.ndarray:
    return matriz / np.expand_dims(np.sqrt(np.sum(np.power(matriz, 2), axis=1)), axis=-1)

def cosine_similarity(matriz: np.ndarray) -> np.ndarray:
    return matriz @ matriz.T

X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [1, 0, 0],
    [0, 1, 0]
], dtype=float)

X_normalized = normalizar_matriz(X)
similarity_matrix = cosine_similarity(X_normalized)
print(similarity_matrix)
```

El siguiente código muestra el mismo procedimiento utilizando **PyTorch**:

```py linenums="1"
import torch
import torch.nn.functional as F

X = torch.tensor([
    [1., 2., 3.],
    [4., 5., 6.],
    [1., 0., 0.],
    [0., 1., 0.]
])

# Normalización
X_norm = F.normalize(X, p=2, dim=1)

# Cálculo de la matriz de similitud
similarity = X_norm @ X_norm.T
print(similarity)
```

El resultado obtenido en ambos casos es una matriz de tamaño $N \times N$ que contiene
los valores de similitud entre cada par de vectores. En la diagonal principal aparecen
valores iguales a 1, ya que cada vector presenta similitud máxima consigo mismo.

### Operaciones matriciales

Una matriz es un arreglo bidimensional que organiza los datos en filas y columnas, por
lo que puede entenderse como una **colección ordenada de vectores**. Matemáticamente,
una matriz $X \in \mathbb{R}^{A \times B}$ está compuesta por $A$ filas y $B$ columnas,
donde cada elemento $x_{ij}$ representa el valor ubicado en la fila $i$ y la columna
$j$.

Si se dispone de una matriz $X \in \mathbb{R}^{A \times B}$ y otra
$Y \in \mathbb{R}^{B \times C}$, su **producto matricial** se define como:

$$
Z = X Y,
$$

donde $Z \in \mathbb{R}^{A \times C}$. Esta operación es válida únicamente cuando el
número de columnas de $X$ coincide con el número de filas de $Y$. En términos
algebraicos, cada elemento de la matriz resultante se calcula como:

$$
Z_{ij} = \sum_{k=1}^{B} X_{ik} \cdot Y_{kj}.
$$

El producto matricial es una de las operaciones más utilizadas en el aprendizaje
profundo, ya que permite procesar simultáneamente grandes volúmenes de información. En
el contexto de una capa neuronal, los datos de entrada suelen representarse mediante una
matriz donde cada fila corresponde a una muestra y cada columna a una característica. Al
multiplicar esta matriz por otra que contiene los pesos del modelo, se obtiene una
transformación lineal de las entradas, a la cual se suma posteriormente un vector de
sesgo.

Además del producto matricial convencional, existen otras operaciones de gran relevancia
en el cálculo numérico y el aprendizaje profundo. Una de ellas es el **producto de
Hadamard**, también conocido como multiplicación elemento a elemento. A diferencia del
producto matricial, esta operación se realiza exclusivamente entre matrices del mismo
tamaño y se define como:

$$
Z_{ij} = X_{ij} \cdot Y_{ij}.
$$

El producto de Hadamard se emplea en múltiples contextos, entre los cuales destaca su
uso en **mecanismos de enmascaramiento** (_masking_) durante el entrenamiento de
modelos. Esta técnica permite ignorar valores específicos de un tensor para impedir que
influyan en el cálculo de los gradientes o en la propagación de errores. Dicha propiedad
es esencial en arquitecturas modernas como **_Transformers_**, donde se aplica para
restringir la atención a determinadas posiciones o para manejar secuencias de longitud
variable sin afectar el aprendizaje global del modelo.

### Operaciones con tensores en PyTorch

La biblioteca PyTorch proporciona un conjunto amplio, eficiente y flexible de
herramientas para la creación, manipulación y transformación de tensores, que
constituyen la estructura de datos fundamental en el aprendizaje profundo. Los tensores
generalizan los conceptos de escalares, vectores y matrices hacia dimensiones
superiores, lo que permite representar datos complejos de manera multidimensional y
realizar operaciones matemáticas de forma vectorizada y optimizada.

A continuación, se presentan ejemplos prácticos y comentados que ilustran las
operaciones más comunes con tensores en PyTorch. Estas operaciones son esenciales para
comprender el funcionamiento interno del código empleado en la creación de modelos de
aprendizaje profundo. En la práctica, muchas arquitecturas modernas o modificaciones de
arquitecturas existentes surgen a partir de pequeñas variaciones en la manipulación de
tensores, ya sea mediante la selección de elementos específicos (_slicing_), la
optimización de cálculos o el uso de estrategias que reduzcan el coste computacional.

Para crear tensores, es posible hacerlo a partir de listas, mediante inicialización
aleatoria o con valores fijos:

```py linenums="1"
import torch

# Tensores básicos
escalar = torch.tensor(7)
vector = torch.tensor([1, 2, 3])
matriz = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Tensores aleatorios y de valores fijos
tensor_aleatorio = torch.rand((2, 3))
ceros = torch.zeros((2, 3))
unos = torch.ones((2, 3))
rango = torch.arange(0, 10, 2)

print("Escalar:", escalar)
print("Vector:", vector)
print("Matriz:\n", matriz)
print("Tensor aleatorio:\n", tensor_aleatorio)
print("Tensor de ceros:\n", ceros)
print("Tensor de unos:\n", unos)
print("Rango:", rango)
```

Cada tensor contiene información sobre su **tipo de dato**, sus **dimensiones** y el
**dispositivo de almacenamiento** (CPU o GPU). El tipo de dato (`dtype`) determina la
precisión numérica del tensor; a mayor precisión, mayor será el rango de valores
posibles, pero también el consumo de memoria. El dispositivo (`device`) es relevante
porque un tensor ubicado en la GPU no puede ser manipulado directamente desde la CPU,
por lo que es necesario transferirlo o copiarlo según sea necesario:

```py linenums="1"
tensor = torch.rand((2, 3, 4))
print("Tipo de dato:", tensor.dtype)
print("Forma:", tensor.shape)
print("Dispositivo:", tensor.device)
print("Número de elementos:", tensor.numel())
```

Las operaciones de agregación permiten resumir la información contenida en un tensor.
Algunas de las más comunes son la suma, la media o la obtención del valor máximo o
mínimo. El parámetro `dim` indica el eje sobre el cual se aplica la operación, donde
`dim=0` actúa sobre las filas (por columnas), mientras que `dim=1` actúa sobre las
columnas (por filas):

```py linenums="1"
tensor = torch.tensor([[1., 2., 3.], [4., 5., 6.]])

print("Suma total:", tensor.sum())
print("Promedio:", tensor.mean())
print("Máximo por columna:", tensor.max(dim=0))
print("Promedio por fila:", tensor.mean(dim=1))
```

Otras funciones, como `view()`, `reshape()`, `unsqueeze()` y `squeeze()`, permiten
modificar la forma del tensor sin alterar sus datos subyacentes. Estas operaciones son
fundamentales para adaptar las dimensiones de los tensores según las necesidades de las
redes neuronales:

```py linenums="1"
x = torch.arange(1, 7)
print("Tensor original:", x)

# Cambiar forma
x_reshaped = x.view(2, 3)
print("Tensor 2x3:\n", x_reshaped)

# Añadir dimensión
x_unsqueezed = x.unsqueeze(0)
print("Tensor con nueva dimensión:", x_unsqueezed.shape)

# Eliminar dimensión
x_squeezed = x_unsqueezed.squeeze()
print("Tensor tras eliminar dimensión:", x_squeezed.shape)
```

Las funciones `permute()` y `transpose()` permiten reordenar las dimensiones de un
tensor, lo cual es especialmente útil en el procesamiento de imágenes o secuencias, por
ejemplo, al desplazar canales de color o mapas de características:

```py linenums="1"
tensor = torch.rand((2, 3, 4))
print("Forma original:", tensor.shape)

# Transposición (intercambio de dos dimensiones)
tensor_T = tensor.transpose(1, 2)
print("Forma tras transpose:", tensor_T.shape)

# Permutación general de ejes
tensor_P = tensor.permute(2, 0, 1)
print("Forma tras permute:", tensor_P.shape)
```

También es posible combinar tensores mediante funciones como `torch.cat()` y
`torch.stack()`. La primera une tensores existentes a lo largo de un eje específico,
mientras que la segunda crea una nueva dimensión para apilarlos:

```py linenums="1"
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])

# Concatenación (mismo número de filas)
cat_0 = torch.cat((a, b), dim=0)
cat_1 = torch.cat((a, b), dim=1)

# Apilamiento (nueva dimensión)
stacked = torch.stack((a, b), dim=0)

print("Concatenación por filas:\n", cat_0)
print("Concatenación por columnas:\n", cat_1)
print("Apilamiento (nueva dimensión):\n", stacked)
```

PyTorch implementa una gran cantidad de **operaciones vectorizadas**, que permiten
realizar cálculos sin recurrir a bucles explícitos. Este enfoque no solo mejora la
legibilidad del código, sino que también aprovecha las optimizaciones internas del
framework y del hardware subyacente, como las implementaciones en CUDA para GPU:

```py linenums="1"
x = torch.tensor([1., 2., 3.])
y = torch.tensor([4., 5., 6.])

print("Suma:", x + y)
print("Producto elemento a elemento:", x * y)
print("Exponencial:", torch.exp(x))
print("Raíz cuadrada:", torch.sqrt(y))
print("Seno:", torch.sin(x))
```

Estas operaciones resultan especialmente útiles para inspeccionar distribuciones de
datos o normalizar tensores antes del entrenamiento, tareas que contribuyen a
estabilizar el aprendizaje de los modelos:

```py linenums="1"
tensor = torch.randn((3, 4))  # Distribución normal
print("Tensor aleatorio:\n", tensor)
print("Media:", tensor.mean())
print("Desviación estándar:", tensor.std())
print("Valor mínimo:", tensor.min())
print("Índice del máximo:", tensor.argmax())
```

Finalmente, PyTorch permite una **conversión directa entre tensores y arreglos de
NumPy**, lo que facilita su integración con bibliotecas de análisis y visualización.
Esta interoperabilidad permite combinar el poder de cálculo de PyTorch con la
versatilidad de ecosistemas como NumPy, Matplotlib o Pandas:

```py linenums="1"
import numpy as np

# Tensor a NumPy
tensor = torch.tensor([[1, 2], [3, 4]])
array = tensor.numpy()
print("Tensor a NumPy:\n", array)

# NumPy a Tensor
nuevo_tensor = torch.from_numpy(array)
print("NumPy a Tensor:\n", nuevo_tensor)
```

En conjunto, estas operaciones proporcionan una visión integral de las capacidades de
PyTorch en la manipulación de tensores, mostrando su versatilidad, eficiencia y
facilidad de integración con otros entornos de análisis. En capítulos posteriores, se
emplearán estos fundamentos para la construcción de modelos de aprendizaje profundo
basados en esta biblioteca.
