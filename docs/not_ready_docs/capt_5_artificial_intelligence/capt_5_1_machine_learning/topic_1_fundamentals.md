---
authors: Daniel Bazo Correa
description: Fundamentos del Machine Learning.
title: Machine Learning
---

## Introducción

### Definición

<p align="center">
  <img src="https://www.techspot.com/articles-info/2048/images/2020-07-07-image.jpg"/>
  <br />
  <em>Ilustración sobre los conjuntos que engloba la inteligencia artificial. [Link](https://www.techspot.com/articles-info/2048/images/2020-07-07-image.jpg)</em>
</p>

El **aprendizaje automático** es una rama de la inteligencia artificial que se centra en
el desarrollo y uso de algoritmos, también denominados **modelos**, capaces de
identificar y comprender patrones en los datos de entrada con el objetivo de optimizar
una métrica establecida.

A diferencia de los enfoques tradicionales de programación, donde las reglas se definen
explícitamente, en el aprendizaje automático los algoritmos ajustan sus parámetros
automáticamente para mejorar su desempeño en función de los datos.

### Técnicas

<p align="center">
  <img src="https://www.sharpsightlabs.com/wp-content/uploads/2021/04/regression-vs-classification_simple-comparison-image_v3.png"/>
  <br />
  <em>Clasificación vs Regresión. [Link](https://www.sharpsightlabs.com/wp-content/uploads/2021/04/regression-vs-classification_simple-comparison-image_v3.png)</em>
</p>

Entre las técnicas más utilizadas se encuentran la **clasificación** y la **regresión**.
La clasificación permite asignar etiquetas o categorías a los datos en función de sus
características comunes. Un ejemplo de clasificación es la identificación del tipo de
planta a partir de atributos como el ancho y la altura de sus hojas. Por otro lado, la
regresión se emplea para realizar predicciones numéricas, como la estimación del precio
de una vivienda en función de sus características.

La elección de la técnica adecuada depende de la naturaleza del problema. Un enfoque
común consiste en evaluar múltiples algoritmos viables y compararlos para determinar cuál
ofrece el mejor rendimiento. Esta comparación se basa en métricas de desempeño obtenidas
a partir de los datos.

**El proceso de entrenamiento de los modelos requiere dividir el conjunto de datos en
distintas partes**: una para el **entrenamiento** del modelo, otra para la **evaluación**
de su desempeño y, en algunos casos, una tercera partición para **validar** su capacidad
de generalización antes de su implementación en entornos reales. Durante este proceso, el
algoritmo analiza las relaciones entre las características de los datos, identifica
patrones y genera predicciones que se comparan con los valores reales. La diferencia
entre las predicciones y las observaciones se mide mediante una métrica de error, lo que
permite ajustar el modelo en cada iteración o **época**, es decir, cada vez que el
algoritmo analiza completamente el conjunto de datos.

<p align="center">
  <img src="https://miro.medium.com/max/1125/1*_7OPgojau8hkiPUiHoGK_w.png"/>
  <br />
  <em>Ejemplo de subajuste, ajuste adecuado y sobreajuste. [Link](https://miro.medium.com/max/1125/1*_7OPgojau8hkiPUiHoGK_w.png)</em>
</p>

Un modelo puede presentar **sobreajuste** (**_overfitting_**) cuando se ajusta demasiado
a los datos de entrenamiento, logrando un alto rendimiento en estos pero fallando en
datos nuevos. En el extremo opuesto, el **subajuste** (**_underfitting_**) ocurre cuando
el modelo es demasiado simple para capturar la estructura subyacente de los datos. Este
equilibrio se conoce como el **compromiso entre sesgo y varianza** (**_bias-variance
tradeoff_**), y su gestión es esencial para obtener modelos que generalicen
correctamente.

El **sesgo** (_bias_) se refiere a la incapacidad de un algoritmo de aprendizaje
automático para capturar la relación real existente en los datos. Un sesgo alto implica
que el modelo realiza suposiciones demasiado simplificadas y no se ajusta adecuadamente
ni siquiera a los datos de entrenamiento. La **varianza** (_variance_), por su parte,
mide la diferencia de ajuste entre el conjunto de entrenamiento y otros conjuntos, como
el de validación o el de pruebas. Una varianza alta indica que el modelo es muy sensible
a las particularidades del conjunto de entrenamiento y no generaliza bien a datos nuevos.
Lo ideal es alcanzar un bajo sesgo, para modelar con mayor exactitud la distribución de
los datos, y una baja varianza, para que el resultado de las predicciones sea consistente
para diferentes conjuntos de datos.

### Tipos de datos

#### Variables dependientes e independientes

En un conjunto de datos, cada atributo que varía entre muestras se denomina **variable**.
Si una variable depende de otra, se considera **dependiente**; en caso contrario, se
clasifica como **independiente**. Las variables independientes, también llamadas
**características** (**_features_**), son las utilizadas en el entrenamiento del modelo
para predecir la variable dependiente.

#### Datos continuos y discretos

<p align="center">
  <img src="https://agencyanalytics.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fdfcvkz6j859j%2F6k4gJrY1mvlPUxf7WZhqdp%2F9f2e800789b81fa6fe751fabf50e9069%2FDiscrete-vs-Continuous-Data-Supporting-Graphics-1.png&w=3840&q=75"/>
  <br />
  <em>Datos discretos vs datos continuos. [Link](https://agencyanalytics.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fdfcvkz6j859j%2F6k4gJrY1mvlPUxf7WZhqdp%2F9f2e800789b81fa6fe751fabf50e9069%2FDiscrete-vs-Continuous-Data-Supporting-Graphics-1.png&w=3840&q=75)</em>
</p>

Los datos pueden clasificarse en **continuos** o **discretos**. Los valores continuos
pueden tomar cualquier número dentro de un rango, como la altura de una persona, ya que
pueden existir valores intermedios con una precisión arbitraria. En contraste, los
valores discretos solo pueden asumir ciertos valores específicos, como la cantidad de
páginas de un libro, donde no existen valores intermedios entre un número entero y otro.

## Estrategias para la selección y validación de datos

Los datos son un elemento esencial en los algoritmos de aprendizaje automático. Sin una
selección adecuada, es posible obtener relaciones no significativas o incluso
perjudiciales.

No todos los datos o métricas son útiles, por lo que es fundamental ajustarse al
problema, asegurar la coherencia dentro de la misma distribución y minimizar la presencia
de valores atípicos. Una correcta selección de los datos permite desarrollar modelos más
robustos. Para ello, se emplea la **validación cruzada**.

### Validación cruzada

<p align="center">
  <img src="https://www.sharpsightlabs.com/wp-content/uploads/2024/02/cross-validation-explained_FEATURED-IMAGE.png"/>
  <br />
  <em>Esquema de funcionamiento de la validación cruzada. [Link](https://www.sharpsightlabs.com/wp-content/uploads/2024/02/cross-validation-explained_FEATURED-IMAGE.png)</em>
</p>

La selección de muestras para el entrenamiento y validación de un modelo puede resultar
compleja, ya que una elección inadecuada puede generar sesgos en el modelo. Por ejemplo,
en conjuntos de datos con dependencia temporal, como el tráfico de una red a lo largo del
día, la distribución de las muestras puede influir en el desempeño del modelo. Si los
datos se registran en orden cronológico y las primeras muestras corresponden a la mañana
mientras que las últimas a la noche, seleccionar las primeras muestras para entrenamiento
y las últimas para prueba podría generar un modelo que no capture correctamente patrones
generales.

Para evitar este problema, se recomienda introducir aleatoriedad en la selección de las
muestras y definir un porcentaje para cada partición del conjunto de datos.

!!! note

    Es fundamental establecer una **semilla aleatoria** antes de cualquier proceso que requiera aleatorización, garantizando así la reproducibilidad de los resultados.

Por ejemplo, el siguiente código establece semillas para las bibliotecas más utilizadas
en Python para aprendizaje automático y profundo, garantizando la reproducibilidad de los
experimentos:

```py linenums="1"
import random
import numpy as np
import tensorflow as tf
import torch
import sklearn.utils

# Valor de la semilla
SEED = 42

# Establecer semilla en Python (random)
random.seed(SEED)

# Establecer semilla en NumPy
np.random.seed(SEED)

# Establecer semilla en TensorFlow
tf.random.set_seed(SEED)

# Establecer semilla en PyTorch
torch.manual_seed(SEED)
torch.cuda.manual_seed(SEED)  # Para GPUs
torch.cuda.manual_seed_all(SEED)  # Para múltiples GPUs
torch.backends.cudnn.deterministic = True  # Para reproducibilidad en CUDA
torch.backends.cudnn.benchmark = False

# Establecer semilla en Scikit-learn
sklearn.utils.check_random_state(SEED)
```

La **validación cruzada** es una técnica fundamental en aprendizaje automático para
evaluar y comparar diferentes modelos. Su objetivo es estimar el rendimiento de un modelo
en datos no vistos y seleccionar el algoritmo más adecuado. El proceso consiste en
dividir el conjunto de datos en múltiples subconjuntos denominados **_folds_**,
generalmente de tamaño similar, y entrenar el modelo de manera iterativa. El caso más
común es el **k-Fold Cross Validation**, donde $k$ suele ser cinco o diez, dependiendo
del tamaño del conjunto de datos y de la complejidad del modelo. El procedimiento se
desarrolla de la siguiente manera:

1. Se separa el conjunto de datos en $k$ folds.
2. En cada iteración, se utiliza un fold como conjunto de prueba y los restantes como
   conjunto de entrenamiento.
3. El modelo se entrena con los folds de entrenamiento y se evalúa con el fold de prueba.
4. Este procedimiento se repite hasta que todos los folds hayan sido utilizados como
   conjunto de prueba una vez.
5. Finalmente, se promedian las métricas de evaluación obtenidas en cada iteración, como
   precisión, error o sensibilidad.

Una ventaja de la validación cruzada es la reducción del problema conocido como **_data
leakage_**, que ocurre cuando características utilizadas en el entrenamiento también
están presentes en la fase de prueba, generando una evaluación artificialmente optimista
del modelo.

## Conceptos de estadística

### Distribuciones

Antes de realizar predicciones, es fundamental recopilar datos. En muchas ocasiones, esta
recopilación genera histogramas, que permiten visualizar la distribución de los datos. Un
histograma se compone de dos ejes principales: el eje $x$, donde se representan los datos
agrupados en categorías, y el eje $y$, que indica la frecuencia de cada categoría, es
decir, el número de muestras que pertenecen a cada grupo. Las divisiones en el eje $x$
para agrupar los datos en rangos similares se conocen como **_bins_** o contenedores.

El uso de histogramas facilita la identificación de tendencias en los datos. En casos
donde los valores pueden solaparse, los _bins_ ayudan a agrupar puntos de datos dentro de
un intervalo definido. De este modo, se generan distribuciones que permiten analizar el
comportamiento de los datos.

!!! note

    La elección del número de _bins_ es crucial, ya que debe reflejar correctamente la distribución de los datos. Este tipo de histogramas resulta especialmente útil en algoritmos como **Naïve Bayes**, donde se generan distribuciones de probabilidad en cada iteración, permitiendo obtener valores como medias e intervalos de confianza.

El conjunto completo de datos recopilados se denomina **población** y se representa con
la letra $N$. Un subconjunto de la población se denomina **muestra** y se representa con
la letra $n$.

La probabilidad de que un dato pertenezca a una determinada parte del histograma se
calcula dividiendo el número de muestras en esa sección entre el número total de muestras
en la población.

!!! note

    La confianza en los resultados depende del tamaño de la muestra: cuanto mayor sea el número de muestras, mayor será la confianza en la estimación. La confianza representa el grado de incertidumbre asociado a una probabilidad.

### Características de la probabilidad

La probabilidad está normalizada en un rango de 0 a 1, donde 0 indica imposibilidad y 1
certeza absoluta. Cuando todos los resultados posibles tienen la misma probabilidad, se
habla de **equiprobabilidad**. Además, la suma de todas las probabilidades en un sistema
debe ser 1.

Cuando el número de datos disponibles es insuficiente, las estimaciones de probabilidad
pueden no ser precisas. No obstante, recopilar más datos puede resultar costoso en
términos de tiempo, esfuerzo y dinero. Para mitigar esta limitación, se emplean
**distribuciones de probabilidad**, que pueden ser **discretas** (cuando los datos toman
valores específicos y finitos) o **continuas** (cuando los datos pueden tomar cualquier
valor dentro de un rango determinado).

A continuación, se presentan algunas de las distribuciones más comunes.

#### Distribución binomial (discreta)

Cuando se trabaja con datos discretos y se requiere calcular probabilidades en eventos
independientes con solo dos posibles resultados, **éxito** o **fracaso** (representados
por 1 y 0, respectivamente), se trata de un **problema binario**.

Para modelar este tipo de situaciones, se utiliza la **distribución binomial**, que
permite calcular la probabilidad de obtener una determinada cantidad de éxitos en una
secuencia de ensayos independientes. La distribución binomial se expresa mediante la
siguiente fórmula:

$$
P(X = k | n, p) = \binom{n}{k} \cdot p^k \cdot (1 - p)^{n - k},
$$

donde:

- $X$ representa el número de éxitos en los ensayos.
- $n$ es el número total de ensayos.
- $p$ es la probabilidad de éxito en un único ensayo.
- $k$ es el número de éxitos deseados.
- $\binom{n}{k}$ es el coeficiente binomial, que calcula de cuántas formas se pueden
  obtener $k$ éxitos en $n$ ensayos, sin importar el orden. Se calcula mediante la
  siguiente fórmula:

$$
\binom{n}{k} = \frac{n!}{k! \cdot (n-k)!}.
$$

Esta distribución es útil en situaciones donde se realizan múltiples intentos
independientes de un mismo experimento y se desea conocer la probabilidad de obtener un
número específico de éxitos.

???+ example "Ejemplo"

    Supongamos que se lanza una moneda equilibrada (equiprobable, la probabilidad de obtener cara es la misma que la de obtener cruz) 5 veces y se quiere calcular la probabilidad de obtener exactamente 3 caras.

    Se definen los parámetros:

    - $n = 5$ (número total de lanzamientos).
    - $p = 0.5$ (probabilidad de obtener cara en un solo lanzamiento).
    - $k = 3$ (número de caras que se desean obtener).

    Aplicando la fórmula de la distribución binomial:

    $$
    P(X = 3 | n=5, p=0.5) = \binom{5}{3} \cdot (0.5)^3 \cdot (1 - 0.5)^{5 - 3}
    $$

    Calculamos el coeficiente binomial:

    $$
    \binom{5}{3} = \frac{5!}{3! \cdot (5-3)!} = \frac{5!}{3! \cdot 2!} = 10
    $$

    Sustituyendo en la ecuación:

    $$
    P(X = 3) = 10 \cdot (0.5)^3 \cdot (0.5)^2 = 0.3125
    $$

    Por lo tanto, la probabilidad de obtener exactamente 3 caras en 5 lanzamientos de una moneda equilibrada es del 31.25%.

#### Distribución de Poisson (discreta)

La **distribución de Poisson** se utiliza para modelar la probabilidad de que ocurra un
número determinado de eventos en un intervalo de tiempo o espacio, siempre que los
eventos ocurran de manera independiente y a una tasa promedio constante. Algunos ejemplos
de aplicación incluyen: el número de llamadas recibidas en una central telefónica durante
una hora, el número de accidentes en una intersección en un día, o la cantidad de errores
tipográficos en una página de texto.

La distribución de Poisson se expresa mediante la siguiente fórmula:

$$
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!},
$$

donde:

- $X$ es el número de eventos que ocurren en un intervalo específico.
- $\lambda$ es el número promedio de eventos en dicho intervalo.
- $k$ es el número de eventos cuya probabilidad se desea calcular.
- $e$ es la base del logaritmo natural.

Esta distribución es especialmente útil cuando se estudian eventos raros o poco
frecuentes en un período de tiempo determinado.

???+ example "Ejemplo"

    Supongamos que una central telefónica recibe en promedio 10 llamadas por hora y se desea calcular la probabilidad de que en una hora lleguen exactamente 7 llamadas.

    Se definen los parámetros:

    - $\lambda = 10$ (promedio de llamadas por hora).
    - $k = 7$ (número específico de llamadas que se desea calcular).

    Aplicamos la fórmula de la distribución de Poisson:

    $$
    P(X = 7) = \frac{10^7 e^{-10}}{7!} \approx 0.0902
    $$

    Por lo tanto, la probabilidad de recibir exactamente 7 llamadas en una hora es del 9.02%.

#### Distribución normal o gaussiana (continua)

La distribución normal, también denominada distribución gaussiana, se representa mediante
una curva en forma de campana. En esta distribución, el eje $y$ indica la
**verosimilitud** (**_likelihood_**) de observar un determinado valor en el eje $x$.

!!! note "Verosimilitud vs. Probabilidad"

    Aunque son conceptos relacionados, la verosimilitud y la probabilidad tienen diferencias clave:

    - **Probabilidad**: Representa la posibilidad de que ocurra un evento dado un modelo y sus parámetros. Se expresa como $P(D|\theta)$, donde $D$ son los datos y $\theta$ los parámetros del modelo. Responde a la pregunta: _Dado que los parámetros del modelo son conocidos, ¿qué tan probable es observar ciertos datos?_
    - **Verosimilitud**: Mide qué tan bien un conjunto de parámetros explica un conjunto de datos observados. Se denota como $L(\theta | D)$ y representa la plausibilidad de los parámetros $\theta$ dados los datos $D$. Responde a la pregunta: _Dado que los datos han sido observados, ¿qué tan plausible es que provengan de un modelo con ciertos parámetros?_

    Mientras que la probabilidad se emplea para predecir eventos futuros basándose en un modelo conocido, la verosimilitud se usa para evaluar qué tan bien un modelo con ciertos parámetros explica los datos observados. Para obtener probabilidades a partir de la verosimilitud, se puede utilizar el Teorema de Bayes.

La distribución normal es **simétrica** respecto a su **media** ($\mu$), lo que implica
que el valor más verosímil es precisamente la media. La forma de la curva normal está
determinada por dos parámetros: la media ($\mu$) y la desviación típica ($\sigma$). Una
curva alta y estrecha indica que los datos están más concentrados alrededor de la media,
lo que corresponde a una baja varianza. Una curva baja y ancha sugiere una mayor
dispersión de los datos, es decir, mayor varianza.

La **desviación típica** ($\sigma$) mide la dispersión de los datos respecto a la media,
mientras que la **varianza** ($\sigma^2$) es el cuadrado de la desviación típica. La
varianza se puede calcular de las siguientes dos maneras:

- **Varianza muestral**:

$$
s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}.
$$

- **Varianza poblacional**:

$$
\sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}.
$$

Donde $x_i$ son los valores de la muestra o población, $\bar{x}$ es la media muestral,
$\mu$ es la media poblacional, $n$ es el tamaño de la muestra y $N$ es el tamaño de la
población.

La distribución normal es fundamental en estadística y aprendizaje automático debido a su
presencia en numerosos fenómenos naturales y conjuntos de datos del mundo real.

##### Función de densidad de probabilidad

La **función de densidad de probabilidad** (_Probability Density Function_, PDF) de la
distribución normal se define como:

$$
f(X|\mu, \sigma) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x_i - \mu)^2}{2\sigma^2}}.
$$

