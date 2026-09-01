---
authors: Daniel Bazo Correa
description: Modelos secuenciales para datos temporales y secuencias.
title: Modelos secuenciales
---

!!! warning

    El contenido de esta página no ha sido revisado ni corregido, por lo que puede
    estar incompleto, contener errores o presentar información desactualizada. Además,
    es posible que esté desordenado, carezca de una estructura clara o incluya notas
    copiadas directamente.

Muchos problemas en inteligencia artificial se caracterizan por involucrar datos
**secuenciales**, es decir, información organizada en un orden temporal o lógico.
Ejemplos destacados incluyen el reconocimiento de voz, la generación de música, el
análisis de sentimientos en texto, la interpretación de secuencias de ADN o la
traducción automática de idiomas. A diferencia de las imágenes, donde la información
espacial es clave, en las secuencias la dependencia entre elementos previos y
posteriores resulta esencial.

En el contexto de los modelos secuenciales, resulta importante definir el concepto de
**modelo causal**: una capa es causal si la salida correspondiente al $i$-ésimo elemento
de la secuencia depende únicamente de los elementos anteriores o del propio elemento.
Por ejemplo, una capa convolucional con _kernel_ de tamaño 1 es causal, ya que cada
elemento se procesa considerando solo a sí mismo. Sin embargo, una capa convolucional
con _kernel_ de tamaño 3 no es causal, ya que considera un elemento a la izquierda y
otro a la derecha. Cualquier convolución puede convertirse en su variante causal
mediante el enmascaramiento parcial de los pesos correspondientes a conexiones no
causales. Este es uno de los métodos utilizados en modelos como los _Transformers_ en la
parte del decodificador, que funciona como un modelo autoregresivo gracias al
enmascarado.

## Representación de secuencias

En el procesamiento del lenguaje natural, las palabras deben transformarse en
representaciones que puedan ser interpretadas por un modelo. Este procedimiento se
denomina **tokenización** y consiste en asignar a cada palabra un índice único dentro de
un diccionario y, posteriormente, transformarla en un vector que codifica su
información. El proceso contempla también el uso de **_tokens_ especiales**, como un
_token_ reservado para palabras desconocidas y un _token_ de fin de secuencia empleado
en tareas de generación de texto.

## Redes neuronales recurrentes

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

## Modelos de lenguaje y predicción de secuencias

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

## Mecanismo de atención

El mecanismo de atención constituye un componente fundamental en las arquitecturas
modernas de procesamiento de secuencias. Se implementa a través de tres vectores:
**Query (Q)**, que representa lo que se está buscando; **Key (K)**, que codifica la
información disponible que puede ser relevante; y **Value (V)**, que contiene el
contenido asociado para construir la representación final. El funcionamiento consiste en
comparar la _Query_ con cada _Key_ para calcular pesos de relevancia relativa, que se
aplican a los _Values_ correspondientes para generar representaciones contextuales.

## _Transformers_

Los _Transformers_, introducidos en el artículo _Attention is All You Need_,
revolucionaron el procesamiento de secuencias al eliminar la necesidad de recurrir a
RNN, permitiendo un procesamiento paralelo de los datos. Desde una perspectiva
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

Cada bloque del _Transformer_ combina mecanismos de **autoatención (_self-attention_)**
y redes totalmente conectadas. Dado que los _Transformers_ no procesan los elementos de
manera secuencial, se incorporan **_positional encodings_** para preservar información
sobre el orden de los elementos. El **_multi-head attention_** constituye una extensión
clave que permite al modelo observar relaciones desde múltiples perspectivas
simultáneamente.

Existen múltiples variantes de la arquitectura _Transformer_:

- **BERT (_Bidirectional Encoder Representations from Transformers_)**: Utiliza
  únicamente el _encoder_. Su entrenamiento se basa en la enmascaración de palabras en
  un texto y la predicción de las mismas. Es especialmente eficaz en tareas de
  clasificación y análisis de sentimientos.
- **GPT (_Generative Pre-trained Transformer_)**: Utiliza solamente el _decoder_ y está
  orientado a la generación de texto. Se entrena proporcionando secuencias incompletas
  que el modelo debe completar. Es un **modelo autoregresivo**, donde la salida generada
  en el tiempo $t$ se utiliza como entrada en el tiempo $t+1$, lo que permite mantener
  coherencia en la generación.
- **_Autoencoders_ enmascarados**: Se aplican principalmente en modelos visuales.
  Dividen una imagen en múltiples parches, ocultan algunos de ellos, y el objetivo es
  reconstruir los parches faltantes, de manera análoga al entrenamiento de BERT pero
  aplicado al dominio visual.

Estas arquitecturas basadas en _Transformers_ han destacado especialmente en el ámbito
de la **inteligencia artificial generativa**, donde el modelo es capaz de generar nuevos
datos a partir de una distribución de probabilidades aprendida. Las alucinaciones que
pueden presentar estos modelos se deben a factores como la insuficiencia de datos, la
presencia de ruido o datos sucios, la falta de contexto o la ausencia de restricciones y
pautas adecuadas.
