---
sidebar_position: 9
authors:
Daniel Bazo Correa
description: Crea y almacena tus artefactos en repositorios.
title: Creacion de APIs
---

## API

Arquitectura monolítica es cuando creamos software combinado todo en un mismo grupo
incluso cuando su funcionalidad es variada. El problema es la escalabilidad, la
flexibilidad y el mantenimiento. Una solución es utilizar micro servicios que consiste en
crear un código específico para cada cosa está modularidad, pues permite resolver los
fallos y los problemas anteriores aquí por ejemplo tendríamos una aplicación que podría
tener por ejemplo un modelo para la inferencia y luego un modelo que se crearía durante
el proceso de entrenamiento, pues la idea es separar la lógica de ambos. Créame un código
específico que puede ser puesto en producción, de manera independiente.

También utilizar arquitecturas basadas en micro servicios, pues permite utilizar
tecnologías diferentes para cada tipo de micro servicios, por ejemplo para la creación de
un modelo de Machine Lerning. Podríamos utilizar Python para inferencia y crear una API.
Podríamos utilizar Go o para Pipeline de datos. Podríamos utilizar escala con los micros
de servicios, pues al final podemos escalar componentes de manera independiente, reduce
el impacto de fallo, ya que un código no afecta otro para la comunicación entre
servicios, pues se usan las apps que definen reglas y protocolos para dicha comunicación,
sin importar el lenguaje de programación utilizado para ello utilizan protocolos de
comunicación como puede ser GRPC, Rest o HTTP.

Las Apis pueden ser de dos maneras de manera síncrona o asíncrona, y sin embargo, existe
una serie de limitaciones las Apis síncronas, pues es cuando los usuarios tienen que
esperar peticiones de los usuarios de adelante entonces si yo tengo hasta acá usuarios,
el usuario que tiene que esperar en el segundo es de latencia donde K sería el usuario
carísimo. Esa latencia es el tiempo de respuesta desde que el usuario mando una petición
hasta que he resuelto. Al final esto supone un problema de escalabilidad, y para ello
están las Apis asíncronas que permiten ejecutar ciertas acciones de la aplicación de
manera concurrente. En vez de secuencial una API puede tener dos procesos en general
tareas de transferencia de datos, lo que se conoce como el I/O que son operaciones de
entrada y salida o operaciones de escritura y tenemos tareas de procesado que están
relacionadas con la CPU al final las limitaciones en la entrada y salida, pues depende de
lo rápido que seas para transferir datos acceder a espacio de memoria de la capacidad de
Internet, y luego tenemos la limitaciones en la CPU que son a nivel de hardware. Por
tanto, la programación asíncrona no depende de la velocidad de la CPU y se utiliza
sobretodo para optimizar procesos. Una API tiene normalmente la funcionalidad cruz que es
crear leer actualizar y borrar donde crear es un Post leer es un Goethe actualizar es un
puto y borrar es un delito como hemos dicho existen diferentes tipos de protocolos de
comunicaciones, como puede ser HTTP web, so Kets o similares y luego tenemos el protocolo
de datos utilizados que podría ser XML Jason.

Existen diferentes paradigmas de Apis que puede ser API resto Graco el Ojer PC. Luego
tenemos limitadores de radio en lápiz o tenemos cor setting con para el control de
dominios.

---

sidebar_position: 10 authors:

- name: Daniel Bazo Correa description: Exportación de modelos para inferencia con ONNX.
  title: ONNX

---

## Bibliografía

