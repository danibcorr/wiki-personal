---
authors: Daniel Bazo Correa
description: Fundamentos del Deep Learning.
title: Deep Learning
---

## Bibliografía

- [Alice's Adventures in a differentiable wonderland: A primer on designing neural networks (Volume I)](https://amzn.eu/d/3oYyuHg)
- [Deep Learning for Coders with Fastai and PyTorch: AI Applications Without a PhD](https://course.fast.ai/Resources/book.html)
- [Stanford](https://youtube.com/playlist?list=PLoROMvodv4rNjRoawgt72BBNwL2V7doGI&si=TXQ-EA7J7sAwfKEQ).

## Introducción al aprendizaje profundo

Antes de abordar el estudio del **aprendizaje profundo (_Deep Learning_)**, resulta
esencial comprender el concepto de inteligencia, una noción que, aunque aparentemente
simple, presenta una complejidad notable cuando se intenta definir con precisión. En
términos generales, la inteligencia puede entenderse como la **capacidad de procesar
información y utilizarla para tomar decisiones orientadas al logro de objetivos
específicos**.

Desde una perspectiva biológica, el cerebro humano constituye el ejemplo más sofisticado
de sistema inteligente conocido. El **hipocampo**, una estructura cerebral fundamental,
desempeña funciones esenciales de memoria, navegación y planificación, construyendo
**mapas cognitivos** que representan el mundo físico en un espacio mental interno. Las
neuronas de posicionamiento (_place cells_) se activan en ubicaciones específicas del
entorno, generando patrones de actividad incluso en espacios tridimensionales. Cuando el
entorno cambia, se produce un **remapeo neuronal**: las neuronas dejan de activarse en
las mismas zonas y se reorganizan en función de las nuevas condiciones. Este remapeo no
depende únicamente de cambios físicos, sino también de factores contextuales como los
estímulos olfativos, lo que evidencia que estas representaciones son **dependientes del
contexto** y no se limitan a codificar información puramente espacial. El hipocampo
integra múltiples variables continuas para construir estas representaciones, mientras que
el **neocórtex** se encarga de procesar información más abstracta, incluyendo el lenguaje
y el conocimiento conceptual.

Dentro del neocórtex se encuentra la **columna cortical**, considerada la unidad
fundamental de procesamiento inteligente. La **hipótesis columnar** postula que, si el
_hardware_ biológico (la columna cortical replicada) es universal e idéntico en todas sus
instancias, entonces el algoritmo que gobierna su funcionamiento también debe serlo. Esta
idea se relaciona directamente con el concepto de **inteligencia artificial general
(AGI)**: un único algoritmo universal capaz de adaptarse a cualquier tipo de entrada,
donde solo varía el _input_ que recibe. Cada columna cortical opera como un sistema
independiente, pero existe un **traspaso de mensajes entre columnas** que puede
interpretarse como una interfaz de comunicación (análoga a una API en sistemas
informáticos). Incrementar el número de columnas corticales equivale a aumentar la
capacidad de cómputo del sistema. A medida que el cerebro adquiere características del
mundo, construye **marcos de referencia** que permiten localizar y relacionar conceptos,
facilitando la generación de nuevas acciones y predicciones, un proceso conocido como
**integración de caminos** (_path integration_). Las columnas corticales emplean además
un mecanismo de **votación por mayoría** para alcanzar un consenso sobre lo que se
percibe, donde la entrada de una columna puede ser tanto información sensorial directa
como información procesada por otra columna cortical.

Este concepto constituye el fundamento del campo de la **Inteligencia Artificial (IA)**,
disciplina que se dedica al desarrollo de técnicas y algoritmos capaces de reproducir
ciertos aspectos del comportamiento humano. La IA busca emular la inteligencia mediante
sistemas computacionales, permitiendo que las máquinas procesen información, se adapten a
diversos contextos y realicen predicciones para resolver problemas de manera autónoma,
minimizando la intervención humana.

Dentro de la IA se encuentra el **aprendizaje automático (_Machine Learning_)**, cuyo
propósito es permitir que las máquinas **aprendan a partir de la experiencia**, sin
necesidad de recibir instrucciones explícitas para cada tarea. En lugar de programar
manualmente cada paso del proceso, se diseñan algoritmos que **identifican patrones en
los datos**, ajustando sus parámetros internos con el objetivo de mejorar progresivamente
su rendimiento a medida que acumulan ejemplos. Este proceso de aprendizaje se guía
mediante una **función objetivo**, la cual mide el grado de aproximación del sistema a la
meta deseada.

El investigador Andrej Karpathy ha descrito este paradigma como "software 2.0", en
contraposición al enfoque tradicional de programación. En el "software 1.0", el
programador define de forma explícita las reglas y procedimientos que el sistema debe
ejecutar. En cambio, en el "software 2.0", el programador proporciona **ejemplos,
recompensas o etiquetas** que guían el proceso de optimización del algoritmo, permitiendo
que el propio sistema descubra de manera implícita las reglas necesarias para cumplir la
tarea. Este cambio de paradigma marca una transición desde la programación manual hacia
el aprendizaje basado en datos, donde el sistema adquiere la capacidad de generalizar más
allá de los ejemplos proporcionados durante el entrenamiento.

El aprendizaje profundo representa una evolución dentro del aprendizaje automático. Su
principal característica radica en el uso de **redes neuronales artificiales** como
núcleo del proceso de aprendizaje. Estas redes, inspiradas en la estructura y el
funcionamiento del cerebro biológico humano, están compuestas por múltiples capas de
procesamiento que permiten **aprender representaciones jerárquicas de la información**.
Gracias a esta arquitectura, el aprendizaje profundo puede capturar relaciones complejas
entre variables, lo que le permite reconocer patrones altamente complejos en los datos.
Como resultado, el aprendizaje profundo ha demostrado un rendimiento excepcional en
tareas que antes se consideraban exclusivas del razonamiento humano, tales como el
reconocimiento de imágenes, el procesamiento del lenguaje natural, el análisis de audio y
la interpretación de grandes volúmenes de datos no estructurados.

Las ventajas fundamentales del aprendizaje profundo pueden resumirse en tres aspectos. En
primer lugar, la **simplicidad**: elimina la necesidad de ingeniería manual de
características, sustituyendo complejas cadenas de procesamiento por modelos entrenables
de extremo a extremo construidos con unas pocas operaciones tensoriales. En segundo
lugar, la **escalabilidad**: se beneficia enormemente de la paralelización en GPU y TPU,
y al entrenarse sobre pequeños lotes de datos, puede trabajar con conjuntos de datos de
tamaño arbitrario. En tercer lugar, la **versatilidad y reutilización**: los modelos
entrenados pueden actualizarse con datos adicionales sin reiniciar el proceso, y las
representaciones aprendidas pueden transferirse a nuevas tareas, lo que permite construir
sistemas cada vez más potentes a partir de trabajo previo.

### Escalabilidad y leyes de crecimiento

Un aspecto esencial en la evolución del aprendizaje profundo es el estudio de las **leyes
de escalado neuronal (_Neural Scaling Laws_)**, las cuales describen comportamientos
empíricamente observables en el rendimiento de los modelos a medida que se incrementan
los recursos disponibles. Estas leyes establecen que, al aumentar de forma sistemática el
tamaño de los conjuntos de datos, la capacidad computacional y el número de parámetros de
un modelo, se obtiene una mejora predecible y sostenida en la precisión y eficiencia de
las predicciones.

Este fenómeno ha guiado gran parte de la estrategia de desarrollo en la industria
tecnológica contemporánea. Empresas líderes como Google, Meta, OpenAI y otras
organizaciones han adoptado el principio del escalado como un eje fundamental de su
investigación y desarrollo, apostando por la creación de modelos cada vez más grandes y
sofisticados. La aplicación práctica de estas leyes ha dado lugar a la construcción de
redes neuronales más profundas y con un mayor número de neuronas, lo que ha impulsado la
aparición de los denominados **modelos de gran escala**, entre los que destacan los
**modelos de lenguaje de gran tamaño (_Large Language Models, LLMs_)**. Estos modelos han
demostrado una capacidad notable para generalizar conocimientos, generar texto coherente,
responder preguntas complejas y adaptarse a una amplia variedad de tareas cognitivas.
Además, exhiben capacidades emergentes, como el razonamiento en cadena, la resolución de
problemas matemáticos o la comprensión de instrucciones complejas, que no fueron
programadas explícitamente durante su entrenamiento.

En paralelo, existe una tendencia creciente en la investigación que busca optimizar la
eficiencia computacional sin sacrificar la calidad del modelo. Esta línea de trabajo
resulta relevante en entornos donde los recursos son limitados, como los dispositivos
móviles, los sistemas embebidos o las plataformas de Internet de las Cosas (_Internet of
Things_, IoT).

Para abordar estas limitaciones, se desarrollan múltiples estrategias, entre ellas:

- **Arquitecturas especializadas:** Diseños de redes más ligeras y eficientes, adaptadas
  a las restricciones de hardware.
- **Optimización a nivel de hardware:** Uso de unidades de procesamiento específicas,
  como _Graphics Processing Units_ (GPU), _Tensor Processing Units_ (TPU) o _Neural
  Processing Unit_ (NPU), capaces de acelerar las operaciones matriciales y reducir el
  consumo de energía.
- **Compilación a lenguajes de bajo nivel:** Traducción del modelo a representaciones más
  próximas al hardware para mejorar el rendimiento.

En conjunto, estas estrategias permiten democratizar el acceso y uso del aprendizaje
profundo, posibilitando su ejecución incluso en equipos de consumo general. De este modo,
el campo avanza no solo hacia modelos más grandes y potentes, sino también hacia sistemas
más eficientes, accesibles y sostenibles desde el punto de vista energético y económico.

### Memoria implícita y modelos fundacionales

Las redes neuronales artificiales poseen la capacidad de aproximar distribuciones de
probabilidad a partir de los datos de entrada. En esencia, su propósito es construir una
función parametrizada que permita comprender, representar y generalizar el comportamiento
de los datos observados.

En los modelos actuales, esta capacidad alcanza niveles en los que la red puede llegar a
memorizar parte de los datos de entrenamiento. Aunque las arquitecturas contemporáneas no
suelen incorporar mecanismos explícitos de memoria, como una base de datos interna o una
estructura dedicada al almacenamiento, la información queda codificada en los propios
parámetros del modelo. Este fenómeno se manifiesta en la activación selectiva de neuronas
ante determinados contextos, lo que sugiere que la red conserva rastros de información
previa y los utiliza para procesar nuevas entradas.

Aunque esta memoria no sea explícita, existen líneas de investigación que buscan extender
o complementar este comportamiento con mecanismos dedicados. En algunos casos, se
exploran estructuras que incorporan memoria persistente, como las redes recurrentes o los
_Transformers_ con mecanismos de atención. En otros, se utilizan recursos _hardware_,
como la memoria caché o el almacenamiento intermedio en disco, para gestionar información
temporal durante los procesos de entrenamiento e inferencia. Estas aproximaciones buscan
aumentar la capacidad de los modelos para manejar secuencias largas, retener información
contextual de manera más eficiente y facilitar un aprendizaje más continuo.

La existencia de esta memoria implícita plantea, además, una distinción fundamental entre
los **datos dentro de distribución (_in-distribution_)** y los **datos fuera de
distribución (_out-of-distribution_)**. Los primeros se refieren a ejemplos similares a
los utilizados durante el entrenamiento, en los cuales el modelo optimiza su función
objetivo hasta alcanzar la **convergencia**, es decir, hasta que los ajustes en los
parámetros dejan de producir mejoras significativas en el desempeño. Los segundos, en
cambio, corresponden a entradas que difieren significativamente del conjunto de
entrenamiento, lo que puede provocar fallos, respuestas erróneas o predicciones con alta
incertidumbre. Por ejemplo, un modelo entrenado exclusivamente para reconocer perros no
es capaz de identificar correctamente un gato, ya que este pertenece a una distribución
distinta de patrones visuales y características. Sin embargo, debido a que los conjuntos
de datos empleados actualmente son cada vez más amplios, diversos y heterogéneos, esta
separación entre ambos tipos de datos tiende a desdibujarse. La capacidad de los modelos
para generalizar más allá de su distribución de entrenamiento constituye un área activa
de investigación.

En este contexto, el estudio de la **capacidad de generalización** de los modelos
adquiere un papel central. Los avances recientes han explorado estrategias que permiten
mejorar la inferencia y la estimación de incertidumbre. Entre estas estrategias destacan
el uso de técnicas de cálculo en tiempo de inferencia (_test-time computation_), que
permiten al modelo dedicar más recursos computacionales a problemas complejos en el
momento de la predicción, las redes neuronales bayesianas, que incorporan distribuciones
de probabilidad sobre los parámetros en lugar de valores fijos, y técnicas como _Monte
Carlo Dropout_, que simula múltiples predicciones mediante la desactivación aleatoria de
neuronas durante la inferencia. Estas aproximaciones posibilitan la creación de
**intervalos de confianza** para las predicciones, otorgando a los modelos una mayor
robustez frente a datos desconocidos y una capacidad para expresar el grado de seguridad
de sus respuestas.

Paralelamente, existe el fenómeno del **olvido catastrófico (_catastrophic
forgetting_)**, que describe la tendencia de las redes neuronales a perder información
previamente aprendida cuando incorporan nuevo conocimiento. Este problema representa uno
de los mayores desafíos del **aprendizaje continuo (_continual learning_)**, un paradigma
en el que se busca que el modelo sea capaz de actualizarse de manera progresiva sin
olvidar su conocimiento previo. La solución a este desafío requiere el desarrollo de
mecanismos que equilibren la plasticidad (la capacidad de aprender nueva información) con
la estabilidad (la preservación del conocimiento existente).

La evolución de estas ideas conduce al desarrollo de los **modelos fundacionales
(_foundation models_)**, que se conciben como sistemas de aprendizaje generalista capaces
de adaptarse a múltiples dominios y tareas. Estos modelos no están diseñados para una
tarea específica, sino que aprenden representaciones amplias y abstractas del mundo que
pueden reutilizarse en diversos contextos. A partir de una base preentrenada sobre
grandes volúmenes de datos, es posible **ajustarlos finamente (_fine-tuning_)** para
resolver tareas concretas sin necesidad de entrenarlos desde cero.

### El aprendizaje como problema de optimización

El proceso de aprendizaje en redes neuronales debe entenderse, desde una perspectiva
formal, como un problema de optimización matemática. En este marco, un modelo se define a
partir de un conjunto de parámetros ajustables que determinan su comportamiento. Estos
parámetros representan el conocimiento adquirido durante el entrenamiento y se actualizan
progresivamente con el objetivo de **minimizar una función que mide el error del modelo**
respecto a los datos observados.

Las redes neuronales se consideran **modelos diferenciables** porque su mecanismo de
aprendizaje se basa en la capacidad de **calcular derivadas parciales** de una **función
de coste** (también denominada **función de pérdida**) con respecto a sus parámetros.
Esta función cuantifica la discrepancia entre las predicciones generadas por el modelo y
los valores reales, actuando como una medida de su rendimiento. Los parámetros
aprendibles son, por tanto, aquellas variables internas que se modifican iterativamente
para reducir dicha discrepancia y mejorar la capacidad predictiva del sistema.

El proceso de aprendizaje es **iterativo y dinámico**. Consiste en un ciclo continuo de
cálculo, actualización y evaluación que se repite hasta alcanzar un criterio de parada
determinado. Este criterio puede definirse en función del número de iteraciones, de la
estabilidad alcanzada por la función de coste o de la satisfacción de una métrica de
desempeño preestablecida. En la práctica, este procedimiento se implementa mediante
algoritmos de optimización, entre los que destaca el **descenso del gradiente**, que
ajusta los parámetros en la dirección que más reduce la pérdida. Existen además variantes
adaptativas, que mejoran la eficiencia del proceso y aceleran la convergencia en
arquitecturas complejas.

Una herramienta fundamental que posibilita este proceso es la **diferenciación
automática**, la cual permite calcular de manera eficiente las derivadas necesarias para
actualizar los parámetros del modelo. Gracias a esta técnica, es posible entrenar redes
profundas sin requerir una derivación manual de las expresiones analíticas. La
diferenciación automática constituye, por tanto, uno de los pilares que han hecho viable
la expansión moderna del aprendizaje profundo.

No obstante, el carácter diferenciable del modelo impone ciertas restricciones sobre los
tipos de datos que pueden procesarse directamente. Las derivadas solo son aplicables a
funciones continuas, por lo que representaciones discretas (como caracteres, palabras o
números enteros) no pueden utilizarse tal cual en los cálculos diferenciales. Para
hacerlos compatibles, los datos deben transformarse en representaciones numéricas
continuas, generalmente en forma de **vectores o tensores**, que permitan aplicar las
operaciones matemáticas requeridas durante el entrenamiento.

Este proceso de conversión se denomina **_embedding_**, y su función no se limita
únicamente a permitir el procesamiento diferencial, sino también a **capturar las
relaciones semánticas, estructurales y contextuales entre los elementos de los datos**.
Por ejemplo, en el caso del lenguaje natural, los _embeddings_ permiten representar
palabras o frases de modo que aquellas con significados similares se encuentren próximas
en el **espacio vectorial**, que constituye el espacio matemático multidimensional creado
por el propio modelo. Este espacio permite al sistema establecer y mapear las relaciones
semánticas entre los datos de manera cuantitativa, facilitando operaciones como la
comparación de similitudes, la búsqueda de analogías o la agrupación de conceptos
relacionados. De este modo, los _embeddings_ transforman información simbólica en
representaciones geométricas que preservan y codifican el significado subyacente de los
datos originales.

A medida que el modelo optimiza su función de coste, desarrolla internamente una forma de
**entender y codificar la información** que refleja la estructura subyacente de los
datos. Cuanto mejor sea la capacidad del modelo para comprimir la información sin perder
significado, más eficaz será su desempeño. La compresión eficiente implica que el modelo
ha aprendido a distinguir entre la información relevante y la irrelevante, capturando
solo aquellos patrones que resultan esenciales para la tarea. Este principio de
compresión es, en última instancia, una manifestación del aprendizaje mismo: la habilidad
de mapear, abstraer y recuperar información compleja sin necesidad de conservar todos los
detalles explícitos.

### Arquitecturas y tipos de datos

El aprendizaje profundo se adapta a diferentes problemas mediante el uso de arquitecturas
especializadas, diseñadas para extraer información relevante según la naturaleza y
estructura del tipo de datos analizados. Cada arquitectura incorpora componentes y
operaciones específicas que explotan las características intrínsecas de los datos,
permitiendo al modelo capturar patrones de manera más eficiente y efectiva. Entre las
principales arquitecturas destacan:

- **Redes neuronales densas o totalmente conectadas (_Fully Connected Networks_, FCN)**:
  Constituyen la arquitectura más básica y general, en la que cada neurona de una capa
  está conectada con todas las neuronas de la capa siguiente. Estas redes pueden
  procesar, por lo general, cualquier tipo de datos, siempre que estos se presenten en
  forma vectorial unidimensional, es decir, aplanados (_flattened_). Aunque versátiles,
  presentan limitaciones al trabajar con datos de alta dimensionalidad o con estructuras
  espaciales o temporales complejas, debido al elevado número de parámetros que requieren
  y a su incapacidad para explotar eficientemente dichas estructuras.

- **Redes convolucionales (_Convolutional Neural Networks_, CNN)**: Diseñadas
  específicamente para el procesamiento de datos que poseen estructura espacial o
  espacio-temporal, como imágenes y vídeos. Las CNN utilizan operaciones de convolución
  que aplican filtros deslizantes sobre los datos de entrada, detectando patrones locales
  como bordes, texturas o formas geométricas en las primeras capas, y progresivamente
  características más abstractas y complejas en capas más profundas. Esta arquitectura
  explota la localidad espacial y la invariancia traslacional, reduciendo
  significativamente el número de parámetros en comparación con redes densas
  equivalentes, y facilitando la generalización del modelo a diferentes posiciones dentro
  de la imagen.

- **Redes recurrentes (_Recurrent Neural Networks_, RNN)** y sus variantes modernas, como
  las LSTM (_Long Short-Term Memory_) y GRU (_Gated Recurrent Units_): Empleadas en el
  tratamiento de secuencias, donde el orden temporal de los datos es primordial. Estas
  arquitecturas son especialmente adecuadas para procesar texto, series temporales,
  señales de audio o cualquier tipo de datos secuenciales. Las RNN incorporan conexiones
  recurrentes que permiten a la red mantener un estado interno o memoria que captura
  información de elementos anteriores de la secuencia, posibilitando la modelización de
  dependencias temporales.

- **Modelos basados en _Transformers_**: Representan una evolución significativa en el
  procesamiento de secuencias, basándose en mecanismos de atención que permiten al modelo
  ponderar la importancia de diferentes elementos de la entrada de manera dinámica y
  contextual. Los _Transformers_ han demostrado ser altamente efectivos para tareas de
  procesamiento de lenguaje natural y han sido adoptados también en otros dominios como
  la visión por computador.

- **Modelos multimodales**: Capaces de integrar y procesar información proveniente de
  distintas fuentes o modalidades, como texto, imágenes, audio y vídeo. Estos modelos se
  basan en la idea de representar todos los datos de entrada, independientemente de su
  formato original, como **representaciones embebidas** (_embeddings_) en un espacio
  vectorial común. Este espacio, creado y aprendido por el modelo durante el
  entrenamiento, permite establecer relaciones semánticas entre elementos de diferentes
  modalidades, facilitando que conceptos similares (expresados en formatos distintos) se
  encuentren próximos en dicho espacio. Este proceso de conversión se conoce actualmente
  como **tokenización**, y consiste en la creación de **_tokens_**, representaciones
  vectoriales aprendibles y entendibles por el modelo que encapsulan unidades
  significativas de información. Un único modelo final puede entonces procesar estos
  _tokens_ de manera unificada, independientemente de su origen modal, permitiendo tareas
  complejas como la generación de descripciones textuales a partir de imágenes, la
  búsqueda multimodal o la traducción entre diferentes tipos de contenido.

En este contexto, resulta necesario distinguir entre diferentes tipos de datos según su
estructura y formato. Los **datos estructurados** se organizan en tablas de filas y
columnas, donde cada fila representa una observación o ejemplo, y cada columna
corresponde a una característica o variable con un significado bien definido. Este
formato es característico de las bases de datos relacionales tradicionales y de las hojas
de cálculo. Para este tipo de datos, suelen bastar algoritmos de aprendizaje automático
clásicos, como árboles de decisión o regresión logística, que pueden alcanzar
rendimientos competitivos sin requerir la complejidad arquitectónica del aprendizaje
profundo. No obstante, las redes neuronales también pueden aplicarse a datos
estructurados, especialmente cuando existen interacciones complejas entre variables o
cuando se combinan con datos no estructurados en modelos híbridos.

Los **datos no estructurados**, por el contrario, carecen de una organización tabular
predefinida y presentan formatos heterogéneos y complejos. Ejemplos incluyen imágenes,
grabaciones de voz, documentos en lenguaje natural, vídeos o señales biomédicas. Estos
datos requieren arquitecturas avanzadas de aprendizaje profundo para su procesamiento
efectivo, pues contienen patrones intrincados, relaciones jerárquicas y dependencias
contextuales que no pueden ser fácilmente capturadas por algoritmos tradicionales. El
aprendizaje profundo se muestra especialmente eficaz en estos casos, permitiendo extraer
automáticamente representaciones significativas y patrones complejos a partir de grandes
volúmenes de información, sin necesidad de ingeniería manual de características.

En cuanto a la representación tensorial de los datos, cada tipo de dato se mapea a un
rango específico de tensor. Los datos vectoriales se representan como tensores de rango 2
con forma $(muestras, características)$. Las series temporales o datos secuenciales
adoptan tensores de rango 3 con forma $(muestras, pasos\_temporales, características)$.
Las imágenes se codifican como tensores de rango 4 con forma
$(muestras, alto, ancho, canales)$. Finalmente, los vídeos se representan como tensores
de rango 5 con forma $(muestras, fotogramas, alto, ancho, canales)$.

## Conceptos básicos de matemáticas

### Tensores como estructura fundamental

En el ámbito del aprendizaje profundo, los **tensores** constituyen la estructura de
datos esencial sobre la cual se construye y ejecuta la totalidad del proceso de cómputo.
Un tensor puede definirse formalmente como una colección ordenada de elementos numéricos
organizados en un espacio de $N$ dimensiones, que permite representar, almacenar y
manipular información de manera eficiente dentro de un modelo de red neuronal.

Su principal ventaja radica en su compatibilidad con sistemas de cómputo masivamente
paralelos, como las unidades de procesamiento gráfico (GPU) o las unidades de
procesamiento tensorial (TPU). Estas arquitecturas están diseñadas para ejecutar de forma
simultánea miles de operaciones matemáticas, lo cual resulta indispensable para el
entrenamiento y la inferencia en redes neuronales de gran escala, donde la eficiencia
computacional y el manejo óptimo de los recursos son factores determinantes.

Cada tensor se describe a partir de dos componentes fundamentales: el tipo de datos que
contiene y la precisión numérica empleada en los cálculos. Los valores almacenados suelen
ser numéricos, representados comúnmente como enteros o números en coma flotante. En la
práctica, los modelos de aprendizaje profundo suelen utilizar tensores de 32 bits
(precisión simple), aunque es frecuente aplicar técnicas de **cuantización** que reducen
la precisión a 16, 8 o incluso 4 bits, especialmente una vez completada la fase de
entrenamiento. Estas reducciones, sin embargo, dependen de las capacidades del hardware,
ya que no todas las arquitecturas soportan operaciones de baja precisión con la misma
eficiencia o estabilidad numérica.

Bibliotecas especializadas como **PyTorch**, **TensorFlow** o **Keras** facilitan estos
procesos mediante instrucciones de alto nivel. La elección del nivel de precisión implica
un compromiso entre exactitud y eficiencia. En aplicaciones donde los errores mínimos son
tolerables, como la clasificación de imágenes comunes, puede optarse por una menor
precisión para reducir el consumo energético y acelerar el entrenamiento. En cambio, en
entornos donde la seguridad y la fiabilidad son críticas, se requiere una precisión
numérica más alta que garantice la estabilidad y exactitud de los resultados. Por tanto,
existe una relación directa entre la precisión numérica, el error acumulado y el coste
computacional, de modo que optimizar este equilibrio constituye uno de los aspectos clave
del diseño de modelos eficientes. El uso de **precisión mixta**, que combina tipos de
punto flotante de 16 y 32 bits durante el entrenamiento, permite acelerar la ejecución y
reducir el consumo de memoria manteniendo la estabilidad numérica en las operaciones
críticas.

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

Aunque existen otras alternativas consolidadas, como **TensorFlow**, **JAX** y **Keras**,
PyTorch destaca por su creciente popularidad y por su estrecha vinculación con la Linux
Foundation, lo que garantiza un desarrollo sostenido y un soporte comunitario cada vez
mayor. Además, múltiples proyectos de terceros, como **Ray**, utilizado para la creación
de sistemas distribuidos de entrenamiento de modelos, también forman parte del ecosistema
de la Linux Foundation. Este entorno colaborativo impulsa la innovación y asegura un
soporte activo tanto por parte de empresas tecnológicas reconocidas como de la comunidad
de código abierto.

Una de las principales ventajas de PyTorch es su sintaxis intuitiva y expresiva, que
sigue de forma natural los principios del estilo "**pythónico**", es decir, un diseño
limpio y legible que favorece la comprensión del código.

Independientemente de la biblioteca elegida, los principios matemáticos y conceptuales
que sustentan el aprendizaje profundo son los mismos. Las diferencias radican
principalmente en la sintaxis y en las implementaciones específicas de cada entorno, pero
la base teórica y las operaciones fundamentales definidas sobre tensores permanecen
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
utilizar funciones como `squeeze()`, `unsqueeze()` o `view()` para ajustar su estructura.
Dado que la biblioteca se actualiza con frecuencia, se recomienda consultar la
documentación oficial para obtener información actualizada sobre las funciones
disponibles.

Si se disponen dos vectores del mismo tamaño, $x$ y $y$, es posible combinarlos
linealmente mediante coeficientes escalares $a$ y $b$, generando un nuevo vector $z$, tal
que:

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

Otra operación esencial es el **producto escalar** (o **producto punto**), definido como:

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
capturar relaciones semánticas y sintácticas a través de simples operaciones vectoriales.

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

Una matriz es un arreglo bidimensional que organiza los datos en filas y columnas, por lo
que puede entenderse como una **colección ordenada de vectores**. Matemáticamente, una
matriz $X \in \mathbb{R}^{A \times B}$ está compuesta por $A$ filas y $B$ columnas, donde
cada elemento $x_{ij}$ representa el valor ubicado en la fila $i$ y la columna $j$.

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
profundo, ya que permite procesar simultáneamente grandes volúmenes de información. En el
contexto de una capa neuronal, los datos de entrada suelen representarse mediante una
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

El producto de Hadamard se emplea en múltiples contextos, entre los cuales destaca su uso
en **mecanismos de enmascaramiento** (_masking_) durante el entrenamiento de modelos.
Esta técnica permite ignorar valores específicos de un tensor para impedir que influyan
en el cálculo de los gradientes o en la propagación de errores. Dicha propiedad es
esencial en arquitecturas modernas como **_Transformers_**, donde se aplica para
restringir la atención a determinadas posiciones o para manejar secuencias de longitud
variable sin afectar el aprendizaje global del modelo.

### Operaciones con tensores en PyTorch

La biblioteca PyTorch proporciona un conjunto amplio, eficiente y flexible de
herramientas para la creación, manipulación y transformación de tensores, que constituyen
la estructura de datos fundamental en el aprendizaje profundo. Los tensores generalizan
los conceptos de escalares, vectores y matrices hacia dimensiones superiores, lo que
permite representar datos complejos de manera multidimensional y realizar operaciones
matemáticas de forma vectorizada y optimizada.

A continuación, se presentan ejemplos prácticos y comentados que ilustran las operaciones
más comunes con tensores en PyTorch. Estas operaciones son esenciales para comprender el
funcionamiento interno del código empleado en la creación de modelos de aprendizaje
profundo. En la práctica, muchas arquitecturas modernas o modificaciones de arquitecturas
existentes surgen a partir de pequeñas variaciones en la manipulación de tensores, ya sea
mediante la selección de elementos específicos (_slicing_), la optimización de cálculos o
el uso de estrategias que reduzcan el coste computacional.

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
porque un tensor ubicado en la GPU no puede ser manipulado directamente desde la CPU, por
lo que es necesario transferirlo o copiarlo según sea necesario:

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

Estas operaciones resultan especialmente útiles para inspeccionar distribuciones de datos
o normalizar tensores antes del entrenamiento, tareas que contribuyen a estabilizar el
aprendizaje de los modelos:

```py linenums="1"
tensor = torch.randn((3, 4))  # Distribución normal
print("Tensor aleatorio:\n", tensor)
print("Media:", tensor.mean())
print("Desviación estándar:", tensor.std())
print("Valor mínimo:", tensor.min())
print("Índice del máximo:", tensor.argmax())
```

Finalmente, PyTorch permite una **conversión directa entre tensores y arreglos de
NumPy**, lo que facilita su integración con bibliotecas de análisis y visualización. Esta
interoperabilidad permite combinar el poder de cálculo de PyTorch con la versatilidad de
ecosistemas como NumPy, Matplotlib o Pandas:

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
PyTorch en la manipulación de tensores, mostrando su versatilidad, eficiencia y facilidad
de integración con otros entornos de análisis. En capítulos posteriores, se emplearán
estos fundamentos para la construcción de modelos de aprendizaje profundo basados en esta
biblioteca.

## Regresión lineal y logística

Los modelos de regresión lineal y logística constituyen la base conceptual del
aprendizaje profundo. También se conocen como modelos diferenciables, ya que su
estructura está compuesta por transformaciones lineales seguidas de funciones no lineales
que son derivables, lo que permite aplicar cálculo diferencial para optimizar sus
parámetros mediante métodos basados en gradientes. Este principio es el fundamento de
todas las arquitecturas de redes neuronales modernas.

El entrenamiento de una neurona, o de una red neuronal, se apoya en dos procesos
fundamentales: la **propagación hacia adelante (_forward propagation_)** y la
**propagación hacia atrás (_backpropagation_)**.

La propagación hacia adelante consiste en calcular la predicción del modelo a partir de
los datos de entrada. En este proceso, los datos ingresan por la capa de entrada y
atraviesan las distintas capas de la red, aplicando sucesivas combinaciones lineales y no
lineales hasta obtener una salida numérica. El resultado que produce el modelo antes de
aplicar una función de activación final se conoce como **_logit_**. Este valor representa
una proyección numérica de los datos de entrada en el espacio interno del modelo,
resultado de las transformaciones que la red realiza. Posteriormente, el modelo compara
esta salida con el valor real esperado y calcula una tasa de error o función de pérdida,
la cual mide qué tan precisa ha sido la representación aprendida.

Por otro lado, la propagación hacia atrás es el proceso mediante el cual el modelo ajusta
sus parámetros internos con el objetivo de minimizar el error obtenido en la propagación
hacia adelante. En este proceso, los gradientes (las derivadas parciales de la función de
pérdida respecto a cada parámetro) se propagan desde la salida hasta las capas iniciales
del modelo. Dichos gradientes indican cómo deben modificarse los pesos y sesgos para
reducir el error en las siguientes iteraciones, permitiendo así un aprendizaje progresivo
y dirigido por el descenso del gradiente.

Un modelo lineal puede expresarse matemáticamente como:

$$
\hat{y} = \mathbf{w}^\top \mathbf{x} + b,
$$

donde $\mathbf{x} \in \mathbb{R}^n$ es el vector de entrada,
$\mathbf{w} \in \mathbb{R}^n$ representa el vector de pesos del modelo,
$b \in \mathbb{R}$ es el sesgo o término independiente, y $\hat{y} \in \mathbb{R}$ es la
salida predicha por el modelo. Cuando la salida $\hat{y}$ no está restringida a un rango
específico, el modelo se utiliza en tareas de regresión, donde el objetivo es predecir
valores continuos. En este contexto, la salida puede tomar cualquier valor real, positivo
o negativo.

Sin embargo, cuando la salida está asociada a un conjunto discreto de clases
$\mathcal{C} = \{1, 2, \dots, M\}$, el modelo aborda un problema de clasificación. En
estos casos, la representación numérica (_logits_) generada por el modelo se transforma
en probabilidades mediante una función no lineal, generalmente una función sigmoide para
clasificación binaria o una función _Softmax_ para clasificación multiclase. En la
clasificación binaria ($M = 2$), el modelo aprende a distinguir entre dos posibles
categorías (por ejemplo, "positivo" y "negativo", o "clase 0" y "clase 1"). En cambio, en
los problemas multiclase, el modelo puede asignar cada entrada a una de varias categorías
posibles, como en la clasificación de imágenes por tipo de objeto o raza de perro.
Además, existen escenarios de clasificación multietiqueta, donde una misma entrada puede
pertenecer simultáneamente a varias clases. Un ejemplo típico se da en los sistemas de
visión artificial para conducción autónoma, en los cuales una sola imagen puede contener
múltiples elementos etiquetables, como peatones, vehículos y señales de tráfico.

En los modelos diferenciables, la estructura general se puede describir como una
composición de funciones lineales y no lineales:

$$
f(\mathbf{x}) = f_{L} \circ f_{L-1} \circ \dots \circ f_1 (\mathbf{x}),
$$

donde cada capa aplica una transformación de la forma:

$$
f_{\ell}(\mathbf{x}) = \sigma_{\ell}(\mathbf{W}_{\ell}\mathbf{x} + \mathbf{b}_{\ell}).
$$

En esta formulación, $\mathbf{W}_\ell$ y $\mathbf{b}_\ell$ representan los pesos y sesgos
de la capa $\ell$, respectivamente, mientras que $\sigma_{\ell}(\cdot)$ es una función de
activación diferenciable. Esta función introduce no linealidad al modelo y permite
restringir el rango de valores de salida, lo que dota al modelo de la capacidad de
aproximar relaciones complejas y no lineales entre los datos de entrada y salida.

### Clasificación mediante regresión logística

En lugar de desarrollar manualmente una aplicación con reglas explícitas para identificar
si una imagen contiene un gato u otro tipo de animal, se puede adoptar un enfoque basado
en aprendizaje profundo. En este contexto, se construye un conjunto de datos compuesto
por múltiples ejemplos de imágenes etiquetadas, algunas con gatos y otras sin ellos. Este
conjunto permite que el modelo aprenda automáticamente a distinguir un gato de otros
animales a partir de los patrones estadísticos presentes en los datos, sin requerir
instrucciones específicas para cada caso.

El objetivo principal de este proceso es modelar la distribución de los datos de manera
que el sistema sea capaz de identificar diferencias entre las distintas clases. En un
escenario de aprendizaje supervisado, cada ejemplo del conjunto de datos se asocia con
una etiqueta que indica si pertenece o no a la clase "gato". Con ello, el modelo aprende
la relación entre las características de las imágenes y su respectiva clasificación.

Durante este proceso, las etiquetas se representan mediante valores numéricos. Cada clase
tiene asignado un identificador único. Este identificador puede gestionarse mediante un
diccionario, en el que la clave representa el identificador numérico y el valor
corresponde al nombre de la clase. Una vez que el modelo produce sus predicciones, se
selecciona la clase con el valor más alto y se traduce nuevamente al nombre de la clase
utilizando dicho diccionario. Por ejemplo, si el modelo predice que el índice más alto
corresponde al identificador `1`, el sistema puede mapear este valor a la clase `"gato"`.

Gracias a la disponibilidad de grandes volúmenes de datos etiquetados, los sistemas
supervisados se han convertido en los más empleados en la práctica. Cada muestra del
conjunto de datos se considera independiente e idénticamente distribuida (i.i.d.), lo que
significa que cada ejemplo es representativo y estadísticamente consistente con la
distribución global de los datos. Este supuesto garantiza que el modelo pueda aprender
patrones estables y generalizables, de modo que las representaciones internas que genera
(también conocidas como espacios embebidos o espacios de representación) resulten
estructuradas y separables, permitiendo agrupar ejemplos similares en regiones cercanas
del espacio de características que crea el modelo internamente.

Siguiendo con el ejemplo de la clasificación de gatos, cada imagen de entrada se
representa mediante un conjunto de píxeles con tres canales de color (rojo, verde y
azul). Si cada canal tiene una resolución de, por ejemplo, $64 \times 64$ píxeles, el
número total de valores por imagen es $64 \times 64 \times 3 = 12288$.

Para que esta información pueda ser procesada por un modelo de red neuronal, las tres
matrices de color se **aplanan (_flatten_)**, convirtiéndose en un único vector columna
de dimensión $12288 \times 1$. Este vector conserva la información de los píxeles, pero
la reorganiza en una estructura unidimensional apta para cálculos matriciales.

Si se dispone de $M$ ejemplos, la matriz de características $X$ tendrá dimensión
$(n, M)$, donde $n = 12288$, mientras que el vector de etiquetas $Y$ tendrá dimensión
$(1, M)$ y contendrá los valores binarios correspondientes a cada muestra.

Para resolver este problema, se emplea la regresión logística, un algoritmo de
aprendizaje supervisado diseñado específicamente para tareas de clasificación binaria. Su
funcionamiento es similar al de la regresión lineal, pero incorpora una **función de
activación sigmoide** que transforma la salida del modelo en un valor comprendido entre 0
y 1, interpretable como una probabilidad. La función sigmoide se define como:

$$
\sigma(z) = \frac{1}{1 + e^{-z}},
$$

donde:

$$
z = \mathbf{w}^\top \mathbf{x} + b.
$$

En esta formulación, $\mathbf{w}$ representa el vector de pesos, $b$ el término de sesgo,
y $\mathbf{x}$ el vector de características de la imagen. La predicción final del modelo
se expresa como:

$$
\hat{y} = \sigma(\mathbf{w}^\top \mathbf{x} + b),
$$

donde $\hat{y}$ indica la probabilidad de que la imagen pertenezca a la clase positiva
(es decir, que contenga un gato). Si el valor de $\hat{y}$ supera un determinado umbral
de decisión (por ejemplo, 0.5), la imagen se clasifica como perteneciente a la clase
"gato"; en caso contrario, se clasifica como "no gato".

### Función de pérdida y función de coste

Una vez obtenidos los datos, es necesario formalizar el proceso mediante el cual un
modelo ajusta sus predicciones a los resultados esperados. Este procedimiento se
fundamenta en la **función de pérdida**, una magnitud escalar y diferenciable que
cuantifica el error cometido por el modelo en una predicción individual. Su valor refleja
el grado de discrepancia entre la salida estimada y el valor real, constituyendo así un
indicador directo del rendimiento del modelo.

Durante el entrenamiento, el objetivo principal es **minimizar la función de pérdida**,
reduciendo la diferencia entre las predicciones generadas y los valores verdaderos. En el
caso del aprendizaje supervisado, esta minimización se realiza comparando las etiquetas
reales con las salidas del modelo. Por el contrario, en contextos no supervisados, donde
no existen etiquetas explícitas, se optimizan otras métricas, como las distancias entre
muestras o el error cuadrático medio entre reconstrucciones y los datos originales, entre
otras.

El proceso de optimización se ejecuta habitualmente mediante el **descenso del
gradiente**. Durante este proceso, los parámetros del modelo, los pesos ($w$) y el sesgo
($b$), se ajustan iterativamente con el fin de minimizar la discrepancia entre las
predicciones y las etiquetas reales.

Es importante distinguir entre función de pérdida y función de coste. La función de
pérdida mide el error correspondiente a un único ejemplo de entrenamiento, mientras que
la función de coste representa el promedio de dichas pérdidas a lo largo de todo el
conjunto de entrenamiento:

$$
J(w, b) = \frac{1}{M} \sum_{i=1}^{M} \mathcal{L}(\hat{y}^{(i)}, y^{(i)}),
$$

donde $M$ representa el número total de ejemplos. El objetivo del entrenamiento es
encontrar los parámetros óptimos de $(w, b)$ que minimicen la función de pérdida
$\mathcal{L}$, la cual mide la discrepancia entre las predicciones $\hat{y}_i$ y los
valores verdaderos $y_i$.

En la regresión logística, la función de pérdida más empleada es la **_log-loss_** o
pérdida logarítmica, definida como:

$$
\mathcal{L}(\hat{y}, y) = - \big( y \cdot \log(\hat{y}) + (1 - y) \cdot \log(1 - \hat{y}) \big).
$$

A partir de esta definición, la función de coste correspondiente se expresa como el
promedio de todas las pérdidas individuales:

$$
J(w, b) = -\frac{1}{M} \sum_{i=1}^{M} \Big[ y^{(i)} \log(\hat{y}^{(i)}) + (1 - y^{(i)}) \log(1 - \hat{y}^{(i)}) \Big],
$$

donde $\hat{y}^{(i)} = \sigma(w^T x^{(i)} + b)$ es la probabilidad estimada por el modelo
para el ejemplo $i$, $x^{(i)}$ representa el vector de características del ejemplo,
$y^{(i)}$ es la etiqueta real y $\sigma(z)$ es la **función sigmoide**. Esta formulación
penaliza de forma más efectiva los errores en problemas de clasificación binaria que el
error cuadrático medio (_Mean Square Error_, MSE), ya que la _log-loss_ proporciona
gradientes más estables y evita ciertos problemas de convergencia asociados a funciones
no logarítmicas.

Sin embargo, el MSE sigue siendo ampliamente utilizado en tareas de regresión, donde se
define como:

$$
\text{MSE} = \frac{1}{M} \sum_{i=1}^{M} (\hat{y}^{(i)} - y^{(i)})^2.
$$

En problemas de regresión, la elección de la función de pérdida depende de la naturaleza
de los datos y de la sensibilidad deseada frente a valores atípicos. La MSE penaliza con
mayor intensidad los errores grandes, por lo que resulta sensible a la presencia de
valores extremos. En contraposición, la pérdida absoluta media (_Mean Absolute Error_,
MAE) ofrece una alternativa más robusta frente a valores atípicos, aunque su derivada no
está definida en los puntos donde $y_i = \hat{y}_i$:

$$
\mathcal{L}_{\text{MAE}} = \frac{1}{N} \sum_{i=1}^{N} |y_i - \hat{y}_i|.
$$

Para equilibrar las ventajas de ambas métricas, se utiliza con frecuencia la pérdida de
Huber, que introduce un parámetro de transición $\delta > 0$ y combina los
comportamientos del MSE y del MAE en una sola formulación:

$$
\mathcal{L}_{\text{Huber}} =
\begin{cases}
\frac{1}{2}(y_i - \hat{y}_i)^2, & \text{si } |y_i - \hat{y}_i| \leq \delta \\
\delta \cdot (|y_i - \hat{y}_i| - \frac{1}{2}\delta), & \text{en otro caso.}
\end{cases}
$$

La pérdida de Huber es diferenciable en casi todos los puntos, salvo en el límite
$|y_i - \hat{y}_i| = \delta$, aunque esta discontinuidad no genera inestabilidad numérica
debido a la precisión finita de los cálculos. Por este motivo, se aplica habitualmente en
contextos donde se busca un equilibrio entre la robustez frente a valores atípicos y la
estabilidad del proceso de optimización.

Finalmente, cabe destacar que un modelo que obtiene un coste bajo en el conjunto de
entrenamiento no garantiza un buen rendimiento general. Este fenómeno, conocido como
sobreajuste (_overfitting_), se presenta cuando el modelo alcanza una elevada precisión
en los datos de entrenamiento, pero su desempeño se degrada significativamente al
evaluarse en datos nuevos. En tales casos, el modelo no aprende patrones generalizables,
sino que memoriza los ejemplos específicos del conjunto de entrenamiento. El sobreajuste
puede deberse a un número insuficiente de muestras, a arquitecturas excesivamente
complejas o a problemas en la representación de los datos, como etiquetado incorrecto,
desequilibrio de clases o sesgos en el conjunto de entrenamiento. Asimismo, las
diferencias entre las distribuciones de los datos de entrenamiento y los de producción
pueden comprometer la capacidad de generalización del modelo. Los modelos entrenados con
datos que contienen valores de características poco frecuentes son especialmente
susceptibles al sobreajuste, ya que tienden a memorizar estas particularidades en lugar
de aprender patrones generalizables.

### Descenso del gradiente

El descenso del gradiente constituye uno de los algoritmos fundamentales para el
entrenamiento de modelos en aprendizaje automático. Su propósito es encontrar los valores
de los parámetros que minimizan una determinada función de coste, garantizando que las
predicciones del modelo se ajusten lo mejor posible a los datos observados.

En el caso de la regresión logística, la función de coste $J(w, b)$ se define a partir de
la función de pérdida logarítmica:

$$
J(w, b) = -\frac{1}{M} \sum_{i=1}^{M} \Big[ y^{(i)} \log(\hat{y}^{(i)}) + (1 - y^{(i)}) \log(1 - \hat{y}^{(i)}) \Big].
$$

Para reducir el valor de $J(w, b)$, se calculan las derivadas parciales con respecto a
los parámetros del modelo. Estas derivadas determinan la dirección del gradiente, es
decir, el sentido en el que la función de coste crece más rápidamente. Dado que el
objetivo es minimizarla, el algoritmo ajusta los parámetros en la dirección opuesta al
gradiente:

$$
\frac{\partial J}{\partial w} = dw = \frac{1}{M} \sum_{i=1}^{M} (\hat{y}^{(i)} - y^{(i)}) x^{(i)}, \quad
\frac{\partial J}{\partial b} = db = \frac{1}{M} \sum_{i=1}^{M} (\hat{y}^{(i)} - y^{(i)}).
$$

Estos términos indican cómo deben modificarse $w$ y $b$ en cada iteración para disminuir
el error. El procedimiento completo del descenso del gradiente se desarrolla de forma
iterativa y puede resumirse en las siguientes fases:

1. **Inicialización de los parámetros**: Se asignan valores iniciales, generalmente
   pequeños, ya sean ceros o valores aleatorios.
2. **Propagación hacia adelante**: Se calculan las predicciones $\hat{y}$ a partir de los
   datos de entrada $X$ y se evalúa la función de pérdida $\mathcal{L}(\hat{y}, y)$ y la
   función de coste $J(w, b)$.
3. **Propagación hacia atrás**: Se obtienen las derivadas parciales $dw$ y $db$, que
   indican la dirección del ajuste de los parámetros.
4. **Actualización de parámetros**: Se actualizan los valores de $w$ y $b$ según la
   regla:

$$
w := w - \alpha \cdot dw, \quad b := b - \alpha \cdot db,
$$

donde $\alpha$ es la tasa de aprendizaje o ratio de aprendizaje, un hiperparámetro que
controla el tamaño del paso dado en cada iteración. Si $\alpha$ es demasiado grande, el
algoritmo puede divergir; si es demasiado pequeño, la convergencia será muy lenta. El
proceso se repite hasta alcanzar un mínimo adecuado de $J(w, b)$, lo que se traduce en
predicciones más precisas.

En la práctica, el descenso del gradiente se implementa de forma vectorizada,
aprovechando operaciones matriciales sobre todos los ejemplos del conjunto de
entrenamiento en paralelo. Esta formulación no solo simplifica la implementación, sino
que también permite aprovechar la capacidad de cómputo de las GPU.

Para ilustrar el funcionamiento del algoritmo, considérese la función bidimensional:

$$
f(x) = \sin(x_1)\cos(x_2) + \sin(0.5x_1)\cos(0.5x_2), \quad x \in [0, 10].
$$

El objetivo consiste en aplicar el descenso del gradiente sobre esta función, calculando
explícitamente las derivadas parciales respecto a $x_1$ y $x_2$:

```py linenums="1"
import numpy as np
import matplotlib.pyplot as plt

# Definición de la función
def function(input: np.ndarray) -> np.ndarray:
    assert input.shape[-1] == 2, "La entrada debe contener 2 elementos"
    return np.sin(input[:, 0]) * np.cos(input[:, 1]) + np.sin(0.5 * input[:, 0]) * np.cos(0.5 * input[:, 1])

# Cálculo del gradiente (derivadas parciales)
def gradiente(input: np.ndarray) -> np.ndarray:
    assert input.shape[-1] == 2, "La entrada debe contener 2 elementos"

    df_x1 = np.cos(input[:, 0]) * np.cos(input[:, 1]) + 0.5 * np.cos(0.5 * input[:, 0]) * np.cos(0.5 * input[:, 1])
    df_x2 = -np.sin(input[:, 0]) * np.sin(input[:, 1]) - 0.5 * np.sin(0.5 * input[:, 0]) * np.sin(0.5 * input[:, 1])

    return np.stack([df_x1, df_x2], axis=1)

# Algoritmo de descenso del gradiente
def descenso_gradiente(num_puntos: int = 10, num_iteraciones: int = 30, learning_rate: float = 1e-3):
    dim = 2

    # Inicialización en el dominio [0,10]
    X = np.random.rand(num_puntos, dim) * 10
    trayectorias = [X.copy()]

    for _ in range(num_iteraciones):
        X = X - learning_rate * gradiente(input=X)
        trayectorias.append(X.copy())

    return np.array(trayectorias)

# Ejecución del descenso del gradiente
trayectoria = descenso_gradiente(num_puntos=5, num_iteraciones=30)

# Visualización de las trayectorias
for i in range(trayectoria.shape[1]):
    plt.plot(trayectoria[:, i, 0], trayectoria[:, i, 1], marker="o")

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Trayectorias del descenso del gradiente")
plt.show()
```

Al ejecutar este código, se observa que los puntos iniciales evolucionan siguiendo
trayectorias determinadas por el gradiente de la función. En cada iteración, las
posiciones se actualizan desplazándose en la dirección opuesta a la pendiente local, lo
que permite avanzar hacia valores más bajos de la función objetivo.

En el contexto de redes neuronales, el cálculo de derivadas necesarias para aplicar el
descenso del gradiente se realiza mediante sistemas de **diferenciación automática**. En
PyTorch, este proceso se gestiona mediante el módulo **`autograd`**, que permite calcular
derivadas de manera automática sobre operaciones tensoriales y constituye la base del
algoritmo de _backpropagation_. Cada tensor en PyTorch puede llevar asociada la propiedad
`requires_grad=True`, que indica si debe participar en el cálculo de gradientes. PyTorch
construye un grafo computacional dinámico que registra las operaciones realizadas sobre
los tensores, y al invocar el método `backward()`, aplica la regla de la cadena para
calcular las derivadas necesarias. Este mecanismo se conoce también como el modo inverso
de diferenciación automática:

```py linenums="1"
import torch

x = torch.tensor([2.0, 3.0], requires_grad=True)
y = x**2 + 2*x + 1
z = y.sum()
z.backward()

# Derivadas parciales de z respecto a x
print(x.grad)
```

Además, PyTorch permite desactivar el cálculo de gradientes cuando no es necesario, como
durante la fase de inferencia, utilizando el contexto `with torch.no_grad():` o el modo
`with torch.inference_mode():`, que resulta aún más eficiente. Esto reduce
significativamente el consumo de memoria y mejora el rendimiento computacional.

Para mejorar la eficiencia, en lugar de calcular los gradientes utilizando el conjunto
completo de datos, se emplea el **descenso de gradiente estocástico (SGD)**, que utiliza
pequeños subconjuntos (_mini-batches_). Esta aproximación introduce aleatoriedad,
disminuye el coste computacional y ayuda a escapar de regiones problemáticas, como los
puntos de silla, donde los gradientes se anulan sin representar un mínimo real. Calcular
los gradientes sobre un subconjunto reducido del conjunto de datos puede interpretarse
como una aproximación de Monte Carlo de la función de coste global, lo que resulta
suficientemente representativo para actualizar los parámetros de la red de manera
efectiva.

El descenso de gradiente básico puede resultar ineficiente en ciertos escenarios, por lo
que se han desarrollado variantes que mejoran su rendimiento. Una de ellas es el
**algoritmo Momentum**, que introduce un efecto de inercia acumulando información de
gradientes previos para suavizar las actualizaciones:

$$
v_t = \beta v_{t-1} + (1-\beta) \, \nabla_\theta \mathcal{L}(\theta_t),
$$

$$
\theta_{t+1} = \theta_t - \eta \, v_t,
$$

donde $v_t$ representa la "velocidad" acumulada y $\beta \in [0,1)$ es el coeficiente de
decaimiento, generalmente fijado en 0.9. Este mecanismo reduce las oscilaciones en
direcciones de alta curvatura y acelera la convergencia en valles estrechos.

Otro método es **RMSprop**, que adapta la tasa de aprendizaje a cada parámetro mediante
el escalado de los gradientes por una media móvil de sus valores al cuadrado:

$$
s_t = \rho s_{t-1} + (1-\rho) \left(\nabla_\theta \mathcal{L}(\theta_t)\right)^2,
$$

$$
\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{s_t + \epsilon}} \, \nabla_\theta \mathcal{L}(\theta_t),
$$

donde $\rho \approx 0.9$ y $\epsilon \approx 10^{-8}$ para evitar divisiones por cero.
Este ajuste permite que los parámetros con gradientes grandes reciban pasos más pequeños,
mientras que aquellos con gradientes pequeños se actualizan más rápidamente, mejorando la
estabilidad del entrenamiento.

El optimizador **Adam** combina las ventajas de Momentum y RMSprop, acumulando tanto la
media de los gradientes como la media de sus cuadrados. Su formulación se realiza en
cuatro etapas:

1. **Media de gradientes (primer momento):**

$$
m_t = \beta_1 m_{t-1} + (1-\beta_1) \, \nabla_\theta \mathcal{L}(\theta_t).
$$

2. **Media de cuadrados de gradientes (segundo momento):**

$$
v_t = \beta_2 v_{t-1} + (1-\beta_2) \, \left(\nabla_\theta \mathcal{L}(\theta_t)\right)^2.
$$

3. **Corrección del sesgo inicial:**

$$
\hat{m}_t = \frac{m_t}{1-\beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1-\beta_2^t}.
$$

4. **Actualización final de los parámetros:**

$$
\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{\hat{v}_t} + \epsilon} \, \hat{m}_t.
$$

Los valores recomendados son $\beta_1 = 0.9$, $\beta_2 = 0.999$ y $\epsilon = 10^{-8}$.
Este optimizador se utiliza ampliamente debido a su rapidez, estabilidad y robustez
frente a configuraciones no óptimas de hiperparámetros.

A modo de ilustración, se presenta una implementación de los principales optimizadores
aplicada a la función de prueba $f(\theta) = \theta^2$, cuyo mínimo global se encuentra
en $\theta=0$:

```py linenums="1"
import numpy as np

# Función de pérdida y gradiente
loss = lambda theta: theta**2
grad = lambda theta: 2*theta

# Valor inicial
theta_init = 5.0

# Descenso de gradiente estocástico (SGD)
def sgd(theta, grad, eta=0.1, steps=20):
    for t in range(steps):
        theta -= eta * grad(theta)
    return theta

# Momentum
def momentum(theta, grad, eta=0.1, beta=0.9, steps=20):
    v = 0
    for t in range(steps):
        v = beta * v + (1 - beta) * grad(theta)
        theta -= eta * v
    return theta

# RMSprop
def rmsprop(theta, grad, eta=0.1, rho=0.9, eps=1e-8, steps=20):
    s = 0
    for t in range(steps):
        g = grad(theta)
        s = rho * s + (1 - rho) * g**2
        theta -= eta / (np.sqrt(s) + eps) * g
    return theta

# Adam
def adam(theta, grad, eta=0.1, beta1=0.9, beta2=0.999, eps=1e-8, steps=20):
    m, v = 0, 0
    for t in range(1, steps+1):
        g = grad(theta)
        m = beta1 * m + (1 - beta1) * g
        v = beta2 * v + (1 - beta2) * g**2
        m_hat = m / (1 - beta1**t)
        v_hat = v / (1 - beta2**t)
        theta -= eta / (np.sqrt(v_hat) + eps) * m_hat
    return theta

print("SGD:", sgd(theta_init, grad))
print("Momentum:", momentum(theta_init, grad))
print("RMSprop:", rmsprop(theta_init, grad))
print("Adam:", adam(theta_init, grad))
```

### Métodos de regularización

En el contexto de la regresión lineal, es posible obtener una solución analítica para los
pesos del modelo mediante la **pseudoinversa de Moore–Penrose**, que proporciona una
estimación cerrada de los parámetros cuando la matriz de diseño no es cuadrada o no tiene
inversa directa. Esta solución se expresa como:

$$
\mathbf{w} = (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{y},
$$

donde $\mathbf{X} \in \mathbb{R}^{N \times n}$ representa la matriz de datos de entrada y
$\mathbf{y} \in \mathbb{R}^N$ los valores objetivo. Sin embargo, este enfoque puede
resultar numéricamente inestable cuando la matriz $(\mathbf{X}^\top \mathbf{X})$ es casi
singular, es decir, cuando algunos de sus valores propios son muy pequeños o cercanos a
cero. En tales casos, pequeñas variaciones en los datos pueden producir grandes cambios
en los parámetros estimados, lo que conduce a un modelo **sobreajustado** y con escasa
capacidad de generalización.

Para mitigar este problema y mejorar la estabilidad del modelo, se introduce un **término
de regularización** en la función de coste. La regularización actúa como un mecanismo de
control que penaliza los pesos excesivamente grandes, favoreciendo soluciones más
estables y reduciendo la varianza del modelo. De este modo, se logra un equilibrio entre
el ajuste a los datos de entrenamiento y la capacidad de generalización ante nuevos
ejemplos. Los métodos más comunes son la **regularización L2 (_Ridge Regression_)** y la
**regularización L1 (_Lasso Regression_)**.

La regularización L2 agrega al término de error un componente proporcional al cuadrado de
la magnitud de los pesos. Este término penaliza los parámetros de gran magnitud,
promoviendo valores pequeños y distribuidos de manera más uniforme. Su función de pérdida
se define como:

$$
\mathcal{L}_{\text{Ridge}} = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2 + \lambda |\mathbf{w}|_2^2,
$$

donde $\lambda$ es un hiperparámetro que controla la intensidad de la penalización.
Cuanto mayor sea su valor, más fuerte será la restricción sobre los pesos. La
regularización L2 produce modelos más suaves y estables, ya que evita oscilaciones
excesivas en los parámetros y contribuye a que el proceso de entrenamiento sea más
controlado. En la práctica, esto se traduce en cambios menos abruptos en la salida ante
pequeñas desviaciones en la entrada, comportamiento que también se conoce como
**decaimiento de los pesos (_weight decay_)**.

Por otro lado, la regularización L1 incorpora un término basado en la suma de los valores
absolutos de los pesos:

$$
\mathcal{L}_{\text{Lasso}} = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2 + \lambda |\mathbf{w}|_1.
$$

A diferencia de la regularización L2, el término L1 tiende a forzar algunos coeficientes
a ser exactamente cero, lo que induce esparsidad en el modelo. En la práctica, esto
significa que ciertos parámetros se eliminan completamente, dando lugar a modelos más
simples y con menos variables efectivamente activas. Este comportamiento convierte a la
regularización L1 en una herramienta útil para selección de características, ya que
identifica de manera implícita las variables más relevantes para la predicción. Sin
embargo, la regularización L1 es menos común en aprendizaje profundo porque no interactúa
bien con la no convexidad de los problemas de optimización y con el uso del descenso del
gradiente.

La regularización y la normalización son técnicas fundamentales para mejorar la capacidad
de generalización de los modelos de aprendizaje profundo y reducir el riesgo de
sobreajuste. Ambas estrategias buscan limitar la dependencia excesiva del modelo respecto
a los datos de entrenamiento, promoviendo representaciones más robustas y estables que
permitan un rendimiento consistente en datos no vistos. Entre las técnicas de
regularización más utilizadas destacan:

- **Dropout**: Desactiva aleatoriamente un subconjunto de neuronas durante el
  entrenamiento, impidiendo que las unidades desarrollen dependencias excesivas entre sí.
  Esto obliga a la red a generar representaciones redundantes y más robustas. Durante la
  inferencia, todas las neuronas se utilizan, pero la salida se convierte en una variable
  aleatoria dependiente de las máscaras de desactivación aplicadas. Para obtener una
  salida determinista, se puede aproximar el valor esperado mediante muestreo de Monte
  Carlo (realizando múltiples pasadas hacia adelante con diferentes máscaras y
  promediando los resultados), lo que además proporciona una medida de incertidumbre
  sobre la predicción. No obstante, dado que realizar múltiples pasadas resulta costoso,
  la práctica más habitual consiste en reemplazar las variables aleatorias capa por capa
  mediante un ajuste proporcional de los pesos, lo que constituye una aproximación
  razonable y eficiente.

- **Aumentación de datos (_data augmentation_)**: Crea ejemplos adicionales a partir de
  transformaciones aplicadas a los datos originales, como rotaciones, traslaciones,
  cambios de escala o variaciones de iluminación. Esta técnica incrementa la diversidad
  del conjunto de entrenamiento y hace que el modelo sea menos sensible a variaciones
  irrelevantes.

- **Detención temprana (_early stopping_)**: Supervisa el rendimiento del modelo sobre el
  conjunto de validación y detiene el entrenamiento cuando el error deja de mejorar,
  evitando que la red se ajuste demasiado a las particularidades del conjunto de
  entrenamiento.

- **Normalización de entradas**: Escala y centra las características de los datos para
  garantizar magnitudes comparables, acelerando la convergencia, mejorando la estabilidad
  numérica y evitando que ciertos parámetros dominen el aprendizaje. Una práctica
  habitual consiste en restar la media y dividir por la desviación estándar de cada
  característica, de modo que los datos queden centrados en cero con varianza unitaria.

En complemento a la regularización, las técnicas de **normalización de activaciones**
resultan esenciales para estabilizar el entrenamiento y acelerar la convergencia. Durante
la optimización, las activaciones pueden variar significativamente entre capas, lo que
genera inestabilidad y dificulta el ajuste de los parámetros. La normalización busca
mantener distribuciones equilibradas de las activaciones a lo largo de la red:

- **_Batch Normalization_**: Normaliza las activaciones de cada capa utilizando la media
  y la varianza calculadas sobre los ejemplos de un mini-lote. Esto reduce el problema
  del _internal covariate shift_, acelera el aprendizaje, permite tasas de aprendizaje
  más altas y simplifica el ajuste de hiperparámetros. Sin embargo, su efectividad
  depende del tamaño y la composición de los lotes, siendo menos adecuada en lotes
  pequeños o en datos con distribuciones muy variables.

- **_Layer Normalization_**: Normaliza las activaciones a nivel de capa, calculando
  estadísticas por muestra en lugar de por mini-lote. Es especialmente útil en
  arquitecturas secuenciales, como los _Transformers_, y en escenarios de entrenamiento
  distribuido, ya que no requiere compartir estadísticas entre lotes, facilitando la
  paralelización y la escalabilidad.

### Sistemas de clasificación multiclase y la función Softmax

En los sistemas de clasificación multiclase, el objetivo del modelo es asignar una
probabilidad a cada una de las posibles clases, de modo que la suma de todas ellas sea
igual a uno. Para lograrlo, la capa de salida del modelo suele aplicar la **función
_Softmax_** sobre los valores de activación o _logits_ generados por la red neuronal.
Estos logits se definen como:

$$
z_i = \mathbf{w}_i^\top \mathbf{x} + b_i,
$$

donde $\mathbf{x}$ representa el vector de entrada, $\mathbf{w}_i$ los pesos asociados a
la clase $i$, y $b_i$ el sesgo correspondiente. A partir de estos valores, la función
_Softmax_ transforma los logits en una distribución de probabilidad normalizada:

$$
p_i = \text{Softmax}(z_i) = \frac{e^{z_i / T}}{\sum_{j=1}^{M} e^{z_j / T}},
$$

donde $T > 0$ es el **parámetro de temperatura** que controla la "nitidez" de la
distribución. Cuando el valor de $T$ es grande, las diferencias entre los exponentes se
atenúan, y la distribución resultante se aproxima a una distribución uniforme, lo que
refleja una mayor incertidumbre del modelo. Por el contrario, cuando $T$ tiende a cero,
la probabilidad se concentra en la clase más probable, haciendo que las predicciones sean
más deterministas.

El proceso de predicción final se realiza seleccionando la clase con la probabilidad más
alta:

$$
\hat{y} = \arg\max_i \, p_i.
$$

Con el fin de evitar que el modelo sea excesivamente confiado en sus predicciones, se
utiliza una técnica denominada **suavizado de etiquetas (_label smoothing_)**. Este
procedimiento ajusta las etiquetas verdaderas, reduciendo ligeramente la probabilidad
asignada a la clase correcta y redistribuyendo parte de ella entre las demás clases,
según la expresión:

$$
y_i' = (1 - \varepsilon) y_i + \frac{\varepsilon}{M},
$$

donde $\varepsilon \in [0,1]$ determina el grado de suavizado.

Para el entrenamiento de modelos de clasificación, la **función de pérdida por entropía
cruzada** es una de las más empleadas:

$$
\mathcal{L}_{\text{CE}} = - \sum_{i=1}^{M} y_i \log(p_i).
$$

El objetivo del aprendizaje consiste en minimizar esta pérdida, lo cual equivale a
**maximizar la probabilidad asignada a la clase correcta**. Desde un punto de vista
teórico, la entropía cruzada puede descomponerse como:

$$
\mathcal{L}_{\text{CE}} = H(\mathbf{y}, \mathbf{p}) = H(\mathbf{y}) + D_{KL}(\mathbf{y} \,||\, \mathbf{p}),
$$

donde $H(\mathbf{y})$ representa la entropía de las etiquetas verdaderas y
$D_{KL}(\mathbf{y} \,||\, \mathbf{p})$ es la **divergencia de Kullback–Leibler**,
definida como:

$$
D_{KL}(\mathbf{y} \,||\, \mathbf{p}) = \sum_{i=1}^{M} y_i \log \frac{y_i}{p_i}.
$$

Minimizar la entropía cruzada implica reducir la divergencia entre la distribución
predicha y la distribución verdadera.

### Incertidumbre, calibración y pérdida focal

Aunque la función _Softmax_ transforma los _logits_ en probabilidades dentro del
intervalo $[0, 1]$ que suman 1, estas **no reflejan necesariamente la verdadera
incertidumbre del modelo**. Un valor de probabilidad elevado no garantiza que la
predicción sea fiable, ya que muchos modelos modernos tienden a ser excesivamente
confiados en sus predicciones, incluso cuando son erróneas.

La **calibración del modelo** surge para corregir este comportamiento. Su objetivo es
alinear las probabilidades predichas con las frecuencias empíricas observadas. Un modelo
se considera perfectamente calibrado cuando:

$$
P(Y = k \mid \hat{P}(Y = k) = p) = p.
$$

El flujo general del proceso de calibración se desarrolla en las siguientes etapas:
entrenamiento del modelo sobre el conjunto de entrenamiento, obtención de los _logits_ o
probabilidades sobre un conjunto de validación independiente, aplicación de un método de
calibración (como el escalado de temperatura, el _Platt scaling_ o la regresión
isotónica), optimización de los parámetros del calibrador, evaluación del grado de
calibración mediante métricas especializadas como el _Expected Calibration Error_ (ECE) o
el _Maximum Calibration Error_ (MCE), e implementación del calibrador final para ajustar
las probabilidades durante la inferencia en producción.

Uno de los métodos más simples y eficaces para calibrar redes neuronales es el **escalado
de temperatura** (_temperature scaling_), que consiste en ajustar un único parámetro
$T > 0$ que reescala los _logits_ antes de aplicar la función _Softmax_. El valor de $T$
se optimiza sobre un conjunto de validación minimizando la entropía cruzada. Cabe
destacar que este ajuste no altera la clase predicha (el valor de $\arg\max$ permanece
igual), sino que modifica la confianza asociada a cada predicción.

Para problemas de clasificación binaria, el **_Platt Scaling_** ofrece una alternativa
paramétrica en la que los _logits_ se ajustan mediante una función sigmoide con
parámetros $A$ y $B$ optimizados sobre validación. La **regresión isotónica**, por su
parte, constituye un método no paramétrico que ajusta las probabilidades mediante una
función monótonamente creciente, ofreciendo mayor flexibilidad aunque requiriendo más
muestras de validación.

Las métricas de evaluación de la calibración incluyen el **ECE** (_Expected Calibration
Error_):

$$
\text{ECE} = \sum_{m=1}^M \frac{|B_m|}{N} \Big| \text{acc}(B_m) - \text{conf}(B_m) \Big|,
$$

y el **MCE** (_Maximum Calibration Error_):

$$
\text{MCE} = \max_m \Big| \text{acc}(B_m) - \text{conf}(B_m) \Big|.
$$

En escenarios con desbalance de clases o gran cantidad de ejemplos "fáciles", la función
de pérdida tradicional por entropía cruzada puede resultar insuficiente. Para mitigar
este efecto, Lin et al. (2017) propusieron la **pérdida focal (_Focal Loss_)**:

$$
\mathcal{L}_{\text{Focal}} = - (1 - p_t)^\gamma \log(p_t),
$$

donde $p_t$ es la probabilidad predicha para la clase verdadera y $\gamma \ge 0$ es un
parámetro de enfoque que aumenta el peso relativo de los ejemplos difíciles. Cuando
$\gamma = 0$, la pérdida focal se reduce a la entropía cruzada estándar.

### Implementación de la regresión logística

Para ilustrar de forma práctica los conceptos presentados anteriormente, a continuación
se muestra una implementación básica de la regresión logística utilizando Python y la
librería NumPy. Este ejemplo incluye todas las etapas fundamentales del modelo: la
inicialización de parámetros, _forward propagation_, _backward propagation_, la
actualización de los parámetros mediante descenso del gradiente y, finalmente, la
generación de predicciones y la evaluación del modelo:

```py linenums="1"
import numpy as np
import matplotlib.pyplot as plt

# Dataset de ejemplo
np.random.seed(1)
m = 200  # número de ejemplos
n = 2    # número de características

# Clase 0
X0 = np.random.randn(m//2, n) + np.array([-2, -2])
Y0 = np.zeros((m//2, 1))

# Clase 1
X1 = np.random.randn(m//2, n) + np.array([2, 2])
Y1 = np.ones((m//2, 1))

# Concatenar y transponer
X = np.vstack((X0, X1)).T
Y = np.vstack((Y0, Y1)).T

# Funciones auxiliares
def sigmoid(z):
    """Función sigmoide."""
    return 1 / (1 + np.exp(-z))

def initialize_params(n):
    """Inicializa los parámetros del modelo."""
    w = np.zeros((n, 1))
    b = 0
    return w, b

def forward_propagation(w, b, X, Y):
    """Calcula la activación y el coste."""
    m = X.shape[1]
    Z = np.dot(w.T, X) + b
    A = sigmoid(Z)
    cost = -(1/m) * np.sum(Y*np.log(A) + (1-Y)*np.log(1-A))
    return A, cost

def backward_propagation(A, X, Y):
    """Calcula los gradientes del coste respecto a los parámetros."""
    m = X.shape[1]
    dw = (1/m) * np.dot(X, (A - Y).T)
    db = (1/m) * np.sum(A - Y)
    return dw, db

def update_params(w, b, dw, db, learning_rate):
    """Actualiza los parámetros usando descenso del gradiente."""
    w -= learning_rate * dw
    b -= learning_rate * db
    return w, b

# Entrenamiento del modelo
def logistic_regression(X, Y, num_iterations=1000, learning_rate=0.1, print_cost=False):
    """Entrena el modelo de regresión logística."""
    n = X.shape[0]
    w, b = initialize_params(n)
    costs = []

    for i in range(num_iterations):
        A, cost = forward_propagation(w, b, X, Y)
        dw, db = backward_propagation(A, X, Y)
        w, b = update_params(w, b, dw, db, learning_rate)

        if i % 100 == 0:
            costs.append(cost)
            if print_cost:
                print(f"Iteración {i}: coste = {cost:.4f}")

    return w, b, costs

# Predicción
def predict(w, b, X):
    """Genera predicciones binarias a partir de los parámetros entrenados."""
    A = sigmoid(np.dot(w.T, X) + b)
    return (A > 0.5).astype(int)

# Entrenar y evaluar el modelo
w, b, costs = logistic_regression(X, Y, num_iterations=1000, learning_rate=0.1, print_cost=True)
Y_pred = predict(w, b, X)
accuracy = 100 - np.mean(np.abs(Y_pred - Y)) * 100
print(f"\nExactitud del modelo: {accuracy:.2f}%")

# Visualización de la evolución del coste
plt.plot(costs)
plt.xlabel("Iteraciones (x100)")
plt.ylabel("Coste")
plt.title("Reducción del coste durante el entrenamiento")
plt.show()
```

## Neurona artificial y redes neuronales

Para ilustrar el funcionamiento básico de los modelos de aprendizaje profundo, puede
considerarse el problema de estimar el precio de una vivienda. Si se representa
gráficamente el tamaño de la casa frente a su precio, se observa una tendencia creciente
positiva: a mayor tamaño de la vivienda, mayor precio. Una forma de capturar esta
relación es mediante la **regresión lineal**, que consiste en ajustar una línea recta que
describe la relación entre ambas variables. Esta línea se caracteriza por dos parámetros
fundamentales: su posición vertical, determinada por el término independiente, y su
pendiente, que define la tasa de cambio del precio respecto al tamaño. Sin embargo, este
enfoque presenta limitaciones importantes. Por ejemplo, al extrapolar la línea recta
hacia valores muy pequeños de tamaño, el modelo podría asignar precios negativos a
viviendas extremadamente reducidas, lo cual carece de sentido práctico. Para resolver
este problema, se incorporan funciones que restringen los resultados a intervalos válidos
de salidas, garantizando que las predicciones mantengan coherencia con la realidad física
del problema.

Este procedimiento puede comprenderse mejor mediante la analogía de una **neurona
artificial**, también conocida como perceptrón. La neurona recibe el tamaño de la
vivienda como entrada y aplica un cálculo lineal parametrizado, cuyos parámetros se han
obtenido a partir de ejemplos de entrenamiento. Posteriormente, utiliza una función de
activación que filtra valores inválidos, produciendo una estimación coherente del precio
dentro de un rango válido. De este modo, la neurona artificial transforma la entrada
mediante una combinación de operaciones lineales y no lineales, ajustándose
progresivamente a los patrones presentes en los datos.

Esta abstracción computacional tiene su origen en la estructura de la **neurona
biológica**. En el cerebro, una neurona se compone de tres partes principales: las
**dendritas**, que constituyen las entradas y reciben señales de otras neuronas; el
**soma** (cuerpo celular), donde se realiza el procesamiento; y el **axón**, que
transmite la señal de salida. Una neurona biológica se activa cuando la suma de los
impulsos recibidos a través de las dendritas alcanza un umbral determinado, generando un
potencial de acción (_spike_) que se propaga por el axón. Cuando esta señal llega a la
**sinapsis**, la conexión con la siguiente neurona, el proceso de transmisión pasa de ser
eléctrico a químico mediante la liberación de **neurotransmisores**. En la neurona
receptora, estos neurotransmisores generan una nueva señal eléctrica, completando así la
cadena de comunicación.

La sinapsis posee un **detector de coincidencias** basado en receptores NMDA, que se
activa cuando confluyen simultáneamente una señal química (llegada de neurotransmisores
de otra neurona) y una señal eléctrica (despolarización de la membrana de la neurona
receptora). Este mecanismo subyace al **principio hebbiano**: las neuronas que se activan
juntas refuerzan sus conexiones mutuas. Además, mecanismos locales, como la activación
simultánea de sinapsis cercanas, contribuyen a modular la fuerza de las conexiones. Esta
capacidad de modificar el número y la sensibilidad de los receptores sinápticos se
denomina **plasticidad sináptica**, y constituye la base biológica del aprendizaje.

Una neurona biológica presenta dos tipos diferenciados de conexiones dendríticas. Las
**dendritas apicales** reciben conexiones de retroalimentación (_feedback_) con
información asociativa procedente de áreas corticales superiores, mientras que las
**dendritas basales** procesan conexiones de alimentación directa (_feedforward_) con
información sensorial y motora local. Las redes neuronales artificiales actuales modelan
principalmente la integración basal local junto con una plasticidad dependiente del error
de salida, pero no capturan las señales apicales ni la plasticidad dependiente del
contexto global o de los vecindarios neuronales, lo que representa una simplificación
significativa respecto al sistema biológico original.

No obstante, el valor de una vivienda depende de múltiples factores adicionales, como el
número de dormitorios, el número de baños, la ubicación geográfica, la proximidad a
servicios públicos o el estado de conservación de la propiedad. La incorporación de estas
características incrementa la **dimensionalidad** de los datos. En este escenario, la
simple regresión lineal se vuelve insuficiente, puesto que una única línea recta solo es
capaz de relacionar linealmente dos variables. Para abordar problemas de mayor
complejidad, resulta necesario combinar múltiples perceptrones organizados en **capas**,
lo que da lugar a arquitecturas que permiten modelar no solo relaciones lineales
individuales entre pares de variables, sino también combinaciones complejas de múltiples
parámetros de entrada. Además, estas arquitecturas posibilitan que las neuronas de capas
sucesivas procesen y combinen las representaciones generadas por capas anteriores,
construyendo progresivamente abstracciones de mayor nivel que capturan patrones
sofisticados en los datos.

En las arquitecturas de aprendizaje profundo se distinguen tres tipos de capas
fundamentales. La **capa de entrada** recibe las características iniciales del problema,
es decir, los datos de entrada tras aplicar las transformaciones oportunas para obtener
valores numéricos que el modelo pueda procesar. Las **capas ocultas** (_hidden layers_)
se sitúan entre la entrada y la salida, y su función consiste en procesar y transformar
progresivamente dichas características, extrayendo representaciones intermedias cada vez
más abstractas y relevantes para la tarea en cuestión. Finalmente, la **capa de salida**
genera la predicción final del modelo. La profundidad de la red, determinada por el
número de capas ocultas, influye directamente en su capacidad para aprender relaciones
complejas y no lineales entre las variables.

Cada neurona artificial asigna un **peso** a cada característica de entrada, indicando la
importancia relativa de esa variable en el resultado final. Además, cada neurona incluye
un **sesgo** (_bias_), un valor adicional que permite ajustar la función de salida y
otorga mayor flexibilidad al modelo. Tanto los pesos como el sesgo se inicializan de
manera aleatoria al comienzo del entrenamiento y se ajustan progresivamente mediante
algoritmos de optimización. Estos constituyen los **parámetros aprendibles** de los
modelos de inteligencia artificial, cuya configuración final determina el comportamiento
y las capacidades del modelo entrenado.

El resultado de la combinación lineal de las entradas ponderadas por los pesos, sumado al
sesgo, pasa posteriormente por una **función de activación no lineal**. Este componente
es esencial, ya que otorga a la red la capacidad de capturar relaciones complejas y no
lineales entre variables, superando las limitaciones de los modelos puramente lineales.
Sin funciones de activación no lineales, una red neuronal multicapa se comportaría
simplemente como un modelo lineal, independientemente de su profundidad. Un ejemplo
clásico que ilustra esta limitación es el problema de la **puerta XOR**: a pesar de tener
solo cuatro posibles combinaciones de entrada (00, 01, 10, 11), sus salidas (0, 1, 1, 0)
no pueden separarse mediante una frontera de decisión lineal, lo que demuestra la
necesidad de combinaciones no lineales para resolver incluso problemas aparentemente
simples.

El **teorema de aproximación universal** establece que una red neuronal con suficiente
profundidad o anchura (donde la profundidad se refiere al número de capas y la anchura al
número de neuronas por capa) y funciones de activación no lineales puede aproximar
cualquier función continua con precisión arbitraria. Sin embargo, este resultado es de
naturaleza teórica y no garantiza que dicha aproximación sea prácticamente alcanzable con
los recursos y algoritmos de entrenamiento disponibles.

Las redes neuronales profundas constituyen una extensión de las redes neuronales
artificiales tradicionales. Su principal diferencia radica en la presencia de múltiples
capas ocultas, dispuestas de manera secuencial, lo que permite construir representaciones
jerárquicas de la información. Las primeras capas de la red, situadas cerca de la
entrada, suelen detectar únicamente características elementales. Por ejemplo, en
arquitecturas diseñadas para procesar imágenes, las capas iniciales tienden a identificar
líneas horizontales, verticales o diagonales. Conforme se avanza hacia capas más
profundas, las representaciones se vuelven progresivamente más sofisticadas, ya que se
construyen combinando las características detectadas en etapas anteriores. De este modo,
en niveles intermedios es posible identificar formas más estructuradas, mientras que en
las capas finales se logran representaciones de alto nivel que corresponden a objetos
completos o conceptos abstractos.

### Composición de funciones y no linealidad

Un concepto fundamental en el diseño de redes neuronales es la **composición de
funciones**, que consiste en descomponer operaciones complejas en secuencias de
transformaciones más simples y manejables. El funcionamiento de una red neuronal puede
expresarse como múltiples operaciones parametrizadas encadenadas una tras otra:

$$
f(x) = (f_2 \circ f_1)(x) = f_2(f_1(x)),
$$

donde cada función $f_\ell$ corresponde a una capa del modelo con sus propios parámetros.
Esta composición puede extenderse a un número arbitrario de funciones, siempre que cada
una conserve el tipo de datos de la capa anterior. Los parámetros de cada función se
ajustan durante el entrenamiento de manera interdependiente, ya que la salida de una capa
constituye la entrada de la siguiente.

Sin embargo, si todas las funciones de la composición son lineales, la cadena completa
colapsa en una única transformación lineal, independientemente del número de capas. Por
ejemplo, si se tienen dos funciones lineales sucesivas $f_1(x) = W_1 x + b_1$ y
$f_2(h) = W_2 h + b_2$, la composición resulta en
$f_2(f_1(x)) = W_2 W_1 x + W_2 b_1 + b_2$, que sigue siendo una función lineal. Por ello,
la introducción de **funciones de activación no lineales** entre capas resulta
imprescindible para romper este colapso y dotar a la red de la capacidad de modelar
relaciones complejas.

### De neuronas a redes neuronales

Una **neurona artificial** se puede representar de manera similar a una regresión
logística: recibe entradas, las combina linealmente mediante pesos y sesgo, y aplica una
función de activación para producir una salida. Una **red neuronal** se construye al
**apilar múltiples neuronas organizadas en capas**, interconectadas entre sí, de manera
que la información procesada por una neurona puede transmitirse a otras neuronas de la
misma capa o de capas posteriores.

Añadir capas ocultas hace que el problema de optimización de las redes neuronales se
convierta en **no convexo**, lo que significa que la función de coste puede presentar
múltiples mínimos locales. A mayor número de capas y parámetros, es decir, a mayor número
de grados de libertad de la red, más no convexa es la función que debe optimizarse. En
consecuencia, pequeños cambios en la inicialización de los parámetros pueden alterar
significativamente el resultado final del entrenamiento.

### Parámetros e hiperparámetros

En el entrenamiento de redes neuronales profundas resulta esencial distinguir entre
parámetros e hiperparámetros. Los **parámetros** incluyen los pesos y sesgos de la red,
los cuales se aprenden automáticamente mediante algoritmos de optimización. Los
**hiperparámetros**, en cambio, se definen antes del entrenamiento y controlan aspectos
estructurales y dinámicos del modelo. Entre ellos destacan la **tasa de aprendizaje**, el
número de iteraciones o épocas, la cantidad de capas ocultas, el número de neuronas por
capa y la elección de funciones de activación. La búsqueda de hiperparámetros constituye
un proceso iterativo en el que se combinan prueba y error con estrategias más
sistemáticas, con el fin de encontrar la configuración que produzca el mejor desempeño.

### Funciones de activación

Las **funciones de activación** introducen no linealidad en la red neuronal, permitiendo
que el modelo aprenda relaciones complejas entre los datos. La elección de la función de
activación es fundamental y depende del tipo de capa y del problema a resolver. Las
salidas de la función parametrizada de la neurona o red neuronal se conocen como los
_logits_, y es posible distinguir entre las salidas **pre-activación** (antes de aplicar
la función de activación) y **post-activación** (después de aplicarla).

En las **capas ocultas**, se emplean funciones de activación como:

- **ReLU (_Rectified Linear Unit_)**: Es ampliamente utilizada en redes profundas, ya que
  acelera el entrenamiento y evita problemas de gradientes muy pequeños. No obstante,
  puede provocar **neuronas muertas**, que siempre devuelven cero. Para mitigar este
  efecto se utilizan variantes como _Leaky ReLU_, que mantiene un pequeño gradiente para
  valores negativos:

$$
f(x) = \max(0, x).
$$

- **Sigmoide**: Transforma los valores en el rango $[0,1]$. Se utiliza en redes
  recurrentes, aunque presenta el problema de **gradientes que desaparecen** en los
  extremos:

$$
\sigma(x) = \frac{1}{1 + e^{-x}}.
$$

- **Tangente hiperbólica (tanh)**: Normaliza las salidas en el rango $[-1, 1]$. Suele
  preferirse frente a la sigmoide en capas ocultas porque sus activaciones tienen media
  cercana a cero, lo que facilita el entrenamiento. Tanto la sigmoide como la tangente
  hiperbólica tienden a saturarse en valores extremos, provocando gradientes muy pequeños
  que ralentizan el proceso de aprendizaje:

$$
\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}.
$$

En las **capas de salida**, la función de activación se selecciona según el rango de
valores esperado:

- **Clasificación binaria:** Sigmoide.
- **Clasificación multiclase (mutuamente excluyentes):** _Softmax_.
- **Clasificación multietiqueta:** Sigmoide, ya que una muestra puede pertenecer
  simultáneamente a varias clases.
- **Regresión:** Activación lineal, permitiendo que la salida adopte cualquier valor
  real.

### Implementación de una red neuronal

El siguiente ejemplo implementa una red neuronal de dos capas para un conjunto de datos
sintético. Este código ilustra de manera práctica cómo construir, entrenar y evaluar una
red neuronal simple utilizando **ReLU** en la capa oculta y **sigmoide** en la capa de
salida para un problema de clasificación binaria:

```py linenums="1"
import numpy as np
import matplotlib.pyplot as plt

# Crear dataset sintético
np.random.seed(0)
m = 200  # número de ejemplos
X = np.random.randn(2, m)  # 2 características
Y = (X[0, :] * X[1, :] > 0).astype(int).reshape(1, m)

# Funciones auxiliares
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def relu(z):
    return np.maximum(0, z)

def relu_derivative(z):
    return (z > 0).astype(float)

def compute_loss(Y, A):
    m = Y.shape[1]
    return -(1/m) * np.sum(Y*np.log(A+1e-8) + (1-Y)*np.log(1-A+1e-8))

# Inicializar parámetros
def initialize_parameters(n_x, n_h, n_y):
    np.random.seed(1)
    W1 = np.random.randn(n_h, n_x) * 0.01
    b1 = np.zeros((n_h, 1))
    W2 = np.random.randn(n_y, n_h) * 0.01
    b2 = np.zeros((n_y, 1))
    return {"W1": W1, "b1": b1, "W2": W2, "b2": b2}

# Forward propagation
def forward_propagation(X, params):
    W1, b1, W2, b2 = params["W1"], params["b1"], params["W2"], params["b2"]
    Z1 = np.dot(W1, X) + b1
    A1 = relu(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)
    cache = {"Z1": Z1, "A1": A1, "Z2": Z2, "A2": A2}
    return A2, cache

# Backpropagation
def backward_propagation(X, Y, params, cache):
    m = X.shape[1]
    W2 = params["W2"]
    A1, A2, Z1 = cache["A1"], cache["A2"], cache["Z1"]

    dZ2 = A2 - Y
    dW2 = (1/m) * np.dot(dZ2, A1.T)
    db2 = (1/m) * np.sum(dZ2, axis=1, keepdims=True)

    dA1 = np.dot(W2.T, dZ2)
    dZ1 = dA1 * relu_derivative(Z1)
    dW1 = (1/m) * np.dot(dZ1, X.T)
    db1 = (1/m) * np.sum(dZ1, axis=1, keepdims=True)

    return {"dW1": dW1, "db1": db1, "dW2": dW2, "db2": db2}

# Actualizar parámetros
def update_parameters(params, grads, lr):
    params["W1"] -= lr * grads["dW1"]
    params["b1"] -= lr * grads["db1"]
    params["W2"] -= lr * grads["dW2"]
    params["b2"] -= lr * grads["db2"]
    return params

# Entrenamiento
def model(X, Y, n_h=3, num_iterations=10000, lr=0.1, print_loss=True):
    n_x, n_y = X.shape[0], Y.shape[0]
    params = initialize_parameters(n_x, n_h, n_y)

    for i in range(num_iterations):
        A2, cache = forward_propagation(X, params)
        loss = compute_loss(Y, A2)
        grads = backward_propagation(X, Y, params, cache)
        params = update_parameters(params, grads, lr)

        if print_loss and i % 1000 == 0:
            print(f"Iteración {i}, pérdida: {loss:.4f}")

    return params

# Predicciones
def predict(X, params):
    A2, _ = forward_propagation(X, params)
    return (A2 > 0.5).astype(int)

# Ejecutar el modelo
params = model(X, Y, n_h=3, num_iterations=10000, lr=0.1)
Y_pred = predict(X, params)
acc = np.mean(Y_pred == Y) * 100
print(f"Precisión final: {acc:.2f}%")
```

### División del conjunto de datos

En el entrenamiento de modelos de aprendizaje automático, la gestión adecuada de los
datos constituye un paso fundamental para garantizar un proceso de optimización eficiente
y una evaluación rigurosa del rendimiento.

Como se mencionó anteriormente, el descenso de gradiente estocástico permite aplicar el
algoritmo de optimización sobre subconjuntos de datos en lugar de sobre la totalidad del
conjunto de entrenamiento. Al evaluar el gradiente en un lote reducido, se obtiene
información temprana sobre el progreso de la optimización sin necesidad de procesar todas
las muestras, lo que facilita un aprendizaje más rápido y actualizaciones de los
parámetros con mayor frecuencia.

El uso de lotes resulta especialmente ventajoso en entornos con GPU, ya que estas
permiten almacenar los datos en memoria gráfica y ejecutar cálculos de manera altamente
paralelizada. El tamaño de los lotes depende principalmente de la capacidad de memoria
disponible, siendo comunes valores como 32, 64, 128 o superiores. En general, se tiende a
utilizar lotes tan grandes como lo permita la memoria, aunque el tamaño seleccionado
puede afectar las métricas de evaluación del modelo. Por ejemplo, en arquitecturas
basadas en _autoencoders_, se observa un mejor desempeño con lotes pequeños, ya que esto
limita la tendencia de la red a memorizar patrones específicos. En contraste, en tareas
supervisadas de clasificación de imágenes o en metodologías contrastivas, los lotes más
grandes suelen ser beneficiosos, ya que permiten calcular un mayor número de métricas de
distancia entre pares de muestras y construir matrices de similitud más robustas.

En contextos de aprendizaje autosupervisado, el modo en que se agrupan las muestras en
lotes afecta directamente tanto a las funciones de coste como al proceso de optimización,
ya que muchas de estas funciones se basan en medidas de distancia entre elementos de un
mismo lote. Incluso en modelos de lenguaje de gran escala se ha observado que la forma de
dividir los datos en lotes repercute en la salida final del modelo, generando
variabilidad que se explica no solo por errores numéricos, sino también por la
composición de los mini-lotes y las distribuciones de las muestras que los componen.

El procedimiento habitual consiste en aplicar una permutación aleatoria (_shuffle_) al
conjunto de entrenamiento y dividirlo en lotes consecutivos de tamaño fijo. Una vez
procesados todos los lotes, se vuelve a permutar el conjunto y se repite el proceso. Esta
división puede distribuirse entre múltiples nodos o GPU, lo que se conoce como
**paralelización de datos**: cada GPU procesa de manera independiente un lote, calcula
los gradientes correspondientes, y posteriormente todos los gradientes se agregan de
forma síncrona para actualizar los parámetros globales de la red. Cuando el lote completo
no cabe en una sola GPU, se puede recurrir a la **acumulación de gradientes**, que
consiste en iterar sobre subconjuntos más pequeños acumulando los gradientes antes de
realizar la actualización, aunque este enfoque es menos eficiente al no aprovechar
plenamente la paralelización del hardware.

```py linenums="1"
from torch.utils.data import DataLoader
dataloader = DataLoader(dataset, shuffle=True, batch_size=32)
for xb, yb in dataloader:
    pass  # Procesamiento del lote
```

De manera clásica, durante el desarrollo de modelos de aprendizaje automático los
conjuntos de datos se dividen en tres subconjuntos principales:

1. **Conjunto de entrenamiento**: Se emplea para ajustar los parámetros internos del
   modelo mediante el proceso de optimización.
2. **Conjunto de validación**: Formado por ejemplos no utilizados en el entrenamiento
   directo. Su función es evaluar la capacidad de generalización del modelo y guiar la
   selección de hiperparámetros, reduciendo el riesgo de sobreajuste.
3. **Conjunto de prueba**: Reservado para la evaluación final y objetiva del modelo una
   vez completado el entrenamiento y optimizados los hiperparámetros.

La proporción destinada a cada subconjunto depende de la cantidad de datos disponibles.
Con bases de datos pequeñas, se suele aplicar una partición del 70 % para entrenamiento y
30 % para prueba. En bases de datos más extensas, resulta común asignar un 60 % al
entrenamiento, 20 % a la validación y 20 % a la prueba. Es esencial que los subconjuntos
de validación y prueba sigan la misma distribución que los datos de entrenamiento, ya que
una discrepancia significativa puede generar degradaciones en las métricas de evaluación.
Cuando los datos son escasos, la **validación cruzada K-fold** constituye una alternativa
robusta: el conjunto de datos se divide en $K$ particiones, se entrenan $K$ modelos
idénticos utilizando $K-1$ particiones para entrenamiento y la restante para validación,
y la métrica final se obtiene como el promedio de las $K$ evaluaciones.

En entornos de producción, las distribuciones de los datos suelen variar con el tiempo,
fenómeno conocido como **cambio de concepto (_concept drift_)**. Para detectar y
cuantificar estas desviaciones se utilizan métricas como la divergencia de
Kullback-Leibler, la divergencia de Jensen-Shannon u otras medidas de distancia entre
distribuciones. Asimismo, técnicas como el análisis de entropía, los _autoencoders_ o el
Análisis de Componentes Principales (PCA) permiten medir errores de reconstrucción y
establecer umbrales para identificar muestras fuera de distribución. La detección de
datos fuera de distribución constituye una línea de investigación activa, con
aplicaciones en el aprendizaje activo, el _meta-learning_ y la mitigación del olvido
catastrófico.

Es importante tener en cuenta ciertas consideraciones al dividir los datos. Si se trabaja
con datos temporales (predicción del futuro a partir del pasado), no se deben mezclar
aleatoriamente antes de la división, ya que esto crearía una fuga temporal donde el
modelo se entrenaría con datos del futuro. En estos casos, los datos de prueba deben ser
siempre posteriores a los de entrenamiento. Además, si existen datos duplicados o
redundantes, es necesario asegurarse de que no aparezcan simultáneamente en los conjuntos
de entrenamiento y validación, ya que esto equivaldría a evaluar el modelo con parte de
sus propios datos de entrenamiento.

### Sesgo y varianza

El análisis de sesgo y varianza constituye una herramienta fundamental para comprender
las fuentes de error en los modelos de aprendizaje automático. El **sesgo** se define
como la diferencia sistemática entre las predicciones del modelo y los valores reales. Un
sesgo alto indica la presencia de subajuste, lo que significa que el modelo no logra
capturar de manera adecuada la complejidad de la relación existente en los datos. Por
otro lado, la **varianza** mide la sensibilidad del modelo frente a pequeñas variaciones
en los datos de entrenamiento. Una varianza alta refleja la existencia de sobreajuste.

La reducción del sesgo suele requerir un aumento en la capacidad de representación del
modelo, mediante arquitecturas más profundas o complejas, el incremento del número de
parámetros, un mayor tiempo de entrenamiento o la adopción de algoritmos alternativos. En
contraste, para disminuir la varianza se recurre a estrategias orientadas a mejorar la
capacidad de generalización, tales como el incremento de la cantidad y diversidad de
datos de entrenamiento, la aplicación de técnicas de regularización o ajustes en la
arquitectura y en los hiperparámetros del modelo.

En la práctica, el análisis de sesgo y varianza se complementa con la noción de **techo
de referencia humano**, empleado para evaluar modelos cuyo desempeño se compara con el
nivel de expertos humanos. En este marco, el **sesgo evitable** se entiende como la
diferencia entre el error mínimo alcanzable por un ser humano y el error observado en el
modelo, mientras que la **varianza** se cuantifica como la diferencia entre el error en
el conjunto de entrenamiento y el error en el conjunto de validación.

### Desvanecimiento y explosión de gradientes

Uno de los principales desafíos en el entrenamiento de redes neuronales profundas es el
fenómeno conocido como desvanecimiento o explosión de gradientes. Ambos problemas se
presentan durante el proceso de _backpropagation_, cuando los gradientes tienden a
disminuir hasta valores cercanos a cero o, por el contrario, a crecer de manera
exponencial. Esta inestabilidad dificulta o incluso imposibilita el aprendizaje, ya que
los parámetros no se actualizan de manera adecuada. En la práctica, este comportamiento
puede provocar que la función de pérdida devenga en valores **NaN** (_Not a Number_),
interrumpiendo el proceso de optimización.

Para mitigar estos fenómenos se emplean diversas estrategias:

- **Inicialización adecuada de los pesos**: Métodos como Xavier o He ajustan la escala
  inicial de los parámetros según la cantidad de neuronas por capa, evitando que los
  gradientes crezcan o decrezcan de manera descontrolada desde el inicio del
  entrenamiento.
- **Normalización de los datos de entrada**: Escalar las características de entrada para
  que tengan media cero y varianza unitaria contribuye a estabilizar el flujo de
  gradientes.
- **Funciones de activación más estables**: El uso de activaciones como ReLU y sus
  variantes reduce la saturación observada en funciones como la sigmoide o la tangente
  hiperbólica.
- **Clipado de gradientes**: Consiste en limitar el rango de valores que pueden alcanzar
  los gradientes durante la retropropagación, evitando actualizaciones excesivas. Es
  común emplear intervalos como $[-1, 1]$, aunque también existen variantes dinámicas.
- **Diseño arquitectónico específico**: La introducción de mecanismos de memoria y
  compuertas en redes como LSTM o GRU permite manejar dependencias de largo plazo. Más
  recientemente, los _Transformers_ han reemplazado en gran medida a las RNN, reduciendo
  estas limitaciones.

### Estrategia en el proceso de optimización

El diseño de una estrategia adecuada en el desarrollo de modelos de aprendizaje
automático resulta crucial para alcanzar un rendimiento óptimo. No todas las mejoras
introducidas durante el proceso de construcción del modelo tienen el mismo impacto en su
desempeño. En muchos casos, incrementar la cantidad y diversidad de datos disponibles o
modificar de manera sustancial la arquitectura de la red genera beneficios mucho mayores
que ajustes menores sobre los hiperparámetros.

Las métricas de evaluación dependen directamente del tipo de aprendizaje empleado, aunque
comparten el objetivo común de cuantificar la calidad de las predicciones. En aprendizaje
supervisado de clasificación, destacan medidas como la **precisión**, el **recall** o
sensibilidad, y la **puntuación F1**, definida como la media armónica entre la precisión
y el recall. Más allá de las métricas de exactitud, es indispensable considerar
indicadores de **eficiencia computacional**, tales como el tiempo de entrenamiento, la
latencia en la inferencia, el consumo de memoria y la escalabilidad del modelo.

Para implementar una estrategia de aprendizaje coherente y sostenible, se recomienda
emplear plataformas especializadas en la gestión de experimentos, como **MLflow**,
**Weights & Biases (wandb)** y soluciones similares. Estas herramientas permiten
registrar y organizar de forma sistemática todos los artefactos generados durante el
desarrollo del modelo, garantizando la **replicabilidad de los experimentos** y
facilitando la **comparación justa entre diferentes configuraciones**.

### Aprendizaje por transferencia

Además de las arquitecturas tradicionales, en el campo del aprendizaje profundo se han
desarrollado enfoques que no constituyen arquitecturas en sí mismas, sino **paradigmas de
aprendizaje** que buscan aprovechar de manera más eficiente los recursos computacionales
y los datos disponibles.

El **aprendizaje por transferencia** consiste en reutilizar el conocimiento adquirido por
un modelo previamente entrenado en una tarea determinada para aplicarlo en otra tarea
relacionada. La similitud entre las tareas es un requisito fundamental: no resulta viable
transferir directamente el conocimiento de un modelo entrenado en visión por computadora
a uno diseñado para procesar texto, ya que las representaciones internas aprendidas
difieren por completo.

El grado de reutilización depende en gran medida de la disponibilidad de datos en la
nueva tarea. Cuando los datos son escasos, suele reajustarse únicamente la parte final de
la red, mientras que el resto de la arquitectura se congela, preservando así las
representaciones generales previamente aprendidas. En cambio, cuando se dispone de una
cantidad suficiente de datos, es posible aplicar un ajuste fino o **_fine-tuning_**, que
consiste en reentrenar toda la red para adaptar gradualmente los parámetros a las
particularidades del nuevo dominio.

## Diferenciación automática

La diferenciación numérica, simbólica y automática constituye un conjunto de enfoques
complementarios para obtener derivadas de funciones. Cada método se fundamenta en
principios distintos y presenta características particulares que determinan su precisión,
su coste computacional y su aplicabilidad.

La **diferenciación numérica** aproxima la derivada a partir de valores concretos de la
función, sin manipular expresiones algebraicas ni reglas simbólicas. Se basa directamente
en la definición de derivada y sustituye el límite por un incremento finito $h$
suficientemente pequeño. La formulación más simple es la diferencia hacia adelante,
mientras que la diferencia centrada ofrece mayor precisión con un error de orden
$O(h^2)$:

$$
f'(x) \approx \frac{f(x+h) - f(x)}{h}, \quad f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}.
$$

El método opera exclusivamente con números y produce resultados aproximados cuya calidad
depende de la elección de $h$. Si $h$ es demasiado grande, la aproximación se degrada; si
es demasiado pequeño, emergen errores de redondeo asociados a la aritmética de coma
flotante. Además, cada derivada requiere varias evaluaciones de la función, lo que vuelve
esta técnica poco viable para problemas con grandes cantidades de variables. Por ello se
emplea sobre todo con fines de validación o en contextos de baja dimensionalidad.

La **diferenciación simbólica** opera directamente sobre la expresión matemática de la
función y utiliza reglas formales de derivación para obtener una fórmula exacta. Este
enfoque trabaja con símbolos en lugar de valores numéricos y permite obtener derivadas
sin aproximaciones. Sin embargo, al manipular expresiones complejas puede generar
fórmulas extremadamente grandes, fenómeno conocido como _expression swell_. Esta
explosión combinatoria limita su aplicación en programas extensos o en funciones
definidas de forma procedimental.

La **diferenciación automática** (AD) se sitúa conceptualmente entre los dos métodos
anteriores. No se basa en aproximaciones numéricas ni en transformaciones simbólicas
exhaustivas, sino en la evaluación sistemática de la estructura computacional de la
función. Aplica las reglas del cálculo diferencial durante la ejecución del programa y
propaga derivadas elementales a través de las operaciones que lo componen. El resultado
es exacto hasta los límites de la precisión de máquina, sin incurrir en errores de
aproximación ni en crecimiento explosivo de expresiones. En modo directo, el coste es
proporcional al número de variables; en modo inverso, utilizado en aprendizaje automático
para implementar _backpropagation_, el coste es comparable al de evaluar la propia
función. Esta eficiencia explica su papel central en la optimización de modelos
contemporáneos.

## Redes neuronales convolucionales

### Procesamiento visual humano y su analogía con las redes convolucionales

El procesamiento visual humano es un proceso jerárquico que transforma la información
lumínica captada por los ojos en representaciones visuales complejas y significativas. La
luz ingresa al ojo a través de la córnea y atraviesa el cristalino, que actúa como una
lente convexa proyectando la imagen invertida sobre la retina. En la retina, los
fotorreceptores (conos y bastones) convierten la energía lumínica en señales eléctricas,
iniciando la codificación neuronal de la información visual.

Estas señales se transmiten por el nervio óptico hasta el quiasma óptico, donde ocurre un
cruce parcial de la información visual que permite la percepción binocular y contribuye a
la percepción de profundidad. Posteriormente, las señales continúan hasta el núcleo
geniculado lateral (LGN) del tálamo, que funciona como estación de relevo y organiza la
información entrante. Desde el LGN, las señales se transmiten hacia la corteza visual
primaria (V1), localizada en el lóbulo occipital, que se organiza de manera retinotópica.

En la corteza visual primaria se distinguen tres tipos principales de células: células
simples, que responden a bordes con orientación específica; células complejas, que
detectan bordes o movimientos en rangos más amplios; y células hipercomplejas, que
reaccionan ante combinaciones más sofisticadas, como esquinas o terminaciones de líneas.
El procesamiento continúa en áreas corticales posteriores (V2, V4, IT), donde se analizan
características más complejas, incluyendo texturas, formas tridimensionales, rostros y
objetos completos.

Las redes neuronales convolucionales, también conocidas como **_Convolutional Neural
Networks_ (CNNs)**, son modelos computacionales diseñados para procesar datos visuales de
manera eficiente, inspirados directamente en esta arquitectura del sistema visual humano:

| Sistema Visual Humano                      | Redes Convolucionales (CNNs)                                     |
| ------------------------------------------ | ---------------------------------------------------------------- |
| Retina                                     | Imagen de entrada                                                |
| Nervio óptico / Quiasma óptico             | Preprocesamiento y alineación de la información visual           |
| LGN (núcleo geniculado lateral)            | División en canales o filtros por tipo de característica         |
| Corteza visual (V1, V2, V4, IT)            | Capas convolucionales jerárquicas                                |
| Células simples, complejas, hipercomplejas | Filtros convolucionales de bajo, medio y alto nivel              |
| Campos receptivos                          | Regiones locales (_receptive fields_) de los filtros (_kernels_) |
| Percepción jerárquica                      | Aprendizaje progresivo de características visuales               |

### Campo receptivo y jerarquía de procesamiento

El **campo receptivo** se define como la región del campo visual (o de la entrada) que
influye directamente en la actividad de una neurona específica. En las etapas iniciales
del procesamiento, los campos receptivos son pequeños y especializados en detectar
patrones simples. A medida que se avanza jerárquicamente, los campos receptivos se
expanden y se vuelven más complejos, integrando información de múltiples regiones para
formar representaciones más abstractas y globales.

En las redes convolucionales, el campo receptivo se puede simular definiendo ceros en las
matrices de pesos para aquellas regiones de píxeles que se encuentran fuera de la zona de
interés. Cada píxel tiene una relación con sus vecinos que puede representarse como un
grafo completamente conectado, donde la importancia de cada conexión depende de la
distancia entre los píxeles. Al colocar un cero en la matriz de pesos, se elimina la
influencia de un píxel vecino sobre el píxel evaluado. El campo receptivo crece
linealmente con el número de capas convolucionales, lo que motiva la noción de
**localidad**: aunque una sola capa está limitada por el tamaño del _kernel_, una pila
suficientemente grande de capas convolucionales resulta en un campo receptivo global.

### Conceptos fundamentales de la convolución

La visión computacional constituye uno de los campos más dinámicos de la inteligencia
artificial, con aplicaciones que abarcan desde la conducción autónoma hasta el
reconocimiento facial, la clasificación automática de imágenes y la segmentación de
objetos. Las redes convolucionales pueden trabajar con datos secuenciales de cualquier
tipo, aprovechando dos características fundamentales: la **capacidad de localización** y
el **compartimiento de parámetros**. Estas propiedades confieren a la operación de
convolución cierta invariancia a la traslación de la ventana (el propio _kernel_ o
filtro), aunque en la práctica esta propiedad se rompe cuando se combinan con otras
operaciones como mecanismos de _pooling_.

El principio subyacente que permite la transferencia de conocimiento entre dominios es la
existencia de una estructura espacio-temporal en los datos. En el caso de las imágenes,
esta estructura se refleja en la disposición relativa de los píxeles. Si se logra
transformar otros tipos de datos en representaciones visuales que conserven dicha
organización, es posible aplicar arquitecturas convolucionales de manera eficaz. Un
ejemplo de este enfoque se observa en la conversión de series temporales en imágenes
mediante técnicas como los _Gramian Angular Fields_, o en la transformación de señales de
audio en espectrogramas de tipo _Mel_.

El principal desafío al trabajar con imágenes radica en la elevada cantidad de
información que contienen. Una imagen en color de 64 × 64 píxeles con tres canales de
color requiere **12288 entradas** para la red neuronal. Introducir directamente esta
cantidad de datos en una arquitectura densa obligaría a disponer de capas iniciales con
decenas de miles de neuronas, lo que genera un coste computacional muy alto y un elevado
riesgo de sobreajuste.

La solución a este problema se encuentra en la operación de **convolución**. Este
procedimiento aplica filtros, también denominados _kernels_, que recorren la imagen en
busca de patrones característicos como bordes, esquinas o texturas. El resultado de cada
aplicación es un **mapa de características** (_activation map_), que cuantifica la
presencia del patrón detectado en diferentes regiones de la imagen. Desde el punto de
vista del procesamiento de señales, esta operación corresponde a un filtrado mediante
filtros de respuesta finita al impulso (FIR), implementado a través de una convolución
discreta. A diferencia de los filtros clásicos diseñados manualmente (como Sobel o
Scharr), los filtros de las redes convolucionales se inicializan aleatoriamente y se
entrenan mediante descenso del gradiente, lo que permite al modelo descubrir patrones
mucho más complejos y adaptados a la tarea específica.

Una propiedad fundamental de este mecanismo es la **invariancia al desplazamiento**, que
permite reconocer un mismo patrón independientemente de su ubicación. Esta invariancia se
origina gracias al compartimiento de pesos entre los diferentes filtros: lo que se
aprende en una parte de la imagen se traslada a otra parte. No obstante, esta propiedad
se manifiesta de manera estricta únicamente cuando la convolución se realiza con un
tamaño de paso igual a uno, y puede perderse parcialmente al introducir variaciones como
_stride_, _padding_ o capas densas posteriores.

A medida que la información avanza a través de las capas convolucionales, el tamaño
espacial de las representaciones disminuye mientras que el número de canales se
incrementa. Este proceso permite capturar progresivamente patrones de mayor nivel de
abstracción. En las imágenes, la influencia de un píxel sobre sus vecinos suele reducirse
con el incremento de la distancia, lo que implica que a mayor distancia entre píxeles,
menor correlación existe entre ellos. Esta propiedad de **localidad** es fundamental en
mecanismos modernos como la atención, que evalúan la importancia de los píxeles vecinos
para obtener un mejor entendimiento de la semántica de la imagen.

Las capas convolucionales no dependen del tamaño de la imagen de entrada, sino del tamaño
del filtro y del número de canales utilizados. Sin embargo, en la práctica resulta
complicado procesar tensores de tamaños variables en un mismo lote, y además pueden
surgir problemas como el olvido catastrófico, ya que entrenar con distribuciones de datos
de tamaños muy diferentes altera las relaciones entre píxeles vecinos y las componentes
de alta frecuencia.

### Componentes de una capa convolucional

El uso de convoluciones en redes neuronales introduce una serie de elementos esenciales.
El **relleno (_padding_)** consiste en añadir bordes artificiales alrededor de la imagen
para evitar la pérdida de información en los márgenes y mantener las dimensiones
originales de la entrada. El **desplazamiento (_stride_)** define el número de píxeles
que el filtro avanza en cada paso al recorrer la imagen; un valor mayor reduce las
dimensiones de la salida y disminuye el número de cálculos necesarios. Cuando el tamaño
del _stride_ coincide con el del filtro, el proceso es equivalente a dividir la imagen en
fragmentos independientes (_patches_), concepto que ha dado lugar a arquitecturas
avanzadas basadas en _Transformers_, como **ViT** (_Vision Transformer_), donde cada
submatriz de la imagen se convierte en un _token_ que el modelo procesa.

En el caso de imágenes en color, los filtros se extienden a tres dimensiones para
recorrer simultáneamente los canales rojo, verde y azul. El número de parámetros de una
capa convolucional depende únicamente del tamaño y la cantidad de filtros, y no de las
dimensiones de la imagen de entrada. Por ejemplo, una capa con 10 filtros de 3 × 3 × 3
requiere solo 280 parámetros, cifra muy reducida frente a los millones de conexiones que
implicaría una arquitectura densa equivalente.

Las convoluciones resultan efectivas por dos motivos principales: permiten una
**reducción drástica del número de parámetros** y implementan la **compartición de
parámetros**, ya que un patrón aprendido en una región de la imagen puede aplicarse en
cualquier otra.

Tras la convolución, suele aplicarse una etapa de **agrupamiento (_pooling_)**, destinada
a reducir las dimensiones intermedias y aportar robustez frente a pequeñas variaciones
espaciales. La técnica más extendida es el **_max pooling_**, que selecciona el valor
máximo dentro de cada región, priorizando la detección de la presencia de una
característica por encima de su ubicación exacta. Otra variante frecuente es el
**_average pooling_**, que sustituye cada región por el valor promedio de sus elementos.
Los mecanismos de _pooling_ global destruyen la información espacial, por lo que se
implementan técnicas parciales como el _max pooling_ con ventanas de 2 × 2, que permite
reducir la resolución espacial a la mitad manteniendo el número de canales intacto.

En la gran mayoría de arquitecturas modernas basadas en convolución, ya no se utilizan
capas densas finales con aplanamiento de tensores. En su lugar, se emplea **_Global
Average Pooling_**, que consiste en calcular el promedio global de los valores de cada
mapa de características, obteniendo un único valor por canal. Este mecanismo es
invariante a los desplazamientos, preserva la información espacial, y reduce
significativamente la cantidad de parámetros en comparación con el aplanamiento seguido
de capas densas. Sin embargo, la agregación uniforme del _Global Average Pooling_ puede
generar una geometría pobre en las representaciones embebidas del modelo.

La arquitectura típica de una red convolucional se divide en dos partes: el
**_backbone_** (esqueleto del modelo), que utiliza capas convolucionales para extraer
características de los datos de entrada, y la **cabeza** (_head_), que emplea las capas
finales para realizar la tarea específica (clasificación, regresión, etc.).

### Tipos de operaciones convolucionales

Existen variantes especializadas de la convolución que permiten optimizar el
procesamiento:

- **Convolución 1×1 (_pointwise convolution_)**: Actualiza la representación de cada
  píxel mediante una combinación ponderada de sus canales, sin considerar los píxeles
  vecinos. Resulta útil para modificar la dimensión de canales.
- **Convolución en profundidad (_depthwise convolution_)**: Combina píxeles en un
  vecindario pequeño, pero procesando cada canal de manera independiente. Puede
  generalizarse considerando grupos de canales (_groupwise convolution_).
- **Convolución separable en profundidad (_depthwise separable convolution_)**: Alterna
  convoluciones 1×1 (para mezclar canales) y convoluciones en profundidad (para mezclar
  píxeles). Es común en CNNs diseñadas para dispositivos de bajo consumo, como MobileNet.

### Evolución de las arquitecturas

El incremento en la profundidad de las redes neuronales ha permitido avances
significativos en la visión computacional. Sin embargo, a partir de cierto punto, el
rendimiento no mejora sino que se degrada, debido a fenómenos como la desaparición o
explosión de gradientes.

La solución a este desafío surgió con las **redes residuales (ResNet)**, que incorporan
**conexiones de atajo (_skip connections_)** que transmiten directamente las activaciones
de una capa hacia otra más profunda. Cada bloque residual no aprende una transformación
completa, sino la diferencia (_residuo_) entre la entrada y la salida esperada. Las redes
residuales pueden verse como la suma de múltiples caminos donde la entrada permanece sin
alterar a la par que recibe transformaciones o combinaciones de múltiples
transformaciones. El número de caminos crece exponencialmente con el número de bloques
residuales, y estos caminos pueden interpretarse como pequeños modelos que comparten
información entre sí mediante _weight-sharing_. Desde una perspectiva neurocientífica,
este mecanismo recuerda a la organización de la **columna cortical**, que se estructura
en seis niveles jerárquicos: desde las capas superiores de reconexión con pocas neuronas,
pasando por las capas intermedias de procesamiento y las capas que reciben información
sensorial directa, hasta las capas inferiores que almacenan información espacial y de
posición. El salto de información desde las capas inferiores (nivel 6) hacia las capas
superiores (niveles 2 y 3) constituye una analogía biológica directa de las _skip
connections_ empleadas en las redes residuales.

Otra innovación relevante fue la **arquitectura Inception** (GoogLeNet), que aplica en
paralelo filtros de distintos tamaños (1×1, 3×3 y 5×5) junto con una operación de
_pooling_, y concatena los resultados. Para controlar el coste computacional, se
introdujeron convoluciones de 1×1 como cuellos de botella.

Con la expansión de los dispositivos móviles surgieron las **MobileNet**, basadas en
**convoluciones separables en profundidad**. La segunda generación, **MobileNetV2**,
incorporó conexiones residuales junto con capas de expansión mediante filtros 1×1.

### Sistemas de detección de objetos

En muchas aplicaciones de la visión computacional no basta con clasificar una imagen en
su conjunto, sino que es imprescindible identificar **qué objetos aparecen en la escena y
en qué lugar se encuentran**. Este desafío se aborda mediante la **detección de
objetos**, que combina simultáneamente la clasificación y la localización de los
elementos presentes a través de recuadros delimitadores (_bounding boxes_).

Una estrategia habitual consiste en dividir la imagen en una **malla de celdas**, donde
cada celda predice la presencia de objetos cuyo centro se encuentra en su interior. Uno
de los algoritmos más influyentes es **YOLO (_You Only Look Once_)**, que aplica la red
convolucional a toda la imagen de manera simultánea, permitiendo detecciones en tiempo
real.

El desempeño de los modelos de detección se evalúa mediante métricas como la
**Intersección sobre Unión (IoU)**, la **Supresión de No Máximos (NMS)** y las **Cajas de
Anclaje (_anchor boxes_)**. Además de la detección convencional, existen variantes como
la detección de puntos de referencia y los métodos basados en regiones.

### Segmentación semántica y convoluciones transpuestas

La **segmentación semántica** asigna una **clase específica a cada píxel** de la imagen.
Para reconstruir la resolución espacial original a partir de representaciones
comprimidas, se emplea la **convolución transpuesta**, que expande las dimensiones
espaciales.

Un hito en este ámbito lo constituye la **arquitectura U-Net**, que se estructura en una
etapa de compresión (_encoder_) y una etapa de expansión (_decoder_), conectadas mediante
**conexiones de omisión (_skip connections_)** que transfieren información directamente
desde las capas de compresión a las de expansión, conservando detalles finos de bordes y
contornos.

### _One-Shot Learning_

Los modelos de visión por computador suelen requerir grandes volúmenes de datos para
alcanzar un entrenamiento eficaz. Sin embargo, en numerosos escenarios prácticos solo se
dispone de un número muy reducido de ejemplos por clase. Este desafío se aborda mediante
técnicas como el **_One-Shot Learning_** y el **_Few-Shot Learning_**, que buscan dotar a
los sistemas de la capacidad de generalizar a partir de datos escasos.

El principio fundamental consiste en aprender un **espacio de representación** en el que
las imágenes similares se ubiquen próximas entre sí, mientras que las correspondientes a
clases distintas aparezcan más alejadas. Una de las arquitecturas más representativas son
las **redes siamesas**, que procesan en paralelo dos imágenes mediante una misma red
convolucional que comparte parámetros. Otra estrategia ampliamente utilizada es la basada
en la **pérdida triple (_triplet loss_)**, que organiza el entrenamiento a partir de
tríos de imágenes: _anchor_, positiva y negativa.

### Aprendizaje contrastivo y autosupervisado

El **aprendizaje autosupervisado** permite entrenar modelos robustos sin la necesidad de
disponer de grandes volúmenes de datos etiquetados, generando automáticamente señales de
supervisión a partir de los propios datos. Dentro de este paradigma, una de las
estrategias más influyentes emplea la **pérdida contrastiva**, cuyo propósito es aprender
un espacio de representación en el que las imágenes similares se ubiquen próximas entre
sí.

En escenarios sin etiquetas, los **pares positivos** se generan mediante transformaciones
aplicadas a una misma imagen (rotaciones, cambios de escala, recortes aleatorios,
modificaciones de color), mientras que las **imágenes distintas** se consideran pares
negativos.

El proceso de entrenamiento contrastivo incluye varias etapas esenciales: obtención de un
conjunto de datos no etiquetados, generación de _embeddings_ mediante un modelo
preentrenado, optimización mediante _fine-tuning_ utilizando medidas de distancia entre
_embeddings_, e iteración con ajuste manual de las muestras más problemáticas.

Entre las funciones de pérdida más utilizadas destacan:

La **Triplet Loss** se fundamenta en tres elementos (ancla, par positivo y par negativo):

$$
L = \min_{\theta}\left(\max\left(0, \text{dist}(X, X^+) - \text{dist}(X, X^-) + \text{margen}\right)\right).
$$

La **Contrastive Loss** se aplica a pares de datos:

$$
L = (1 - y) \frac{1}{2} \left( \text{dist}(X_1, X_2) \right)^2 + y \frac{1}{2} \left( \max(0, m - \text{dist}(X_1, X_2)) \right)^2.
$$

La **InfoNCE Loss**, utilizada en arquitecturas como **SimCLR**, maximiza la similitud
entre un dato ancla y su par positivo mientras minimiza la similitud con los pares
negativos:

$$
L = -\frac{1}{N} \sum_{i=1}^N \log \frac{\exp(\text{sim}(z_i, z_i^+)/\tau)}{\sum_{j=1}^K \exp(\text{sim}(z_i, z_j^-)/\tau)}.
$$

Entre las limitaciones del aprendizaje contrastivo se encuentran la dependencia de
transformaciones adecuadas de aumentación de datos y la necesidad de un gran número de
épocas y lotes suficientemente grandes para obtener pares negativos efectivos. Además, en
sistemas con múltiples atributos finos, puede producirse un fenómeno de
**_entanglement_** donde las características finas no son fácilmente separables, lo que
provoca un colapso de las representaciones embebidas: muestras que deberían estar
diferenciadas acaban con representaciones muy similares en el espacio latente. Este
colapso también puede ocurrir con los filtros que aprenden las redes convolucionales,
donde un número excesivo de filtros puede llevar a que muchos de ellos aprendan
características redundantes.

Modelos como **DINOv1** y **DINOv2** de Meta han demostrado la eficacia del aprendizaje
autosupervisado en visión computacional, utilizando representaciones de imágenes con
recortes parciales para el estudiante y visiones completas para el maestro, lo que
permite obtener representaciones globales de alta calidad. Estos sistemas también se
emplean para refinar conjuntos de datos, eliminando duplicados y filtrando imágenes no
apropiadas mediante búsqueda de similitud entre representaciones embebidas.

## Convolución en otros tipos de datos

Las convoluciones no se limitan al procesamiento de imágenes, sino que pueden aplicarse a
cualquier tipo de datos que presente una estructura espacio-temporal. En **series
temporales**, se emplean convoluciones unidimensionales que capturan patrones locales a
lo largo del eje temporal. En **audio**, la señal puede representarse mediante
espectrogramas _Mel_ obtenidos a partir de la transformada discreta de Fourier, lo que
convierte el sonido en una imagen bidimensional que evoluciona con la frecuencia y el
tiempo. En **vídeo**, la representación corresponde a un tensor de cuatro dimensiones
(alto, ancho, canales y tiempo), donde el tiempo refleja la sucesión de fotogramas.

Es importante señalar que las dimensiones espaciales (como las de una imagen) pueden
considerarse simétricas, mientras que las dimensiones temporales son asimétricas: una
señal de audio invertida en su eje temporal es, en general, inválida, y una serie
temporal invertida representa una evolución del futuro hacia el pasado.

En el ámbito del **procesamiento del lenguaje natural**, las frases o palabras se dividen
en secuencias de unidades más pequeñas denominadas **_tokens_**. Un _token_ puede
representar un carácter, una palabra completa, un fragmento intermedio entre ambos,
signos de puntuación, símbolos especiales o incluso emojis, que pueden aportar
información contextual relevante (por ejemplo, para la detección de sentimientos). Esta
división depende del tipo de arquitectura y de las decisiones de diseño durante la
creación del modelo. Cada _token_ se convierte posteriormente en una representación
embebida (_embedding_) que el modelo puede procesar.

Empresas como OpenAI han publicado de forma abierta sus tokenizadores, que cuentan con un
vocabulario definido para convertir el corpus de texto en _tokens_. La conversión de
_tokens_ a _embeddings_ puede realizarse mediante modelos preentrenados o integrando el
entrenamiento de los _embeddings_ junto con el resto de la red. Técnicas como _one-hot
encoding_ resultan menos eficientes debido a la gran cantidad de ceros que generan,
produciendo vectores dispersos (_sparse_) que pueden sufrir la maldición de la
dimensionalidad al realizar operaciones vectoriales. Los _embeddings_ densos, en cambio,
permiten obtener representaciones que codifican relaciones semánticas directas entre
palabras, como sinónimos, antónimos, cambios de género o variaciones de capitalización.

Dado que las secuencias de texto suelen ser extensas, la convolución estándar puede
quedarse limitada en capturar todo el contexto. Para ampliar el campo receptivo sin
incrementar el número de parámetros, se emplean **convoluciones dilatadas** (_dilated
convolutions_): una dilatación igual a uno equivale a una convolución estándar, mientras
que una dilatación igual a dos implica que el filtro solo considera píxeles alternos,
ampliando el campo receptivo sin aumentar la complejidad del modelo. Este tipo de
convoluciones se ha utilizado en arquitecturas como **WaveNet** para la generación de
audio.

## Otras técnicas del procesamiento de imágenes

En el preprocesamiento de imágenes existen diversas técnicas que permiten mejorar la
calidad visual y la distribución de intensidades antes de alimentar un modelo. La
**ecualización de histograma** extiende el rango de colores distribuyendo los valores
entre los diferentes intervalos (_bins_) del histograma. Una variante más sofisticada es
**CLAHE** (_Contrast Limited Adaptive Histogram Equalization_), que divide la imagen en
ventanas (_patches_) y ecualiza cada una de forma independiente. Aunque esto mejora el
contraste local, puede incrementar el ruido al perder información global. El parámetro de
_clip limit_ permite limitar esta amplificación del ruido, controlando el contraste
máximo permitido en cada ventana.

Estas técnicas de procesamiento pueden combinarse con las capacidades de las redes
convolucionales para crear sistemas o _pipelines_ que permitan recopilar y curar datos de
Internet. Por ejemplo, si se dispone de una representación embebida de una categoría de
imágenes (como gatos), es posible utilizar sistemas de búsqueda por similitud entre
_embeddings_ para ampliar el conjunto de datos, eliminar duplicados o filtrar imágenes no
apropiadas, reduciendo así el coste de almacenamiento y refinando la calidad del conjunto
de datos.

## Modelos secuenciales

Muchos problemas en inteligencia artificial se caracterizan por involucrar datos
**secuenciales**, es decir, información organizada en un orden temporal o lógico.
Ejemplos destacados incluyen el reconocimiento de voz, la generación de música, el
análisis de sentimientos en texto, la interpretación de secuencias de ADN o la traducción
automática de idiomas. A diferencia de las imágenes, donde la información espacial es
clave, en las secuencias la dependencia entre elementos previos y posteriores resulta
esencial.

En el contexto de los modelos secuenciales, resulta importante definir el concepto de
**modelo causal**: una capa es causal si la salida correspondiente al $i$-ésimo elemento
de la secuencia depende únicamente de los elementos anteriores o del propio elemento. Por
ejemplo, una capa convolucional con _kernel_ de tamaño 1 es causal, ya que cada elemento
se procesa considerando solo a sí mismo. Sin embargo, una capa convolucional con _kernel_
de tamaño 3 no es causal, ya que considera un elemento a la izquierda y otro a la
derecha. Cualquier convolución puede convertirse en su variante causal mediante el
enmascaramiento parcial de los pesos correspondientes a conexiones no causales. Este es
uno de los métodos utilizados en modelos como los _Transformers_ en la parte del
decodificador, que funciona como un modelo autoregresivo gracias al enmascarado.

### Representación de secuencias

En el procesamiento del lenguaje natural, las palabras deben transformarse en
representaciones que puedan ser interpretadas por un modelo. Este procedimiento se
denomina **tokenización** y consiste en asignar a cada palabra un índice único dentro de
un diccionario y, posteriormente, transformarla en un vector que codifica su información.
El proceso contempla también el uso de **_tokens_ especiales**, como un _token_ reservado
para palabras desconocidas y un _token_ de fin de secuencia empleado en tareas de
generación de texto.

### Redes neuronales recurrentes

Las **redes neuronales recurrentes (_Recurrent Neural Networks_, RNN)** constituyen una
extensión de las redes tradicionales diseñada para procesar datos secuenciales. Su
principal característica es la capacidad de **recordar información previa**, ya que
reutilizan la salida de un paso anterior como parte de la entrada en el siguiente. Este
mecanismo permite que los parámetros se compartan a lo largo de la secuencia, reduciendo
el número de variables que deben aprenderse.

No obstante, las RNN se enfrentan a problemas significativos de desvanecimiento y
explosión de gradientes. Para superar estas limitaciones, se desarrollaron variantes más
sofisticadas:

- **RNN bidireccionales:** Procesan la secuencia tanto hacia adelante como hacia atrás,
  integrando simultáneamente información del pasado y del futuro.
- **LSTM (_Long Short-Term Memory_):** Introducen celdas de memoria acompañadas de
  puertas de control que regulan qué información se conserva, cuál se descarta y cuál se
  utiliza en cada paso.
- **GRU (_Gated Recurrent Unit_):** Constituyen una variante simplificada de las LSTM,
  con una estructura más ligera y eficiente.

### Modelos de lenguaje y predicción de secuencias

Los **modelos de lenguaje** son sistemas diseñados para asignar probabilidades a
secuencias de palabras, permitiendo predecir la siguiente palabra en un texto dado el
contexto previo. En el procesamiento del lenguaje natural, un concepto central es el de
los **_word embeddings_**, vectores densos que representan palabras en un espacio
continuo donde las relaciones semánticas se reflejan en la geometría.

El aprendizaje de _embeddings_ puede realizarse mediante diferentes técnicas.
**Word2Vec** entrena modelos para predecir palabras a partir de su contexto en ventanas
de texto, utilizando estrategias como _negative sampling_. **GloVe** combina información
de coocurrencia global con factorización de matrices, integrando información local y
estadística global del corpus. Estas representaciones pueden preentrenarse en grandes
corpus y transferirse a tareas específicas, aunque es importante señalar que los
_embeddings_ también reflejan **sesgos presentes en los datos de entrenamiento**, los
cuales pueden identificarse y mitigarse mediante técnicas de neutralización o ajuste
post-entrenamiento.

### Mecanismo de atención

El mecanismo de atención constituye un componente fundamental en las arquitecturas
modernas de procesamiento de secuencias. Se implementa a través de tres vectores: **Query
(Q)**, que representa lo que se está buscando; **Key (K)**, que codifica la información
disponible que puede ser relevante; y **Value (V)**, que contiene el contenido asociado
para construir la representación final. El funcionamiento consiste en comparar la _Query_
con cada _Key_ para calcular pesos de relevancia relativa, que se aplican a los _Values_
correspondientes para generar representaciones contextuales.

### _Transformers_

Los _Transformers_, introducidos en el artículo _Attention is All You Need_,
revolucionaron el procesamiento de secuencias al eliminar la necesidad de recurrir a RNN,
permitiendo un procesamiento paralelo de los datos. Desde una perspectiva
neurocientífica, los _Transformers_ presentan similitudes funcionales con las **máquinas
de Tolman-Eichenbaum (TEM)**, modelos computacionales del hipocampo que obtienen
información de diferentes entornos, realizan una autocorrelación para evaluar las
relaciones entre ellos (análoga al mecanismo de atención) y determinan la acción o
posición a tomar en función de dichas relaciones. La arquitectura se organiza en dos
componentes principales:

- **_Encoder_**: Procesa la secuencia de entrada y genera representaciones internas
  enriquecidas. Se encarga de transformar la entrada en una representación vectorial
  interna, aplicando mecanismos de _self-attention_ y _cross-attention_ para identificar
  las partes más relevantes.
- **_Decoder_**: Utiliza estas representaciones para generar la secuencia de salida de
  manera autoregresiva. Emplea la representación generada por el _encoder_, junto con
  información adicional, para generar nuevo contenido.

Cada bloque del _Transformer_ combina mecanismos de **autoatención (_self-attention_)** y
redes totalmente conectadas. Dado que los _Transformers_ no procesan los elementos de
manera secuencial, se incorporan **_positional encodings_** para preservar información
sobre el orden de los elementos. El **_multi-head attention_** constituye una extensión
clave que permite al modelo observar relaciones desde múltiples perspectivas
simultáneamente.

Existen múltiples variantes de la arquitectura _Transformer_:

- **BERT (_Bidirectional Encoder Representations from Transformers_)**: Utiliza
  únicamente el _encoder_. Su entrenamiento se basa en la enmascaración de palabras en un
  texto y la predicción de las mismas. Es especialmente eficaz en tareas de clasificación
  y análisis de sentimientos.
- **GPT (_Generative Pre-trained Transformer_)**: Utiliza solamente el _decoder_ y está
  orientado a la generación de texto. Se entrena proporcionando secuencias incompletas
  que el modelo debe completar. Es un **modelo autoregresivo**, donde la salida generada
  en el tiempo $t$ se utiliza como entrada en el tiempo $t+1$, lo que permite mantener
  coherencia en la generación.
- **_Autoencoders_ enmascarados**: Se aplican principalmente en modelos visuales. Dividen
  una imagen en múltiples parches, ocultan algunos de ellos, y el objetivo es reconstruir
  los parches faltantes, de manera análoga al entrenamiento de BERT pero aplicado al
  dominio visual.

Estas arquitecturas basadas en _Transformers_ han destacado especialmente en el ámbito de
la **inteligencia artificial generativa**, donde el modelo es capaz de generar nuevos
datos a partir de una distribución de probabilidades aprendida. Las alucinaciones que
pueden presentar estos modelos se deben a factores como la insuficiencia de datos, la
presencia de ruido o datos sucios, la falta de contexto o la ausencia de restricciones y
pautas adecuadas.

## Redes neuronales de grafos

Los grafos constituyen una estructura flexible y poderosa para representar información
compleja. Están formados por **nodos** (o vértices) y **aristas** (o conexiones) que
describen las relaciones existentes entre los elementos. Las **Redes Neuronales de Grafos
(_Graph Neural Networks_, GNN)** están diseñadas para procesar directamente estas
estructuras, extrayendo representaciones cada vez más ricas de los nodos y del grafo en
su conjunto.

Cada nodo se representa mediante un vector de características que se actualiza en
sucesivas iteraciones combinando la información propia del nodo con la de sus vecinos.
Las operaciones de agregación (suma, promedio o máximo) deben ser conmutativas,
garantizando que el resultado no dependa del orden en que se procesen los vecinos. La
topología del grafo puede representarse mediante **matrices de adyacencia** o **listas de
adyacencia**.

Las GNN permiten abordar problemas a nivel de grafo (clasificación de moléculas), a nivel
de nodo (segmentación de imágenes, detección de usuarios influyentes) y a nivel de arista
(sistemas de recomendación, predicción de enlaces). Entre las arquitecturas más
destacadas se encuentran las **Graph Convolutional Networks (GCN)** y las **Graph
Attention Networks (GAT)**, que incorporan mecanismos de atención para ponderar la
relevancia relativa de cada vecino. En grafos muy grandes, se introducen mecanismos como
el **nodo maestro (_masternode_)** para centralizar la propagación de información global.

## Otros paradigmas de aprendizaje

### Aprendizaje multitarea

El **aprendizaje multitarea (_Multi-Task Learning_)** persigue que un mismo modelo sea
capaz de resolver de manera simultánea múltiples problemas relacionados. La idea central
es que al compartir representaciones internas entre diferentes tareas, la red aprende
descriptores más generales y robustos que benefician a todas ellas. Un ejemplo
paradigmático se encuentra en la conducción autónoma, donde un único modelo puede
segmentar imágenes, clasificar señales de tráfico y predecir trayectorias
simultáneamente.

El objetivo general se formula como:

$$
\min_{\theta} \sum_{i=1}^{T} w_i \cdot L_i(\theta, D_i),
$$

donde $D_i$ es el conjunto de datos de la tarea $i$ y $w_i$ permite ajustar la relevancia
de cada tarea. Las principales estrategias incluyen el uso de _embeddings_ condicionales,
sistemas _multi-head_ (un modelo único con múltiples salidas) y condicionales
multiplicativos.

### _Meta-Learning_

El **_Meta-Learning_** se enfoca en dotar a los modelos de la habilidad de identificar y
aprovechar patrones subyacentes en los datos, lo que les permite adaptarse rápidamente a
nuevos problemas con un mínimo de información. Este enfoque es particularmente útil en
escenarios con datos limitados o costosos de obtener.

### _Few-Shot Learning_

El **_Few-Shot Learning_ (FSL)** se centra en entrenar modelos que logren un alto
rendimiento con un número muy limitado de ejemplos etiquetados por clase. Se organiza en
torno a un **_Support Set_** (conjunto de entrenamiento con pocas muestras etiquetadas) y
un **_Query Set_** (conjunto de prueba). El aprendizaje se describe según dos parámetros:
**_K-shot Learning_** (número de ejemplos por clase) y **_N-way Classification_** (número
de clases diferentes).

Existen dos tipos de modelos en este régimen: los **modelos no parametrizados** (como
_k-Nearest Neighbors_), simples y eficaces cuando se dispone de _embeddings_ de alta
calidad, y los **modelos parametrizados** (redes neuronales profundas), que generan
_embeddings_ que capturan las características relevantes en un espacio de menor
dimensionalidad.

## Aprendizaje autosupervisado

El principal problema del aprendizaje supervisado radica en la cantidad de datos
etiquetados que se requieren, el tiempo necesario para etiquetar de manera manual y los
sesgos que pueden introducir los anotadores. La gran mayoría de los datos disponibles son
no etiquetados, por lo que obtener abstracciones que permitan generalizaciones a partir
de datos sin etiquetar resulta fundamental. Este es el proceso natural de aprendizaje
humano: adquirir ideas y luego extrapolar el conocimiento.

El aprendizaje autosupervisado está estrechamente relacionado con el aprendizaje
multimodal. El aprendizaje requiere conocimiento previo y redundancia en las señales.
Cuando se aprenden asociaciones entre $N$ eventos, es necesario almacenar $N^2$ posibles
probabilidades; si los eventos son independientes, las probabilidades pueden calcularse
por separado y la probabilidad total es el producto de las probabilidades individuales.

Entre las técnicas de aprendizaje autosupervisado destacan: _inpainting_ (reconstrucción
de regiones ocultas), reordenación de _puzzles_ (recomponer parches desordenados de una
imagen), colorización de imágenes en escala de grises, predicción de rotaciones,
aprendizaje contrastivo, _pseudo-labelling_ (entrenar un modelo supervisado con datos
etiquetados, predecir datos no etiquetados y reentrenar con las pseudoetiquetas
generadas) y aprendizaje de puntos clave de objetos.

## Flujo de trabajo para el desarrollo de modelos

El flujo de trabajo para el desarrollo de modelos de aprendizaje profundo se estructura
en tres fases principales.

La primera fase consiste en **definir la tarea**: comprender el dominio del problema y la
lógica subyacente, recopilar un conjunto de datos representativo, comprender qué
representan los datos y elegir cómo medir el éxito. Es fundamental enmarcar correctamente
el problema, identificando el tipo de tarea (clasificación binaria, multiclase,
regresión, segmentación, etc.), las soluciones existentes y las restricciones del entorno
(cifrado, latencia, dispositivo de destino). Un buen conjunto de datos es un activo que
merece cuidado e inversión; si se dispone de tiempo adicional, dedicarlo a recopilar más
datos suele ser más efectivo que buscar mejoras incrementales en el modelado. La
infraestructura de anotación de datos determina la calidad de las etiquetas y, por tanto,
la calidad del modelo.

La segunda fase es **desarrollar un modelo**: preparar los datos para que puedan ser
procesados (normalización, limpieza, manejo de valores faltantes), seleccionar un
protocolo de evaluación, establecer un punto de referencia simple a superar, entrenar un
primer modelo con capacidad de generalización y, finalmente, regularizar y ajustar hasta
lograr el mejor rendimiento posible. La **ingeniería de características** (_feature
engineering_) consiste en aplicar transformaciones codificadas a los datos antes de que
ingresen al modelo, haciendo el problema más fácil de resolver. Aunque el aprendizaje
profundo moderno reduce la necesidad de esta ingeniería, las buenas características
siguen permitiendo resolver problemas de manera más elegante y con menos datos.

La tercera fase es **desplegar el modelo**: presentar los resultados a las partes
interesadas con expectativas realistas (evitando declaraciones abstractas como "98% de
precisión" y prefiriendo hablar de tasas de falsos negativos y falsos positivos
vinculadas a objetivos de negocio), optimizar el modelo para inferencia mediante técnicas
como la **poda de pesos** (_weight pruning_) y la **cuantización de pesos** (_weight
quantization_), y supervisar el rendimiento del modelo en producción para detectar
degradaciones y recopilar datos para futuras iteraciones.
