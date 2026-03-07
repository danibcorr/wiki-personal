---
authors: Daniel Bazo Correa
description: Herramientas necesarias para DevOps.
title: Docker
---

## Bibliografía

- [Aprende Docker ahora! Curso completo gratis desde cero](https://youtu.be/4Dko5W96WHg?si=pOAHHRxpPkqpQ2go)
- [Docker Docs](https://docs.docker.com/)
- [DevOps con Docker, Jenkins, Kubernetes, Git, GitFlow CI y CD](https://www.udemy.com/course/devops-con-dockers-kubernetes-jenkins-y-gitflow-cicd/)
- [Minikube Docs](https://minikube.sigs.k8s.io/docs/)
- [Kubernetes Tutorials](https://youtube.com/playlist?list=PLiMWaCMwGJXnHmccp2xlBENZ1xr4FpjXF&si=mxLcHpXxnZUhSGu3)
- [Kubernetes: De novato a pro! (Curso completo en español)](https://youtu.be/DCoBcpOA7W4?si=KioSNJrOkZp-Dx5K)

## Docker

<p align="center">
  <img src="/assets/img/docs/logos/docker-logo.png" width="500"/>
  <br />
  <em>Logo de Docker</em>
</p>

Docker es una plataforma de código abierto que facilita la creación, implementación y
ejecución de aplicaciones mediante contenedores. Los contenedores permiten empaquetar una
aplicación junto con sus dependencias y configuraciones en una unidad estandarizada, lo
que simplifica el desarrollo de software y garantiza consistencia entre entornos. Entre
sus características principales destacan la portabilidad, ya que los contenedores se
ejecutan en cualquier sistema que soporte Docker independientemente del sistema
operativo; la ligereza, puesto que comparten el kernel del sistema operativo del host, lo
que los hace más rápidos de iniciar que las máquinas virtuales; la consistencia, al
asegurar que una aplicación se ejecute de la misma manera en cualquier entorno; el
aislamiento, dado que cada contenedor opera de manera independiente mejorando la
seguridad y evitando conflictos entre aplicaciones; y la escalabilidad, al facilitar la
creación y eliminación rápida de instancias.

### Contenedores frente a máquinas virtuales

Los contenedores y las máquinas virtuales son tecnologías de virtualización que permiten
ejecutar múltiples aplicaciones en un solo servidor físico. Aunque comparten objetivos
similares, como optimizar el uso de recursos y asegurar aislamiento, difieren
significativamente en su implementación y arquitectura subyacente.

<p align="center">
  <img src="https://profile.es/wp-content/media/image-1-1024x266.png"/>
  <br />
  <em>Pasos para la creación de un contenedor Docker</em>
</p>

Los contenedores constituyen una forma de virtualización a nivel del sistema operativo,
también conocida como virtualización ligera. A diferencia de las máquinas virtuales, que
virtualizan un sistema operativo completo, los contenedores comparten el núcleo del
sistema operativo del host y ejecutan aplicaciones dentro de espacios de usuario
completamente aislados. Cada contenedor contiene únicamente la aplicación y sus
dependencias —bibliotecas, archivos de configuración y variables de entorno—, lo que lo
hace extremadamente portátil y fácil de desplegar en diferentes entornos, desde la
máquina local de un desarrollador hasta un clúster en la nube.

El aislamiento de los contenedores se logra mediante tecnologías del kernel de Linux. Los
_namespaces_ (espacios de nombres) aíslan recursos del sistema operativo: `pid` aísla los
identificadores de procesos, `net` proporciona pilas de red separadas, `mnt` aísla los
puntos de montaje del sistema de archivos, `ipc` aísla recursos de comunicación entre
procesos, `uts` aísla nombres de host y dominios, y `user` aísla identificadores de
usuarios y grupos. Por su parte, los _cgroups_ (grupos de control) gestionan el uso de
recursos como CPU, memoria y disco, garantizando que los contenedores no consuman más
recursos de los asignados. Además, el _Union Filesystem_ (UFS) permite que los
contenedores se construyan en capas: las capas de solo lectura contienen archivos del
sistema, mientras que las capas de escritura se mantienen en la parte superior,
minimizando el uso de almacenamiento y facilitando el desarrollo iterativo.

Las máquinas virtuales (VMs), por su parte, son una tecnología de virtualización más
tradicional que permite ejecutar múltiples sistemas operativos en un servidor físico
mediante un hipervisor, como VMware o VirtualBox. Un hipervisor puede ejecutarse
directamente en el hardware del servidor (tipo 1) o sobre un sistema operativo (tipo 2),
gestionando la creación y ejecución de múltiples VMs y asignando recursos de hardware de
forma eficiente. Cada VM dispone de su propio sistema operativo completo, lo que
proporciona un aislamiento más fuerte que los contenedores, pero a costa de un mayor
consumo de CPU, memoria y almacenamiento, así como tiempos de inicio más prolongados.

Los contenedores resultan ideales para desarrollo y pruebas, arquitecturas de
microservicios y despliegue continuo, mientras que las máquinas virtuales son más
adecuadas para aplicaciones monolíticas que requieren aislamiento completo del sistema
operativo, entornos con múltiples sistemas operativos y cargas de trabajo heredadas.

En la nube, proveedores como Amazon Web Services (AWS), Google Cloud Platform (GCP) y
Microsoft Azure ofrecen servicios tanto de contenedores —AWS ECS/Fargate, EKS, Azure
Kubernetes Service (AKS) y Google Kubernetes Engine (GKE)— como de máquinas virtuales
—EC2 (AWS), VM Instances (GCP) y Azure Virtual Machines—. Para la gestión local de
contenedores, herramientas como Docker Desktop, Docker CLI y Docker Compose permiten
desarrollar, gestionar y desplegar contenedores en entornos de desarrollo.

### Recopilación de comandos

|                          Comando                          |                                                                      Uso/función                                                                       |
| :-------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------: |
|                      `docker images`                      |                                          Devuelve un listado de todas las imágenes descargadas en la máquina.                                          |
|                `docker pull nombre_imagen`                |                                       Descarga una imagen de Docker desde [Docker Hub](https://hub.docker.com/).                                       |
|            `docker image rm nombre_imagen:tag`            |                                                             Elimina una imagen de Docker.                                                              |
|               `docker create nombre_imagen`               |                                   Crea un contenedor a partir de una imagen y devuelve el ID del contenedor creado.                                    |
|  `docker create --name nombre_contenedor nombre_imagen`   |                                          Crea un contenedor con un nombre específico a partir de una imagen.                                           |
|               `docker start ID_contenedor`                |                                                          Inicia un contenedor mediante su ID.                                                          |
|             `docker start nombre_contenedor`              |                                                        Inicia un contenedor mediante su nombre.                                                        |
|                        `docker ps`                        |                                  Muestra los contenedores activos con información sobre ID, imagen, estado y nombre.                                   |
|                      `docker ps -a`                       |                                             Muestra todos los contenedores, tanto activos como detenidos.                                              |
|              `docker stop nombre_contenedor`              |                                                        Detiene un contenedor usando su nombre.                                                         |
|                `docker stop ID_contenedor`                |                                                          Detiene un contenedor usando su ID.                                                           |
|               `docker rm nombre_contenedor`               |                                                            Elimina un contenedor de Docker.                                                            |
| `docker run -d -p 8080:80 -i --name Debian debian:latest` | Crea y ejecuta un contenedor mapeando puertos. `-d`: Segundo plano. `-p`: Mapeo de puertos. `-i`: Acceso al terminal. `--name`: Nombre del contenedor. |
|         `docker exec -it nombre_contenedor bash`          |                                               Accede al terminal del contenedor para interactuar con él.                                               |
|  `docker cp ruta_host nombre_contenedor:ruta_contenedor`  |                                                         Copia archivos del host al contenedor.                                                         |
|             `docker stats nombre_contenedor`              |                                          Monitorea el uso de CPU, memoria y ancho de banda de un contenedor.                                           |
|                      `docker stats`                       |                                          Monitorea el uso de recursos de todos los contenedores en ejecución.                                          |
|                    `docker network ls`                    |                                                    Muestra todas las redes configuradas en Docker.                                                     |
|            `docker network inspect nombre_red`            |                            Obtiene detalles sobre una red específica, incluyendo direcciones IP y contenedores conectados.                             |
|            `docker network create nombre_red`             |                                                              Crea una red personalizada.                                                               |
|              `docker network rm nombre_red`               |                                                                    Elimina una red.                                                                    |
|           `docker volume create nombre_volumen`           |                                                                    Crea un volumen.                                                                    |
|                    `docker volume ls`                     |                                                               Lista todos los volúmenes.                                                               |
|             `docker volume rm nombre_volumen`             |                                                                  Elimina un volumen.                                                                   |
|            `docker inspect nombre_contenedor`             |                                                           Muestra detalles de un contenedor.                                                           |
|              `docker logs nombre_contenedor`              |                                                         Muestra los registros del contenedor.                                                          |
|            `docker logs -f nombre_contenedor`             |                                                Muestra los registros del contenedor de manera continua.                                                |
|         `docker tag nombre_imagen nueva_etiqueta`         |                                                                  Etiqueta una imagen.                                                                  |
|                      `docker login`                       |                                                             Inicia sesión en un registry.                                                              |
|                `docker push nombre_imagen`                |                                                             Sube una imagen a Docker Hub.                                                              |
|                      `docker logout`                      |                                                             Cierra sesión en un registry.                                                              |
|                `docker system prune --all`                |                                        Elimina todos los contenedores detenidos e imágenes que no estén en uso.                                        |
|                   `docker volume prune`                   |                                                    Elimina todos los volúmenes que no estén en uso.                                                    |
|                  `docker network prune`                   |                             Elimina todas las redes que no estén en uso, excepto las predeterminadas (bridge, none, host).                             |
|    `docker update [OPTIONS] CONTAINER [CONTAINER...]`     |         Actualiza la configuración de uno o varios contenedores. [Documentación](https://docs.docker.com/engine/reference/commandline/update/)         |
|    `docker run --cpu-shares=512 -m 256m nombre_imagen`    |                                           Especifica recursos de sistema (CPU, memoria) para un contenedor.                                            |
|               `docker stop $(docker ps -q)`               |                                                      Detiene todos los contenedores en ejecución.                                                      |
|             `docker start $(docker ps -a -q)`             |                                                             Inicia todos los contenedores.                                                             |
|              `docker rm $(docker ps -a -q)`               |                                                            Elimina todos los contenedores.                                                             |

### Acceso a contenedores mediante mapeo de puertos

El mapeo de puertos, o _port mapping_, asigna un puerto específico del host al puerto de
un contenedor, lo que permite que una aplicación dentro del contenedor sea accesible
desde el host o desde otros contenedores. Por ejemplo, el siguiente comando crea un
contenedor de MongoDB y mapea el puerto 27017 del host al puerto 27017 del contenedor:

```bash linenums="1"
docker container create -p 27017:27017 --name mongodb mongo
```

En este comando, `-p` mapea un puerto del host al puerto del contenedor, `mongodb` es el
nombre del contenedor y `mongo` es la imagen utilizada.

### Crear e iniciar un contenedor con Docker Run

El comando `docker run` combina los comandos `docker create` y `docker start`, realizando
los siguientes pasos: busca la imagen especificada (si no está disponible localmente, la
descarga del repositorio), crea un contenedor a partir de la imagen e inicia el
contenedor. El siguiente ejemplo ejecuta un contenedor de MongoDB en segundo plano
mapeando el puerto 27017:

```bash linenums="1"
docker run -d -p 27017:27017 --name mongodb mongo
```

### Variables de entorno en contenedores

Para conectar una base de datos con una aplicación dentro de Docker, se utilizan
variables de entorno específicas para la imagen del contenedor. Por ejemplo, para crear
un contenedor de MongoDB con credenciales de administrador:

```bash linenums="1"
docker create -e MONGO_INITDB_ROOT_USERNAME=<usuario> -e MONGO_INITDB_ROOT_PASSWORD=<contraseña> mongo
```

Estas variables configuran el usuario y la contraseña del administrador de la base de
datos durante la inicialización del contenedor. Es importante revisar la documentación de
cada imagen, ya que las variables de entorno varían según la imagen utilizada.

### Construcción de imágenes mediante Dockerfile

Un `Dockerfile` es un archivo de texto con instrucciones que permiten construir una
imagen Docker personalizada. Cada imagen se construye sobre una imagen previa, que puede
ser oficial de Docker o una personalizada. A continuación se muestra un ejemplo de
`Dockerfile`:

```dockerfile
# Imagen base
FROM node:18

# Crear un directorio para el código
RUN mkdir -p /home/app

# Copia los archivos del host al contenedor
COPY . /home/app

# Exponer el puerto de la aplicación
EXPOSE 3000

# Ejecutar la aplicación
CMD ["node", "/home/app/index.js"]
```

Para construir una imagen a partir de un `Dockerfile` se utiliza el siguiente comando:

```bash linenums="1"
docker build -t nombre-imagen:etiqueta ruta/dockerfile
```

Para permitir la comunicación entre contenedores, es necesario configurar una red
interna. Docker permite crear redes personalizadas con
`docker network create mi-nueva-red`, y los contenedores en la misma red pueden
comunicarse entre sí usando su nombre como dominio. Para crear un contenedor en una red
específica:

```bash linenums="1"
docker create -p 27017:27017 --name mongodb --network mi-nueva-red mongo
```

Docker ofrece diferentes modos de red: el modo _bridge_, que es el predeterminado y donde
la red es reconocible solo dentro del host y el contenedor, y las redes personalizadas,
que permiten especificar el rango de direcciones IP y otros parámetros.

### Definición y gestión de múltiples contenedores mediante Docker Compose

Docker Compose es una herramienta que permite definir y gestionar múltiples contenedores
como un conjunto de servicios interconectados. Utiliza un archivo de configuración
`docker-compose.yml` en formato YAML para especificar la configuración de los servicios,
redes, volúmenes y otros aspectos relacionados con los contenedores, simplificando la
gestión de aplicaciones complejas compuestas por varios contenedores.

A continuación se muestra un ejemplo de `docker-compose.yml`:

```yaml
version: "3.9"

services:
  mi-app:
    build: .
    ports:
      - "3000:3000"
    links:
      - mongodb

  mongodb:
    image: mongo
    ports:
      - "27017:27017"
    environment:
      - MONGO_INITDB_ROOT_USERNAME=<usuario>
      - MONGO_INITDB_ROOT_PASSWORD=<contraseña>
```

En este archivo se definen dos servicios: uno para la aplicación (`mi-app`), que se
construye a partir del contexto del directorio actual y mapea el puerto 3000, y otro para
MongoDB (`mongodb`), que utiliza una imagen preexistente, mapea el puerto 27017 y
establece las credenciales de acceso mediante variables de entorno.

Para iniciar los servicios definidos en el archivo se ejecuta `docker compose up`, que
descarga las imágenes necesarias, crea los contenedores y los pone en funcionamiento.
Para detener y eliminar los servicios, incluidos los contenedores, redes y volúmenes
asociados, se utiliza `docker compose down`. Otros comandos útiles son
`docker-compose scale servicio=num_instancias` para escalar servicios y
`docker-compose logs servicio` para ver los registros.

### Creación de volúmenes para la persistencia de datos

En Docker, los volúmenes permiten la persistencia de datos en los contenedores. Esto
significa que, incluso si un contenedor se elimina, los datos asociados a los volúmenes
permanecen disponibles, lo cual resulta especialmente útil cuando se desea mantener
información a través de reinicios o actualizaciones de contenedores.

Los volúmenes pueden ser de diferentes tipos: los volúmenes anónimos, que son volúmenes
sin nombre y no pueden referenciarse explícitamente desde otros contenedores; los
volúmenes de host, que permiten especificar qué carpeta del sistema anfitrión se monta
dentro del contenedor; y los volúmenes nombrados, que disponen de un nombre y pueden
referenciarse en otros contenedores o en múltiples servicios.

El siguiente ejemplo muestra un `docker-compose.yml` con volúmenes:

```yaml
version: "3.9"

services:
  mi-app:
    build: .
    ports:
      - "3000:3000"
    links:
      - mongodb

  mongodb:
    image: mongo
    ports:
      - "27017:27017"
    environment:
      - MONGO_INITDB_ROOT_USERNAME=<usuario>
      - MONGO_INITDB_ROOT_PASSWORD=<contraseña>
    volumes:
      - mongo-data:/data/db

volumes:
  mongo-data:
```

En este ejemplo, el servicio `mongodb` utiliza un volumen nombrado llamado `mongo-data`
para almacenar los datos persistentes de la base de datos. Este volumen se monta en el
directorio `/data/db` del contenedor, lo que asegura que los datos de MongoDB se
conserven incluso si el contenedor es detenido o eliminado. Docker se encarga de
gestionar la creación y almacenamiento de dicho volumen de forma completamente
automatizada.

## Kubernetes

<p align="center">
  <img src="/assets/img/docs/logos/kubernetes-logo.png" width="500"/>
  <br />
  <em>Logo de Kubernetes</em>
</p>

La adopción de Kubernetes se motiva principalmente por la necesidad de administrar de
manera eficiente y escalable múltiples contenedores de Docker distribuidos en diversos
servidores. Kubernetes facilita la orquestación de estos contenedores a través de una
infraestructura declarativa, en la que los usuarios definen la configuración deseada en
un manifiesto —un archivo de configuración— que se procesa mediante la API de Kubernetes.
La plataforma asume la responsabilidad de distribuir la carga de trabajo entre los nodos
disponibles y de administrar los recursos requeridos por los contenedores.

Kubernetes también posibilita la construcción de _pipelines_ ETL utilizando herramientas
como Spark o Airflow, y se emplea extensamente en el entrenamiento de modelos de
aprendizaje automático, como se evidencia en su uso en Kubeflow. Al gestionar la
infraestructura de cómputo, redes y almacenamiento, Kubernetes simplifica la
implementación y administración de aplicaciones en contenedores a gran escala.

### Componentes de Kubernetes

**Kubectl** es una interfaz de línea de comandos que facilita la interacción con un
clúster de Kubernetes, permitiendo la gestión de objetos como pods, servicios y
despliegues.

Para la creación de un clúster de Kubernetes en un entorno local, se utiliza
**Minikube**. Esta herramienta permite la ejecución de Kubernetes de manera local para
fines de prueba o desarrollo, creando un clúster con uno o varios nodos virtualizados.
Por defecto, Minikube crea un clúster que contiene un nodo. Para inicializar el clúster
se utiliza el comando `minikube start`, y para verificar su estado, `minikube status`.

### Nodos

Un nodo representa la unidad más pequeña dentro de un clúster de Kubernetes. Puede ser
una máquina física o una máquina virtual donde se ejecutan las aplicaciones. Kubernetes
abstrae el hardware subyacente, permitiendo una gestión eficiente de los requisitos de
recursos. Si un nodo no puede proporcionar más recursos o falla, Kubernetes redistribuye
las cargas de trabajo a otros nodos disponibles. Existen diferentes tipos de nodos: los
nodos bajo demanda (_On-Demand Nodes_), que se crean cuando los recursos requeridos son
elevados (CPU, GPU, RAM), y los nodos al mejor precio (_Spot Nodes_), que son más
económicos pero pueden ser retirados en cualquier momento.

### Pods

Un pod es la unidad mínima de ejecución en Kubernetes y puede contener uno o más
contenedores que comparten los mismos recursos y red local. Todos los contenedores dentro
del mismo pod pueden comunicarse entre sí y comparten el mismo entorno de red. Al escalar
un pod, todos los contenedores dentro de él se escalan conjuntamente.

### Clúster

Un clúster es un conjunto de nodos, también conocidos como _workers_, que se ejecutan en
Kubernetes. La relación entre las aplicaciones que se ejecutan en cada nodo es
independiente. Por ejemplo, si se dispone de un servidor de Proxmox con dos máquinas
virtuales, VM1 y VM2, a pesar de que cuenten con diferentes pods, si todos están
gestionados por Kubernetes, ambos formarán parte del mismo clúster.

### StatefulSet y volúmenes

Dado que no se puede garantizar el lugar de ejecución de una aplicación, el uso del disco
local para almacenar datos resulta inviable, siendo útil únicamente para almacenamiento
temporal como caché. Kubernetes emplea volúmenes persistentes que, a diferencia de otros
recursos como la CPU, GPU y RAM gestionados por los clústeres, deben adjuntarse al propio
clúster desde unidades locales o en la nube. Estos volúmenes no se asocian a un nodo en
particular.

**StatefulSet** permite la creación de pods con volúmenes persistentes, garantizando la
integridad de los datos incluso si el pod se reinicia o se elimina. A continuación se
muestra un ejemplo:

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: my-csi-app-set
spec:
  selector:
    matchLabels:
      app: my-frontend
  serviceName: "my-frontend"
  replicas: 1
  template:
    metadata:
      labels:
        app: my-frontend
    spec:
      containers:
        - name: my-frontend
          image: busybox
          args:
            - sleep
            - infinity
          volumeMounts:
            - name: data
              mountPath: "/data"
  volumeClaimTemplates:
    - metadata:
        name: csi-pvc
      spec:
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 1Gi
```

Para verificar el estado de los volúmenes y los StatefulSets se utilizan los comandos
`kubectl get pvc` (para ver la asignación del volumen, capacidad, etc.) y
`kubectl get sts` (para ver los StatefulSets).

### Manifiestos

Un manifiesto es un archivo en formato YAML o JSON que especifica cómo desplegar una
aplicación en un clúster de Kubernetes. Este archivo se conoce como un registro de
intención, donde se le indica a Kubernetes el estado deseado del clúster.

Un concepto importante asociado es el de _namespace_, que constituye la división lógica
del clúster de Kubernetes y permite separar la carga del clúster. Se pueden crear
políticas para separar tráfico entre _namespaces_, aunque por defecto los datos de un
_namespace_ son visibles desde otro. Para obtener los _namespaces_ del clúster se utiliza
`kubectl get ns`, para obtener los pods de un _namespace_ específico se emplea
`kubectl -n nombre_namespace get pods -o wide` (la opción `-o wide` proporciona
información adicional como la IP del pod y el nodo), y para eliminar un pod se usa
`kubectl -n nombre_namespace delete pod nombre_pod`.

A continuación se muestra un ejemplo de manifiesto para crear un pod simple:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
    - name: nginx
      image: nginx:alpine
```

Para aplicar el manifiesto se ejecuta `kubectl apply -f nombre.yaml`, y para ver el
estado del pod, `kubectl get pods`.

El siguiente ejemplo muestra un manifiesto más complejo que incluye variables de entorno,
solicitudes y límites de recursos, así como _readiness probe_ y _liveness probe_:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
    - name: nginx
      image: nginx:alpine
      env:
        - name: MI_VARIABLE
          value: "valor_ejemplo"
        - name: MI_OTRA_VARIABLE
          value: "otro_valor"
        - name: DD_AGENT_HOST
          valueFrom:
            fieldRef:
              fieldPath: status.hostIP
      resources:
        requests:
          memory: "64Mi"
          cpu: "200m"
        limits:
          memory: "128Mi"
          cpu: "500m"
      readinessProbe:
        httpGet:
          path: /
          port: 80
        initialDelaySeconds: 5
        periodSeconds: 10
      livenessProbe:
        tcpSocket:
          port: 80
        initialDelaySeconds: 15
        periodSeconds: 20
      ports:
        - containerPort: 80
```

En este manifiesto, la sección `resources.requests` define los recursos garantizados que
la instancia debe tener disponibles para poder realizar el despliegue, medidos en
milicores para CPU (donde 1000 milicores equivalen a 1 core). La sección
`resources.limits` establece el límite máximo de recursos que el pod puede consumir; si
se excede, el kernel de Linux finaliza el proceso y el pod se reinicia. La _readiness
probe_ indica a Kubernetes que el pod está listo para recibir tráfico, mientras que la
_liveness probe_ confirma que el pod sigue activo y no debe ser eliminado.

### Despliegue y gestión de réplicas

Un despliegue (_Deployment_) permite declarar el número de réplicas de pods y asegurar
que el estado deseado se mantenga, monitorizándolos de forma continua:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:alpine
          ports:
            - containerPort: 80
```

### DaemonSet

Un DaemonSet es una forma de despliegue que garantiza que un pod se ejecute en todos los
nodos del clúster, con exactamente un pod por nodo. No se especifica el número de
réplicas, ya que depende del número de nodos. Se utiliza habitualmente para servicios de
monitoreo:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: nginx-daemonset
spec:
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:alpine
```

### Exponer aplicaciones

#### Tipos de servicios

Los servicios en Kubernetes permiten acceder a los pods desde dentro y fuera del clúster.
Existen varios tipos de servicios según las necesidades de exposición.

**ClusterIP** proporciona una dirección IP virtual única a nivel de clúster, facilitando
la comunicación y el balanceo de carga entre pods de forma interna.

**NodePort** crea un puerto en cada nodo que recibe el tráfico y lo redirige a los pods
correspondientes, permitiendo que la aplicación sea accesible desde fuera del clúster.
Suele utilizar puertos dentro del rango 30000-32767:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mi-servicio
spec:
  type: NodePort
  selector:
    app: mi-aplicacion
  ports:
    - port: 80
      targetPort: 9376
      nodePort: 30007
```

**LoadBalancer** está orientado a proveedores de la nube y crea un balanceador de carga
que proporciona una IP estable para el servidor, facilitando su acceso desde internet:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mi-servicio
spec:
  type: LoadBalancer
  selector:
    app: mi-aplicacion
  ports:
    - port: 80
      targetPort: 80
```

#### Ingress

Ingress administra el acceso externo a los servicios del clúster, típicamente HTTP.
Proporciona balanceo de carga y terminación SSL, y permite el acceso al servicio mediante
_paths_. Suele requerirse un controlador Ingress-Nginx que se instala por separado.

### Networking y almacenamiento

Cada pod en Kubernetes tiene su propia dirección IP, y para comunicar pods en diferentes
nodos se utiliza el _Cloud Cluster Networking Interface_. En cuanto al almacenamiento,
**etcd** es un almacén de datos clave-valor distribuido utilizado para guardar datos de
configuración, estado y metadatos del clúster.