En las distribuciones continuas, el cálculo de probabilidades requiere la integración de
la función de densidad de probabilidad (PDF). Esta integración permite obtener el área
bajo la curva entre dos puntos, lo que representa la probabilidad acumulada en dicho
intervalo. Dado que el área total bajo la curva es igual a 1, el área acumulada hasta la
media en una distribución normal es de 0.5.

Es importante destacar que la probabilidad exacta en un único punto es igual a 0. Esto se
debe a que, gráficamente, un punto no tiene ancho y, por lo tanto, no contribuye con área
bajo la curva. En consecuencia, solo es posible calcular probabilidades en intervalos.

La **función de distribución acumulada** (_Cumulative Distribution Function_, CDF)
expresa la probabilidad acumulada hasta un determinado valor. Matemáticamente, representa
el área bajo la curva de la función de densidad desde $-\infty$ hasta dicho punto.

##### Propiedades de la función de distribución acumulada

Sea $F$ la función de distribución acumulada (CDF) y $\mathbb{R}$ el conjunto de números
reales, entonces se cumple que $F: \mathbb{R} \to [0,1]$, lo que significa que el rango
de valores de la función de distribución está comprendido entre 0 y 1.

!!! note

    Se usa mayúscula para $F(x)$ porque se refiere a la función matemática que mapea los valores de la variable aleatoria $X$ a la probabilidad acumulada, distinguiéndola de la función de densidad de probabilidad que se representa en minúscula, como $f(x)$.

Algunas de sus propiedades fundamentales son:

- $F(x) = P(A_x) = P(X \leq x)$, donde $A_x$ representa el evento $X \leq x$.
- $P(X \leq x) = F(x)$, lo que corresponde a la función de distribución acumulada (CDF).
- $P(X > x) = 1 - P(X \leq x) = 1 - F(x)$, es decir, la probabilidad complementaria a
  $P(X \leq x)$.
- $P(a < X \leq b) = F(b) - F(a)$, para calcular la probabilidad de que $X$ esté entre
  dos valores $a$ y $b$.
- $P(X \geq a) = P(X > a) + P(X = a)$, una forma de descomponer la probabilidad de que
  $X$ sea mayor o igual que $a$.
- $P(X = a) = F(a) - \lim_{h \to 0^+} F(a - h) = F(a) - P(X \leq a)$, que calcula la
  probabilidad de que $X$ tome el valor $a$.

Estas propiedades permiten calcular probabilidades acumuladas y facilitan el análisis de
distribuciones de probabilidad continuas.

???+ example "Ejemplo"

    Se desea calcular la probabilidad de que un valor se encuentre en el intervalo $[142.5, 155.7]$ en una distribución normal $N(\mu=155.7, \sigma=6.6)$.

    La probabilidad se obtiene a partir de la función de distribución acumulada (CDF):

    $$P(a < X \leq b) = P(142.5 < X \leq 155.7) = F(155.7) - F(142.5)$$

    $$P(X \leq 155.7) - P(X \leq 142.5) \approx 0.5 - 0.02275 \approx 0.4772$$

    Implementación en Python:

    ```py linenums="1"
    from statistics import NormalDist

    # Se calcula la función de distribución acumulada (CDF) en los puntos de interés
    cdf_p1 = NormalDist(155.7, 6.6).cdf(155.7)
    # cdf_p1 = 0.5, debido a la simetría de la distribución normal

    cdf_p2 = NormalDist(155.7, 6.6).cdf(142.5)
    # cdf_p2 ≈ 0.02275

    # Se obtiene la probabilidad del intervalo restando las probabilidades acumuladas
    diff = cdf_p1 - cdf_p2
    # diff ≈ 0.4772 = 47.72%
    ```

    Por lo tanto, la probabilidad de que un valor de esta distribución normal se encuentre en el intervalo $[142.5, 155.7]$ es aproximadamente del 47.72%.

#### Distribución exponencial (continua)

La distribución exponencial se emplea para modelar el tiempo transcurrido entre eventos
en un proceso de Poisson, donde los eventos ocurren de manera independiente y con una
tasa constante. Se utiliza en el análisis de tiempos de espera, confiabilidad de sistemas
y modelado de fallos en ingeniería.

