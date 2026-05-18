---
authors: Daniel Bazo Correa
description:
    Conceptos fundamentales de Amazon Web Services, desde la infraestructura global
    hasta los principales servicios de cómputo, almacenamiento y redes.
title: Fundamentos
---

## Bibliografía

- [AWS Cloud Practitioner Essentials](https://skillbuilder.aws/learn/94T2BEN85A/aws-cloud-practitioner-essentials/8D79F3AVR7)

## Introducción a AWS

**Amazon Web Services** (AWS) es una plataforma de servicios en la nube (_cloud_) que
ofrece capacidad de cómputo, almacenamiento, bases de datos, redes y una amplia variedad
de herramientas bajo un modelo de pago por uso (_pay-as-you-go_). En lugar de adquirir y
mantener infraestructura física propia, las organizaciones pueden aprovisionar recursos
de forma inmediata y pagar únicamente por lo que consumen, lo que elimina la necesidad
de grandes inversiones iniciales en _hardware_.

Las principales ventajas de adoptar AWS incluyen la economía de escala, ya que los
costes se reparten entre millones de usuarios, lo que permite ofrecer precios más
competitivos que los de un centro de datos privado. La capacidad de escalar recursos de
forma elástica, tanto al alza como a la baja, garantiza que la infraestructura se adapte
en todo momento a la demanda real. La agilidad que proporciona la nube permite desplegar
nuevos entornos en cuestión de minutos, acelerando los ciclos de desarrollo y
experimentación. Además, el despliegue global resulta inmediato gracias a la extensa red
de centros de datos distribuidos por todo el mundo.

Toda operación dentro de AWS se realiza mediante llamadas a una interfaz de programación
de aplicaciones (API). Ya sea crear una instancia de cómputo, almacenar un fichero o
configurar una red, cada acción se traduce internamente en una petición API. Existen
tres formas principales de interactuar con estas API. La primera es la **AWS Management
Console**, una interfaz web gráfica que permite gestionar los servicios de forma visual
e intuitiva, especialmente útil para tareas de exploración y configuración inicial. La
segunda es la **AWS CLI** (_Command Line Interface_), una herramienta de línea de
comandos que permite automatizar operaciones y ejecutar secuencias de instrucciones de
forma reproducible. AWS proporciona además **AWS CloudShell**, una terminal integrada
directamente en la consola web que incluye la CLI preconfigurada, sin necesidad de
instalación local. La tercera vía son los **AWS SDKs** (_Software Development Kits_),
bibliotecas disponibles para múltiples lenguajes de programación que permiten integrar
los servicios de AWS directamente en el código de las aplicaciones. Un ejemplo destacado
es **Boto3**, el SDK oficial para Python, ampliamente utilizado en proyectos de ciencia
de datos e inteligencia artificial.

## Infraestructura global

La infraestructura de AWS se organiza en tres niveles jerárquicos que garantizan la
redundancia, la alta disponibilidad y la proximidad geográfica a los usuarios finales.

En el nivel superior se encuentran las **regiones**. Cada región es un área geográfica
independiente, como Europa (Irlanda) o Asia Pacífico (Tokio), que contiene múltiples
centros de datos agrupados. Las regiones están completamente aisladas entre sí, de modo
que un fallo en una región no afecta a las demás. La elección de una región adecuada
depende de varios factores. El primero es el **cumplimiento normativo (_compliance_)**,
ya que ciertas regulaciones exigen que los datos permanezcan dentro de una jurisdicción
concreta. El segundo es la **latencia**, puesto que conviene seleccionar la región más
cercana a los usuarios finales para minimizar los tiempos de respuesta. El tercero es la
**disponibilidad de servicios**, dado que no todos los servicios de AWS están
disponibles en todas las regiones y algunas funcionalidades se lanzan primero en
regiones específicas. El cuarto es el **precio**, que varía entre regiones debido a
diferencias en el coste de la energía, los impuestos y otros factores locales.

Dentro de cada región existen las **zonas de disponibilidad** (_Availability Zones_,
AZ). Cada zona de disponibilidad está compuesta por uno o varios centros de datos
físicamente separados, dotados de alimentación eléctrica, refrigeración y conectividad
de red independientes. Las zonas de disponibilidad de una misma región están
interconectadas, lo que permite diseñar arquitecturas que repliquen datos y servicios
entre varias zonas para tolerar el fallo completo de una de ellas.

Además de las regiones y las zonas de disponibilidad, AWS dispone de las denominadas
**_Edge Locations_**. Se trata de puntos de presencia distribuidos en un número de
ciudades muy superior al de las regiones, cuya función principal es acercar el contenido
a los usuarios finales. Estos puntos de presencia son la base de las redes de
distribución de contenido (_Content Delivery Network_, CDN). **Amazon CloudFront** es el
servicio CDN de AWS que almacena en caché copias del contenido en las _Edge Locations_
más cercanas al usuario, reduciendo significativamente la latencia en la entrega de
páginas web, vídeos, API y otros recursos estáticos o dinámicos.

## Modelo de responsabilidad compartida

El **_Shared Responsibility Model_** (modelo de responsabilidad compartida) define la
división de obligaciones de seguridad entre AWS y el cliente.

AWS asume la responsabilidad de la seguridad de la nube (_security of the cloud_). Esto
abarca la protección de toda la infraestructura física que sustenta los servicios: los
centros de datos, el _hardware_ de los servidores, la red global, los hipervisores y el
_software_ de virtualización. AWS se encarga del mantenimiento, la refrigeración, la
seguridad física de las instalaciones y la gestión de la red troncal que interconecta
las regiones y las zonas de disponibilidad.

El cliente, por su parte, es responsable de la seguridad en la nube (_security in the
cloud_). Esta responsabilidad incluye la gestión de los datos almacenados, la
configuración del cifrado, la administración de los accesos mediante políticas de
identidad, la configuración del sistema operativo de las instancias, la gestión de las
reglas de red y la protección de las aplicaciones desplegadas. En definitiva, todo
aquello que el cliente puede ver y configurar desde su cuenta de AWS recae bajo su
ámbito de responsabilidad.

## Gestión de identidades y accesos

**AWS Identity and Access Management** (_IAM_) es el servicio que permite controlar de
forma granular quién puede acceder a los recursos de AWS y qué acciones puede realizar
sobre ellos.

Al crear una cuenta de AWS se genera automáticamente un usuario _root_ que posee
permisos ilimitados sobre todos los recursos. Debido a su nivel de privilegio, se
recomienda encarecidamente no utilizar la cuenta _root_ para las operaciones diarias. En
su lugar, conviene crear usuarios de IAM individuales con los permisos estrictamente
necesarios para cada tarea, siguiendo el **principio de mínimo privilegio** (_least
privilege_).

Los permisos en IAM se definen mediante **políticas** (_policies_), documentos en
formato JSON que especifican qué acciones están permitidas o denegadas sobre qué
recursos y bajo qué condiciones. Estas políticas pueden asociarse a usuarios
individuales, aunque la práctica recomendada consiste en agrupar a los usuarios en
**grupos** de IAM y asignar las políticas al grupo, de modo que todos sus miembros
hereden los mismos permisos.

Los **roles** de IAM representan otro mecanismo fundamental. Un rol es una identidad con
permisos específicos que puede ser asumida temporalmente por un usuario, una aplicación
o un servicio de AWS. A diferencia de los usuarios, los roles no disponen de
credenciales permanentes. Cuando una entidad asume un rol, recibe credenciales
temporales con una duración limitada, lo que reduce el riesgo asociado a la exposición
de claves de acceso de larga duración. Los roles resultan especialmente útiles para
conceder permisos a instancias de EC2 que necesitan acceder a otros servicios de AWS, o
para permitir el acceso entre cuentas sin compartir credenciales.

## Redes en AWS

**Amazon VPC** (_Virtual Private Cloud_) es el servicio que permite crear redes
virtuales aisladas dentro de la infraestructura de AWS. Cada VPC funciona como un
entorno de red privado en el que se despliegan los recursos, con control total sobre el
rango de direcciones IP, las tablas de enrutamiento y las puertas de enlace.

Al crear una cuenta de AWS, se genera automáticamente una **VPC por defecto** en cada
región, configurada para que los recursos desplegados en ella tengan acceso a Internet
de forma inmediata. Si bien esta configuración resulta conveniente para pruebas y
prototipos, en entornos de producción es recomendable crear **VPC personalizadas** que
permitan definir con precisión qué recursos son accesibles desde Internet y cuáles
permanecen aislados.

Dentro de una VPC, los recursos se organizan en **subredes**. Las subredes públicas
están asociadas a una tabla de enrutamiento que dirige el tráfico hacia una puerta de
enlace de Internet (_Internet Gateway_), lo que permite que los recursos alojados en
ellas sean accesibles desde el exterior. Las subredes privadas, en cambio, carecen de
esta ruta, por lo que los recursos que contienen solo pueden comunicarse dentro de la
VPC o a través de mecanismos controlados como puertas de enlace NAT.

### Direccionamiento CIDR

El rango de direcciones IP de una VPC y sus subredes se define mediante la notación
**CIDR** (_Classless Inter-Domain Routing_). Una dirección IPv4 está compuesta por 32
bits. La notación CIDR indica cuántos bits son fijos (identifican la red) y cuántos son
libres (disponibles para asignar a los recursos). Por ejemplo, `10.0.0.0/24` significa
que los primeros 24 bits son fijos y los 8 restantes están disponibles, lo que permite
direcciones desde `10.0.0.0` hasta `10.0.0.255` (256 direcciones). Es importante tener
en cuenta que AWS reserva siempre 5 direcciones por subred: la dirección de red, la de
_broadcast_ y tres adicionales para uso interno.

### Conectividad con Internet y redes externas

Para que una VPC tenga acceso a Internet, es necesario asociar un **Internet Gateway**
(IGW) a la VPC y configurar la tabla de enrutamiento de las subredes públicas para
dirigir el tráfico hacia él. Las subredes privadas no disponen de esta ruta y, por
tanto, sus recursos no son accesibles directamente desde Internet.

Para conectar una VPC con redes privadas externas, como centros de datos _on-premise_ o
redes corporativas, AWS ofrece varias opciones:

| Servicio                 | Descripción                                                                                                                                                                                                                      |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AWS Client VPN**       | Servicio completamente gestionado y elástico que permite conectar trabajadores remotos y redes _on-premise_ a AWS sin requerir _hardware_ dedicado. Escala automáticamente.                                                      |
| **AWS Site-to-Site VPN** | Establece conexiones cifradas entre redes _on-premise_ y AWS a través de Internet, con alta disponibilidad y escalado elástico.                                                                                                  |
| **AWS PrivateLink**      | Permite establecer conexiones privadas entre una VPC y servicios externos, otras VPCs u otros recursos, manteniendo el tráfico dentro de la red de AWS.                                                                          |
| **AWS Direct Connect**   | Conexión física privada y dedicada entre las instalaciones del cliente y AWS. Requiere tender fibra óptica hasta un punto de presencia de AWS, ofreciendo mayor ancho de banda y menor latencia que las conexiones por Internet. |

El **Virtual Private Gateway** es el componente del lado de AWS que permite establecer
una conexión VPN. Se asocia a una VPC y actúa como punto de terminación de los túneles
VPN, permitiendo que el tráfico procedente de la red corporativa acceda a los recursos
de la VPC de forma segura.

### Control de tráfico: Security Groups y ACL

La seguridad a nivel de red se gestiona mediante dos mecanismos complementarios.

Los **grupos de seguridad** (_Security Groups_) actúan como cortafuegos virtuales **a
nivel de instancia**. Cada grupo de seguridad define reglas de entrada y salida que
especifican qué tipo de tráfico se permite. Por ejemplo, para un servidor web es
habitual configurar un grupo de seguridad que permita tráfico HTTP (puerto 80) y HTTPS
(puerto 443) desde cualquier origen, mientras que el acceso SSH (puerto 22) se restringe
a direcciones IP específicas. Los grupos de seguridad son **_stateful_**, lo que
significa que si se permite una conexión de entrada, la respuesta correspondiente se
permite automáticamente sin necesidad de una regla de salida explícita.

Las **listas de control de acceso de red** (_Network ACL_ o NACL) operan **a nivel de
subred**. Cada subred tiene asociada una NACL que evalúa los paquetes que entran y salen
de ella. A diferencia de los grupos de seguridad, las NACL son **_stateless_**: no
recuerdan si un paquete fue permitido previamente, por lo que cada paquete (tanto de
entrada como de salida) se evalúa de forma independiente contra las reglas definidas. Un
paquete que sale de una subred debe cumplir las reglas de salida de la NACL de origen, y
para entrar en la subred de destino debe cumplir las reglas de entrada de la NACL de
destino.

| Característica      | Security Group   | Network ACL             |
| :------------------ | :--------------- | :---------------------- |
| Nivel de aplicación | Instancia        | Subred                  |
| Estado              | _Stateful_       | _Stateless_             |
| Reglas              | Solo de permiso  | De permiso y denegación |
| Evaluación          | Todas las reglas | En orden numérico       |

## Servicios de cómputo

AWS ofrece una amplia gama de servicios de cómputo (_Compute as a Service_) que se
adaptan a diferentes necesidades, desde máquinas virtuales tradicionales hasta entornos
completamente _serverless_.

### Amazon EC2

**Amazon EC2** (_Elastic Compute Cloud_) es el servicio de cómputo más fundamental de
AWS. Proporciona máquinas virtuales redimensionables, denominadas **instancias**, que
permiten ejecutar prácticamente cualquier carga de trabajo. EC2 opera bajo un modelo de
**_multitenancy_**, en el que múltiples instancias de distintos clientes comparten el
mismo _hardware_ físico subyacente. El aislamiento entre instancias lo garantiza un
hipervisor gestionado por AWS, que se encarga de asignar los recursos de CPU, memoria y
almacenamiento de forma segura y eficiente.

Para lanzar una instancia es necesario seleccionar una **AMI** (_Amazon Machine Image_),
que es una plantilla preconfigurada que define el sistema operativo, las aplicaciones
preinstaladas y la configuración inicial de la instancia. Las AMI pueden ser
proporcionadas por AWS, creadas por la comunidad, adquiridas en el _AWS Marketplace_ o
generadas por el propio usuario a partir de instancias existentes. Una misma AMI permite
crear múltiples instancias con configuraciones idénticas, lo que facilita la
reproducibilidad de los entornos.

Las instancias de EC2 se clasifican en **familias** optimizadas para distintos tipos de
carga de trabajo. Las instancias de propósito general (_General Purpose_) ofrecen un
equilibrio entre cómputo, memoria y red, y resultan adecuadas para servidores web y
entornos de desarrollo. Las instancias optimizadas para cómputo (_Compute Optimized_)
proporcionan mayor potencia de procesamiento para tareas intensivas en CPU, como el
procesamiento por lotes o el modelado científico. Las instancias optimizadas para
memoria (_Memory Optimized_) están diseñadas para cargas que requieren grandes
cantidades de RAM, como bases de datos en memoria. Las instancias de computación
acelerada (_Accelerated Computing_) incorporan aceleradores de _hardware_ como GPU para
tareas de aprendizaje profundo o renderizado gráfico. Las instancias optimizadas para
almacenamiento (_Storage Optimized_) ofrecen alto rendimiento de lectura y escritura en
disco para bases de datos distribuidas o sistemas de ficheros de alto rendimiento.

La nomenclatura de las instancias sigue un patrón estandarizado. Por ejemplo, en
`t3.medium`, la letra `t` identifica la familia, el número `3` indica la generación y
`medium` especifica el tamaño, que determina la cantidad de CPU virtual y memoria
asignada. Es posible cambiar el tipo de instancia en cualquier momento para adaptarse a
nuevas necesidades de rendimiento.

Al configurar una instancia, el campo **_User Data_** permite especificar un _script_ en
Bash que se ejecuta automáticamente durante el primer arranque. Este mecanismo resulta
útil para instalar dependencias, configurar servicios o descargar código de forma
automatizada sin intervención manual.

Es importante tener en cuenta que las instancias de EC2 no ofrecen persistencia de datos
por defecto. Cuando una instancia se termina, toda la información almacenada en su
almacenamiento efímero se pierde. Por este motivo, los datos que deban conservarse deben
almacenarse en volúmenes persistentes como Amazon EBS o en servicios de almacenamiento
como Amazon S3.

### Modelos de precios de EC2

AWS ofrece varios modelos de precios para las instancias de EC2, diseñados para cubrir
distintos patrones de uso y niveles de compromiso.

El modelo **_On-Demand_** permite pagar por segundo o por hora de uso sin ningún
compromiso a largo plazo. Es la opción más flexible y resulta adecuada para cargas de
trabajo impredecibles, pruebas y prototipos, aunque también es la más costosa por unidad
de tiempo.

Los **_Savings Plans_** ofrecen descuentos significativos a cambio de un compromiso de
uso constante durante un período de uno o tres años. El compromiso se expresa en una
cantidad de gasto por hora, independientemente del tipo de instancia utilizado, lo que
proporciona flexibilidad para cambiar de familia o región.

Las **_Reserved Instances_** proporcionan descuentos similares a los _Savings Plans_,
pero vinculados a un tipo de instancia y una región específicos. El cliente puede elegir
entre pago total anticipado, pago parcial anticipado o sin pago anticipado, obteniendo
mayores descuentos cuanto mayor sea el pago inicial. Este modelo resulta idóneo para
cargas de trabajo predecibles y estables.

Las **_Spot Instances_** permiten acceder a capacidad de cómputo no utilizada con
descuentos de hasta el 90 % respecto al precio _On-Demand_. A cambio, AWS puede
interrumpir estas instancias con un aviso de dos minutos cuando necesite recuperar la
capacidad. Son especialmente útiles para tareas tolerantes a interrupciones, como
procesamiento por lotes, integración continua o análisis de datos a gran escala.

Los **_Dedicated Hosts_** proporcionan un servidor físico completo reservado para uso
exclusivo del cliente. Este modelo resulta necesario cuando existen requisitos de
licenciamiento de _software_ que exigen visibilidad sobre el _hardware_ subyacente o
cuando las regulaciones impiden compartir infraestructura física con otros usuarios.

Las **_Dedicated Instances_** son instancias que se ejecutan en _hardware_ dedicado al
cliente, pero sin la visibilidad ni el control a nivel de servidor físico que ofrecen
los _Dedicated Hosts_. Proporcionan aislamiento físico respecto a las instancias de
otros clientes.

### Contenedores en AWS

Los contenedores ofrecen una alternativa ligera a las máquinas virtuales, empaquetando
la aplicación junto con todas sus dependencias y configuraciones en una unidad portátil
y reproducible. AWS proporciona varios servicios para la gestión y ejecución de
contenedores.

**Amazon ECS** (_Elastic Container Service_) es un servicio de orquestación de
contenedores completamente gestionado que permite ejecutar, detener y administrar
contenedores _Docker_ a escala. ECS se integra de forma nativa con otros servicios de
AWS, lo que simplifica la configuración de redes, el balanceo de carga y la gestión de
permisos.

**Amazon EKS** (_Elastic Kubernetes Service_) es el servicio gestionado de _Kubernetes_
en AWS. Permite desplegar, gestionar y escalar aplicaciones contenerizadas utilizando el
estándar abierto de _Kubernetes_, lo que facilita la portabilidad entre entornos y la
adopción de herramientas del ecosistema _Kubernetes_.

**Amazon ECR** (_Elastic Container Registry_) es un registro de imágenes de contenedores
completamente gestionado, compatible con _Docker_, que permite almacenar, gestionar y
desplegar imágenes de contenedores de forma segura. El flujo de trabajo habitual
consiste en subir las imágenes a ECR y, a continuación, desplegarlas en ECS o EKS.

### Computación _serverless_

La computación _serverless_ representa un modelo en el que el desarrollador se
desentiende por completo de la gestión de la infraestructura subyacente. No es necesario
aprovisionar servidores, configurar sistemas operativos ni aplicar parches de seguridad.
AWS se encarga de todo ello, lo que permite al equipo de desarrollo centrarse
exclusivamente en el código de la aplicación. Desde la perspectiva del modelo de
responsabilidad compartida, AWS asume una mayor proporción de las responsabilidades
operativas en los servicios _serverless_.

**AWS Lambda** es el servicio _serverless_ más representativo de AWS, basado en el
paradigma de _Function as a Service_ (FaaS). El funcionamiento consiste en empaquetar el
código en una función _Lambda_, configurar uno o varios **_triggers_**
(desencadenadores) y dejar que el servicio ejecute la función automáticamente cada vez
que se produce el evento asociado. Los _triggers_ pueden ser muy variados: una petición
HTTPS a través de _API Gateway_, la subida de un fichero a Amazon S3, un mensaje en una
cola de Amazon SQS o un evento programado, entre otros.

AWS Lambda escala de forma automática replicando las instancias de la función en
respuesta a la demanda, sin intervención del usuario. El modelo de facturación se basa
exclusivamente en el número de invocaciones y en el tiempo de ejecución consumido,
medido en milisegundos, de modo que no se incurre en coste alguno cuando la función no
se ejecuta. La duración máxima de una ejecución de Lambda es de 15 minutos, lo que lo
convierte en una solución idónea para procesos basados en eventos, microservicios y
tareas de corta duración que no requieren un servidor activo de forma permanente. Lambda
soporta múltiples lenguajes de programación a través de distintos _runtimes_ y también
admite la ejecución de contenedores.

**AWS Fargate** es un motor de cómputo _serverless_ diseñado específicamente para
contenedores. Permite ejecutar contenedores en ECS o EKS sin necesidad de aprovisionar
ni gestionar instancias de EC2. Con Fargate, el usuario define los requisitos de CPU
virtual, memoria y almacenamiento para cada contenedor, y AWS se encarga de la
infraestructura subyacente. La facturación se calcula en función de los recursos
consumidos por cada contenedor.

### Otros servicios de cómputo

**AWS Elastic Beanstalk** es un servicio que simplifica el despliegue y la gestión de
aplicaciones en EC2. El desarrollador solo necesita proporcionar el código de la
aplicación y Elastic Beanstalk se encarga del aprovisionamiento de la infraestructura,
la configuración del balanceo de carga, el escalado automático y la monitorización,
manteniendo al mismo tiempo la visibilidad y el control sobre los recursos subyacentes.

**AWS Batch** es un servicio diseñado para ejecutar tareas de procesamiento por lotes
(_batch_) a gran escala. Gestiona de forma automática la infraestructura necesaria,
soporta procesamiento en paralelo y escala dinámicamente los recursos, desplegando
instancias de EC2 o _Spot Instances_ según la carga de trabajo.

**Amazon Lightsail** ofrece una experiencia simplificada para el despliegue de
aplicaciones web, sitios _WordPress_, entornos de desarrollo y pequeñas bases de datos,
con precios predecibles y una interfaz diseñada para usuarios que no requieren la
complejidad completa de EC2.

**AWS Outposts** es un servicio que extiende la infraestructura y los servicios de AWS a
las instalaciones del cliente (_on-premise_). Permite ejecutar servicios de AWS de forma
local, lo que resulta especialmente útil para cargas de trabajo que requieren baja
latencia, procesamiento local de datos o el cumplimiento de requisitos normativos que
impiden que los datos abandonen las instalaciones del cliente.

## Escalado y alta disponibilidad

Diseñar sistemas que soporten variaciones en la demanda y que continúen operando ante
fallos parciales constituye uno de los principios fundamentales de la arquitectura en la
nube.

El **escalado vertical** (_scaling up_) consiste en aumentar la capacidad de una
instancia existente, por ejemplo, migrando a un tipo de instancia con más CPU o memoria.
Aunque es sencillo de implementar, presenta un límite físico determinado por el tamaño
máximo de instancia disponible y requiere generalmente un reinicio.

El **escalado horizontal** (_scaling out_) consiste en añadir más instancias para
distribuir la carga de trabajo entre ellas. Este enfoque permite una paralelización
efectiva, no tiene un límite teórico de capacidad y resulta más resiliente, ya que el
fallo de una instancia individual no compromete la disponibilidad del servicio.

**Amazon EC2 Auto Scaling** permite automatizar el escalado horizontal de las instancias
de EC2 en función de la demanda. El servicio monitoriza métricas como la utilización de
CPU, la latencia de las peticiones o indicadores personalizados, y ajusta
automáticamente el número de instancias dentro de unos límites mínimo y máximo definidos
por el usuario. De este modo, se garantiza que siempre exista la capacidad suficiente
para atender la demanda sin incurrir en costes innecesarios durante los períodos de baja
actividad.

**Elastic Load Balancing** (ELB) es el servicio de balanceo de carga de AWS que
distribuye automáticamente el tráfico entrante entre múltiples instancias, contenedores
u otros destinos. El balanceador de carga se sitúa entre los usuarios y el grupo de
instancias, y emplea algoritmos de distribución como _round robin_, menor número de
conexiones activas (_least connections_), _hash_ de IP o menor tiempo de respuesta
(_least response time_) para repartir las peticiones de forma uniforme. Cuando EC2 Auto
Scaling lanza una nueva instancia, esta se registra automáticamente en el balanceador de
carga y comienza a recibir tráfico una vez que supera las comprobaciones de estado. ELB
también escala de forma automática para adaptarse al volumen de tráfico.

Para lograr una alta disponibilidad real, es fundamental desplegar las instancias en
**múltiples zonas de disponibilidad** dentro de una misma región. De este modo, si una
zona de disponibilidad completa experimenta un fallo, las instancias en las zonas
restantes continúan atendiendo las peticiones sin interrupción. La combinación de EC2
Auto Scaling, Elastic Load Balancing y despliegues en múltiples zonas de disponibilidad
constituye el patrón básico para construir arquitecturas tolerantes a fallos en AWS.

## Monitorización

**Amazon CloudWatch** es el servicio de monitorización y observabilidad de AWS que
permite recopilar, visualizar y analizar métricas, registros (_logs_) y eventos de
prácticamente cualquier recurso de la plataforma. CloudWatch proporciona información en
tiempo real sobre el rendimiento de las instancias de EC2, el estado de los
balanceadores de carga, la utilización de las bases de datos y cualquier otra métrica
relevante para la operación de la infraestructura.

A partir de las métricas recopiladas, es posible configurar alarmas que se activan
cuando un indicador supera o desciende por debajo de un umbral definido. Estas alarmas
pueden desencadenar acciones automáticas, como el escalado de instancias a través de EC2
Auto Scaling o el envío de notificaciones al equipo de operaciones. CloudWatch resulta,
por tanto, un componente esencial para la toma de decisiones informadas sobre el
dimensionamiento de los recursos y la detección temprana de problemas de rendimiento o
disponibilidad.

## Mensajería y desacoplamiento

En arquitecturas distribuidas, la comunicación directa y síncrona entre componentes
genera un acoplamiento fuerte que puede provocar fallos en cascada: si un componente
deja de responder, todos los que dependen de él se ven afectados. Para evitar este
problema, AWS ofrece servicios de mensajería que permiten una comunicación asíncrona y
desacoplada entre los distintos componentes de una aplicación.

**Amazon SQS** (_Simple Queue Service_) es un servicio de colas de mensajes
completamente gestionado. Un componente emisor deposita mensajes en la cola y un
componente receptor los consume a su propio ritmo. Los mensajes permanecen en la cola
hasta que son procesados, lo que garantiza que no se pierden aunque el receptor no esté
disponible temporalmente. Este patrón de comunicación elimina la dependencia temporal
entre emisor y receptor, aumentando la resiliencia del sistema.

**Amazon SNS** (_Simple Notification Service_) es un servicio de mensajería basado en el
modelo de publicación y suscripción (_pub/sub_). Un publicador envía un mensaje a un
**tema** (_topic_) de SNS, y el servicio se encarga de distribuirlo a todos los
suscriptores registrados, que pueden ser colas de SQS, funciones Lambda, puntos de
enlace HTTP o direcciones de correo electrónico, entre otros. SNS resulta especialmente
útil para difundir notificaciones o eventos a múltiples consumidores de forma
simultánea.

**Amazon EventBridge** es un servicio _serverless_ de bus de eventos que permite
conectar diferentes componentes de una aplicación, servicios de AWS y aplicaciones de
terceros mediante eventos. EventBridge facilita la construcción de arquitecturas
orientadas a eventos (_event-driven_) al proporcionar reglas de enrutamiento que dirigen
cada evento al destino adecuado en función de su contenido.

## Almacenamiento

**Amazon S3** (_Simple Storage Service_) es el servicio de almacenamiento de objetos de
AWS. Permite almacenar y recuperar cualquier cantidad de datos, de cualquier tipo de
fichero, en cualquier momento y desde cualquier lugar. S3 organiza los datos en
**buckets** (contenedores) y cada objeto almacenado se identifica mediante una clave
única. El servicio ofrece una durabilidad del 99,999999999 % (once nueves) y está
diseñado para soportar prácticamente cualquier caso de uso, desde el alojamiento de
sitios web estáticos hasta el almacenamiento de copias de seguridad, _data lakes_ y
contenido multimedia.

**Amazon RDS** (_Relational Database Service_) es un servicio gestionado que facilita la
configuración, operación y escalado de bases de datos relacionales en la nube. RDS
soporta varios motores de bases de datos, como MySQL, PostgreSQL, MariaDB, Oracle y SQL
Server, además de **Amazon Aurora**, el motor propio de AWS compatible con MySQL y
PostgreSQL. Al ser un servicio gestionado, AWS se encarga de las tareas de
administración rutinarias como la aplicación de parches, las copias de seguridad
automáticas y la replicación entre zonas de disponibilidad, lo que permite al equipo de
desarrollo centrarse en el diseño del esquema y la optimización de las consultas.

## Infraestructura como código

**AWS CloudFormation** es el servicio de infraestructura como código (_Infrastructure as
Code_, IaC) nativo de AWS. Permite definir todos los recursos de una arquitectura en
plantillas declarativas escritas en formato JSON o YAML. A partir de estas plantillas,
CloudFormation aprovisiona y configura los recursos de forma automática, reproducible y
consistente. Si es necesario realizar cambios, basta con modificar la plantilla y
aplicar la actualización, y CloudFormation se encarga de determinar qué recursos deben
crearse, actualizarse o eliminarse. Este enfoque elimina la configuración manual, reduce
los errores humanos y permite versionar la infraestructura del mismo modo que se
versiona el código fuente de una aplicación.

## Despliegues híbridos

No todas las organizaciones migran la totalidad de su infraestructura a la nube. En
muchos casos, los requisitos de latencia, la normativa sobre residencia de datos o la
existencia de sistemas heredados hacen necesario mantener parte de la infraestructura en
las propias instalaciones (_on-premise_) y combinarla con servicios en la nube. Este
enfoque se conoce como **despliegue híbrido**.

**AWS Outposts** permite ejecutar servicios de AWS directamente en el centro de datos
del cliente, utilizando el mismo _hardware_ y _software_ que en las regiones de AWS. De
este modo, las aplicaciones que requieren baja latencia o que deben procesar datos
sensibles de forma local pueden beneficiarse de las mismas API, herramientas y modelos
operativos que se utilizan en la nube pública. Outposts se integra de forma transparente
con la región de AWS más cercana, lo que permite construir arquitecturas híbridas
coherentes en las que los datos y las cargas de trabajo fluyen entre el entorno local y
la nube según las necesidades del negocio.
