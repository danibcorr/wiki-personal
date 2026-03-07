---
authors:
Daniel Bazo Correa
description: Conceptos básicos de MLOps.
title: MLOps
---

## Bibliografía

- [ML in Production: From Data Scientist to ML Engineer](https://www.udemy.com/course/ml-in-production/?couponCode=SKILLS4SALEA)
- [PEP 8 — the Style Guide for Python Code](https://pep8.org/)

## Introducción

<p align="center">
  <img src="/assets/img/docs/logos/mlops-logo.png" width="500"/>
  <br />
  <em>Ciclo de vide de un proyecto MLOps</em>
</p>

MLOps, o _Machine Learning Operations_, es el conjunto de prácticas, herramientas y
procesos que permiten desarrollar, implementar y mantener modelos de _machine learning_
en entornos de producción. Este enfoque combina conocimientos de ingeniería de software,
computación en la nube y gestión de redes, siendo fundamental para garantizar que los
modelos sean eficaces, escalables y sostenibles.

<p align="center">
  <img src="https://ml-ops.org/img/mlops-phasen.jpg" width="500"/>
  <br />
  <em>Ejemplo de los pasos seguidos en un proyecto de MLOps</em>
</p>

Un sistema de MLOps se compone de diversos elementos. En su núcleo está el modelo o
algoritmo, que representa la solución entrenada en datos. Este modelo opera sobre una
infraestructura que puede variar desde servicios en la nube hasta servidores locales o en
los propios dispositivos (_on edge_), dependiendo de las necesidades. Una API o interfaz
es esencial para procesar solicitudes y devolver predicciones, mientras que la gestión de
predicciones y la monitorización aseguran la calidad, fiabilidad y rendimiento en tiempo
real.

## Los desafíos de MLOps

Uno de los principales desafíos en la adopción de metodologías de MLOps es la correcta
definición tanto del problema como de la posible solución. Además, es fundamental
implementar tecnologías que puedan comunicarse eficazmente entre sí, permitiendo la
creación de sistemas y procesos automatizados que agilicen la recopilación, el
tratamiento, el análisis y el uso de los datos. Este enfoque requiere una infraestructura
sólida, cuyo diseño y construcción demandan tiempo y conocimientos especializados.

Una vez establecida la infraestructura necesaria para integrar los diferentes
componentes, surgen nuevos retos en la etapa de puesta en producción.

Entre ellos destaca el **_data drift_**, que ocurre cuando los datos de producción
difieren de los de entrenamiento, afectando la precisión del modelo. Otro desafío común
es el manejo de **datos fuera de distribución** (_Out of Distribution_, OOD), aquellos
que no encajan con los patrones aprendidos durante el entrenamiento. Además, la
actualización y el mantenimiento de los modelos para adaptarlos a nuevos datos o
requerimientos constituyen un esfuerzo continuo.

!!!note "Nota"

El mantenimiento de modelos basados en inteligencia artificial suele implicar su
reentrenamiento con nuevos datos para evitar la degradación de las métricas establecidas
y asegurar un rendimiento óptimo.

### Ciclo de vida de MLOps

El ciclo de vida de MLOps es un proceso iterativo que permite realizar ajustes en
cualquier etapa para optimizar el sistema. Un diseño efectivo de un producto basado en
_machine learning_ debe justificar su necesidad, detallar sus objetivos e impacto, y
abordar las siguientes áreas clave:

1. **Definición del proyecto**: En esta etapa se identifican las necesidades del usuario
   y los objetivos del producto, además de evaluar la viabilidad técnica y financiera.
   Los pasos esenciales incluyen:
   - **Identificación de problemas y métricas clave**: Métricas como precisión, latencia
     y ROI (Retorno de Inversión) son fundamentales para medir el éxito del proyecto.
   - **Propuesta de valor**: Se define cómo el producto resolverá problemas específicos y
     generará beneficios para los usuarios.
   - **Factibilidad**: Se evalúan los recursos necesarios (humanos, tecnológicos y
     financieros) para implementar la solución.
   - **Planificación**: Se establecen cronogramas y se asignan recursos para el
     desarrollo del producto.

2. **Datos**: El manejo de datos es la base de cualquier sistema de ML. Incluye los
   siguientes procesos:
   - **Recopilación y organización**: Los datos pueden provenir de bases de datos,
     archivos o servicios web. En proyectos complejos, el almacenamiento en la nube es
     una opción ideal.
   - **Etiquetado y preprocesamiento**: Incluye normalización, codificación y extracción
     de características para garantizar que los datos sean adecuados para el
     entrenamiento.
   - **Análisis exploratorio de datos (EDA)**: Se analiza la distribución de los datos,
     se identifican anomalías y se descubren correlaciones relevantes.
   - **Manejo de desequilibrios**: Técnicas como el sobremuestreo o submuestreo
     equilibran clases desbalanceadas, asegurando que los datos sean representativos.
   - **División en conjuntos**: Los datos se dividen en conjuntos de entrenamiento,
     validación y prueba, manteniendo distribuciones similares para evitar problemas como
     el sobreajuste.

3. **Modelado**: El modelado implica seleccionar, entrenar y validar modelos de ML. Las
   principales actividades incluyen:
   - **Desarrollo iterativo**: Se comienza con soluciones base y se incrementa la
     complejidad según sea necesario.
   - **Optimización**: Herramientas como Ray permiten el entrenamiento distribuido en
     sistemas escalables, mientras que técnicas como _pruning_, _quantization_ y
     _distillation_ optimizan modelos grandes.
   - **Ajuste de hiperparámetros y seguimiento de experimentos**: Se experimenta con
     configuraciones para obtener un rendimiento óptimo, guiándose por métricas
     específicas como F1 en clasificaciones desbalanceadas.
   - **Despliegue del modelo**: Los modelos se implementan como servicios robustos, ya
     sea para predicciones en tiempo real o por lotes, asegurando personalización,
     pruebas exhaustivas y escalabilidad.

4. **Despliegue**: El modelo se implementa inicialmente en entornos de preproducción,
   donde se evalúa con un número limitado de usuarios o bajo condiciones controladas.
   Posteriormente, se despliega en producción, aumentando gradualmente el tráfico de
   usuarios mientras se monitorizan métricas clave y se configuran alertas para detectar
   anomalías.

5. **Mantenimiento**: Incluye el entrenamiento continuo con datos recientes y la
   monitorización constante para identificar y resolver problemas de rendimiento,
   asegurando que el modelo siga cumpliendo los objetivos establecidos.

Un diseño robusto debe abarcar todos los elementos necesarios, desde la ingesta de datos
hasta la entrega de predicciones, tomando en cuenta:

- **Carga de trabajo ML**: Definición de fuentes de datos, etiquetado y selección de
  características.
- **Inferencia**: Elección entre inferencia en lotes o en tiempo real, dependiendo de los
  requisitos del sistema.
- **Impacto real**: Garantizar que el sistema genere valor tangible y que su rendimiento
  mejore continuamente.

Este enfoque integral e iterativo asegura que los sistemas de ML sean sostenibles,
escalables y efectivos en el mundo real.

### Estrategias de despliegue

Existen diversas técnicas para implementar modelos en producción de manera segura y con
el mínimo impacto:

- **Gradual ramp-up**: Consiste en incrementar progresivamente el tráfico hacia el nuevo
  modelo, lo que permite monitorear su desempeño y hacer ajustes según sea necesario.
- **Rollback**: Esta estrategia permite revertir rápidamente al modelo anterior en caso
  de que el nuevo no cumpla con las expectativas o falle.
- **Canary deployment**: En esta técnica, se asigna inicialmente un pequeño porcentaje de
  tráfico al nuevo modelo, incrementándolo gradualmente si demuestra ser eficaz y
  estable.
- **Blue-green deployment**: Utiliza dos entornos paralelos (uno activo y otro de
  prueba), lo que facilita la implementación de cambios y una rápida recuperación en caso
  de problemas.

### Consideraciones de desarrollo

El desarrollo de modelos de ML puede seguir dos enfoques principales:
**_model-centric_**, enfocado en optimizar algoritmos, y **_data-centric_**, que prioriza
la mejora de la calidad de los datos, lo cual es esencial para garantizar un buen
rendimiento en producción.

Es crucial realizar un _sanity check_ inicial para validar las hipótesis del modelo,
establecer líneas base robustas y emplear herramientas de versionado como **MLFlow** o
**DVC** para rastrear de manera efectiva modelos, datos y resultados.

El mantenimiento continuo de los modelos requiere una supervisión constante para detectar
**_drifts_** (desviaciones en el comportamiento del modelo) y **datos OOD** (fuera de
distribución), así como la recolección de métricas clave para evaluar su rendimiento.
Además, es fundamental equilibrar adecuadamente los conjuntos de datos y mantener la
consistencia en las divisiones para entrenamiento, validación y prueba, garantizando que
el modelo sea fiable y escalable a largo plazo.

## Otras notas

cómo pasar desde un negocio a problemas de ciencia de datos pues primero lo que hay que
definir es una serie de hipótesis discutirlas y ver cuál es la que más se ajusta ocurre
en la realidad cada hipótesis tendrá diferentes soluciones y luego definida la hipótesis
hay que definir los objetivos, la idea ejecutarlo y establecer métricas.

# MLOps

## Ej.

**Edge**  
**Detective**  
**API**  
**Predict**  
**Prediction Server**  
**Cloud, edge**

---

## Problemas:

- **Data drift:** La distribución de los datos puede variar en la realidad, respecto a
  los datos de entreturamiento / test / validación.

- **POC → Product of Concept**

---

## Véasele:

- **Los pasos pueden ir de un lado a otro proceso:**
  1. Scoping: Definir el proyecto, reiterativo.
  2. Data: Definir los datos y establecer un baseline, etiquetar y organizar los datos.
  3. Modelado: Seleccionar y entrenar el modelo, realizar un análisis de errores.
  4. Deployment: Deployar un productivo, automatizar y mantener las tiendas.

---

- **Manual:**
  - **Automatización:**
    - **Reemplazo de los datos.**

- **OK Training**
- **OK Valid / Test**
- **OK Production**

1. Scoping  
   Définir une théorie, comme la précision requérante de l'outil, la technologie, la
   technologie, la technologie, la technologie, la technologie, la technologie, la
   technologie, le temps, la technologie, la technologie, la technologie, la technologie,
   la technologie, la technologie, les données, les données, les données, les données,
   les données, les données, les données, et les données.  
   (Esto depende de los datos, y el software)

2. Data  
   Los datos son los datos, los datos son los datos, los datos son los datos, los datos
   son los datos, los datos, los datos son los datos, los datos son los datos, los datos
   son los dados, los datos son los datos, los datos son los datos, los datos son los
   datos, las données son los datos, las données son los datos, las données son los
   datos, las données son las données, las données son las données, las données son las
   données, las données son las données, los datos son las données, los datos son las
   données, los datos son las données, los datos son los datos, los datos son los datos,
   los datos son los datos, la información es una información, la información es una
   información, la información es una información, la información es una información, las
   données son las données, las données son las données, las données son las données, la
   información es una información, las données son las données, las données son las
   données, la información es una información, la información es una información, la
   información es una información, los datos son los datos, los datos son los datos, los
   datos son los datos, el software es una información, el software es una información,
   el software es una información, el software es una información, los datos son los
   datos, los datos son los datos, los datos son las données, los datos son las données,
   los datos son las données, las données son las données, las données son las données,
   las données son los datos, los datos son los datos, los datos son los datos, los datos
   son las données, las données son las données, las données son las données, los datos
   son los datos, los datos son los datos, los datos son las données, la información es
   una información, la información es una información, la información es un software, la
   información es un software, la información es un software, la información es un
   software, los datos son los datos, los datos son los datos, los datos son las données,
   el software es una información, el software es una información, el software es un
   software, el software es un software, los datos son los datos, los datos son los
   datos, los datos son los datos, un software es una información, un software es una
   información, un software es un software, un software es un software, los datos son los
   datos, los datos son los datos, los datos es una información, los datos es una
   información, los datos es un software, los datos es un software, los datos es un
   software, los datos es un software, las données son las données, las données son las
   données, las données son las données, el software es una información, el software es
   una información, el software es una información, un software es una información, los
   datos son los datos, los datos son los datos, los datos es una información, el
   software es una información, el software es una información, el software es un
   software, los datos son los datos, los datos son los datos, el software es una
   información, los datos son los datos, los datos son las données, el software es una
   información, los datos son las données, los datos son las données, el software es una
   información, los datos son las données, el software es un software, los datos son los
   datos, los datos son los datos, un software es una información, los datos es una
   información, los datos es un software, los datos es una información, los datos es un
   software, los datos es un software, las données son las données, los datos son las
   données, los datos es una información, los datos es una información, los datos es un
   software, las données son las données, los datos es una información, los datos es una
   información, los datos es una información, los datos es un software, la información es
   una información, la información es una información, la información es un software, los
   datos son los datos, los datos son los datos, el software es un software, los datos
   son los datos, los datos son los datos, la información es una información, los datos
   es una información, los datos es un software, los datos es la información, los datos
   es la información, los datos es un software, los datos es un software, los datos es un
   software

Gear distintos que permiten detectar datos difíciles mediante una medición de la
temperatura para tener predicciones consistentes.

Otras consideraciones en la parte de software:

- Procesamiento: en tiempo real o fáciles.
- Utilizar en la web o en el edge.
- Computo disponible.
- Materiales, filmografía.
- Usar logging y registros de los pasos o fallos.
- Seguridad y privacidad de los usuarios, en la recopilación de datos.

Caso de uso de un deploymant:

- Gradual ramp up with monitoring.
- Rollback.

El primer permite regular la cantidad de tráfico de usuarios que van a usar un modelo u
otro, el rollback permite volver al modelo anterior.

Sharding: usar un modelo para realizar una recopilación de datos de una sola medición, el
modelo de recopilación del modelo.

Canary deployment: "pregunta" utiliza los tráficos de recopilación de datos para
controlar la recopilación y monitorear su efectividad, anulando el modelo de tráfico para
el paso.

Blue green deployment: usar el modelo antiguo y nuevo modelo, un modelo que cambia a una
nueva y otra, rollback rápido.

3. Los modelos requerirán, eventualmente, desde cero o reentrando a datos, partes. Esto
   también es un problema de investigación, continuidad, learning y catastróficas. Porque
   (y) para no depender de un modelo, con el tiempo debido a la variabilidad del los
   datos en producción.

Algunos apoyaques:

1. Entender el modelo con todas las datos.
2. "Asignando mayores pesos/relevancia a los nuevos datos."
3. Si hemos recopilado suficientes datos, podemos eliminar los datos antiguos.

Podemos tener 2 apoyaques de desarrollo:

- Model centrí: mayor enfoque en mejorar el modelo, esto tiene unos datos de bedwomark,
  en SOTA → Researc.
- Data centrí: mayor enfoque en mejorar los datos, no en incrementar los datos, sino en
  tratarlos, tener un mejor autenticidad de los datos, etc. → Más útil en producción/uso.

Establecer las bases, (Importante para evaluar mejor)

- Utilizando predicciones de personas y compañeros, con el sistema actual creado.
- Ver el SOTA en temas relacionados con el trabajo.
- Realizar comparaciones con sistemas empleados anteriormente.

Podemos hacer un "sanity check" para comprobar el resultado del modelo, estrenando el
modelo en nuestro sistema y comprobando si se ajusta, para luego estudiar si es óptimo.  
Realizar los datos o corregir/despegar el código modelo.

Priorizar el trabajo, enfocarse en las categorías para trabajar.

- Ver cuento de puede mejorar el modelo.
- Estudiar la frecuencia con la que aparecen las muestras.
- Estudiar si merece la pena mejorar la precisión de una clase en particular.

Generalmente, generamos datos, aumentamos, ciertamente,  
complejos, que permiten tener un modelo robusto  
pero, y también hay que analizar los resultados  
pues estos podrían afectar negativamente en el  
resultado del modelo.

Recomendable utilizar sistemas de tracking para  
el personalizado de algoritmos, código, dataset, usados  
hiperparámetros, resultados,...

Consideraciones en los datos:

- Los problemas con datos no estructurados  
  y con datos reducidos (< 1000 muestras, p.ej. por  
  clase, aunque dependen de la naturaleza del  
  problema), requieren de aumentación de datos.

- En el caso de problemas con datos  
  estructurados depende más de la consistencia  
  de las etiquetas.

- Financiar clases para reducir incumplimientos y  
  simplificar el etiquetado.

- Induoso colocar una nueva clase con casos  
  autogrupos.

- Realizar divisores (clasi/fest/valid) balanceadas.

Tener un POC (Proof of Concept) evaluar el  
rendimiento e iterar sobre todo definiendo  
muy bien el pipeline usado para ser  
replicado luego en producción de forma una  
automatizacion con herramientas como Apache  
Airflow o similar.

Tener información adicional de metadatos  
también permite tener un mejor contexto  
de los datos, su contenido, origen, facilitar  
el análisis de errores (puede que ciertos  
errores se den en ... para partes concretas).

Scoping:

- Identificación del problema, sobretodo en la  
  relación del entorno, no de un problema de  
  IA en AI.

- Identificar posibles soluciones.
- Evaluar viabilidad y valor, validar la  
  factibilidad y el ... RACI Retorno de Inversión

- Establecer hitos y recursos: planificar los  
  hitos del proyecto y presupuestar los  
  recursos necesarios.

# Introducción a MLoPS

- MLoPS es la estandarización y agilización del ciclo de vida de procesos relacionados
  con el machine learning.

- Con la automatización de procesos de decisión (mínima o ninguna intervención humana),
  los modelos empiezan a ser más críticos y en paralelo gestionan su riesgo. Se vuelve
  más relevante.

- Define business goals → access, understand and clean data → build machine learning →
  deploy machine learning.

- Deployment: dinámico, los datos cambian, los modelos se deben adaptar, reestructurar y
  volver a desplegar. (codigo + datos)

- Monitoreo: continuo del rendimiento, el riesgo dependerá del valor/renuncia de dichos
  modelos en el modelo de negocios de la empresa.

- Riesgos: - Enviando periodicamente.
  1. Modelo no disponible por un periodo de tiempo.
  2. Mala predicción.
  3. Degradación de la precisión de los modelos con el tiempo.
  4. Riesgo de perder talento, que mantenga dichos modelos.

- Tener un control del verdadero, sobretodo en la fase experimental.
- Estender qué modelos son mejores que los anteriores, hacer métricas, beduinales
  establecidos, etc.

- Model development:
  - Establecer objetivos de negocios.
  - Obtención y exploración de los datos.
  - Factore empleos y selección.
  - Estructuración y evaluación.
  - Reproducible.
  - Producto y despliegue.

- Tipos de deployment:
  - Model - as - a - service: modelo desplazado como un framework y crear una API Rest.
  - Modelo cubeblico.

- Podemos reducir los dependencias exportando el modelo a ONNX o similar.
  - Estructuralmente, diarias y redeplyuent.
  - Federated Learning, Approaches.

- Possible pipeline:
  - Build Model → model artifacts → send to storage → sanity/others devices → reports.
  - Deploy test → Test performance → Validation.
  - Deploy production → Canary → Full model.

# Artifacts modelo:

- Código modelo, preprocesado, etc.
- Miperparámetro, y configurações.
- Datos, etiquetación y validación.
- Modelo, atractivo, atreunado, y ejecutable.
- Entorno (requisitos para la ejecución).
- Documentación.

→ Blue-Green, deployment, in Kubernetes para despliegue. Sin eliminar el sistema
existente. (?)

---

# Data Science, Metadology

- Seguir una guía para la toma de decisiones durante los procesos.

→ Recopilación de datos. → Creación estratégica de medición. → Comparativas de métodos de
análisis de datos.

---

# Business Understanding

→ Analytic Approach.

→ Data Requirements.

→ Data Collection.

→ Data Understanding.

→ Data Preparation.

→ Data Modeling.

→ Data Evaluation.

→ Data Collection.

→ Data Understanding.

→ Data Preparation.

- Definir el problema:
- Determinar el abordaje:
  - **Objetivos:**
    1. ¿Qué problema pretenden resolver?
    2. ¿Cómo vamos a los datos para resolver esos preguntas / problemas?
    3. Al recopilar los datos:
    4. ¿Qué datos necesitamos?
    5. ¿Cómo se van a almacenar los datos?
    6. ¿Cómo recopilados representan el problema a solucionar?
    7. ¿Cómo trabajan adicional se requiere para manipular los datos?
- Validación:  
   8. Al realizar visualizaciones de los datos, ¿es necesario que los resultados sean
  respaldados?  
   9. ¿Se deben ajustar los datos?  
   10. ¿Podemos poner el modelo en producción?  
   11. ¿Podemos obtener feedback con el que revisar el proceso?

- **Data**  
  **Sauces**  
  **Methodology**

- **Data**  
  **Requirements**  
  **Stage**  
  **Identificar**  
  **el**  
  **cautelar**  
  **de**  
  **los**  
  **datos**  
  **necesarios**  
  **formatos**  
  **y**  
  **fuentes**

- **Durante**  
  **la**  
  **colección**  
  **de**  
  **los**  
  **datos**  
  para  
  **poder**  
  **observar**  
  **y**  
  **medir**  
  **la**  
  **calidad**  
  **de**  
  **los**  
  **datos**

- **Objetivo**  
  **Insignitas**  
  **Podemos**  
  **realizar**  
  **visualización**  
  **de**  
  **datos**  
  **y**  
  **estadística**  
  **descriptiva**

- **La**  
  **colección**  
  **de**  
  **datos**  
  **requiere**  
  **la**  
  **colaboración**  
  **con**  
  **las**  
  **personas**  
  **de**  
  **inquietud**  
  **de**  
  **datos**  
  **programadores**  
  **etc**  
  **para**  
  **asegurar**  
  **la**  
  **calidad**  
  **y**  
  **eficiencia**

- **Entender**  
  **los**  
  **datos**  
  **usando**  
  **estadísticas**  
  **como**  
  **la**  
  **variante**  
  **media**  
  **maximo**  
  **y**  
  **mínimos**  
  **conveniente**  
  **etc**

---

- **Estilos**  
  **varios**

- **Evolutivo**  
  **Algoritmos**  
  **por**  
  **Nuestros**  
  **Architectos**  
  **Algoritmos**  
  **genéricos**  
  **para**  
  **la**  
  **construcción**  
  **de**  
  **algoritmos**  
  **incluidos**  
  **más**  
  **establecidos**  
  **precisos**  
  **etc**

- **Natural**  
  **Architectura**  
  **Search**  
  **Busqueda**  
  **Buscar**  
  **Busqueda**  
  **Buscar**  
  **Buscar**  
  **Buscar**  
  **Buscar**

- **Crea**  
   **injetivo**  
   **dentro**  
   **aparta**  
   **notebooks**  
   **del**  
   **proyecto**  
   **que**  
   **crea**

  **Designing ML Systems (cap. 3)**

- El algoritmo es sólo una pequeña parte de un sistema en producción. Hay businesses
  requerientes, intrapagos, ataque de datos, etc.  
  Lógica, monitoreación, aprendizaje continuo, infraestructura.

- Incluso para problemas que pueden solucionar con HL, puede que usen ML no sea la mejor
  opción.  
  → La más óptima.  
  → En datos.

- Aprende gracias a la existencia de patrones,  
  que pueden no ser tan obvios,  
  o que el dataset no lo recoga de forma correcta → Feature Engineering.

- Existen casos donde se despliegan modelos sin entrenarse en ningún tipo de datos  
  que aprenda directamente de datos en producción.

- HL es viable cuando el coste de las predicciones incorrectas es barato. No supone una
  gran pérdida para la empresa.  
  O si el % de aciertos predicciones positivas compensa → ejemplo: código autónomo.

- HL es viable si se puede escalar, si los patrones cambian constantemente para tener
  reglas pre-fijadas.

- Descompone el problema en partes más pequeñas para involucrar el ML en ciertos partes
  simplificando el proceso.

- Aplicaciones de ML en empresas, tienen a tener requisitos diferentes y consideraciones
  que los aplicaciones de consumidores. Como restricciones de precisión y latencia más
  estrictas.
- O en casos como la medición donde existen casos de privacidad más estrictas.

- ML en producción varía mucho de ML en investigación.

| Requisitos    | R&D          | Productiva                            |
| ------------- | ------------ | ------------------------------------- |
|               | SOTA         | Standardos, cada 4 con sus requisitos |
| Computo       | ↑ Training   | ↑ Inference                           |
|               | ↑ Throughput | ↓ Latency                             |
| Patro         | Statics      | Dynamics (Shift)                      |
| Sego          | No pico      | Considerado                           |
| Interrability | No pico      | Considerado                           |

- Modelos muy complejos para ser utilizados.
- En producción, cada standard de requerimientos regulares para generar un modelo de
  producción.
- El proceso de producción es muy complejo de generar modelos de diseño.

- En ocasiones para crear un sistema de un que satisfaga diferentes objetivos de dividir
  dichos objetivos y de crear un modelo para cumplirlos, para finalmente combinar sus
  predicciones.

- Tener requisitos diferentes en R&D y producto hace que busquen prototipos, nunca se
  lleven a producción, ej: Ensamblajes Modelos, combinación de las predicciones de
  múltiples modelos que pueden generar los mejores resultados, a diferencia de las
  predicciones, pero que no se pueden generar y utilizar en producción por su
  complejidad, latencia, etc.

- Huidas empresas se centran más en la mejora de los datos (Data-centric) que en la
  mejora de los modelos (Model-centric).

- A mayor complejidad de los modelos, es la explícibilidad, ya que ello, mayor es la
  complejidad de detectar (Explicar) el motivo del los fallos.

- Designing ML System (Cap.2)

- Asignar los datos para los componentes y los diseñadores pueden trabajar juntos para
  satisfacer los objetivos y requisitos.

- Requisitos a tener en cuenta: readability, scalability, maintainability, y
  adaptabilidad.

- No empresas no lo imputan las métricas de los modelos (F1-Score, precisión,
  interacción, latency, ...) si no mueve ninguna métrica de negocio. (Business Metrics).

- Huidas compañias crean sus propias metálicas que las mueven a métricas a seguir por los
  modelos.

- Cuanto más tiempo se adopte el uso de ML, más eficientes serán las propias y más rápida
  será el desarrollo, mueven tiempo de ingeniería y menos coste en la nube.

- El sistema debe seguir funcionando correctamente en el nivel deseado. Incluso con
  adversidades, no falla en hardware y software o errores humanos.

- Un sistema puede escalar en complejidad, en volumen de trabajo, escalado en recursos
  generacionales de forma dinámica y disponibilidad, la cantidad de artefactos a manejar.

- Hay que estructurar novedades e infraestructuras con el fin de usar herramientas
  acordes y estandarizado. Entre grupos, código documentado, artefactos y versionados.
  Ofrecer coarte de suficiente.

- Capacidad para adaptarse a cambios en la distribución de los datos y requisitos del
  negocio. Hay relacionado con el automotivability.

- Desarrollar un sistema de ML es un proceso iterativo y que casi nunca acaba.

- Paso:

4. Scoping → 7. Data Engineering → 8. Model Development → 9. Monitoring and Control → 10.
   Learning

- En su experiencia los modelos de clasificación principalmente requieren al menos 100
  ejemplos por clase para aprender a clasificar.

- En general, cuando se tienen múltiples objetivos por optimizar, resulta buena idea
  dividirlos en varias métricas y porcentilarlos por extremadamente, haciendo que el
  desarrollo y mantenimiento de más sencillo.

**Paramentalización**

Total Loss = $$\alpha \cdot \log_2(1 + \beta \cdot \log_2 \frac{\alpha}{\beta})$$

Total Score = $$\alpha \cdot Score_1 + \beta \cdot Score_2$$

Ajustable sin necesidad de reestructurar.

- **Designing ML Systems (Cap 8)**

- Los datos son interesantes de almacenar si se tiene como objeto sacar un muy de los por
  lo que no es solo importante conocer cómo formatear los documentos sino también cómo se
  estructuran.

- Conocer cómo colectar, procesar, almacenar, obtener y procesar grandes volúmenes de
  datos es esencial para crear sistemas de ML en producción.

- Conocer la fuente de los datos permite usar los datos de manera más eficiente.
  - Usuario (input data)
  - datos generados por el sistema (output)
  - internal databases

First Party Data: datos recopilados por la propia empresa de sus usuarios y clientes.

- Second Party Data: datos colectados por otra compañía en sus propios usuarios al que
  posiblemente tenga que pagar para obtener sus datos.

- Third Party Data: datos públicos recopilados.

- Almacenar datos = Persistente → No fácil, y puede ser caro, conectar: 100.000.000 → 9.

- JSON editable, por el humano pero al estar bien basado en texto captura, muchísimo
  espacio.

- CSV es row-major: documentos consecutivos en una fila. Se almacena uno al lado del otro
  en una columna. Los Parquet son column-major, lo mismo pero en columna.

- Por lo que sí una tabla es row-major acceder a sus valores por la fila. Será más rápido
  que a sus columnas.

- Por tanto, CSV es mejor para acceder a los parquet y Parquet a los columnas.

- Row-major más rápido para escritura, y columnar mejor para lectura.

- Pandas se basa en un concepto de las Data Frame de R. Que son columnar y en NumPy, por
  defecto, son row-major.

- AUS recomienda utilizar formato Parquet porque es más rápido y ocupa menos en los
  buckets de SS comparado con los formatos de texto.

- **df.info()** → **df.df.to_table()**.

- El canto representamos los datos no solo afecta a una construcción, el sistema, sino el
  problema que puede resolver el modelo.

- Los modelos relacionados consisten en un modelo donde los datos están organizados en
  relaciones (tuplas), sin orden (se puede mezclar (A,B) = (B,A)). y se debe almacenar en
  ficheros como CSV o parquet.

- Para especificar los datos que queremos de una base de datos es un querying lenguaje
  (SQL y NoSQL).

- Declarative ML Subteaus → H2O, AutoML. No se requiere especificar la estructura o
  imperativa de los datos, modelo, experimentar con varios modelos y seleccionar el
  mejor, dada la característica y tareas.

- Los datos estructurados siguen un modelo de datos predeterminados también, con una
  estructura de datos. Esto podría ser una lista de datos, pero si el esquema cambia lo
  harán todos los datos (Bing).

- Los datos no estructurados permiten mayor flexibilidad en las operaciones de
  almacenamiento. Se pueden convertir los datos (independientemente del formato) en un
  formato para almacenarlos.

Un reportorio para almacenar datos estructurados es un → data warehouse, datos no
estructurados → data lake. Los datos que se suelen implementar para almacenar datos antes
de ser procesados, los datos que han sido usados para almacenar datos que han sido
procesados → en formato para un uso.

- Los formatos y modelos de datos especifican la interfaz sobre cómo los usuarios pueden
  almacenar y obtener datos.

- En el mundo digital, una transacción es una acción, se investirán según se generan,
  actualizadas cuando se quieren algo. También, o borrado cuando no se requiere. Siente
  éxito el usuario → Los Latency → Alta disponibilidad.

- ACIO (Atomoicidad, Consistency, Isolation, Durabilidad).

- Cockroach DB, Apache Iceberg, DuckDB.

- Desacoplar almacenamiento del procesado.

- ETL (Extract Transform Load): procesado de propósito general y agregación de los datos
  en el → shape y formato deseado.

- Almacenarlo todo en una única parte (ELT) no es eficiente, conforme los datos crecen.

Cuando los datos pasan de un proceso a otro, existe un flujo de datos de un proceso al
otro (data flow).

- **Transpaso**: entre bases de datos.
- **Transpaso**: usando requests (REST).
- "usando sistemas como Apache Kafka y Amazon Kinesis." → Ticupa real.

- **REST**: perfilaciones, internet, predominantemente en APIs públicas. → HTTP es una
  implementación REST.

- **RPC**: frameworko, está, entre los sistemas que pertenecen a la misma organización. →
  principalmente en un mismo J. datacenter.

- Los sistemas en tiempo real pueden ser: vistos, como sistemas inmersivos. → Se basan en
  eventos. → Suelen ser sistemas pub-sub (publicación - subscripcion).

- Cuando procesamos datos en lotes, se llama Batch Processing. → HAPReduce, y Spark son
  herramientas que procesan batch de forma eficiente.

- Procesado en Stream puede dar bajas, bajas, porque puede procesar datos. → Cuando le
  llegan sin escribir, primero en una base de datos → Apache Flink, es estable,
  distribuido (parallelización).

- Batch Processing: comme on mesure fréquemment, que les procédures en stream. En ILH, il
  est possible de mettre en place des procédures qui permettent de mettre en place des
  processus de traitement.

- Designing ILS Systems (Cap. 4)

- Conforme évoluée en modèle, durant le lifecycle, la set de traitement auto-troublé en
  évoluée.

- La sélection de dates de parfaite manual pour la création de la date de traitement
  auto-troublé.
  - Gérer ses steps y est une aide idéale.

- Reconnaître sampling par flux de dates en tramp real.

- En cas de dates privées, la régulation manuelle.
  - On est possible.

- Dates que visuel de multiples, fluides y autodéfense.
  - Con duperfeite expérience (y précisant) il est possible de la régulation.
  - Unification des dates.

- Temps prévu en une définition de la date de problème.

- Méthodes par objet de régulation.

- Weak Supervision.

- Semi-Supervision.

- Transfer learning.

- Active learning.

- Datos balancados.

- P. G. Smarr
  - Datatypes généraux, généraux et étiquettes.
  - Instrumentation de base.

- (Distribució, balancadeada)

- El no tener los datos balanceados supone un mayor problema de problemas de
  clasificación y multicas.

- Los redes neuronales son sensibles al ruido y decaída de la precisión de los modelos.
  Por lo que anadir nuestras con ruido puede generar modelos mas robustos.

- Designing H1: Sustains (cap. 5)

- Tener las fuentes correctas tiene a dar un mayor boost de rendimientos comparado a
  realizar una búsqueda de hiperparametros.

- Eliminación de columnas o filas (mientras al completo pueden producir pérdidas en la
  precisión del modelo, generar sesgos, etc. → Se podrían completar valores utilizando la
  media, mediana o moda.

- Escalar fuentes que representan diferentes cosas (edad, sexo, salario, etc).

- El Dato Linage es un fenómeno cuando una forma de etiquetas se altera. Se influye a los
  fuentes para hacer predicciones y estimar información no esta disponible en la
  referencia.

- Si los datos tienen dependencia del tiempo hace un split de los datos basada en tiempo
  y no de forma aleatoria (cap. p. ej. valores en bolsa).

- **Privilegio** - **normalizar** dividir los datos (train, test) aplicando estadísticas
  / normalización al set de entrenamiento, las estadísticas obtenidas aplican al
  test/valid (del train).

- **Cuantos** más **pequenas** unas oportunidades de tener datos. Llega a un **computo**,
  **software** y mayor consumo de **memoria** / **computo**, **software** y **latinencia
  en informes**.

- **Feature** - **Imputación** : SHAP, InterpertHL

- **Designing** - **ML** - **Sistema** (cap. 6).

- **Overfit** - en un **batch** pequeño manejo posible. P.ej. 10 imágenes, ver si se
  obtiene una precisión del 100% o muy cerca.

- **gradient** - **descripción** : más computo con menor **dimensión** - **consumido**
  más tiempo.

- **Paralelización** - de datos.

- **Asincrono / Sincrono** - SGD, el primero en tomar en cuenta el **paseo** para
  **converger**, en la práctica, cuando el **no de paso** es grande, la actualización de
  los gradientes es **pobre**. Lo que implica que muchos de los gradientes de los
  parámetros, otro problema es el gran batal de **paseo** a procesar.

- **Hay que buscar formas de balancear la carga de trabajo de los nodos del cluster.**

- Mejor balance de forma simple (no efectiva) es utilizar lotes más pequeños en el main
  window. Y lotes más grandes en los de el resto de windows.

- Paper Related: Existen diferentes tipos de paralelización, datos, torneos, modelo, etc.
  → El paper de Movie Gear de Meta usa en su arquitectura diferentes tipos de
  paralelización → Las múltiples paralelizaciones pueden ser conjuntas → Mejor uso del
  hardware.

- AutoML: keraTuner, Ray con Tune.

- Hyperparameter tuning: random search, grid search, optimization bajo paramo.

- NAS (Neural Architecture Search): buscando de la mejor arquitectura durante su
  entrenamiento.

- Designing ML Systems (capitulo):
  - Predicciones online: busca un predicción para un punto, como se recibe una petición.
    → Un demandado. → RESTful.

  - Las predicciones en batalles es cuando los predicciones son generadas dado un periodo
    o hay un trigger → Almacenados. → Un tablas SQL en una máquina, y demuestra conforme
    se requiere. → Los datos de bandas de datos, data warehouses. → Batches, Features.

- Data parallelism:
  - P, torch: DistributedDataParallel library
  - Horovod: 3PP
  - P, torch: Lightning
  - May, AnyBackend

- Cloud:
  - AWS Sagemaker: Peruse the workflow, the data, the models, the execution, the data,
    the execution, the data, the execution, the data, the execution, the data, and the
    execution.
  - AWS, ec2.amazonaws.com (proxies/protection, the AWS, ec2.amazonaws.com
    (proxies/protection, the AWS, ec3.amazonaws.com (proxies/protection, the AWS,
    ec3.amazonaws.com, the AWS, ec3.amazonaws.com, the AWS, ec3.amazonaws.com, and the
    AWS, ec3.amazonaws.com, the AWS, ec3.amazonaws.com, the Amazon AWS,
    ec3.amazonaws.com, the AWS, ec3.amazonaws.com, the AWS)
  - Testing: modular Python
  - - decorated: checking code in documentation
  - - shellcheck: test shell scripts

- Containers:
  - - Cg: Container for ML
  - - Bento ML
  - - TRUSS
  - - Kubeflow -> kfserving

- Edge:
  - - ZOS: LambdaML
  - - Anadroid: ML ML
  - - PyTorch: mobile

Libro: Machine learning with Python (Ggplot)

Objetivos de un Data Scientist:

- Analistas: analizar y recopilar datos para la creación de datos.

- Modeling: modelar datos (computacionales) mediante el uso de estadística, ML o similar.
  → Busqueda de patrones.

- Working with the customer or user: tener mayor relación directa con el negocio. →
  Decisión Making.

Data Scientist: ML Engineer.

| Prototipo | Producto |
| --------- | -------- |
|           | general  |
|           | valor    |

- En definitiva hay que generar valor, que se puede traducir en realizar alguna acción
  que genere un valor, el coste / inversión de tiempo. Hay que ser estratégica en cuanto
  al tiempo y el tipo de la propuesta de valor.

- Hay que entender la propuesta, del negocio, el cliente y el entorno de trabajo. →
  Conocer la motivación, problemas y necesidades.

- Importancia en la comunicación.

- Conocer el margen o rango de tiempo en el que recopilar datos para hacer estimaciones.

Por ejemplo, en Telco, recopilar datos de 1 semana suele ser ideal para conocer el patron
de variabilidad o existencia de diferentes patrones.

- Usar Cache para almacenar resultados frecuentes. Puede ser común y necesario para
  reducir costes latentes, etc.

- Duda → Rebalance. The training dataset → SHOTE

- Map: Formato para guardar modelos basados en Java virtual machine (JVM), muy usado para
  guardar pipelines de Spark.

- Tipos de depósito:
  1. On-pipeline: Servidores propios.
  2. IaaS (Infrastructure as a Service): S3, EC2, de AWS, p.ej.
  3. Platform as a Service (PaaS): Aws Gaurda

- Herramientas:
  1. Building: Alchemar pipelines, ZenML.
  2. Monitoring: Seldon, Nepheue.ai

- Equipos de CD, publicar paquetes de ftthon a Rpm, o publicar en fttho sistema que
  utilice el modelo para hacer predicciones.

- Ejemplos de tests:
  1. Confirmar que las predicciones ticuen el formato esperado (dtype)
  2. Utilizar datos de validación redondeados para comprobar la precisión

**Cap.3**

- **Training** → [Model] → [Data] → [Data] → [Data] → [Data] → [Data] → [Train] → [Train]
  → [Train] → [Train] → [Train] → [Data] → [Data] → [Data] → [Data] → [Model] → [Model] →
  [Model] → [Model] → [Model] → [Data] → [Data] → [Data] → [Data]
- **Automatizar**  
  **entrenamientos**
- **Detector de Drills**  
  **Ocurre revisión de almacenador modelo**

- **One-hot encoding** → Sparse → Si muchas categorías puede buscar un modelador de la
  dimensionalidad.

- **Rotación**  
  **Train-Realizar**

- Drifts :

1. Concept drift (Covariate drift) : Causales : extraire, cubrir, mettre les relaciones
   de los factores, esto es común en Telco. Con la adopción de nuevos y nuevos factores,
   se produce una en el uso de los datos, que alteran los patrones, existentes → por
   ejemplo, el cambio de intensidad de color (interferencia en UVC).

- Pobles, soluciones : usar PCA/ACE para medir el error de reconstrucción multivariable →
  medir la divergencia de o similar (Jensen - Shannon) y divergencia para medir la
  divergencia de los distribuciones de cada factore individualmente.

- MAL → Esto es un drift en los datos, los relaciones no cubrirán cambios en nuevo,
  intensidad de los valores.

- Para detector drift en los datos, podemos usar Kolmogorov, Smirnov, test, Tcheburev.

- Información como alibi : TabularDrift, utilizando p-values, para que haga un tagger
  auto, habrá que elegir un punto crítico y cuando los varoneses, don nuevos.

- En la detección de las características de los features, puede que algunos de los
  features requiera mayor relevancia que otros de los outros.  
  Esto se conduce a una distinción entre los rasgos que resultan más relevantes y los que
  resultan menos relevantes.

- Podemos tener en cuenta la importancia de las características en ambos de dos
  situaciones que podrían ser:
  - **Cumplimiento de las características de los rasgos**, como el sistema de la alerta,
    pero esto solo hace que se cumpla el cumplimiento de las características de los
    rasgos.
  - **Permutación de los rasgos**, como el orden de los rasgos, pero esto solo hace que
    se cumpla el orden de los rasgos.

- **Permutación importante** → cambios en el orden de los rasgos, pero no en el orden de
  los rasgos.

- **SHAP, los valores de las características en el modelo de los rasgos, pero no en el
  orden de los rasgos**.  
  Esto se conduce a una distinción entre los rasgos que resultan más relevantes y los que
  resultan menos relevantes.

- **SHAP en el modelo de los rasgos**, como el orden de los rasgos, pero esto solo hace
  que se concurr en el orden de los rasgos.

- **SHAP en el modelo de los rasgos**, como el orden de los rasgo, pero esto solo hace
  que se concurr en el orden de los rasgos.

- **Shap, los valores de las características en el modelo de los rasgos**, pero no en el
  orden de los rasgos.

- **SHAP en el modelo de los rasgos**  
  como el orden de los rasgos, pero esto solo hace que se concurr en el orden del rasgo.

- **SHAP en el modelo de los rasgos**  
  como el orden de las características, pero esto solo hace que se concurr en el orden de
  las características.

- **SHAP en el modelo de los rasgos**  
  como el orden de la alerta, pero esto solo hace que se concurr en el orden de la
  alerta.

- **SHAP en el modelo de los rasgos**  
  como el orden de un rasgo, pero esto solo hace que se concurr en el orden del rasgo.

- **SHap en el modelo de los rasgos**  
  como el orden de un rasgo, pero este solo hace que se concurr en el orden del rasgo.

- **SHap en el modelado de los rasgos**  
  como el orden de un rasgo, pero este solo hace en el orden del rasgo.

- **SHap en el modelo de los rasgos** como el orden de un rasgo, pero este solo hace en
  el orden del rasgo.

- SHAP values se calculan centrando el modelo en todas las puntuaciones de features
  posibles que incluyen a un la feature y calulan la contribución marginal de la
  predicción de esa feature.

- Rademond crear scripts: -- main -- py para cuty point / inicializado ar de un módulo.

- Arquitectura en microservicios es aquella donde los computadores funcionales de un
  programa/app o similar de una solución está clonamente separados en sus propios
  servicios ( dejar de ser monoliticos).  
  Esto permite:

- Gestión independiente.
- Mejor mantenimiento, escalabilidad, ...
- División en grupos de trabajo.

- Kubeflow utiliza kafka como hyperparameter search.

- A la hora de crear soluciones es bueno crear ejemplos de historias posibles de usuarios
  / clientes para detectar necesidades y dificultades.

- Herramiento Time serie forecasting: Propret.

- Ray permite extraer múltiples modelos de manera paralela.

- Dyadic?

- Herramiento desarrollo de APIs: Ratman.

- Libro: Kubernetes in production. Best Practices by Aly Saleh and Huat Korshogl.

- Velocidad: velocidad. a la que se acumulan los datos, o se van generando, generalmente
  en un ciclo que no termina.

- Volumen: es la escala de los datos.

- Varieté: es la diversidad de los datos, tipo de dato, procedencia o procesos.

- Veracité: es la calidad y fiabilidad de los datos.

- Valore: valor que aportan los datos.

Algunas de las herramientas utilizadas para trabajar con datos estructurados,
semi-structurados, etc. son:

- Apache Hadoop: conjunto de herramientas que permiten procesar y programar de manera
  distribuida datos.

- Apache Hive: es un data warehouse (sistema que permite recopilar, almacenar, gestionar
  grandes volúmenes de datos provenientes de diversas fuentes) para técnicas (query y
  análisis).

- Apache Spark: un framework para análisis distribuido para datos complejos y en tiempo
  real.

Hadoop (Analizar y procesar big data)

Perúnte almacenamiento distribuido de grandes cantidades de datos entre clusters de
ordenadores.

HDFS (Hadoop Distributed File System) es un sistema de almacenamiento para big data que
se ejecuta en varias equipos básicos conectados a través de una red.

Proporciona almacenamiento escalable y viable para grandes cantidades de datos sobre los
clusters de modos, permite la paralización, ofrece redundancia (availability).

Hive

- No es óptimo para pequeños clientes.
- Más basado en la lectura.
- Apropiado para ETZ, reporting y análisis de datos.

Spark

- Propósito general.
- # In-memory processing.
- Propósito compartido con varios programas/languages.

Data mining process (Iterativa)

1. Goal set → Identificar premissas, lances
2. Select data → Identificar premissas, lances de dados
3. Reprocess → Limpar, adicionar dados
4. Transform → Determinar, realizar, adicionar, etc.
5. Data mine → Analisar métodos, algoritmos, etc.
6. Evaluate → Evaluar, resultados.