La función de densidad de probabilidad (PDF) está definida como:

$$
f(x; \lambda) = \lambda e^{-\lambda x}, \quad x \geq 0, \, \lambda > 0,
$$

donde $\lambda$ indica la frecuencia con la que ocurren los eventos.

La función de distribución acumulada (CDF) se expresa como:

$$
F(x) = 1 - e^{-\lambda x}, \quad x \geq 0.
$$

La media de la distribución exponencial equivale a la **esperanza matemática** $E[X]$.

!!! note

    La **esperanza matemática**, denotada como $E[X]$, es lo que comúnmente se denomina la **media** o el **valor esperado** de una variable aleatoria. Sin embargo, la interpretación de la esperanza matemática puede variar dependiendo del tipo de variable aleatoria y el contexto en el que se utilice.

    Para una variable aleatoria discreta $X$, cuya función de masa de probabilidad es $P(X = x_i)$, la esperanza matemática se calcula mediante la siguiente fórmula:

    $$
    E[X] = \sum_{i} x_i \cdot P(X = x_i)
    $$

    En este caso, el valor esperado se obtiene sumando el producto de cada valor posible de $X$ y su probabilidad correspondiente.

    Para una variable aleatoria continua $X$, cuya función de densidad de probabilidad es $f(x)$, la esperanza matemática se calcula utilizando la integral:

    $$
    E[X] = \int_{-\infty}^{\infty} x \cdot f(x) \,dx
    $$

    Aquí, el valor esperado se obtiene integrando el producto de cada valor de $X$ y su densidad de probabilidad asociada.

    En teoría de probabilidad, la esperanza matemática se considera la media "teórica" de la distribución. **En distribuciones simétricas con un único pico, como la distribución normal, la esperanza matemática coincide con el centro de la distribución. Sin embargo, en distribuciones asimétricas, la esperanza matemática puede no coincidir con la mediana o la moda**. Por ejemplo, en una distribución sesgada a la derecha, como la distribución exponencial, la esperanza matemática es mayor que la mediana, lo que indica que los valores más altos de la variable aleatoria tienen una probabilidad significativa de ocurrir.

En la distribución exponencial, la media se obtiene como:

$$
\mu = E[X] = \frac{1}{\lambda}.
$$

La varianza se expresa como:

$$
\sigma^2 = \frac{1}{\lambda^2}.
$$

#### Distribución uniforme (continua)

La distribución uniforme se caracteriza porque todos los valores dentro de un intervalo
$[a, b]$ tienen la misma probabilidad de ocurrir. Se emplea en la generación de números
aleatorios, simulaciones y situaciones en las que no hay preferencia por ningún valor
específico dentro de un rango determinado.

La función de densidad de probabilidad (PDF) para una distribución uniforme continua es:

$$
f(x) = \begin{cases} \frac{1}{b-a}, & a \leq x \leq b \\ 0, & \text{en otro caso} \end{cases}
$$

La función de distribución acumulada (CDF) está dada por:

$$
F(x) = \begin{cases} 0, & x < a \\ \frac{x-a}{b-a}, & a \leq x \leq b \\ 1, & x > b \end{cases}
$$

La media de la distribución uniforme es:

$$
\mu = E[X] = \frac{a + b}{2}.
$$

Y su varianza se expresa como:

$$
\sigma^2 = \frac{(b-a)^2}{12}.
$$

!!! tip "¿De dónde sale el 12 de la varianza de la distribución uniforme?"

    La varianza de una variable aleatoria continua $X$ se define como:

    $$
    \text{Var}(X) = E[X^2] - (E[X])^2.
    $$

    Para una distribución uniforme continua $U(a, b)$, la esperanza, la cual coincide con la media, se obtiene con la fórmula:

    $$
    E[X] = \frac{a+b}{2}.
    $$

    Por tanto, el cálculo de $E[X^2]$ se realiza como:

    $$
    E[X^2] = \int_a^b x^2 \cdot f(x) \, dx = \int_a^b x^2 \cdot \frac{1}{b-a} \, dx.
    $$

    Resolviendo la integral:

    $$
    E[X^2] = \frac{1}{b-a} \int_a^b x^2 \, dx = \frac{1}{b-a} \cdot \left[ \frac{x^3}{3} \right]_{a}^{b}.
    $$

    Evaluando de $a$ a $b$:

    $$
    E[X^2] = \frac{1}{b-a} \left[ \frac{b^3}{3} - \frac{a^3}{3} \right] = \frac{b^3 - a^3}{3(b-a)}.
    $$

    Ahora, usando la fórmula de la varianza y sustituyendo los valores obtenemos:

    $$
    \text{Var}(X) = E[X^2] - (E[X])^2 = \frac{b^3 - a^3}{3(b-a)} - \left(\frac{a+b}{2} \right)^2.
    $$

    Aplicando las identidades algebraicas siguientes:

    $$
    (a+b)^{2}=a^2+b^2+2ab,
    $$

    $$
    b^3 - a^3 = (b-a)(b^2 + ab + a^2),
    $$

    Finalmente, después de desarrollar la expresión y simplificar, se obtiene:

    $$
    \text{Var}(X) = \frac{(b-a)^2}{12}.
    $$

### P-valores

Los **p-valores** (_p-values_) son números comprendidos entre 0 y 1 que cuantifican la
confianza con la que se puede afirmar que una opción A es diferente de una opción B. Un
p-valor cercano a 0 indica que existe evidencia estadística suficiente para considerar
que A es distinto de B.

En la práctica, se suele utilizar un **umbral de significancia** de 0.05 para determinar
si la diferencia es estadísticamente significativa. Sin embargo, puede darse el caso de
obtener un p-valor pequeño cuando en realidad no existe diferencia, lo que se conoce como
un **falso positivo**. Un umbral de 0.05 implica que aproximadamente el 5% de los
experimentos generará un p-valor menor a 0.05 por azar. Si se requiere mayor seguridad,
se pueden emplear umbrales más bajos; por ejemplo, en medicina se utilizan umbrales como
0.0001, lo que equivale a un falso positivo cada 100.000 experimentos.

El umbral de significancia ($\alpha$) representa la probabilidad máxima aceptada de
cometer un falso positivo, y su inversa indica la frecuencia esperada de falsos
positivos. La idea de determinar si una opción A es igual o diferente a una opción B se
denomina **prueba de hipótesis**. La hipótesis de que A es igual a B se conoce como
**hipótesis nula** ($H_0$). Por tanto, el p-valor mide la probabilidad de que el
resultado observado ocurra asumiendo que la hipótesis nula es verdadera, es decir, que no
existen diferencias reales. Es importante destacar que el p-valor no mide la magnitud de
la diferencia, sino únicamente la probabilidad de observar los datos bajo la hipótesis
nula.

### Evaluación del error

Los modelos de aprendizaje automático requieren datos de entrenamiento para establecer
relaciones entre las variables y construir una función que se aproxime a la distribución
de los datos. Un aspecto fundamental en este proceso es la evaluación del desempeño del
modelo, lo cual se realiza mediante métricas estadísticas.

#### Suma de los cuadrados de los residuales (SSR)

