---
authors: Daniel Bazo Correa
description: Ciclo de vida, desafíos y estrategias de despliegue en MLOps.
title: Fundamentos
---

## Referencias

- [ML in Production: From Data Scientist to ML Engineer](https://www.udemy.com/course/ml-in-production/?couponCode=SKILLS4SALEA)
- [PEP 8 — the Style Guide for Python Code](https://pep8.org/)
- [Effective Machine Learning Teams — David Tan (O'Reilly)](https://www.oreilly.com/library/view/effective-machine-learning/9781098144623/)

## Introducción

<p align="center">
  <img src="../../../assets/img/docs/logos/mlops-logo.png" width="500"/>
  <br />
  <em>Ciclo de vida de un proyecto MLOps</em>
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
infraestructura que puede variar desde servicios en la nube hasta servidores locales o
en los propios dispositivos (_on edge_), dependiendo de las necesidades. Una API o
interfaz es esencial para procesar solicitudes y devolver predicciones, mientras que la
gestión de predicciones y la monitorización aseguran la calidad, fiabilidad y
rendimiento en tiempo real.

## Desafíos

Uno de los principales desafíos en la adopción de metodologías de MLOps es la correcta
definición tanto del problema como de la posible solución. Además, es fundamental
implementar tecnologías que puedan comunicarse eficazmente entre sí, permitiendo la
creación de sistemas y procesos automatizados que agilicen la recopilación, el
tratamiento, el análisis y el uso de los datos. Este enfoque requiere una
infraestructura sólida, cuyo diseño y construcción demandan tiempo y conocimientos
especializados.

Una vez establecida la infraestructura necesaria para integrar los diferentes
componentes, surgen nuevos retos en la etapa de puesta en producción.

Entre ellos destaca el **_data drift_**, que ocurre cuando los datos de producción
difieren de los de entrenamiento, afectando la precisión del modelo. Otro desafío común
es el manejo de **datos fuera de distribución** (_Out of Distribution_, OOD), aquellos
que no encajan con los patrones aprendidos durante el entrenamiento. Además, la
actualización y el mantenimiento de los modelos para adaptarlos a nuevos datos o
requerimientos constituyen un esfuerzo continuo.

!!! note "Nota"

    El mantenimiento de modelos basados en inteligencia artificial suele implicar su
    reentrenamiento con nuevos datos para evitar la degradación de las métricas
    establecidas y asegurar un rendimiento óptimo.

### Ciclo de vida de MLOps

El ciclo de vida de MLOps es un proceso iterativo que permite realizar ajustes en
cualquier etapa para optimizar el sistema. Un diseño efectivo de un producto basado en
_machine learning_ debe justificar su necesidad, detallar sus objetivos e impacto, y
abordar las siguientes áreas clave:

1. **Definición del proyecto**: En esta etapa se identifican las necesidades del usuario
   y los objetivos del producto, además de evaluar la viabilidad técnica y financiera.
   Los pasos esenciales incluyen:
    - **Identificación de problemas y métricas clave**: Métricas como precisión,
      latencia y ROI (Retorno de Inversión) son fundamentales para medir el éxito del
      proyecto.
    - **Propuesta de valor**: Se define cómo el producto resolverá problemas específicos
      y generará beneficios para los usuarios.
    - **Factibilidad**: Se evalúan los recursos necesarios (humanos, tecnológicos y
      financieros) para implementar la solución.
    - **Planificación**: Se establecen cronogramas y se asignan recursos para el
      desarrollo del producto.

2. **Datos**: El manejo de datos es la base de cualquier sistema de ML. Incluye los
   siguientes procesos:
    - **Recopilación y organización**: Los datos pueden provenir de bases de datos,
      archivos o servicios web. En proyectos complejos, el almacenamiento en la nube es
      una opción ideal.
    - **Etiquetado y preprocesamiento**: Incluye normalización, codificación y
      extracción de características para garantizar que los datos sean adecuados para el
      entrenamiento.
    - **Análisis exploratorio de datos (EDA)**: Se analiza la distribución de los datos,
      se identifican anomalías y se descubren correlaciones relevantes.
    - **Manejo de desequilibrios**: Técnicas como el sobremuestreo o submuestreo
      equilibran clases desbalanceadas, asegurando que los datos sean representativos.
    - **División en conjuntos**: Los datos se dividen en conjuntos de entrenamiento,
      validación y prueba, manteniendo distribuciones similares para evitar problemas
      como el sobreajuste.

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
- **Inferencia**: Elección entre inferencia en lotes o en tiempo real, dependiendo de
  los requisitos del sistema.
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
- **Canary deployment**: En esta técnica, se asigna inicialmente un pequeño porcentaje
  de tráfico al nuevo modelo, incrementándolo gradualmente si demuestra ser eficaz y
  estable.
- **Blue-green deployment**: Utiliza dos entornos paralelos (uno activo y otro de
  prueba), lo que facilita la implementación de cambios y una rápida recuperación en
  caso de problemas.

### Consideraciones de desarrollo

El desarrollo de modelos de ML puede seguir dos enfoques principales:
**_model-centric_**, enfocado en optimizar algoritmos, y **_data-centric_**, que
prioriza la mejora de la calidad de los datos, lo cual es esencial para garantizar un
buen rendimiento en producción.

Es crucial realizar un _sanity check_ inicial para validar las hipótesis del modelo,
establecer líneas base robustas y emplear herramientas de versionado como **MLFlow** o
**DVC** para rastrear de manera efectiva modelos, datos y resultados.

El mantenimiento continuo de los modelos requiere una supervisión constante para
detectar **_drifts_** (desviaciones en el comportamiento del modelo) y **datos OOD**
(fuera de distribución), así como la recolección de métricas clave para evaluar su
rendimiento. Además, es fundamental equilibrar adecuadamente los conjuntos de datos y
mantener la consistencia en las divisiones para entrenamiento, validación y prueba,
garantizando que el modelo sea fiable y escalable a largo plazo.

## Equipos efectivos de ML

Entregar proyectos de ML exitosos requiere un enfoque multidisciplinar que abarca
producto, ingeniería de software, datos, ML y gestión de la entrega. Las plataformas y
herramientas de MLOps por sí solas no son suficientes: no escriben tests completos, no
hablan con los usuarios ni reducen el impacto negativo de los silos entre equipos.

### Fallos comunes

Los proyectos de ML fracasan con frecuencia en el mundo real. Las formas más habituales
de fallo incluyen:

- **No resolver el problema correcto**: cuando no se validan las ideas de producto con
  los usuarios de forma temprana y frecuente, se invierte tiempo y esfuerzo en construir
  algo que nadie necesita. La falta de _discovery_ continuo lleva a productos
  técnicamente viables pero sin valor real para el cliente.
- **Incapacidad de llevar modelos a producción**: muchos equipos logran entrenar modelos
  prometedores en entornos controlados pero no consiguen desplegarlos como productos
  funcionales debido a bases de código enrevesadas, falta de automatización y
  dependencias mal gestionadas.
- **Problemas de calidad de datos en producción**: los datos en el mundo real difieren
  de los de entrenamiento. Sin mecanismos de validación y monitorización, los modelos
  degradan su rendimiento silenciosamente.
- **Seguridad y privacidad inadecuadas**: la protección de datos es responsabilidad de
  toda la organización. Incluye anonimizar información personal identificable (PII),
  cifrar datos de producción, establecer controles de acceso y automatizar la detección
  de vulnerabilidades en dependencias.
- **Productos éticamente problemáticos**: sin diversidad en los equipos ni tests de
  sesgo estratificados, los modelos pueden ser sistemáticamente perjudiciales para
  ciertos segmentos de la población.
- **Incapacidad de evolucionar modelos rápidamente**: sin pipelines automatizados ni
  bucles de retroalimentación, los equipos no pueden iterar con la velocidad que el
  negocio requiere.

!!! note "Fallar de forma segura"

    El objetivo no es evitar el fallo, sino fallar de forma rápida, económica y segura,
    creando bucles de retroalimentación cortos y documentando las lecciones aprendidas
    para compartirlas con el equipo.

### Prácticas de desarrollo

Los equipos efectivos de ML adoptan prácticas de ingeniería de software que permiten
iterar con rapidez y confianza:

- **Programación en parejas (_pair programming_)**: los miembros del equipo trabajan
  juntos en una misma tarea, lo que distribuye el conocimiento, reduce silos de
  especialización y mejora la calidad del código desde el primer momento.
- **Bucles de retroalimentación rápidos**: cada cambio incremental se valida en segundos
  o minutos mediante tests automatizados. El pipeline de entrenamiento se ejecuta
  localmente con un dataset reducido para obtener feedback en uno o dos minutos antes de
  lanzar un entrenamiento completo en la nube.
- **CI/CD para ML**: al hacer _commit_, el código pasa por verificaciones automáticas en
  el pipeline de CI/CD que incluyen tests unitarios, _smoke tests_ de entrenamiento y
  tests de calidad del modelo. Si el modelo supera los umbrales de calidad, se empaqueta
  y despliega automáticamente en un entorno de preproducción, donde se ejecutan tests
  post-despliegue.
- **Tests como parte del desarrollo**: los tests no son una actividad posterior sino
  parte integral de cada historia de usuario. Se recomienda TDD (_Test-Driven
  Development_): escribir el test primero, ver que falla, y luego escribir el código
  mínimo para que pase.
- **Tipos de tests en sistemas ML**:
    - _Tests unitarios_: validan funciones individuales de procesamiento de datos e
      ingeniería de características.
    - _Smoke tests de entrenamiento_: ejecutan el pipeline completo con un dataset
      mínimo (incluso 10 muestras) para detectar errores en minutos.
    - _Tests de API_: actúan como tests de contrato ligeros que verifican que la
      interfaz cumple sus promesas.
    - _Tests post-despliegue_: validan que el artefacto desplegado funciona
      correctamente en un entorno real con sus dependencias.
    - _Tests de modelo_: verifican métricas globales y estratificadas, invarianza ante
      dimensiones irrelevantes y expectativas direccionales.

???+ example "Smoke test de entrenamiento"

    Si un pipeline de entrenamiento tarda 3 horas en la nube, se puede crear un smoke
    test que ejecute el mismo pipeline localmente con un dataset diminuto en 1-2 minutos.
    Esto evita el antipatrón de "hacer push para saber si algo funciona" y permite
    detectar regresiones antes de invertir tiempo en entrenamiento completo.

### Calidad de código

La deuda técnica en proyectos de ML tiende a acumularse exponencialmente. Sin tests
automatizados, el refactoring es arriesgado y tedioso, lo que lleva a bases de código
cada vez más difíciles de mantener.

- **Deuda técnica en ML**: una base de código con alta deuda técnica atrae aún más
  deuda, porque su estructura crea un camino de mínima resistencia que favorece los
  _hacks_ rápidos. Esto impacta negativamente en la moral, la confianza y el ritmo de
  progreso del equipo.
- **Refactoring continuo**: el refactoring debe ser tan seguro y sencillo que se pueda
  hacer como parte de la entrega de funcionalidades, no como una actividad separada. La
  regla práctica es dedicar un 80% del tiempo a entregar funcionalidades y un 20% a
  reducir deuda técnica.
- **_Code smells_ frecuentes en ML**:
    - Variables con nombres que no revelan su intención.
    - Comentarios excesivos que enmascaran código confuso.
    - Código muerto que se ejecuta pero cuyo resultado nunca se usa.
    - _Print statements_ de depuración que añaden ruido al código y a los logs.
    - Scripts monolíticos o notebooks sin funciones invocables.
- **Separación de concerns (núcleo funcional / capa imperativa)**: el código se
  estructura en un _núcleo funcional grueso_ compuesto por funciones puras
  (procesamiento de datos, ingeniería de características, transformaciones) que son
  deterministas y fáciles de testear, y una _capa imperativa delgada_ que gestiona los
  efectos secundarios (cargar datos, guardar archivos). Esta separación hace el código
  mucho más testeable y mantenible.
- **Principios de diseño**: crear abstracciones correctas (funciones y clases con
  interfaces claras) permite diseñar sistemas componibles y extensibles. Al
  refactorizar, no se añade funcionalidad nueva simultáneamente.

!!! note "Regla del Boy Scout"

    Deja la base de código un poco más limpia de lo que la encontraste. Si ves un poco
    de "basura" en el camino, recógela como parte de tu tarea si no te cuesta demasiado
    tiempo.

### Gestión de datos

La calidad y gobernanza de los datos son fundamentales para el éxito de los sistemas ML
en producción:

- **Contratos de datos (_data contracts_)**: tests que verifican que los datos cumplen
  el esquema esperado en términos de nombres de atributos, tipos de valores y
  restricciones. Actúan como una promesa formal entre productores y consumidores de
  datos.
- **Tests de calidad de datos**: validan aspectos como exactitud, completitud,
  consistencia, representatividad y puntualidad de los datos que alimentan los pipelines
  de entrenamiento e inferencia.
- **Tests de privacidad de datos**: verifican que los datos proporcionados a los modelos
  no contienen información personal identificable (PII) como nombres, números de
  identificación o direcciones.
- **Feature stores**: repositorios centralizados para ingeniería de características que
  almacenan features preprocesadas utilizadas tanto en entrenamiento como en inferencia.
  El versionado de datos en feature stores permite rastrear y gestionar diferentes
  versiones, asegurando reproducibilidad y consistencia.
- **Bucles de recolección de datos**: los sistemas ML deben incluir mecanismos para
  recopilar datos de producción (peticiones y predicciones) que permitan mejorar los
  modelos continuamente. Técnicas como supervisión débil, aprendizaje activo y
  aprendizaje semi-supervisado facilitan el etiquetado escalable.
- **Versionado integral**: no solo del código, sino también de datasets, parámetros del
  modelo, configuraciones e incluso las semillas del generador de números aleatorios
  usadas durante el entrenamiento.

???+ example "Problema de estratificación oculta"

    La precisión global de un modelo puede mejorar un 1%, pero la precisión para un país
    específico podría caer un 50%. Los tests de métricas estratificadas resuelven este
    problema segmentando el dataset de validación por dimensiones de interés (variable
    objetivo, género, región) y calculando métricas por segmento en lugar de una única
    métrica global.

### Estrategias de despliegue

Más allá de las técnicas básicas de despliegue, los equipos efectivos implementan
estrategias que minimizan el riesgo y maximizan el aprendizaje en producción:

- **Modo sombra (_shadow mode_)**: el nuevo modelo recibe tráfico real y genera
  predicciones, pero estas no se exponen al usuario final. Permite comparar el
  comportamiento del nuevo modelo con el actual sin riesgo para los usuarios.
- **Despliegue gradual con monitorización**: cuando el negocio decide liberar un cambio,
  se hace de forma gradual mientras se monitorizan métricas de negocio y operacionales.
  Si se detectan anomalías, se revierte automáticamente.
- **Tests A/B en producción**: permiten medir el impacto real de un modelo comparando
  métricas de producto entre grupos de usuarios expuestos a diferentes versiones.
- **Monitorización post-despliegue**: abarca tres dimensiones complementarias:
    - _Monitorización de aplicación_: métricas de rendimiento como latencia, throughput
      y tasas de error.
    - _Monitorización de datos_: detección de cambios en la distribución de datos
      mediante tests de sesgo y detección de outliers.
    - _Monitorización de modelo_: seguimiento de métricas de calidad del modelo en
      producción para detectar degradaciones tempranas.
- **Diseño para minimizar el coste de fallos**: dado que los modelos ML inevitablemente
  cometen errores, el diseño del producto debe reducir el impacto de predicciones
  incorrectas. Estrategias incluyen:
    - Incorporar un humano en el bucle para revisar predicciones en escenarios de alto
      riesgo.
    - Usar métricas ponderadas por coste (como F1 ponderado) que visibilicen errores
      costosos.
    - En escenarios de alto riesgo (como transacciones financieras grandes), configurar
      el modelo para ser conservador y señalar posibles problemas incluso con confianza
      moderada.
- **Automatización completa del pipeline de despliegue**: desde que el entrenamiento
  finaliza, un pipeline automatizado ejecuta tests de calidad del modelo, empaqueta el
  artefacto, lo despliega en preproducción y ejecuta tests post-despliegue, todo sin
  intervención manual.

!!! note "Todo como código"

    Adoptar un enfoque _"as code"_ implica tratar infraestructura, configuración,
    despliegues y monitorización como código versionado. Esto permite mejor control de
    versiones, reproducibilidad, automatización y colaboración entre miembros del equipo.
