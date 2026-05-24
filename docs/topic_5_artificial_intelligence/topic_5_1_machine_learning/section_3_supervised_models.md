---
authors: Daniel Bazo Correa
description: Modelos de aprendizaje supervisado.
title: Modelos supervisados
---

## Modelos supervisados

Una vez comprendido el concepto de modelo de aprendizaje automático, donde se utilizan
datos para modelar su distribución, analizar relaciones y extraer conocimiento, es
posible aplicar estos modelos para realizar tareas como clasificación de nuevos datos,
predicción de valores y otras aplicaciones. A continuación, se presentan algunos de los
métodos más utilizados.

!!! tip

    A pesar del auge de los modelos de lenguaje basados en arquitecturas de **aprendizaje profundo (_Deep Learning_)**, su aplicación sigue siendo limitada en ciertos contextos debido a la gran cantidad de datos y capacidad de cómputo que requieren, así como a la necesidad de explicabilidad en sectores específicos. Por ello, los métodos tradicionales siguen desempeñando un papel fundamental, especialmente en el análisis de datos **tabulares**, los cuales representan la mayoría de los datos empresariales.

    Es recomendable iniciar con modelos más sencillos para comprender los resultados y evaluar su utilidad en función de los objetivos del análisis. A partir de esta base, y considerando factores como el tiempo y los recursos disponibles, se puede optar por soluciones más complejas que ofrezcan un mayor retorno de inversión (ROI).

### Naïve Bayes

El clasificador **Naïve Bayes** es un modelo probabilístico basado en el **Teorema de
Bayes** que asume independencia condicional entre las características dadas la clase. A
pesar de que esta suposición de independencia rara vez se cumple en la práctica, el
modelo ofrece un rendimiento sorprendentemente bueno en muchas aplicaciones,
especialmente en clasificación de texto y filtrado de spam.

El Teorema de Bayes permite calcular la probabilidad posterior de una clase $C_k$ dado
un vector de características $\mathbf{x}$:

$$
P(C_k | \mathbf{x}) = \frac{P(\mathbf{x} | C_k) \cdot P(C_k)}{P(\mathbf{x})}.
$$

Bajo la suposición de independencia condicional, la verosimilitud se descompone como el
producto de las probabilidades individuales de cada característica:

$$
P(\mathbf{x} | C_k) = \prod_{i=1}^{n} P(x_i | C_k).
$$

El clasificador asigna a cada nueva observación la clase con mayor probabilidad
posterior. Existen diferentes variantes del modelo según la distribución asumida para
las características: **Gaussiano** (para datos continuos con distribución normal),
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
Forest soluciona esta limitación mediante un enfoque basado en el aprendizaje conjunto
de múltiples árboles de decisión.

El proceso de construcción de un modelo Random Forest se compone de tres etapas
fundamentales. En primer lugar, se generan múltiples subconjuntos de entrenamiento
mediante **muestreo aleatorio con reemplazo** a partir del conjunto de datos original,
un procedimiento conocido como _bootstrap sampling_. Como consecuencia, algunas
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
incorrectamente por el conjunto de árboles, se obtiene el llamado _out-of-bag error_,
que actúa como una estimación fiable del error de generalización.

El número de características consideradas en cada división puede ajustarse como
hiperparámetro del modelo. Este control permite optimizar el equilibrio entre sesgo y
varianza, mejorando la precisión y robustez del Random Forest frente a los árboles de
decisión individuales.

### Máquina de vectores de soporte

La **Máquina de Vectores de Soporte** (_Support Vector Machine_, SVM) es un algoritmo de
aprendizaje supervisado utilizado tanto para clasificación como para regresión. Su
principio fundamental consiste en encontrar el **hiperplano** que mejor separa las
clases en el espacio de características, maximizando el **margen**, es decir, la
distancia entre el hiperplano y los puntos de datos más cercanos de cada clase,
denominados **vectores de soporte**.

En problemas donde los datos no son linealmente separables, las SVM emplean el
denominado **truco del kernel** (_kernel trick_), que consiste en proyectar los datos a
un espacio de mayor dimensionalidad donde sí resultan separables linealmente. Entre los
kernels más utilizados se encuentran el lineal, el polinómico y el de función de base
radial (RBF).

La formulación matemática de la SVM busca minimizar una función objetivo que equilibra
la maximización del margen con la penalización de las clasificaciones erróneas,
controlada por un hiperparámetro de regularización $C$. Un valor alto de $C$ prioriza la
clasificación correcta de todos los puntos (riesgo de sobreajuste), mientras que un
valor bajo permite mayor tolerancia a errores (mayor generalización).

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

donde $G$ es la suma de los gradientes (primeras derivadas de la función de pérdida),
$H$ es la suma de las hessianas (segundas derivadas de la función de pérdida) y
$\lambda$ es el parámetro de regularización. La **ganancia** (_gain_) de una división se
calcula como la diferencia entre la suma de las similaridades de los nodos hijos y la
similaridad del nodo padre:

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