<p align="center">
  <img src="https://images.squarespace-cdn.com/content/v1/5acbdd3a25bf024c12f4c8b4/1600368657769-5BJU5FK86VZ6UXZGRC1M/Mean+Squared+Error.png"/>
  <br />
  <em>Ejemplo de SSR. [Link](https://images.squarespace-cdn.com/content/v1/5acbdd3a25bf024c12f4c8b4/1600368657769-5BJU5FK86VZ6UXZGRC1M/Mean+Squared+Error.png)</em>
</p>

La **Suma de los Cuadrados de los Residuales** (_Sum of Squared Residuals_, SSR) mide la
diferencia entre las predicciones del modelo y los valores reales. Se calcula sumando el
cuadrado de estas diferencias, lo que permite evaluar qué tan buena es la predicción del
modelo. Un valor bajo de SSR indica un mejor ajuste. Matemáticamente, la SSR se expresa
como:

$$
SSR = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2,
$$

donde $y_i$ es el valor real, $\hat{y}_i$ es el valor estimado por el modelo y $n$ es el
número total de observaciones.

Sin embargo, la SSR depende del número de datos, lo que puede dificultar la comparación
entre modelos. Para abordar este problema, se emplea el **Error Cuadrático Medio (MSE)**.

#### Error cuadrático medio (MSE)

El **Error Cuadrático Medio** (_Mean Squared Error_, MSE) se obtiene dividiendo la SSR
entre el número total de muestras. Su objetivo es promediar la magnitud del error para
normalizarlo con respecto al tamaño del conjunto de datos. Se define como:

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2.
$$

A pesar de que el MSE proporciona una medida más interpretable del error, sigue
dependiendo de la escala de los datos. Para eliminar esta dependencia, se emplea el
**Coeficiente de Determinación ($R^2$)**.

#### Coeficiente de determinación

El **Coeficiente de Determinación** ($R^2$) mide la capacidad del modelo para replicar
los resultados observados y la proporción de variabilidad explicada por el modelo en
comparación con la media de los datos. Se expresa como:

$$
R^2 = 1 - \frac{SSR}{SST} = 1 - \frac{SSR(\text{respecto al modelo})}{SSR(\text{respecto a la media})},
$$

donde $SST$ es la **Suma Total de los Cuadrados**, que representa la variabilidad total
de los datos en torno a la media.

El coeficiente $R^2$ varía entre 0 y 1, donde un valor cercano a 1 indica que el modelo
explica bien la varianza de los datos, lo que sugiere un buen ajuste. En cambio, un valor
cercano a 0 sugiere que el modelo apenas mejora la predicción en comparación con la
media. Si $R^2$ es negativo, el modelo tiene un mal ajuste y predice peor que la media.
Por ejemplo, si $R^2 = 0.6$, se interpreta que la variable independiente explica el 60%
de la variación observada en la variable dependiente.

El coeficiente $R^2$ se emplea en problemas de regresión sobre datos continuos.

!!! note

    El coeficiente $R^2$ equivale al cuadrado del coeficiente de correlación de Pearson solo en el caso de la regresión lineal simple.

#### Coeficiente de correlación de Pearson

<p align="center">
  <img src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.statisticshowto.com%2Fwp-content%2Fuploads%2F2012%2F10%2Fpearson-2-small.png&f=1&nofb=1&ipt=25bc8844d74e829cb2103b12684b70568fc8a54b572ffa6ac17a40d3e106789d&ipo=images"/>
  <br />
  <em>Ejemplo de la correlación para una nube de puntos. [Link](http://www.statisticshowto.com/wp-content/uploads/2012/10/pearson-2-small.png)</em>
</p>

El **Coeficiente de Correlación de Pearson** mide la relación lineal entre dos variables
cuantitativas y continuas. Se define como:

$$
r = \frac{\text{cov}(X,Y)}{\sigma_X \sigma_Y},
$$

donde $\text{cov}(X,Y)$ es la **covarianza** entre las variables $X$ e $Y$, y $\sigma_X$
y $\sigma_Y$ son las desviaciones típicas de $X$ e $Y$, respectivamente.

La **covarianza** indica la relación entre dos variables. Si la covarianza es positiva,
un aumento en $X$ se asocia con un aumento en $Y$ (relación directa). Si la covarianza es
negativa, un aumento en $X$ se asocia con una disminución en $Y$ (relación inversa). Una
covarianza cercana a 0 sugiere que no existe relación lineal entre las variables.

Dado que la covarianza depende de la escala de las variables, se normaliza mediante el
coeficiente de correlación de Pearson, que toma valores entre -1 y 1, donde 1 indica una
correlación positiva perfecta, -1 una correlación negativa perfecta y 0 la ausencia de
correlación lineal. Este coeficiente permite evaluar la intensidad y dirección de la
relación lineal entre las variables sin depender de su escala.

## Modelos clásicos

Una vez comprendido el concepto de modelo de aprendizaje automático, donde se utilizan
datos para modelar su distribución, analizar relaciones y extraer conocimiento, es
posible aplicar estos modelos para realizar tareas como clasificación de nuevos datos,
predicción de valores y otras aplicaciones. A continuación, se presentan algunos de los
métodos más utilizados.

!!! tip

    A pesar del auge de los modelos de lenguaje basados en arquitecturas de **aprendizaje profundo (_Deep Learning_)**, su aplicación sigue siendo limitada en ciertos contextos debido a la gran cantidad de datos y capacidad de cómputo que requieren, así como a la necesidad de explicabilidad en sectores específicos. Por ello, los métodos tradicionales siguen desempeñando un papel fundamental, especialmente en el análisis de datos **tabulares**, los cuales representan la mayoría de los datos empresariales.

    Es recomendable iniciar con modelos más sencillos para comprender los resultados y evaluar su utilidad en función de los objetivos del análisis. A partir de esta base, y considerando factores como el tiempo y los recursos disponibles, se puede optar por soluciones más complejas que ofrezcan un mayor retorno de inversión (ROI).

### Regresión lineal

La regresión lineal es uno de los modelos más fundamentales del aprendizaje automático.
Su objetivo consiste en ajustar una línea recta a un conjunto de datos de manera que la
suma de los cuadrados de los residuales (SSR) sea mínima, un procedimiento conocido como
**mínimos cuadrados** (_least squares_). En esencia, se busca la recta que mejor se
ajuste a los datos, es decir, aquella que minimice la distancia entre los valores
observados y los valores predichos por el modelo.

Una vez ajustada la línea, se calcula el coeficiente de determinación $R^2$ para evaluar
la calidad del ajuste, y se pueden obtener los p-valores asociados para determinar la
significancia estadística del modelo. Para analizar visualmente la calidad del ajuste, es
habitual representar los **residuos**, que son las diferencias entre los valores reales y
los valores predichos por la línea ajustada. Esta representación permite observar si el
modelo captura adecuadamente la variabilidad de los datos o si existen patrones no
modelados.

A partir de los datos, se puede calcular la **varianza** como la suma de los cuadrados de
las diferencias entre cada punto y la media, dividida entre el número de puntos. Esta
medida indica el grado de dispersión de los datos. El coeficiente $R^2$ se obtiene como
la diferencia entre la varianza respecto a la media y la varianza respecto al ajuste,
dividida entre la varianza respecto a la media. Por ejemplo, si $R^2 = 0.6$, se
interpreta que la variable independiente explica el 60% de la variación de la variable
dependiente.

En los modelos lineales es posible introducir más parámetros (variables independientes)
para mejorar el ajuste. Sin embargo, si los parámetros adicionales no contribuyen a
mejorar el modelo, el algoritmo les asignará coeficientes cercanos a cero, anulando
efectivamente su influencia en la predicción.

### Descenso del gradiente

El **descenso del gradiente** es un proceso iterativo utilizado para minimizar una
**función de pérdida** (_loss function_), que representa el error promedio del modelo
respecto a todos los puntos del conjunto de datos. El procedimiento comienza
seleccionando un punto de partida aleatorio en la superficie de la función de pérdida. A
continuación, se calcula la derivada (o **gradiente**) de la función en ese punto, lo que
permite conocer la pendiente de la función en dicha posición. Si la derivada es positiva,
la función crece en esa dirección y el algoritmo se desplaza en la dirección opuesta; si
es negativa, el algoritmo avanza en esa misma dirección. Este proceso se repite
iterativamente, ajustando la posición en cada paso hasta alcanzar un mínimo de la función
de pérdida.

El **descenso del gradiente estocástico** (_Stochastic Gradient Descent_, SGD) introduce
una variante importante: en lugar de calcular el gradiente utilizando todos los puntos
del conjunto de datos (lo cual resulta computacionalmente costoso), se selecciona de
forma aleatoria un subconjunto de puntos denominado **lote** (_batch_) en cada iteración.
Esta estrategia no solo reduce el coste computacional, sino que también ayuda a evitar
que el algoritmo quede atrapado en **mínimos locales**, ya que la aleatoriedad en la
selección de los datos introduce variabilidad en la dirección del gradiente.

### Regresión logística

La **regresión logística** es un modelo de clasificación que, a pesar de su nombre, no se
utiliza para problemas de regresión sino para predecir la probabilidad de pertenencia a
una clase. A diferencia de la regresión lineal, que produce valores continuos, la
regresión logística aplica la **función sigmoide** a la salida de una combinación lineal
de las variables de entrada, transformando el resultado en un valor comprendido entre 0 y
1 que se interpreta como una probabilidad.

La función sigmoide se define como:

$$
\sigma(z) = \frac{1}{1 + e^{-z}},
$$

donde $z = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_n x_n$ es la combinación
lineal de las variables independientes con sus coeficientes. El modelo asigna la clase
positiva cuando la probabilidad supera un umbral determinado (generalmente 0.5) y la
clase negativa en caso contrario.

El entrenamiento del modelo se realiza mediante la maximización de la **función de
verosimilitud** o, equivalentemente, la minimización de la **función de pérdida
logarítmica** (_log-loss_ o _binary cross-entropy_), utilizando técnicas de optimización
como el descenso del gradiente.

### Naïve Bayes

El clasificador **Naïve Bayes** es un modelo probabilístico basado en el **Teorema de
Bayes** que asume independencia condicional entre las características dadas la clase. A
pesar de que esta suposición de independencia rara vez se cumple en la práctica, el
modelo ofrece un rendimiento sorprendentemente bueno en muchas aplicaciones,
especialmente en clasificación de texto y filtrado de spam.

El Teorema de Bayes permite calcular la probabilidad posterior de una clase $C_k$ dado un
vector de características $\mathbf{x}$:

$$
P(C_k | \mathbf{x}) = \frac{P(\mathbf{x} | C_k) \cdot P(C_k)}{P(\mathbf{x})}.
$$

Bajo la suposición de independencia condicional, la verosimilitud se descompone como el
producto de las probabilidades individuales de cada característica:

$$
P(\mathbf{x} | C_k) = \prod_{i=1}^{n} P(x_i | C_k).
$$

El clasificador asigna a cada nueva observación la clase con mayor probabilidad
posterior. Existen diferentes variantes del modelo según la distribución asumida para las
características: **Gaussiano** (para datos continuos con distribución normal),
**Multinomial** (para conteos de frecuencias, como en clasificación de texto) y
**Bernoulli** (para características binarias).

### Árboles de decisión

Los **árboles de decisión** son modelos que realizan predicciones mediante una serie de
reglas de decisión organizadas en una estructura jerárquica en forma de árbol. Cada nodo
interno del árbol representa una condición sobre una característica del conjunto de
datos, cada rama corresponde al resultado de esa condición y cada nodo hoja contiene la
predicción final (una clase en clasificación o un valor numérico en regresión).

El proceso de construcción del árbol consiste en seleccionar, en cada nodo, la
característica y el umbral que mejor separan los datos según un criterio de impureza,
como el **índice de Gini** o la **entropía** en clasificación, o la reducción de la
varianza en regresión. Este proceso se repite recursivamente hasta que se cumple algún
criterio de parada, como alcanzar una profundidad máxima o un número mínimo de muestras
por nodo.

Los árboles de decisión son fácilmente interpretables y eficientes en el ajuste a los
datos de entrenamiento. Sin embargo, presentan una alta varianza que los hace propensos
al sobreajuste, especialmente cuando se permite que el árbol crezca sin restricciones.

#### Random Forest

**Random Forest** es una técnica de ensamblado basada en árboles de decisión que mejora
la capacidad de generalización de estos últimos. Aunque los árboles de decisión clásicos
son fácilmente interpretables y eficientes en el ajuste a los datos de entrenamiento,
presentan una alta varianza que los hace poco robustos frente a nuevas muestras. Random
Forest soluciona esta limitación mediante un enfoque basado en el aprendizaje conjunto de
múltiples árboles de decisión.

El proceso de construcción de un modelo Random Forest se compone de tres etapas
fundamentales. En primer lugar, se generan múltiples subconjuntos de entrenamiento
mediante **muestreo aleatorio con reemplazo** a partir del conjunto de datos original, un
procedimiento conocido como _bootstrap sampling_. Como consecuencia, algunas
observaciones pueden repetirse dentro de un subconjunto, mientras que otras no son
seleccionadas. En segundo lugar, cada subconjunto generado se utiliza para entrenar un
árbol de decisión independiente. A diferencia del procedimiento habitual, en cada
división del árbol se selecciona aleatoriamente un subconjunto de características en
lugar de utilizar todas, lo que introduce diversidad entre los árboles y reduce la
correlación entre ellos. En tercer lugar, las predicciones de todos los árboles se
combinan mediante un proceso denominado **_bagging_** (_bootstrap aggregating_), que
consiste en promediar las predicciones (para regresión) o realizar una votación
mayoritaria (para clasificación).

Durante el entrenamiento, algunas muestras no se utilizan en la construcción de un árbol
determinado. Estas observaciones, conocidas como _out-of-bag samples_, se emplean para
evaluar el rendimiento del modelo de manera interna, sin necesidad de un conjunto de
validación adicional. Al calcular el porcentaje de muestras _out-of-bag_ clasificadas
incorrectamente por el conjunto de árboles, se obtiene el llamado _out-of-bag error_, que
actúa como una estimación fiable del error de generalización.

El número de características consideradas en cada división puede ajustarse como
hiperparámetro del modelo. Este control permite optimizar el equilibrio entre sesgo y
varianza, mejorando la precisión y robustez del Random Forest frente a los árboles de
decisión individuales.

### Máquina de vectores de soporte

La **Máquina de Vectores de Soporte** (_Support Vector Machine_, SVM) es un algoritmo de
aprendizaje supervisado utilizado tanto para clasificación como para regresión. Su
principio fundamental consiste en encontrar el **hiperplano** que mejor separa las clases
en el espacio de características, maximizando el **margen**, es decir, la distancia entre
el hiperplano y los puntos de datos más cercanos de cada clase, denominados **vectores de
soporte**.

En problemas donde los datos no son linealmente separables, las SVM emplean el denominado
**truco del kernel** (_kernel trick_), que consiste en proyectar los datos a un espacio
de mayor dimensionalidad donde sí resultan separables linealmente. Entre los kernels más
utilizados se encuentran el lineal, el polinómico y el de función de base radial (RBF).

La formulación matemática de la SVM busca minimizar una función objetivo que equilibra la
maximización del margen con la penalización de las clasificaciones erróneas, controlada
por un hiperparámetro de regularización $C$. Un valor alto de $C$ prioriza la
clasificación correcta de todos los puntos (riesgo de sobreajuste), mientras que un valor
bajo permite mayor tolerancia a errores (mayor generalización).

### XGBoost

**XGBoost** (_Extreme Gradient Boosting_) es un algoritmo de aprendizaje automático
basado en el ensamblado de árboles de decisión mediante la técnica de **_gradient
boosting_**. A diferencia de Random Forest, donde los árboles se entrenan de forma
independiente, en XGBoost cada nuevo árbol se construye para corregir los errores
cometidos por los árboles anteriores, lo que permite mejorar progresivamente el
rendimiento del modelo.

El algoritmo utiliza por defecto el **Error Cuadrático Medio (MSE)** como función de
pérdida para problemas de regresión. El proceso de entrenamiento se basa en la
optimización de una función objetivo que combina la función de pérdida con un término de
regularización para controlar la complejidad del modelo y prevenir el sobreajuste.

Para determinar las divisiones óptimas en cada nodo del árbol, XGBoost calcula una
métrica denominada **similaridad** (_similarity score_), que se define como:

$$
\text{Similarity} = \frac{G^2}{H + \lambda},
$$

donde $G$ es la suma de los gradientes (primeras derivadas de la función de pérdida), $H$
es la suma de las hessianas (segundas derivadas de la función de pérdida) y $\lambda$ es
el parámetro de regularización. La **ganancia** (_gain_) de una división se calcula como
la diferencia entre la suma de las similaridades de los nodos hijos y la similaridad del
nodo padre:

$$
\text{Gain} = \text{Similarity}_{\text{izq}} + \text{Similarity}_{\text{der}} - \text{Similarity}_{\text{padre}}.
$$

Se selecciona la división con mayor ganancia en cada paso. Para determinar los puntos de
corte candidatos, XGBoost puede utilizar un enfoque basado en **cuantiles**
(_quantile-based split finding_), que permite obtener rangos de valores representativos
(por ejemplo, los percentiles 0.1, 0.5 y 0.9) para evaluar las divisiones de forma
eficiente sin necesidad de probar todos los valores posibles.

XGBoost también soporta la **regresión por cuantiles** (_quantile regression_), que en
lugar de predecir un único valor, estima diferentes percentiles de la distribución
condicional de la variable objetivo. La función de pérdida para la regresión por
cuantiles se define como:

$$
L_q(y, \hat{y}) = \begin{cases} q \cdot (y - \hat{y}) & \text{si } y > \hat{y} \\ (1 - q) \cdot (\hat{y} - y) & \text{si } y < \hat{y} \end{cases},
$$

donde $q$ es el cuantil deseado. Esta función de pérdida permite obtener intervalos de
predicción y estimar la incertidumbre asociada a las predicciones del modelo.

## Algoritmos de agrupación

La función principal de la agrupación o _clustering_ consiste en reducir la distancia
entre los puntos de un grupo y maximizar la distancia entre los distintos grupos, es
decir, que los puntos de datos que pertenezcan a un mismo grupo se encuentren lo más
cerca posible entre sí pero alejados de los puntos de datos del resto de grupos. **Este
problema se vuelve más complejo conforme aumenta la dimensionalidad del espacio**, ya que
puntos de datos que parecían alejados pueden pasar a estar más cerca en dimensiones
superiores.

Por ello, **es muy común el uso de técnicas para la reducción de la dimensionalidad en
datos de alta dimensionalidad**, ya que al añadir más características a la entrada del
algoritmo de _clustering_, los datos se vuelven dispersos y el análisis sufre de la
denominada **maldición de la dimensionalidad** (**_curse of dimensionality_**). Algunas
de las técnicas de reducción de dimensionalidad más utilizadas son el análisis de
componentes principales (**_Principal Component Analysis_**, **PCA**) y los
**_Autoencoders_**. El PCA garantiza la búsqueda de la mejor transformación lineal que
reduzca el número de dimensiones con una pérdida mínima de información (en ocasiones, la
información que se pierde se considera ruido irrelevante), mientras que los
_Autoencoders_ comprimen la información recibida a la entrada para adquirir una
representación compacta en su espacio latente.

Los algoritmos de _clustering_ se utilizan en problemas **no supervisados**, es decir,
problemas donde no se dispone de etiquetas y el objetivo es obtener agrupaciones de datos
con similitudes. A continuación, se presentan los principales tipos de algoritmos de
agrupación.

### Métodos basados en particiones

#### K-Means

**K-Means** es uno de los algoritmos de _clustering_ no supervisado más utilizados. Su
principal función es dividir el conjunto de datos en $k$ grupos predefinidos, donde cada
dato pertenece a un único grupo. El algoritmo opera de la siguiente manera:

En primer lugar, se eligen de manera aleatoria $k$ puntos del conjunto de datos, que se
interpretan como los centros iniciales (centroides) de los grupos. A continuación, se
calcula la distancia de cada punto del conjunto de datos a cada centroide, generalmente
utilizando la **distancia euclídea**. Cada punto se asigna al centroide más cercano,
formando así los grupos iniciales. Posteriormente, se recalcula la posición de cada
centroide como la media de todos los puntos asignados a su grupo. Este proceso de
asignación y actualización se repite iterativamente hasta que los centroides convergen
(dejan de cambiar significativamente) o se alcanza un número máximo de iteraciones.

Formalmente, el centro del cluster $k$ se representa con la letra $\mu_k$. Para cada
punto $x_i$ del conjunto de datos, se calcula la distancia euclídea a cada centroide y se
asigna al cluster cuyo centroide sea el más cercano. La **función de coste** del
algoritmo se define como la suma promedio de las distancias euclídeas entre todas las
muestras y sus respectivos centroides:

$$
J = \frac{1}{M} \sum_{i=1}^{M} \| x_i - \mu_{c_i} \|^2,
$$

donde $M$ es el número total de muestras y $c_i$ es el índice del cluster asignado al
punto $x_i$. En cada iteración, la función de coste debería reducirse, lo que permite
comparar el valor actual con el anterior para verificar si el modelo converge.

Para evitar que el algoritmo quede atrapado en mínimos locales, es habitual ejecutar
K-Means múltiples veces con diferentes inicializaciones aleatorias y seleccionar la
ejecución con menor función de coste. El número de clusters $k$ debe ser menor que el
número total de muestras $M$ y su elección es un aspecto crítico del algoritmo.

```python
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generación de datos sintéticos con distribución gaussiana isotrópica
# Una desviación típica baja indica datos más agrupados cerca de su media,
# mientras que una alta indica mayor dispersión
x, y = make_blobs(
    n_samples=200,
    n_features=2,
    centers=3,
    cluster_std=0.5,
    random_state=0
)

# Visualización inicial de los datos en 2D
plt.scatter(x[:, 0], x[:, 1], c='white', edgecolors='black')
plt.title('Datos sin agrupar')
plt.show()

# Configuración y entrenamiento del modelo K-Means
kmeans = KMeans(
    n_clusters=3,
    init='random',
    n_init=1,
    max_iter=10,
    tol=1e-04,
    random_state=2
)

y_km = kmeans.fit_predict(x)

# Visualización de los clusters resultantes
colores = ['lightgreen', 'orange', 'lightblue']
marcas = ['s', 'o', 'v']

for i in range(3):
    plt.scatter(
        x[y_km == i, 0], x[y_km == i, 1],
        s=50, c=colores[i],
        marker=marcas[i], edgecolor='black',
        label=f"Cluster {i}"
    )

# Visualización de los centroides
plt.scatter(
    kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
    s=250, marker='*',
    c='red', edgecolor='black',
    label='Centroides'
)

plt.legend(scatterpoints=1)
plt.title('Resultado de K-Means')
plt.show()
```

#### K-Medoids

**K-Medoids** es una variante de K-Means que, en lugar de utilizar la media de los puntos
como centroide, selecciona un punto real del conjunto de datos como representante de cada
cluster (denominado **medoide**). Esta característica lo hace más robusto frente a
valores atípicos, ya que el medoide siempre es un punto existente en los datos.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn_extra.cluster import KMedoids
from sklearn.metrics import silhouette_score, calinski_harabasz_score
from sklearn import preprocessing

# Configuración del modelo K-Medoids
algoritmo = KMedoids(
    n_clusters=3,
    metric='euclidean',
    method='alternate',  # Cambiar por 'pam' para mayor precisión (más lento)
    init='k-medoids++',
    max_iter=300,
    random_state=0
)

# algoritmo.fit(x)  # Ajustar con el conjunto de datos correspondiente
```

### Métodos basados en jerarquías

El **clustering jerárquico aglomerativo** (_Agglomerative Hierarchical Clustering_, AHC)
es un método que construye una jerarquía de clusters de forma ascendente. Inicialmente,
cada punto de datos se considera un cluster individual. En cada paso, los dos clusters
más cercanos se fusionan, y este proceso se repite hasta que todos los puntos pertenecen
a un único cluster o se alcanza el número deseado de agrupaciones. La distancia entre
clusters se puede medir mediante diferentes criterios de enlace (_linkage_), como el
enlace simple, completo, promedio o el método de Ward.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score, calinski_harabasz_score
from sklearn import preprocessing

# Configuración del modelo de clustering jerárquico aglomerativo
algoritmo = AgglomerativeClustering(
    n_clusters=3,
    metric='euclidean',
    linkage='ward'
)

# algoritmo.fit(x)  # Ajustar con el conjunto de datos correspondiente
```

### Métodos basados en densidad

**DBSCAN** (_Density-Based Spatial Clustering of Applications with Noise_) es un
algoritmo de clustering que agrupa puntos que se encuentran en regiones de alta densidad,
separándolos de las regiones de baja densidad. A diferencia de K-Means, DBSCAN no
requiere especificar el número de clusters de antemano y es capaz de detectar clusters de
formas arbitrarias, así como identificar puntos de ruido (_outliers_) que no pertenecen a
ningún cluster.

### Métodos basados en modelos

Los **Modelos de Mezcla Gaussiana** (_Gaussian Mixture Models_, GMM) asumen que los datos
provienen de una mezcla de varias distribuciones gaussianas, cada una con sus propios
parámetros de media y covarianza. A diferencia de K-Means, que realiza asignaciones duras
(cada punto pertenece a un único cluster), los GMM proporcionan asignaciones
probabilísticas, indicando la probabilidad de que cada punto pertenezca a cada cluster.
El entrenamiento se realiza mediante el algoritmo **Expectation-Maximization (EM)**.

### Métodos basados en grafos

El **clustering espectral** (_Spectral Clustering_) permite agrupar conjuntos de datos
mucho más complejos que no son linealmente separables, como ocurre en el caso de K-Means.
La idea fundamental de este algoritmo consiste en crear un **grafo de afinidad** (o grafo
de similitud) donde cada punto de los datos es un nodo del grafo y las aristas (_edges_)
entre nodos indican la similitud entre ellos.

Para expresar el valor de la similitud entre nodos, se puede utilizar la **función
gaussiana** (o kernel RBF). Cuando la distancia entre dos puntos es pequeña, la similitud
se aproxima a 1, indicando una gran afinidad; cuando la distancia es grande, la similitud
se aproxima a 0. El resultado es una **matriz de similitud** $W$ de dimensión
$n \times n$:

$$
W = \begin{pmatrix}
W_{1,1} & \cdots & W_{1,n} \\
\vdots & \ddots & \vdots \\
W_{n,1} & \cdots & W_{n,n}
\end{pmatrix}
$$

Una vez obtenido el grafo de similitud, el objetivo es dividir los nodos en $k$ grupos
minimizando las conexiones entre grupos y maximizando las conexiones dentro de cada
grupo.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering
from sklearn.datasets import make_blobs

n_samples = 1500
random_state = 170

X, y = make_blobs(n_samples=n_samples, random_state=random_state)

# Transformación para crear datos no linealmente separables
transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
X_aniso = np.dot(X, transformation)

# Aplicación del clustering espectral
y_pred = SpectralClustering(
    n_clusters=3,
    gamma=5,
    random_state=random_state
).fit_predict(X_aniso)

plt.figure(figsize=(6, 5))
plt.scatter(X_aniso[:, 0], X_aniso[:, 1], c=y_pred, s=10)
plt.title("Spectral Clustering")
plt.show()
```

### K-Nearest Neighbors (KNN)

A diferencia de los algoritmos de clustering vistos hasta este punto, **KNN** (_K-Nearest
Neighbors_) es un algoritmo **supervisado** utilizado para problemas de clasificación y
regresión. Su funcionamiento se basa en la idea de que puntos de datos similares tienden
a estar próximos en el espacio de características.

Para clasificar un nuevo punto, el algoritmo calcula la distancia de dicho punto respecto
a todos los puntos del conjunto de datos de entrenamiento, generalmente utilizando la
**distancia euclídea** o la **distancia Manhattan**. A continuación, se seleccionan los
$k$ vecinos más cercanos y se asigna al nuevo punto la clase mayoritaria entre esos
vecinos (en clasificación) o la media de sus etiquetas (en regresión).

La elección del valor de $k$ es un aspecto crítico del algoritmo. Un valor pequeño de $k$
implica un sesgo bajo pero una alta varianza, lo que puede conducir al sobreajuste. Un
valor grande de $k$ implica un sesgo alto pero baja varianza, lo que puede provocar
subajuste. El valor óptimo de $k$ se obtiene mediante técnicas como la validación cruzada
y el análisis de curvas de aprendizaje, buscando un equilibrio entre ambos extremos.

### Mecanismos para la elección del número de clusters

La selección del número óptimo de clusters es un paso fundamental en cualquier algoritmo
de agrupación. Existen varios métodos que permiten evaluar y comparar diferentes
configuraciones para determinar el valor más adecuado.

#### Método del codo

El **método del codo** (_Elbow Method_) utiliza como medida el **WCSS** (_Within-Cluster
Sum of Squares_), que cuantifica la variabilidad de las observaciones dentro de los
clusters. El WCSS se calcula sumando las distancias al cuadrado entre cada observación y
el centroide de su respectivo cluster, y promediando los valores de todos los clusters
para obtener un WCSS global. Los valores más bajos de WCSS son preferibles, ya que
indican una agrupación más compacta.

El procedimiento consiste en ejecutar el algoritmo de clustering con diferentes valores
de $k$ y calcular el WCSS para cada uno. El valor óptimo de $k$ se identifica en el punto
donde la reducción del WCSS deja de ser significativa, formando un "codo" en la gráfica.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Rango de valores para el número de clusters
inf = 2
sup = 10

wcss = []

for i in range(inf, sup + 1):
    algoritmo = KMeans(
        n_clusters=i,
        init='k-means++',
        max_iter=300,
        n_init=10,
        random_state=0
    )
    algoritmo.fit(x)
    wcss.append(algoritmo.inertia_)

plt.scatter(range(inf, sup + 1), wcss, c='red')
plt.plot(range(inf, sup + 1), wcss)
plt.grid(visible=True)
plt.title('Método del codo')
plt.xlabel('Número de clusters')
plt.ylabel('WCSS')
plt.show()
```

#### Puntuación de la silueta

El **coeficiente de silueta** (_Silhouette Score_) se emplea para determinar el valor
óptimo del número de clusters. La puntuación se calcula promediando el coeficiente de
silueta de cada muestra, que se obtiene como la diferencia entre la distancia media al
cluster más cercano y la distancia media dentro del propio cluster, normalizada por el
valor máximo de ambas. Esto produce una puntuación entre $[-1, 1]$, donde 1 corresponde a
clusters muy densos y bien separados, 0 indica solapamiento entre clusters y -1 señala
una agrupación incorrecta.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import SilhouetteVisualizer

inf = 2
sup = 10

punt_silu = []

for i in range(inf, sup + 1):
    algoritmo = KMeans(
        n_clusters=i,
        init='k-means++',
        max_iter=300,
        n_init=10,
        random_state=0
    )
    visualizer = SilhouetteVisualizer(algoritmo, colors='yellowbrick')
    visualizer.fit(x)
    visualizer.show()
    punt_silu.append(silhouette_score(x, algoritmo.labels_))

sil = np.argmax(punt_silu) + 2

plt.grid(visible=True)
plt.plot(range(inf, sup + 1), punt_silu)
plt.scatter(sil, punt_silu[sil - 2], c='red', s=300)
plt.axvline(x=sil, linestyle='--', c='green', label='Punto óptimo')
plt.legend(shadow=True)
plt.title('Método de Puntuación de Silueta')
plt.xlabel('Número de clusters')
plt.ylabel('Puntuación Silueta')
plt.show()
```

#### Índice de Caliński-Harabasz

El **índice de Caliński-Harabasz** (índice CH) evalúa la calidad de la agrupación
midiendo la relación entre la **cohesión** (qué tan similar es un objeto a su propio
grupo) y la **separación** (qué tan diferente es respecto a otros grupos). La cohesión se
estima en función de las distancias desde los puntos de datos hasta el centroide de su
cluster, y la separación se basa en la distancia de los centroides de cada cluster al
centroide global.

Un valor más alto del índice CH indica que los grupos son densos y están bien separados.
No existe un valor de corte universalmente aceptable, por lo que se buscan soluciones que
presenten un cambio abrupto en la gráfica del índice CH. Si la gráfica es suave, no hay
razón para preferir una solución sobre otra.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabasz_score

inf = 2
sup = 10

puntuaciones_CH = []

for i in range(inf, sup + 1):
    algoritmo = KMeans(
        n_clusters=i,
        init='k-means++',
        max_iter=300,
        n_init=10,
        random_state=0
    )
    algoritmo.fit(x)
    puntuaciones_CH.append(calinski_harabasz_score(x, algoritmo.labels_))

ch = np.argmax(puntuaciones_CH) + 2

plt.grid(visible=True)
plt.plot(range(inf, sup + 1), puntuaciones_CH)
plt.scatter(ch, puntuaciones_CH[ch - 2], c='red', s=300)
plt.axvline(x=ch, linestyle='--', c='green', label='Punto óptimo')
plt.legend(shadow=True)
plt.title('Método de Puntuación CH')
plt.xlabel('Número de clusters')
plt.ylabel('Índice CH')
plt.show()
```

#### Combinación de métodos

Es recomendable combinar los métodos de búsqueda del número óptimo de clusters para
obtener un rango de valores óptimos más fiable. A continuación, se muestra un ejemplo que
integra las gráficas del método del codo, la puntuación de silueta y el índice CH en una
única visualización normalizada:

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, calinski_harabasz_score

inf = 2
sup = 10

wcss = []
puntuaciones_CH = []
punt_silu = []

for i in range(inf, sup + 1):
    algoritmo = KMeans(
        n_clusters=i,
        init='k-means++',
        max_iter=300,
        n_init=10,
        random_state=0
    )
    algoritmo.fit(x)

    punt_silu.append(silhouette_score(x, algoritmo.labels_))
    puntuaciones_CH.append(calinski_harabasz_score(x, algoritmo.labels_))
    wcss.append(algoritmo.inertia_)

# Normalización de las puntuaciones para visualización conjunta
punt_silu = np.array(punt_silu) / np.linalg.norm(punt_silu)
puntuaciones_CH = np.array(puntuaciones_CH) / np.linalg.norm(puntuaciones_CH)
wcss = np.array(wcss) / np.linalg.norm(wcss)

plt.grid(visible=True)
plt.plot(range(inf, sup + 1), punt_silu, label='Silueta')
plt.plot(range(inf, sup + 1), puntuaciones_CH, label='CH')
plt.plot(range(inf, sup + 1), wcss, label='Codo')
plt.legend(shadow=True, loc='upper right')
plt.title('Combinación de métodos')
plt.xlabel('Número de clusters')
plt.ylabel('Puntuación normalizada')
plt.show()
```

## Métodos de comparación de modelos

### Clasificación

#### Matriz de confusión

La **matriz de confusión** es una herramienta clave para evaluar la capacidad de un
modelo de clasificación. Relaciona los valores predichos por el modelo con los valores
reales, organizándolos en cuatro categorías:

- **True Positives (TP)**: Instancias positivas correctamente clasificadas.
- **False Positives (FP)**: Instancias negativas clasificadas incorrectamente como
  positivas.
- **True Negatives (TN)**: Instancias negativas correctamente clasificadas.
- **False Negatives (FN)**: Instancias positivas clasificadas incorrectamente como
  negativas.

La diagonal principal de la matriz (TP y TN) refleja la tasa de aciertos del modelo;
valores más elevados indican un mejor desempeño.

#### Sensibilidad y especificidad

Dos métricas derivadas de la matriz de confusión permiten evaluar la capacidad del modelo
para identificar correctamente las clases positivas y negativas.

La **sensibilidad** (_Recall_) mide la proporción de verdaderos positivos respecto al
total de instancias realmente positivas:

$$
\text{Sensibilidad} = \frac{TP}{TP + FN}.
$$

Un valor alto indica que el modelo identifica correctamente la mayoría de las instancias
positivas.

La **especificidad** mide la proporción de verdaderos negativos respecto al total de
instancias realmente negativas:

$$
\text{Especificidad} = \frac{TN}{TN + FP}.
$$

Un valor alto indica que el modelo discrimina adecuadamente las instancias negativas.
Ambas métricas se pueden expresar en porcentaje multiplicando por cien.

???+ example "Ejemplo con matriz de confusión 2×2"

    Supongamos un algoritmo de regresión logística que predice si un paciente tiene enfermedad cardíaca o no, con la siguiente matriz de confusión:

    |                        | Predice enfermedad | Predice no enfermedad |
    | ---------------------- | ------------------ | --------------------- |
    | **Enfermedad real**    | 145 (TP)           | 25 (FN)               |
    | **No enfermedad real** | 30 (FP)            | 100 (TN)              |

    El recall se calcula como:

    $$
    Recall = \frac{145}{145 + 25} = \frac{145}{170} = 0.8529 \; (85.29\%)
    $$

    La especificidad se calcula como:

    $$
    Specificity = \frac{100}{100 + 30} = \frac{100}{130} = 0.7692 \; (76.92\%)
    $$

    Esto indica que el 85.29% de los pacientes con enfermedad han sido clasificados correctamente y el 76.92% de los pacientes sin enfermedad han sido clasificados correctamente. Estas métricas permiten comparar directamente con otros modelos, como un árbol de decisión, y elegir el más adecuado según la prioridad del problema: si detectar pacientes sin enfermedad es más importante, se podría preferir la regresión logística; si detectar pacientes con enfermedad es prioritario, se podría optar por el árbol de decisión.

???+ example "Ejemplo con matriz de confusión multiclase (3×3)"

    Para matrices de confusión de mayor tamaño, la interpretación es análoga, calculando la sensibilidad y la especificidad para cada categoría. Supongamos una matriz de confusión con 3 clases A, B y C:

    | Real \ Predicho | A   | B   | C   |
    | --------------- | --- | --- | --- |
    | **A**           | 50  | 5   | 10  |
    | **B**           | 8   | 45  | 7   |
    | **C**           | 6   | 9   | 40  |

    Los valores de la diagonal principal representan las clasificaciones correctas, las filas representan la clase real y las columnas la clase predicha.

    **Recall por clase:**

    $$Recall_A = \frac{50}{50 + 5 + 10} = \frac{50}{65} = 0.7692 \; (76.92\%)$$

    $$Recall_B = \frac{45}{8 + 45 + 7} = \frac{45}{60} = 0.7500 \; (75.00\%)$$

    $$Recall_C = \frac{40}{6 + 9 + 40} = \frac{40}{55} = 0.7273 \; (72.73\%)$$

    **Especificidad por clase:**

    Para la clase A: $FP_A = 8 + 6 = 14$, $TN_A = 45 + 7 + 9 + 40 = 101$

    $$Specificity_A = \frac{101}{101 + 14} = 0.8783 \; (87.83\%)$$

    Para la clase B: $FP_B = 5 + 9 = 14$, $TN_B = 50 + 10 + 6 + 40 = 106$

    $$Specificity_B = \frac{106}{106 + 14} = 0.8833 \; (88.33\%)$$

    Para la clase C: $FP_C = 10 + 7 = 17$, $TN_C = 50 + 5 + 8 + 45 = 108$

    $$Specificity_C = \frac{108}{108 + 17} = 0.8640 \; (86.40\%)$$

    En resumen, para matrices de confusión multiclase, el recall se calcula a partir de la fila de la clase de interés (proporción de la diagonal respecto al total de la fila), mientras que la especificidad se obtiene considerando todos los valores que no pertenecen a dicha clase. Los verdaderos negativos corresponden a todas las celdas que no están ni en la fila ni en la columna de la clase de interés, y los falsos positivos son los valores de la columna de la clase de interés excluyendo la diagonal.

#### ROC y AUC

La curva **ROC** (_Receiver Operating Characteristic_) es una herramienta gráfica que
permite evaluar el rendimiento de un clasificador binario representando la relación entre
la **tasa de verdaderos positivos** (_True Positive Rate_, TPR o sensibilidad) en el eje
$y$ y la **tasa de falsos positivos** (_False Positive Rate_, FPR) en el eje $x$, ambos
con rangos comprendidos entre 0 y 1.

La diagonal principal de la gráfica ROC representa el rendimiento de un clasificador
aleatorio, es decir, aquel que tiene una proporción igual de falsos positivos y
verdaderos positivos. Los modelos cuya curva se sitúa por encima de esta diagonal
presentan un rendimiento superior al azar, mientras que los que se sitúan por debajo
tienen un rendimiento inferior. La elección de un modelo sobre otro depende de la
importancia relativa de minimizar los falsos positivos o maximizar los verdaderos
positivos según el contexto del problema.

El **AUC** (_Area Under the Curve_) mide el área bajo la curva ROC y proporciona un valor
numérico único para comparar modelos. Un valor de AUC cercano a 1 indica un modelo
excelente, mientras que un valor cercano a 0.5 indica un rendimiento similar al azar. El
AUC resulta especialmente útil para comparar modelos con diferentes curvas ROC.

En conjuntos de datos no balanceados, es habitual sustituir la tasa de falsos positivos
(FPR) por la **precisión** (_precision_), que mide la proporción de resultados positivos
correctamente clasificados respecto al total de predicciones positivas. La curva
resultante, denominada **curva Precision-Recall**, ofrece una evaluación más equilibrada
del rendimiento del modelo en estos escenarios.

## Métodos para la reducción de la dimensionalidad

### PCA

El **Análisis de Componentes Principales** (_Principal Component Analysis_, PCA) es una
técnica de reducción de dimensionalidad que transforma un conjunto de variables
posiblemente correlacionadas en un nuevo conjunto de variables no correlacionadas
denominadas **componentes principales**. Estas componentes se ordenan de manera que la
primera captura la mayor varianza posible de los datos, la segunda captura la mayor
varianza restante (siendo ortogonal a la primera), y así sucesivamente. De este modo, es
posible reducir la dimensionalidad del conjunto de datos conservando la mayor cantidad de
información posible, descartando las componentes que aportan menor varianza (consideradas
ruido).

### t-SNE

**t-SNE** (_t-distributed Stochastic Neighbor Embedding_) es una técnica de reducción de
dimensionalidad no lineal especialmente diseñada para la visualización de datos de alta
dimensionalidad en espacios de dos o tres dimensiones. A diferencia de PCA, que busca
preservar la varianza global, t-SNE se centra en preservar las relaciones de vecindad
local entre los puntos de datos. El algoritmo modela las similitudes entre puntos en el
espacio original mediante distribuciones de probabilidad y busca una representación en
baja dimensionalidad que preserve dichas similitudes, utilizando una distribución t de
Student para evitar el problema de la aglomeración de puntos.

### UMAP

**UMAP** (_Uniform Manifold Approximation and Projection_) es una técnica de reducción de
dimensionalidad basada en la teoría de variedades (_manifold learning_) y la topología
algebraica. Al igual que t-SNE, UMAP es eficaz para la visualización de datos de alta
dimensionalidad, pero ofrece varias ventajas: mayor velocidad de ejecución, mejor
preservación de la estructura global de los datos y la capacidad de realizar
transformaciones sobre nuevos datos sin necesidad de reentrenar el modelo. UMAP construye
una representación topológica de los datos en alta dimensionalidad y optimiza una
representación en baja dimensionalidad que preserve la estructura topológica original.

### Autoencoders

Los **Autoencoders** son redes neuronales diseñadas para aprender representaciones
comprimidas de los datos de forma no supervisada. Su arquitectura se compone de dos
partes fundamentales: un **encoder** $g_{\phi}(\cdot)$, parametrizado con $\phi$, que
comprime la entrada $x$ en una representación de menor dimensionalidad denominada
**espacio latente** $z$; y un **decoder** $g_{\theta}(\cdot)$, parametrizado con
$\theta$, que reconstruye la entrada original a partir de la representación latente. El
objetivo del entrenamiento es minimizar el error de reconstrucción entre la entrada
original y la salida reconstruida.

Desde una perspectiva probabilística, el encoder estima la probabilidad posterior
$q_{\phi}(z|x)$ y el decoder modela la probabilidad de generar los datos
$p_{\theta}(x|z)$.

Los autoencoders tienden al sobreajuste, por lo que se emplean diversas técnicas de
regularización para mejorar su capacidad de generalización:

- **Denoising Autoencoders**: Se agrega ruido gaussiano a la entrada o se eliminan partes
  de la imagen de forma estocástica (mediante técnicas como _Dropout_, _DropBlock_ o
  _SpatialDropout_), forzando al modelo a aprender representaciones más robustas.
- **Sparse Autoencoders**: Penalizan o fuerzan al modelo a mantener un número reducido de
  neuronas activadas simultáneamente. En el caso del **k-Sparse Autoencoder**, solo se
  mantienen activas las $k$ activaciones más altas, poniendo el resto a cero.
- **Contractive Autoencoders**: Penalizan la sensibilidad de la representación latente
  respecto a los datos de entrada, midiendo esta sensibilidad mediante la norma de
  Frobenius de la **matriz Jacobiana** de las activaciones del encoder con respecto a la
  entrada:

$$
J_f(x) = \sum_{i,j} \left( \frac{\partial h_j(x)}{\partial x_i} \right)^2.
$$

## Métodos para la imputación de datos

La imputación de datos es una técnica fundamental en la preparación de datos,
especialmente cuando se enfrentan valores faltantes en un conjunto. Dependiendo del tipo
de variable (numérica o categórica), se aplican diferentes estrategias para completar los
valores ausentes de manera coherente y eficiente.

### Imputación simple

Para variables **numéricas**, se emplean habitualmente medidas de tendencia central como
la **media** o la **mediana**. No obstante, la mediana es preferida en contextos reales
debido a su mayor robustez frente a valores atípicos o fuera de distribución. La decisión
entre usar media o mediana puede fundamentarse en un análisis estadístico preliminar,
como el estudio de la función de distribución acumulada (CDF) y el **rango
intercuartílico (IQR)**, que corresponde a la diferencia entre el percentil 75 y el
percentil 25. Esta evaluación permite identificar valores anómalos y decidir si deben
eliminarse o si la imputación debe ajustarse a una medida más robusta como la mediana.

Para variables **categóricas**, la imputación más común se realiza mediante la **moda**,
es decir, el valor más frecuente en la columna correspondiente. Estas imputaciones se
aplican por columna, es decir, por cada característica del conjunto de datos.

### Imputación basada en vecinos

Una estrategia más avanzada es el uso de métodos basados en los **vecinos más cercanos**,
como el algoritmo **k-Nearest Neighbors (k-NN)**. Este enfoque consiste en identificar,
para una muestra con valores faltantes, las muestras más similares (vecinas) utilizando
métricas de distancia, como la distancia euclídea. Una vez determinadas las $k$ muestras
más cercanas, el valor faltante se imputa en función de las características de esas
vecinas, por ejemplo, mediante la media, la mediana o la moda de los valores presentes en
ese grupo. Esta técnica permite imputar valores de forma contextualizada, mejorando la
precisión respecto a métodos globales.

### Imputación con modelos predictivos

#### MissForest

**MissForest** emplea algoritmos de aprendizaje automático como **Random Forest** para
imputar valores faltantes. El proceso consiste en realizar una imputación inicial de los
valores faltantes utilizando técnicas simples (media, mediana o moda según el tipo de
variable), entrenar un modelo Random Forest con las características completas para
predecir los valores ausentes de cada característica incompleta, actualizar los valores
imputados con las predicciones obtenidas y repetir iterativamente el proceso hasta que se
alcanza la convergencia o un número máximo de iteraciones.

MissForest es especialmente útil en contextos donde las relaciones entre variables son
complejas y no lineales, ofreciendo un balance entre precisión y robustez. La selección
del método de imputación más adecuado depende de la naturaleza de los datos, del patrón
de ausencia y del nivel de precisión requerido en el análisis posterior.

## Sistemas de detección de anomalías

Los sistemas de detección de anomalías se basan en la premisa de que el modelo se entrena
exclusivamente con datos no anómalos, de manera que pueda identificar desviaciones
significativas respecto al comportamiento normal aprendido.

### Métodos basados en densidad

Estos métodos consisten en calcular la probabilidad de que un dato pertenezca al conjunto
de datos normal. Se determina el centro del conjunto de datos y se calcula la
probabilidad de cada punto en función de su distancia respecto a dicho centro,
considerando dos o más características. Los puntos con baja probabilidad (alejados del
centro) se consideran anomalías. Para ello, se establece un **umbral de probabilidad**
que separa los datos normales de los anómalos.

### Métodos basados en distribuciones gaussianas

Otra aproximación consiste en modelar la media y la varianza de cada parámetro a partir
de una **distribución gaussiana**. Los datos que se encuentran en las colas de la
distribución (con probabilidad inferior al umbral establecido) se clasifican como
anomalías. Es recomendable incluir datos anómalos en el conjunto de validación para
evaluar correctamente el rendimiento del detector, y la validación cruzada resulta
especialmente útil en este contexto.

### Detección de anomalías frente al aprendizaje supervisado

La detección de anomalías se diferencia del aprendizaje supervisado en varios aspectos
fundamentales. En la detección de anomalías, se desconocen los tipos de anomalías
posibles y no se asume que los datos nuevos sigan la misma distribución que los datos de
entrenamiento. En cambio, un clasificador supervisado dispone de ejemplos tanto positivos
como negativos y espera que las muestras futuras sigan una distribución similar a la
observada durante el entrenamiento.

Puede darse el caso de que las características de los datos no presenten una forma
gaussiana, lo que requiere aplicar **transformaciones** para normalizar su distribución.
Algunas transformaciones habituales incluyen el logaritmo de los datos ($\log(x)$), el
logaritmo más una constante ($\log(x + c)$) o la aplicación de funciones exponenciales
con diferentes parámetros. El objetivo es encontrar la transformación que haga que los
datos se aproximen a una distribución normal.

### Flujos de normalización

Los **flujos de normalización** (_Normalizing Flows_) son modelos generativos invertibles
que transforman una distribución de datos compleja en una distribución conocida, como la
distribución normal, preservando la dimensionalidad de los datos. A diferencia de otros
modelos generativos como los VAE o las GAN, los flujos de normalización aprenden
directamente la función de densidad de probabilidad $p(x)$ de los datos.

El principio fundamental se basa en una función biyectiva $f$ que mapea los datos $x$ a
un espacio latente $z$:

$$
f: x \rightarrow z,
$$

donde $z$ sigue una distribución conocida (generalmente gaussiana) y $x$ tiene la misma
dimensionalidad que $z$. La función $f$ es invertible, lo que permite tanto la generación
de nuevos datos como la evaluación de la densidad de probabilidad.

La relación entre las distribuciones se establece mediante la **regla del cambio de
variables**. Dada una distribución prior $p(z)$ (gaussiana) y una función invertible $f$,
la densidad de probabilidad de $x$ se determina como:

$$
\log p(x) = \log p(z) + \log \left| \det \frac{\partial f}{\partial x} \right|,
$$

donde el segundo término es el logaritmo del valor absoluto del determinante de la matriz
Jacobiana de la transformación. Para hacer la función más expresiva, se pueden componer
múltiples funciones invertibles aprendibles:

$$
z_0 \xrightarrow{f_1} z_1 \xrightarrow{f_2} \cdots \xrightarrow{f_K} z_K = x.
$$

De esta forma, partiendo de una distribución gaussiana simple, se aplican sucesivas
transformaciones invertibles que permiten modelar distribuciones de datos arbitrariamente
complejas. El entrenamiento se realiza minimizando el negativo del log-likelihood de los
datos observados.

## Sistemas de recomendación

Los **sistemas de recomendación** se utilizan para predecir las preferencias de los
usuarios sobre elementos que aún no han evaluado. Un ejemplo típico es un conjunto de
usuarios con puntuaciones de películas, donde ciertos usuarios no han visto todas las
películas disponibles. El objetivo es estimar la puntuación que un usuario asignaría a
las películas no vistas.

Existen dos enfoques principales. El **filtrado colaborativo** se basa en las similitudes
entre usuarios o entre elementos: si dos usuarios han puntuado de forma similar un
conjunto de películas, es probable que sus preferencias coincidan en películas no
evaluadas. El **filtrado basado en contenido** utiliza las características de los
elementos (género, director, actores) y las preferencias previas del usuario para
recomendar elementos con características similares a los que el usuario ha valorado
positivamente.

## Redes neuronales bayesianas

Las **Redes Neuronales Bayesianas** (_Bayesian Neural Networks_, BNNs) representan un
paradigma que integra la inferencia bayesiana en los modelos de aprendizaje profundo. A
diferencia de las redes neuronales tradicionales, donde los parámetros (pesos y sesgos)
son valores fijos determinados mediante algoritmos de optimización como la
retropropagación y el descenso del gradiente, las BNNs modelan estos parámetros como
**distribuciones de probabilidad**. Este cambio conceptual permite capturar la
incertidumbre inherente tanto en los parámetros del modelo como en sus predicciones,
ofreciendo una comprensión más completa de las limitaciones y la fiabilidad del modelo.

### Fundamentos teóricos de la inferencia bayesiana

La inferencia bayesiana se basa en el **Teorema de Bayes**, que proporciona un marco
matemático para actualizar las creencias sobre un modelo cuando se dispone de nuevas
observaciones. El teorema se expresa matemáticamente como:

$$
P(\theta | D) = \frac{P(D | \theta) P(\theta)}{P(D)},
$$

donde cada componente representa un aspecto específico del proceso de aprendizaje:

- $P(\theta)$ — **Conocimiento previo (distribución prior)**: Representa las creencias
  iniciales sobre los parámetros del modelo antes de observar los datos. Por ejemplo, si
  se desea predecir la altura de una persona, la prior podría establecer que la mayoría
  de las alturas se encuentran entre 1.50 y 2.00 metros, con una media alrededor de 1.70
  metros.
- $P(D | \theta)$ — **Compatibilidad con los datos (verosimilitud)**: Mide la
  probabilidad de los datos observados dado un conjunto específico de parámetros. Evalúa
  qué tan compatibles son las observaciones con las predicciones del modelo.
- $P(D)$ — **Normalización (evidencia)**: Actúa como factor de normalización que
  garantiza que la distribución posterior sume uno, satisfaciendo las propiedades de una
  distribución de probabilidad válida. Representa la probabilidad total de observar los
  datos bajo todos los valores posibles de los parámetros.
- $P(\theta | D)$ — **Conocimiento actualizado (distribución posterior)**: Es el
  resultado final del proceso bayesiano: las creencias actualizadas sobre los parámetros
  después de considerar tanto el conocimiento previo como los datos observados.

### Modelado probabilístico de parámetros

En una BNN, cada peso y sesgo se representa mediante una distribución de probabilidad,
típicamente una distribución normal con media 0 y desviación típica 1, denotada como
$\mathcal{N}(0, 1)$. El proceso de entrenamiento no busca estimar un único valor para
cada parámetro, sino ajustar la distribución posterior que mejor explique los datos
observados.

Este enfoque requiere parametrizar las distribuciones a través de la media y la
desviación típica, actualizándolas iterativamente durante el entrenamiento. El objetivo
es aprender una distribución posterior $P(\theta | D)$ sobre los parámetros $\theta$
dados los datos $D$, donde la distribución prior $P(\theta)$ típicamente asume una forma
gaussiana estándar y la distribución posterior se ajusta durante el entrenamiento para
reflejar el conocimiento adquirido a partir de los datos.

### Métodos de aproximación de la distribución posterior

Dado que el cálculo exacto de la distribución posterior es computacionalmente intratable
en la mayoría de los casos prácticos, se emplean técnicas de inferencia aproximada:

- **Inferencia variacional**: Aproxima la distribución posterior con una distribución más
  simple $q(\theta)$, optimizando la divergencia de Kullback-Leibler (KL) entre
  $q(\theta)$ y $P(\theta | D)$. Este método ofrece eficiencia computacional y
  escalabilidad para modelos grandes, siendo la opción más común en aplicaciones
  prácticas.
- **Markov Chain Monte Carlo (MCMC)**: Métodos basados en muestreo que aproximan la
  posterior generando múltiples muestras. Aunque son computacionalmente más costosos,
  proporcionan aproximaciones más precisas y resultan útiles cuando se prioriza la
  precisión sobre la eficiencia.

### Función de pérdida ELBO

La optimización en las BNNs se basa fundamentalmente en maximizar el **Evidence Lower
Bound (ELBO)**:

$$
\mathcal{L} = \mathbb{E}_{q(\theta)}[\log P(D | \theta)] - KL(q(\theta) \| P(\theta)).
$$

Esta función objetivo equilibra dos componentes críticos. El primer componente,
denominado **término de verosimilitud** $\mathbb{E}_{q(\theta)}[\log P(D | \theta)]$,
maximiza la probabilidad de los datos observados bajo la distribución aproximada
$q(\theta)$, asegurando que el modelo mantenga un buen ajuste a los datos de
entrenamiento. El segundo componente, denominado **término de regularización**
$KL(q(\theta) \| P(\theta))$, minimiza la divergencia KL entre la distribución posterior
aproximada y la distribución prior, actuando como fuerza regularizadora que previene el
sobreajuste.

La divergencia KL se formula de manera diferente según el tipo de distribución. Para
distribuciones discretas:

$$
KL(P \| Q) = \sum_{x} P(x) \log \frac{P(x)}{Q(x)}.
$$

Para distribuciones continuas:

$$
KL(P \| Q) = \int_{-\infty}^{\infty} p(x) \log \frac{p(x)}{q(x)} \, dx.
$$

### Inferencia y cuantificación de la incertidumbre

Durante la fase de inferencia, una BNN genera predicciones muestreando repetidamente de
la distribución de pesos. Este proceso típicamente implica múltiples inferencias
independientes (comúnmente entre 50 y 1000 repeticiones) para la misma entrada,
produciendo un conjunto de predicciones que permite calcular la **media** de las
predicciones como estimación final y determinar la **varianza** o desviación típica como
medida cuantitativa de la incertidumbre asociada.

Esta capacidad de cuantificar la incertidumbre es la principal ventaja de las BNNs,
proporcionando información sobre la fiabilidad de cada predicción individual.

### Tipos de incertidumbre

En el contexto de las BNNs, se distinguen dos tipos fundamentales de incertidumbre:

- **Incertidumbre epistémica**: Se refiere a lo que el modelo no sabe y está directamente
  relacionada con los parámetros del modelo ($y = f(x)$). Es **reducible** con más datos
  o mayor complejidad del modelo.
- **Incertidumbre aleatoria**: Se refiere a la variabilidad inherente en el entorno y
  está relacionada con los datos de entrada. Es **irreducible**, ya que proviene del
  ruido intrínseco del proceso generador de datos.

### Aplicaciones

Las BNNs son particularmente valiosas en contextos donde la cuantificación de la
incertidumbre es crítica: bioquímica y descubrimiento de fármacos, diagnóstico médico,
finanzas, robótica y aprendizaje por refuerzo, y telecomunicaciones. Sus ventajas sobre
los modelos deterministas incluyen la cuantificación formal de la incertidumbre, una
regularización efectiva mediante las distribuciones prior, un mejor rendimiento con datos
limitados y una mayor interpretabilidad de las predicciones.

Las BNNs se integran de forma natural con la **programación probabilística**, un
paradigma que permite describir modelos estadísticos complejos mediante código
declarativo, ampliando significativamente su aplicabilidad en sistemas donde el modelado
explícito de la incertidumbre es esencial.

## Modelos de mezcla de densidades

Los **Modelos de Mezcla de Densidades** (_Mixture Density Networks_, MDN) combinan redes
neuronales con modelos de mezcla para obtener a la salida del modelo la distribución de
probabilidad completa $P(y|x)$, en lugar de un único valor puntual. La salida del modelo
describe la distribución que modela los datos objetivo dados los datos de entrada.

Un MDN modela la distribución condicional como una **mezcla de distribuciones
gaussianas**, donde cada componente de la mezcla se caracteriza por tres parámetros:

- $\mu_i$: La media (centro de la distribución).
- $\sigma_i^2$: La varianza (ancho de la distribución).
- $w_i$: El peso (importancia relativa de cada componente), donde $\sum w_i = 1$.

La red neuronal recibe la entrada $x$ y produce como salida los parámetros de todas las
componentes de la mezcla. La función de pérdida se basa en el negativo del
log-likelihood:

$$
-\log p(y|x) = -\log \left( \sum_{j=1}^{m} w_j \cdot \mathcal{N}(y | \mu_j, \sigma_j^2) \right).
$$

Para la implementación práctica, se utilizan las distribuciones de probabilidad de las
bibliotecas de aprendizaje profundo (como `torch.distributions.Normal`) y la función
`logsumexp` para garantizar la estabilidad numérica en el cálculo del log-likelihood.

### Consideraciones de implementación

Para la **varianza**, se recomienda utilizar la función de activación **ELU modificada**:
$\text{ELU}(z) + 1 + \epsilon$ (donde $\epsilon = 10^{-15}$). La función ELU se desplaza
a la zona de los positivos sumando 1, y se añade un valor pequeño $\epsilon$ para
garantizar la estabilidad numérica. Esta elección evita que la varianza crezca
excesivamente y proporciona un comportamiento suave que se aproxima a lineal para valores
altos.

Para los **pesos** de la mezcla, se puede sustituir la función **Softmax** estándar por
**Gumbel-Softmax**, que genera distribuciones más agresivas y puede asignar probabilidad
cercana a cero a componentes sin importancia, mientras que Softmax produce distribuciones
más suaves. Otras técnicas para evitar el colapso de componentes (donde el modelo ignora
alguna distribución) incluyen la regularización de pesos y la inicialización del centro
de cada gaussiana a partir de un precálculo sobre los datos.

### Intervalos de confianza

A partir de las distribuciones obtenidas por el MDN, es posible calcular **intervalos de
confianza** (_confidence intervals_), que representan un rango de valores que, con cierta
probabilidad (nivel de confianza), contiene el verdadero valor de un parámetro
desconocido. Por ejemplo, un intervalo de confianza del 95% indica que, al repetir un
experimento varias veces, aproximadamente el 95% de los intervalos calculados contendrán
el valor verdadero. Además, se pueden obtener la media, la varianza, los percentiles y
realizar comparaciones visuales y cuantitativas con las distribuciones observadas en los
datos de entrenamiento.

### Estabilidad numérica

Durante el entrenamiento de MDNs, pueden aparecer valores `NaN` debido a varias causas:
el logaritmo de un valor cercano a cero, divisiones con denominador muy pequeño o la
exponencial de un valor muy grande. Para mitigar estos problemas, se pueden emplear
técnicas como el **gradient clipping** (limitación del gradiente), la **regularización de
pesos** y la **normalización por lotes** (_Batch Normalization_) en la capa de salida.