- [Everything You Want to Know About ONNX](https://www.youtube.com/watch?v=cK5AyawZSUI&list=WL&index=38)
- [ONNX](https://onnx.ai/)
- [ONNX Runtime](https://onnxruntime.ai/)

## Motivación

<p align="center">
  <img src="/assets/img/docs/logos/onnx-logo.png" width="500"/>
  <br />
  <em>Logo de ONNX.</em>
</p>

El ecosistema del aprendizaje profundo se caracteriza por una gran fragmentación en los
frameworks utilizados para el desarrollo de modelos, como TensorFlow, Keras, PyTorch,
Caffe y MXNet, además de versiones privadas de distintas empresas. La migración entre
estos frameworks no siempre es sencilla, especialmente considerando la evolución de las
tendencias tecnológicas, lo que puede llevar a la obsolescencia o la falta de soporte de
determinadas herramientas.

Además, el despliegue de modelos de aprendizaje profundo está condicionado por la
compatibilidad con el hardware disponible. Por ejemplo, las tarjetas gráficas de NVIDIA
utilizan CUDA, mientras que Intel ofrece oneAPI. Algunos proveedores de nube, como GCP,
permiten el uso de hardware especializado, como las TPUs.

Existen diversas herramientas para la optimización de modelos en fase de inferencia.
Entre ellas, [TensorRT](https://developer.nvidia.com/tensorrt) optimiza modelos para su
ejecución en GPU, [OpenVINO](https://docs.openvino.ai/2024/index.html) mejora la
inferencia en procesadores, GPUs y NPUs de Intel, y
[JetPack SDK](https://developer.nvidia.com/embedded/jetpack) está diseñado para
dispositivos edge de NVIDIA, como las Jetson. Para entornos embebidos, TensorFlow
proporciona [LiteRT](https://ai.google.dev/edge/litert), lo que antes era Tensorflow
Lite. Sin embargo, la interoperabilidad sigue siendo un desafío, ya que comprender y
utilizar cada una de estas herramientas puede ser costoso y demandar una considerable
inversión de tiempo.

**ONNX (Open Neural Network Exchange)** busca resolver estos problemas facilitando la
interoperabilidad entre modelos de aprendizaje automático, independientemente del
framework en el que hayan sido desarrollados. ONNX proporciona una representación
intermedia de los modelos, reduciendo la cantidad de dependencias necesarias para su
ejecución. Al exportar un modelo a ONNX, no es necesario importar bibliotecas específicas
como PyTorch o TensorFlow, lo que simplifica el despliegue y optimización en distintos
entornos de hardware.

ONNX cuenta con el respaldo de la Fundación Linux y un sólido ecosistema de soporte por
parte de grandes proveedores de la nube como AWS, Azure y GCP. No solo es compatible con
frameworks de aprendizaje profundo, sino también con herramientas de aprendizaje
automático clásico, a través de ONNX-ML, que facilita la integración con bibliotecas como
Scikit-Learn.

Además, ONNX se integra con **Azure**, permitiendo la creación de pipelines para la
gestión de datasets, entrenamiento de modelos y descarga de modelos entrenados.
Posteriormente, estos modelos pueden ser desplegados en dispositivos edge o en la nube
mediante técnicas como la contenerización con Docker.

## Funcionamiento

ONNX representa los modelos mediante un grafo de computación, en el cual cada nodo
corresponde a una operación matemática y cada arista define la relación entre dichas
operaciones. Este formato es compatible con diversos tipos de datos estándar, incluyendo
tensores y tipos no tensoriales, como enteros, flotantes y booleanos, entre otros.

El archivo de modelo en ONNX contiene información esencial, como la versión del modelo,
metadatos y un grafo de flujo de datos de computación acíclico. Dentro del grafo, se
especifican las entradas y salidas del modelo, la lista de nodos de computación y el
nombre del propio grafo. Además, se incluyen definiciones de operadores, parámetros y
tipos de datos utilizados en el modelo.

El estándar ONNX define un conjunto de operadores que permiten mapear las funcionalidades
de los frameworks de alto nivel con su propia representación. Existe una tabla de
operadores compatibles con cada librería, como la que relaciona TensorFlow y Keras con
ONNX, disponible en
[GitHub](https://github.com/onnx/tensorflow-onnx/blob/main/support_status.md). Además,
ONNX permite la creación de operadores personalizados para extender su funcionalidad.

Para facilitar la visualización de los grafos de computación generados, se dispone de la
herramienta [**Netron**](https://netron.app/), que forma parte del ecosistema de ONNX.

### Versionado en ONNX

El versionado en ONNX se estructura en tres niveles:

- **IR Version (Intermediate Representation Version):** Define el formato del archivo y
  la estructura del modelo dentro de ONNX.
- **Opset Version (Operator Set Version):** Indica el conjunto de operadores compatibles
  con el modelo, asegurando compatibilidad con diferentes versiones del framework.
- **Operator Version:** Especifica la versión de cada operador individual dentro del
  conjunto de operadores, lo que permite gestionar cambios en su funcionalidad sin
  afectar la compatibilidad general del modelo.

## ONNX Runtime

ONNX Runtime es un motor de inferencia optimizado para la ejecución eficiente de modelos
en formato ONNX en diversos entornos de hardware, incluyendo la nube y dispositivos edge.
Proporciona una capa de abstracción sobre el hardware utilizado y permite la integración
con bibliotecas de aceleración específicas mediante los **Execution Providers (EP)**.
Soporta completamente la especificación de ONNX, garantizando la interoperabilidad entre
diferentes frameworks y herramientas, y asegura la compatibilidad retroactiva con modelos
creados en versiones anteriores.

Este motor está diseñado para ofrecer alto rendimiento mediante estrategias de
optimización y aceleración, así como una ejecución híbrida que prioriza el uso de
hardware acelerado siempre que esté disponible. En caso de incompatibilidad, el modelo se
ejecuta en la CPU de manera eficiente. Además, ONNX Runtime es una solución portátil y
compatible con múltiples sistemas operativos y plataformas de hardware, permitiendo la
integración con aceleradores personalizados y entornos de ejecución optimizados.

Otro aspecto destacado es su extensibilidad, ya que admite la incorporación de módulos
personalizados para mejorar la funcionalidad y el rendimiento. Gracias a estas
características, ONNX Runtime se posiciona como una solución flexible y eficiente para la
inferencia de modelos en una amplia variedad de entornos y dispositivos.

### Funcionamiento

Para optimizar la ejecución de los modelos, ONNX Runtime realiza una partición del grafo
de computación, dividiéndolo en subgrafos que pueden ejecutarse en diferentes **Execution
Providers (EP)**, lo que permite aprovechar distintas plataformas de hardware y ejecutar
operaciones en paralelo dentro del grafo. Esta optimización se lleva a cabo en varios
niveles:

1. **Partición del grafo:** Se identifican y dividen las secciones del modelo que pueden
   ejecutarse en distintos EP.
2. **Aplicación de transformaciones generales:** Se realizan modificaciones en el grafo
   como inserción de conversiones de tipo (_cast insertion_) o copias de memoria (_mem
   copy insertion_).
3. **Transformaciones generales independientes del EP:** Se aplican optimizaciones que no
   dependen de un hardware específico.
4. **Transformaciones específicas del EP:** Se ajusta el modelo para aprovechar al máximo
   las capacidades de hardware especializadas, como TPU, GPU o FPGA.

Los **Execution Providers (EP)** permiten la integración de bibliotecas específicas de
aceleración de hardware, facilitando la optimización de la inferencia en diversas
plataformas. Además, la interfaz `GetCapability()` asigna nodos o subgrafos del modelo
ONNX a la biblioteca del **Execution Provider** compatible, permitiendo una ejecución
optimizada en distintos tipos de hardware, como CPU, GPU, FPGA y NPU. Más información
sobre los EP está disponible en la
[documentación oficial](https://onnxruntime.ai/docs/execution-providers/).

### Integración y configuración

Los desarrolladores pueden crear e integrar sus propios EPs para ejecutar modelos en
soluciones de aceleración personalizadas. Además, ONNX Runtime permite construir paquetes
con cualquier combinación de EPs, siempre que las bibliotecas necesarias estén
disponibles. Métodos como `get_providers`, `get_provider_options` y `set_providers`
permiten configurar y cambiar los EPs de manera eficiente.

A continuación, se muestra un fragmento de código que inicializa una sesión de inferencia
con un modelo ONNX, estableciendo un orden de prioridad en los EPs (preferencia por CUDA
sobre CPU):

```py linenums="1"
import onnxruntime as ort

session = ort.InferenceSession("modelo.onnx", providers=["CUDAExecutionProvider", "CPUExecutionProvider"])
inputs = {session.get_inputs()[0].name: datos_entrada}
resultados = session.run(None, inputs)
```

También es posible modificar la prioridad de los EPs para utilizar solo el proveedor de
CPU:

```py linenums="1"
session.set_providers(["CPUExecutionProvider"])
```

## Modelos preentrenados

ONNX proporciona un repositorio de modelos preentrenados denominado
[**ONNX Model Zoo**](https://onnx.ai/models/), que incluye modelos de visión
computacional, procesamiento de lenguaje natural (NLP) y audio, entre otros.

## Olive (ONNX LIVE)

Para mejorar aún más la optimización de modelos ONNX, se dispone de
[**Olive (ONNX LIVE)**](https://github.com/microsoft/OLive), una herramienta diseñada
para optimizar modelos ONNX para su ejecución eficiente en la nube o en dispositivos
_edge_. Dado un modelo y un hardware objetivo, Olive selecciona y aplica las técnicas de
optimización más adecuadas para generar un modelo optimizado, teniendo en cuenta
restricciones como precisión y latencia.

Entre sus principales beneficios se encuentran la automatización del proceso de
optimización, eliminando la necesidad de pruebas manuales, y una amplia variedad de
técnicas avanzadas de compresión, ajuste fino (_fine-tuning_) y compilación. Dispone de
una interfaz de línea de comandos (CLI), flujos de trabajo estructurados para gestionar
la transformación y optimización de modelos, y soporte para la compilación de adaptadores
LoRA. Además, ofrece integración con plataformas como **Hugging Face** y **Azure AI**. Un
mecanismo de caché integrado permite mejorar la productividad al almacenar y reutilizar
optimizaciones previas, reduciendo el tiempo de cómputo en experimentaciones repetitivas.

---

sidebar_position: 7 authors:

- name: Daniel Bazo Correa description: Crea y almacena tus artefactos en repositorios.
  title: Gestión y publicación de repositorios

---

## Publicación de un paquete de Python en PyPI

Para publicar un paquete de Python en PyPI, es necesario que el proyecto tenga una
estructura organizada. Es recomendable alojar el paquete en un repositorio para facilitar
el control de versiones, la implementación de pipelines CI/CD y otras prácticas de
desarrollo.

El primer paso es crear un archivo `setup.py` que contenga la configuración del paquete.
A continuación, se muestra un ejemplo de configuración básica:

```py linenums="1"
import os
from setuptools import setup, find_packages
import codecs

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.1.1"
DESCRIPTION = "Essential utilities for data scientists"
LONG_DESCRIPTION = """
    A package of essential tools and utilities for streamlining data science tasks like manipulation,
    augmentation, visualization, among others, enhancing daily *workflows*.
"""

setup(
    name="datasu",
    version=VERSION,
    author="danibcorr (Daniel Bazo)",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danibcorr/data-scientist-utilities",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "numba",
        "ipywidgets",
        "matplotlib",
        "seaborn",
        "pandas",
        "scikit-learn",
    ],
    keywords=[
        "python",
        "data science",
        "machine learning",
        "deep learning",
        "artificial intelligence",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
```

En el archivo `setup.py` se especifican la versión del paquete, una descripción, los
requerimientos y otra información relevante. Es posible consultar parámetros adicionales
en la [guía oficial de setuptools](https://setuptools.pypa.io/en/latest/userguide/).

Una vez configurado el archivo `setup.py`, se pueden generar los archivos de distribución
utilizando el comando:

```bash linenums="1"
python setup.py sdist bdist_wheel
```

Antes de publicar el paquete en PyPI, se recomienda realizar pruebas locales para
asegurarse de que todo funcione correctamente. Para instalar el paquete localmente,
utilice:

```bash linenums="1"
pip install /dist/nombre_fichero.whl
```

Esto permite probar el paquete en un entorno local y ejecutar tests para verificar su
funcionamiento.

Para publicar en PyPI, se requiere una cuenta en el servicio y la configuración de
autenticación multifactor (2FA). Luego, es necesario obtener un token de API desde la
sección correspondiente en la cuenta de PyPI. Este token puede almacenarse en un archivo
`.pypirc` o guardarse de manera segura.

Para publicar el proyecto, se utiliza el siguiente comando:

```bash linenums="1"
twine upload dist/*
```

Si el nombre del proyecto ya está en uso, se recibirá un error y será necesario
seleccionar un nombre diferente para el paquete.
