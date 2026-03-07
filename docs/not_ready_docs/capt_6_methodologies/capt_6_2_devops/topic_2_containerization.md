---

authors:
Daniel Bazo Correa
description: Herramientas necesarias para DevOps.
title: Docker
---

## Bibliografía

- [Aprende Docker ahora! Curso completo gratis desde cero](https://youtu.be/4Dko5W96WHg?si=pOAHHRxpPkqpQ2go)
- [Docker Docs](https://docs.docker.com/)
- [DevOps con Docker, Jenkins, Kubernetes, Git, GitFlow CI y CD](https://www.udemy.com/course/devops-con-dockers-kubernetes-jenkins-y-gitflow-cicd/)

## Introducción

<p align="center">
  <img src="/assets/img/docs/logos/docker-logo.png" width="500"/>
  <br />
  <em>Logo de Docker</em>
</p>

**Docker** es una plataforma de código abierto que facilita la creación, implementación y
ejecución de aplicaciones mediante contenedores. Los contenedores permiten empaquetar una
aplicación junto con sus dependencias y configuraciones en una unidad estandarizada, lo
que simplifica el desarrollo de software y garantiza consistencia entre entornos.

### Características principales

- **Portabilidad**: Los contenedores Docker se ejecutan en cualquier sistema que soporte
  Docker, independientemente del sistema operativo.
- **Ligereza**: Los contenedores comparten el kernel del sistema operativo del host, lo
  que los hace más ligeros y rápidos de iniciar.
- **Consistencia**: Docker asegura que una aplicación se ejecute de la misma manera en
  cualquier entorno.
- **Aislamiento**: Cada contenedor opera de manera independiente, mejorando la seguridad
  y evitando conflictos entre aplicaciones.
- **Escalabilidad**: Docker facilita la creación y eliminación rápida de instancias de
  aplicaciones.

### Diferencia entre un contenedor y una máquina virtual

Los contenedores y las máquinas virtuales son tecnologías de virtualización que permiten
ejecutar múltiples aplicaciones en un solo servidor físico. Aunque comparten objetivos
similares, como optimizar el uso de recursos y asegurar aislamiento, difieren en su
implementación y arquitectura subyacente.

#### Contenedores

<p align="center">
  <img src="https://profile.es/wp-content/media/image-1-1024x266.png"/>
  <br />
  <em>Pasos para la creación de un contenedor Docker</em>
</p>

Los **contenedores** son una forma de virtualización a nivel del sistema operativo,
también conocidos como "virtualización ligera". A diferencia de las máquinas virtuales,
que virtualizan un sistema operativo completo, los contenedores comparten el núcleo del
sistema operativo del host y ejecutan aplicaciones dentro de espacios de usuario
completamente aislados. Esto permite ejecutar múltiples contenedores simultáneamente,
minimizando la interferencia entre ellos.

Cada contenedor contiene solo la aplicación y sus dependencias, como bibliotecas,
archivos de configuración y variables de entorno, lo que lo hace extremadamente
**portátil** y fácil de desplegar en diferentes entornos, desde la máquina local de un
desarrollador hasta un clúster en la nube.

##### Características de los contenedores

- **Imágenes y contenedores**:
  - **Imágenes**: Paquetes inmutables que contienen la aplicación y sus dependencias
    necesarias para ejecutarla. Las imágenes son reutilizables y se almacenan en
    repositorios como [**Docker Hub**](https://hub.docker.com/).
  - **Contenedores**: Instancias en ejecución de imágenes, que pueden crearse, detenerse
    y eliminarse rápidamente.

- **Aislamiento**:
  - Utiliza tecnologías del kernel de Linux para aislar procesos, sistemas de archivos,
    redes, etc., proporcionando un entorno independiente para cada contenedor.
  - Los **namespaces** (espacios de nombres) aíslan recursos del sistema operativo:
    - `pid`: Aísla los identificadores de procesos.
    - `net`: Proporciona pilas de red separadas.
    - `mnt`: Aisla los puntos de montaje del sistema de archivos.
    - `ipc`: Aísla recursos de comunicación entre procesos.
    - `uts`: Aísla nombres de host y dominios.
    - `user`: Aísla identificadores de usuarios y grupos.
  - Los **cgroups** (grupos de control) gestionan el uso de recursos como CPU, memoria y
    disco, garantizando que los contenedores no consuman más recursos de los asignados.
- **Union Filesystem (UFS)**: Permite que los contenedores se construyan en capas. Las
  capas de solo lectura contienen archivos del sistema, mientras que las capas de
  escritura se mantienen en la parte superior, minimizando el uso de almacenamiento y
  facilitando el desarrollo iterativo.

- **Ligereza**: Los contenedores no incluyen un sistema operativo completo; se ejecutan
  como procesos dentro del sistema operativo del host, lo que los hace mucho más ligeros
  que las máquinas virtuales.

##### Casos de uso de los contenedores

Los contenedores son ideales para:

- **Desarrollo y pruebas**: Permiten a los desarrolladores trabajar en un entorno que
  replica exactamente el de producción.
- **Microservicios**: Separan aplicaciones en componentes pequeños y desplegables, que
  pueden escalarse de forma independiente.
- **Despliegue continuo**: Facilitan el ciclo CI/CD al permitir que las aplicaciones se
  empaqueten y desplieguen uniformemente.

#### Máquinas virtuales

**Las máquinas virtuales (VMs)** son una tecnología de virtualización más tradicional que
permite ejecutar múltiples sistemas operativos en un servidor físico mediante un
hipervisor, como **VMware** o **VirtualBox**.

##### Características de las máquinas virtuales

- **Hipervisor**: Un hipervisor puede ejecutarse directamente en el hardware del servidor
  (tipo 1) o sobre un sistema operativo (tipo 2). Este gestiona la creación y ejecución
  de múltiples VMs, asignando recursos de hardware eficientemente.
- **Sistema operativo completo**: Cada VM tiene su propio sistema operativo completo (por
  ejemplo, Linux, Windows), lo que significa que las VMs consumen más recursos de CPU,
  memoria y almacenamiento que los contenedores.
- **Aislamiento fuerte**: Debido a que cada VM tiene su propio kernel y sistema
  operativo, proporciona un aislamiento más fuerte que los contenedores. Esto es útil
  cuando la seguridad es crítica.
- **Rendimiento y uso de recursos**: Las VMs son más pesadas y tienen tiempos de inicio
  más largos en comparación con los contenedores, ya que requieren más recursos debido a
  la necesidad de un sistema operativo completo y un hipervisor.

##### Casos de uso de las máquinas virtuales

Las máquinas virtuales son adecuadas para:

- **Aplicaciones monolíticas**: Donde el aislamiento del sistema operativo completo es
  necesario.
- **Entornos con múltiples sistemas operativos**: Permiten ejecutar varios sistemas
  operativos en un solo servidor.
- **Cargas de trabajo heredadas**: Donde las aplicaciones antiguas o monolíticas deben
  ejecutarse en un entorno virtualizado.

#### Soluciones en la nube

En la nube, proveedores como **Google Cloud Platform (GCP)**, **Amazon Web Services
(AWS)** y **Microsoft Azure** ofrecen servicios de contenedores y máquinas virtuales:

- **AWS ECS/Fargate, EKS**, **Azure Kubernetes Service (AKS)** y **Google Kubernetes
  Engine (GKE)**: Herramientas para gestionar contenedores a gran escala.
- **EC2 (AWS), VM Instances (GCP), Azure Virtual Machines**: Soluciones para desplegar y
  gestionar máquinas virtuales.

#### Herramientas de gestión de contenedores

**Docker Desktop**, **Docker CLI** y **Docker Compose** son herramientas ampliamente
usadas para desarrollar, gestionar y desplegar contenedores en entornos de desarrollo
locales. Permiten a los desarrolladores crear aplicaciones de manera rápida, probarlas y
asegurarse de que se comportarán de la misma manera en producción.

### Recopilación de comandos

|                                   Comando                                   |                                                                                                                                                                                                                                                                           Uso/función                                                                                                                                                                                                                                                                           |
| :-------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                              **docker images**                              |                                                                                                                                                                                                                                              Devuelve un listado de todas las imágenes descargadas en la máquina.                                                                                                                                                                                                                                               |
|                        **docker pull nombre_imagen**                        |                                                                                                                                                                                                                    Descargar una imagen de Docker (puedes visitar [Docker Hub](https://hub.docker.com/) para explorar imágenes disponibles).                                                                                                                                                                                                                    |
|                    **docker image rm nombre_imagen:tag**                    |                                                                                                                                                                                                                                                                 Eliminar una imagen de Docker.                                                                                                                                                                                                                                                                  |
|                       **docker create nombre_imagen**                       |                                                                                                                                                                                                                                        Crear un contenedor a partir de una imagen, devuelve el ID del contenedor creado.                                                                                                                                                                                                                                        |
|          **docker create --name nombre_contenedor nombre_imagen**           |                                                                                                                                                                                                                                              Crear un contenedor con un nombre específico a partir de una imagen.                                                                                                                                                                                                                                               |
|                    **docker start ID_contenedor_creado**                    |                                                                                                                                                                                                                                                                     Iniciar un contenedor.                                                                                                                                                                                                                                                                      |
|                     **docker start nombre_contenedor**                      |                                                                                                                                                                                                                                                           Iniciar un contenedor utilizando su nombre.                                                                                                                                                                                                                                                           |
|                                **docker ps**                                |                                                                                                                                                                                                      Mostrar solo los contenedores activos. Devuelve una tabla con información sobre cada contenedor, incluyendo el ID, la imagen, el estado y el nombre.                                                                                                                                                                                                       |
|                              **docker ps -a**                               |                                                                                                                                                                                                                                                Ver todos los contenedores (activos y no activos) en tu máquina.                                                                                                                                                                                                                                                 |
|                      **docker stop nombre_contenedor**                      |                                                                                                                                                                                                                                                             Detener un contenedor usando su nombre.                                                                                                                                                                                                                                                             |
|                        **docker stop ID_contenedor**                        |                                                                                                                                                                                                                                                               Detener un contenedor usando su ID.                                                                                                                                                                                                                                                               |
|                       **docker rm nombre_contenedor**                       |                                                                                                                                                                                                                                                                Eliminar un contenedor de Docker.                                                                                                                                                                                                                                                                |
|         **docker run -d -p 8080:80 -i --name Debian debian:latest**         | Crear un contenedor para alojar un servicio y publicarlo en un puerto del host para que sea accesible. <br /> - **Debian**: Nombre del contenedor <br /> - **debian:latest**: Imagen del contenedor <br /> - **8080**: Puerto del host <br /> - **80**: Puerto del contenedor <br /> - **-d**: Ejecuta el contenedor en segundo plano y devuelve el ID del contenedor <br /> - **-p**: Mapea un puerto del host con un puerto del contenedor <br /> - **-i**: Mantiene el acceso al terminal del contenedor <br /> - **--name**: Asigna un nombre al contenedor |
|                 **docker exec -it nombre_contenedor bash**                  |                                                                                                                                                                                                                                                   Accede al terminal del contenedor para interactuar con él.                                                                                                                                                                                                                                                    |
| **docker cp ruta_archivos_host nombre_contenedor:ruta_archivos_contenedor** |                                                                                                                                                                                                                                                             Copia archivos del host al contenedor.                                                                                                                                                                                                                                                              |
|                     **docker stats nombre_contenedor**                      |                                                                                                                                                                                                                                        Monitorea el uso de CPU, memoria y ancho de banda de un contenedor en ejecución.                                                                                                                                                                                                                                         |
|                            **docker network ls**                            |                                                                                                                                                                                                                                                         Muestra todas las redes configuradas en Docker.                                                                                                                                                                                                                                                         |
|                    **docker network inspect nombre_red**                    |                                                                                                                                                                                                              Obtiene detalles sobre una red específica, como las direcciones IP de los contenedores conectados y qué contenedores están en la red.                                                                                                                                                                                                              |
|            **docker update [OPTIONS] CONTAINER [CONTAINER...]**             |                                                                                                                                                                                                      Actualiza la configuración de uno o varios contenedores. [Documentación Docker Update](https://docs.docker.com/engine/reference/commandline/update/)                                                                                                                                                                                                       |

### Acceso a contenedores mediante mapeo de puertos

El mapeo de puertos, o _port mapping_, asigna un puerto específico del host al puerto de
un contenedor, lo que permite que una aplicación dentro del contenedor sea accesible
desde el host o desde otros contenedores.

Por ejemplo, el siguiente comando crea un contenedor de MongoDB y mapea el puerto 27017
del host al puerto 27017 del contenedor:

```bash linenums="1"
docker container create -p 27017:27017 --name mongodb mongo
```

En este comando:

- `-p`: Mapea un puerto del host al puerto del contenedor.
- `mongodb`: Nombre del contenedor.
- `mongo`: Imagen del contenedor utilizada.

Docker proporciona comandos para capturar los logs de los contenedores:

- `docker logs nombre_contenedor`: Muestra los registros del contenedor.
- `docker logs -f nombre_contenedor`: Muestra los registros del contenedor de manera
  continua.

### Crear e iniciar un contenedor con Docker Run

El comando `docker run` combina los comandos `docker create` y `docker start` y realiza
los siguientes pasos:

1. Busca la imagen especificada; si no está disponible localmente, la descarga del
   repositorio.
2. Crea un contenedor a partir de la imagen.
3. Inicia el contenedor.

Ejemplo de comando para ejecutar un contenedor de MongoDB en segundo plano (utilizando
`-d`), mapeando el puerto 27017 del host al contenedor:

```bash linenums="1"
docker run -d -p 27017:27017 --name mongodb mongo
```

### Variables de entorno en contenedores

Para conectar una base de datos con una aplicación dentro de Docker, se utilizan
variables de entorno específicas para la imagen del contenedor.

Por ejemplo, para crear un contenedor de MongoDB con un nombre de usuario y una
contraseña:

```bash linenums="1"
docker create -e MONGO_INITDB_ROOT_USERNAME=dani -e MONGO_INITDB_ROOT_PASSWORD=clave mongo
```

Estas variables configuran el usuario y la contraseña del administrador de la base de
datos durante la inicialización del contenedor. Es importante revisar la documentación de
la imagen del contenedor, ya que las variables de entorno varían según cada imagen.

### Construcción de imágenes mediante Dockerfile

Un `Dockerfile` es un archivo de texto con instrucciones que te permiten construir una
imagen Docker. La imagen construida a partir de un `Dockerfile` puede ser usada para
crear contenedores personalizados. Cada imagen se construye sobre una imagen previa, que
puede ser oficial de Docker o una personalizada.

Ejemplo de un `Dockerfile`:

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

Para permitir la comunicación entre contenedores, es necesario configurar una red
interna. Docker proporciona comandos para gestionar estas redes:

- `docker network ls`: Muestra todas las redes configuradas en Docker.
- `docker network create mi-nueva-red`: Crea una red personalizada.

Los contenedores en la misma red pueden comunicarse entre sí usando su nombre como
dominio.

Para construir una imagen a partir de un `Dockerfile`:

```bash linenums="1"
docker build -t nombre-imagen:etiqueta ruta/dockerfile
```

Y para crear un contenedor en una red específica:

```bash linenums="1"
docker create -p 27017:27017 --name mongodb --network mi-nueva-red mongo
```

Modos de red en Docker:

- **Modo bridge**: Modo predeterminado; la red es reconocible solo dentro del host y el
  contenedor.
- **Red personalizada**: Permite especificar el rango de direcciones IP y otros
  parámetros.

### Definición y gestión de múltiples contenedores mediante Docker Compose

Docker Compose es una herramienta que permite definir y gestionar múltiples contenedores
como un conjunto de servicios interconectados. Utiliza un archivo de configuración
`docker-compose.yml` en formato YAML para especificar la configuración de los servicios,
redes, volúmenes y otros aspectos relacionados con los contenedores. Esto simplifica la
gestión de aplicaciones complejas compuestas por varios contenedores.

Ejemplo de `docker-compose.yml`:

```yaml
# Define la versión del archivo de configuración de Docker Compose
version: "3.9"

# Define los servicios que se van a utilizar en esta configuración
services:
  # Servicio para la aplicación
  mi-app:
    # Especifica el contexto de construcción, en este caso el directorio actual
    build: .

    # Mapea el puerto 3000 del contenedor al puerto 3000 del host
    ports:
      - "3000:3000"

    # Define los enlaces de red entre los servicios
    links:
      # Establece un enlace con el servicio 'mongodb'
      - mongodb

  # Servicio para la base de datos MongoDB
  mongodb:
    # Usa la imagen oficial de MongoDB
    image: mongo

    # Mapea el puerto 27017 del contenedor al puerto 27017 del host
    ports:
      - "27017:27017"

    # Configura las variables de entorno para la inicialización de la base de datos
    environment:
      # Define el nombre de usuario raíz para MongoDB
      - MONGO_INITDB_ROOT_USERNAME=dani

      # Define la contraseña para el usuario raíz de MongoDB
      - MONGO_INITDB_ROOT_PASSWORD=clave
```

Con este archivo de configuración, se definen dos servicios: uno para la aplicación
(`mi-app`) y otro para MongoDB (`mongodb`). La aplicación se construye a partir del
contexto del directorio actual, mapeando el puerto 3000 del contenedor al puerto 3000 del
host. El servicio MongoDB utiliza una imagen preexistente (`mongo`), mapea el puerto
27017 y establece las credenciales de acceso mediante variables de entorno.

Para iniciar los servicios definidos en el archivo `docker-compose.yml`, basta con
ejecutar:

```bash linenums="1"
docker compose up
```

Este comando descarga las imágenes necesarias (si no están disponibles localmente), crea
los contenedores y los pone en funcionamiento.

Para detener y eliminar los servicios, incluidos los contenedores, redes y volúmenes
asociados, se utiliza:

```bash linenums="1"
docker compose down
```

### Creación de volúmenes para la persistencia de datos

En Docker, los volúmenes permiten la persistencia de datos en los contenedores. Esto
significa que, incluso si un contenedor se elimina, los datos asociados a los volúmenes
permanecen disponibles. Esto es especialmente útil cuando se quiere mantener información
a través de reinicios o actualizaciones de contenedores.

Los volúmenes pueden ser de diferentes tipos:

1. **Volúmenes anónimos**: Son volúmenes sin nombre, lo que impide referenciarlos
   explícitamente desde otros contenedores.
2. **Volúmenes de host**: Permiten especificar qué carpeta del sistema anfitrión se monta
   dentro del contenedor.
3. **Volúmenes nombrados**: Son volúmenes con nombre, lo que permite referenciarlos en
   otros contenedores o en múltiples servicios.

Ejemplo de `docker-compose.yml` con volúmenes:

```yaml
# Define la versión del archivo de configuración de Docker Compose
version: "3.9"

# Define los servicios que se van a utilizar en esta configuración
services:
  # Servicio para la aplicación
  mi-app:
    # Especifica el contexto de construcción, en este caso el directorio actual
    build: .

    # Mapea el puerto 3000 del contenedor al puerto 3000 del host
    ports:
      - "3000:3000"

    # Define los enlaces de red entre los servicios
    links:
      # Establece un enlace con el servicio 'mongodb'
      - mongodb

  # Servicio para la base de datos MongoDB
  mongodb:
    # Usa la imagen oficial de MongoDB
    image: mongo

    # Mapea el puerto 27017 del contenedor al puerto 27017 del host
    ports:
      - "27017:27017"

    # Configura las variables de entorno para la inicialización de la base de datos
    environment:
      # Define el nombre de usuario raíz para MongoDB
      - MONGO_INITDB_ROOT_USERNAME=dani

      # Define la contraseña para el usuario raíz de MongoDB
      - MONGO_INITDB_ROOT_PASSWORD=clave

    # Monta un volumen para persistir los datos de MongoDB
    volumes:
      # Asocia el volumen 'mongo-data' al directorio '/data/db' en el contenedor
      - mongo-data:/data/db

# Define los volúmenes que se van a utilizar en esta configuración
volumes:
  # Declara un volumen llamado 'mongo-data' para almacenar datos persistentes
  mongo-data:
```

En este ejemplo, el servicio `mongodb` utiliza un volumen nombrado llamado `mongo-data`
para almacenar los datos persistentes de la base de datos. Este volumen se monta en el
directorio `/data/db` del contenedor, lo que asegura que los datos de MongoDB se
conserven incluso si el contenedor es detenido o eliminado.

Al final del archivo `docker-compose.yml`, se declara el volumen `mongo-data` en la
sección `volumes`. De este modo, Docker se encarga de gestionar la creación y
almacenamiento de dicho volumen.

Con este archivo de configuración, el proceso de persistencia de datos es completamente
automatizado, lo que garantiza la disponibilidad continua de los datos en situaciones de
reinicio o actualización de los servicios.

## Bibliografía

- [Minikube Docs](https://minikube.sigs.k8s.io/docs/)
- [Kubernetes Tutorials](https://youtube.com/playlist?list=PLiMWaCMwGJXnHmccp2xlBENZ1xr4FpjXF&si=mxLcHpXxnZUhSGu3)
- [Kubernetes: De novato a pro! (Curso completo en español)](https://youtu.be/DCoBcpOA7W4?si=KioSNJrOkZp-Dx5K)

### Introducción

<p align="center">
  <img src="/assets/img/docs/logos/kubernetes-logo.png" width="500"/>
  <br />
  <em>Logo de Kubernetes</em>
</p>

La adopción de Kubernetes se motiva principalmente por la necesidad de administrar de
manera eficiente y escalable múltiples contenedores de Docker distribuidos en diversos
servidores. Kubernetes facilita la orquestación de estos contenedores a través de una
infraestructura declarativa. En este enfoque, los usuarios definen la configuración
deseada en un manifiesto, es decir, un archivo de configuración, que se procesa mediante
la API de Kubernetes. Kubernetes asume la responsabilidad de distribuir la carga de
trabajo entre los nodos disponibles y de administrar los recursos requeridos por los
contenedores.

Kubernetes también posibilita la construcción de pipelines ETL utilizando herramientas
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
Por defecto, Minikube crea un clúster que contiene un nodo.

Para inicializar el clúster de Minikube podemos utilizar el comando:

```bash linenums="1"
minikube start
```

Mientras que para verificar el estado del clúster, podemos utilizar el comando:

```bash linenums="1"
minikube status
```

#### Nodo

Un nodo representa la unidad más pequeña dentro de un clúster de Kubernetes. Este puede
ser una máquina física o una máquina virtual donde se ejecutan las aplicaciones.
Kubernetes abstrae el hardware subyacente, permitiendo una gestión eficiente de los
requisitos de recursos. Si un nodo no puede proporcionar más recursos o falla, Kubernetes
redistribuye las cargas de trabajo a otros nodos disponibles.

Existen diferentes tipos de nodos:

- **Nodos bajo demanda (On-Demand Nodes)**: Se crean cuando los recursos son elevados
  (CPU, GPU, RAM).
- **Nodos al mejor precio (Spot Nodes)**: Son nodos más económicos que pueden ser
  retirados en cualquier momento.

#### Pod

Un pod es la unidad mínima de ejecución en Kubernetes y puede contener uno o más
contenedores que comparten los mismos recursos y red local. Todos los contenedores dentro
del mismo pod pueden comunicarse entre sí y comparten el mismo entorno de red. Al escalar
un pod, todos los contenedores dentro de él se escalan conjuntamente.

#### Clúster

Un clúster es un conjunto de nodos, también conocidos como workers, que se ejecutan en
Kubernetes. La relación entre las aplicaciones que se están ejecutando en cada nodo es
independiente. Por ejemplo, si se tiene un servidor de Proxmox donde existen dos máquinas
virtuales, VM1 y VM2, a pesar de que cuenten con diferentes Pods, si todos están
gestionados por Kubernetes, ambos formarán parte del mismo clúster.

### StatefulSet y volúmenes

Dado que no se puede garantizar el lugar de ejecución de una aplicación, el uso del disco
local para almacenar datos es inviable, siendo útil únicamente para almacenamiento
temporal de datos, como caché.

Kubernetes emplea volúmenes persistentes, que a diferencia de otros recursos como la CPU,
GPU y RAM, que son gestionados por los clústeres de Kubernetes, deben ser adjuntados al
propio clúster de Kubernetes desde unidades locales o en la nube. Estos volúmenes no se
asocian a un nodo en particular.

**StatefulSet** permite la creación de pods con volúmenes persistentes, garantizando la
integridad de los datos incluso si el pod se reinicia o se elimina.

```yaml
# Versión de la API de Kubernetes que se está utilizando
apiVersion: apps/v1

# Tipo de recurso que se está creando
kind: StatefulSet

metadata:
  # Nombre del StatefulSet
  name: my-csi-app-set

spec:
  selector:
    matchLabels:
      # Etiqueta que debe coincidir para que un pod sea considerado parte
      # de este StatefulSet
      app: my-frontend

  # Nombre del servicio que se utilizará para este StatefulSet
  serviceName: "my-frontend"

  # Número de réplicas del pod que se mantendrán en ejecución
  replicas: 1

  # Plantilla que define los pods que se crearán
  template:
    metadata:
      labels:
        # Etiquetas para los pods que se crearán
        app: my-frontend

    spec:
      containers: # Lista de contenedores que se ejecutarán en cada pod
      my-frontend # Nombre del contenedor
          image: busybox # Imagen del contenedor que se utilizará
          args:
            - sleep
            - infinity # Argumentos que se pasarán al contenedor
          volumeMounts: # Puntos de montaje de los volúmenes en el contenedor
          data # Nombre del volumen
              mountPath: "/data" # Ruta en la que se montará el volumen

  # Plantillas para las solicitudes de volumen persistente
  volumeClaimTemplates:
    - metadata:
        # Nombre de la solicitud de volumen persistente
        name: csi-pvc

      spec:
        # Modos de acceso para el volumen
        accessModes: ["ReadWriteOnce"]

        resources:
          requests:
            # Cantidad de almacenamiento solicitado
            storage: 1Gi
```

Para verificar el estado de los volúmenes y los StatefulSets, se pueden utilizar los
siguientes comandos:

```bash linenums="1"
kubectl get pvc  # Para ver la asignación del volumen, capacidad, etc.
kubectl get sts  # Para ver los StatefulSets.
```

### Manifiestos

Un manifiesto es un archivo en formato YAML o JSON que especifica cómo desplegar una
aplicación en un clúster de Kubernetes. Este archivo se conoce como un registro de
intención, donde se le indica a Kubernetes el estado deseado del clúster.

Además, es importante definir lo que es un namespace, que es la división lógica del
clúster de Kubernetes, permitiendo separar la carga del clúster. Se pueden crear
políticas para separar tráfico entre namespaces. Por defecto, los datos de un namespace
se pueden ver desde otro namespace.

Para obtener el namespace del clúster podemos utilizar el comando:

```bash linenums="1"
kubectl get ns
```

Para obtener los pods de ese namespace podemos utilizar el siguiente comando, que al
añadir al final -o wide, obtenemos información de la IP del pod, nodo, etc.

```bash linenums="1"
kubectl -n nombre_namespace get pods -o wide
```

Para eliminar un pod del namespace podemos utilizar el comando

```bash linenums="1"
kubectl -n nombre_namespace delete pod nombre_pod
```

Ejemplo de manifiesto para crear un Pod simple:

```yaml
# Versión de la API del recurso de Kubernetes, está asociado al tipo
# por lo que hay que mirar la documentación.
apiVersion: v1

# Tipo del manifiesto.
kind: Pod

# Nombre del Pod.
metadata:
  name: nginx

# Contenedores que se ejecutan dentro de este pod. Todos los contenedores
# que se ejecutan dentro de un Pod, tienen la misma IP.
spec:
  containers:
  nginx
      image: nginx:alpine
```

Para aplicar el manifiesto:

```bash linenums="1"
kubectl apply -f nombre.yaml  # Aplica el manifiesto en el namespace por defecto
kubectl get pods  # Ver el estado del pod
```

Ejemplo de manifiesto para crear un Pod más complejo:

El siguiente manifiesto contiene variables de entorno, así como solicitudes y límites de
recursos, además de readiness probe y liveness probe.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  nginx
      image: nginx:alpine
      env:
        # Variables de entorno, al igual que en Docker. Esto es específico
        # de cada contenedor.
      MI_VARIABLE
          value: "pelado"
      MI_OTRA_VARIABLE
          value: "pelade"
      DD_AGENT_HOST
          valueFrom:
            fieldRef:
              # Obtener la IP del Host a partir de la API de Kubernetes.
              fieldPath: status.hostIP
      resources:
        # Recursos garantizados siempre. La instancia debe tener esto, sino
        # no puede hacer el despliegue.
        requests:
          memory: "64Mi"
          # Medida en milicores, donde 1000 milicores es 1 core de CPU.
          cpu: "200m"
        # Límite que puede alcanzar el Pod, si usa más recursos, el kernel de
        # Linux mata el proceso y el pod se reinicia.
        limits:
          memory: "128Mi"
          cpu: "500m"
      # Manera de decirle a Kubernetes que el Pod está listo para recibir
      # tráfico
      readinessProbe:
        httpGet:
          path: /
          port: 80
        initialDelaySeconds: 5
        periodSeconds: 10
      # Manera de decirle a Kubernetes que el Pod está vivo y que no lo mate
      livenessProbe:
        tcpSocket:
          port: 80
        initialDelaySeconds: 15
        periodSeconds: 20
      # Exponer el puerto 80 para nginx.
      ports:
        - containerPort: 80
```

### Despliegue y gestión de réplicas

Un despliegue permite declarar el número de réplicas, es decir, el número de Pods, y
asegurar que el estado deseado se mantenga, monitorizándolos.

```yaml
# Versión de la API del recurso de Kubernetes, está asociado al tipo
# por lo que hay que mirar la documentación.
apiVersion: apps/v1

# Tipo del manifiesto.
kind: Deployment

# Nombre del Despliegue.
metadata:
  name: nginx-deployment

spec:
  # Número de réplicas del pod que se mantendrán en ejecución.
  replicas: 3

  # Etiqueta que debe coincidir para que un pod sea considerado parte de este Despliegue.
  selector:
    matchLabels:
      app: nginx

  # Plantilla que define los pods que se crearán.
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      nginx
          image: nginx:alpine
          ports:
            - containerPort: 80
```

### DaemonSet

Un DaemonSet es una forma de hacer un despliegue de un Pod, pero este Pod va a estar en
todos los nodos del clúster. Un solo Pod en cada nodo. No se especifica por tanto el
número de réplicas, porque depende del número de nodos. Se suele utilizar mucho para
servicios de monitoreo.

```yaml
# Versión de la API del recurso de Kubernetes, está asociado al tipo
# por lo que hay que mirar la documentación.
apiVersion: apps/v1

# Tipo del manifiesto.
kind: DaemonSet

# Nombre del DaemonSet.
metadata:
  name: nginx-daemonset

spec:
  # Etiqueta que debe coincidir para que un pod sea considerado parte de este DaemonSet.
  selector:
    matchLabels:
      app: nginx

  # Plantilla que define los pods que se crearán.
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      nginx
          image: nginx:alpine
```

### Exponer aplicaciones

#### Servicios en Kubernetes

Los servicios en Kubernetes permiten acceder a los pods desde dentro y fuera del clúster.
Un ejemplo de esto es el uso de un Load Balancer:

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
    - protocol: TCP
      port: 80
      targetPort: 9376
```

#### Ingress

Ingress administra el acceso externo a los servicios del clúster, típicamente HTTP.
Proporciona balanceo de carga y terminación SSL. Permite el acceso al servicio mediante
paths, y suele requerirse Ingress-Nginx controller que se suele instalar por separado.

### Networking y almacenamiento

#### Pod Networking

Cada pod tiene su propia IP, y para comunicar pods en diferentes nodos se utiliza el
Cloud Cluster Networking Interface.

#### Almacenamiento persistente

**etcd** es un almacén de datos clave-valor distribuido utilizado para guardar datos de
configuración, estado y metadatos.

### Tipos de servicios

#### Cluster IP

Cluster IP proporciona una forma de exponer aplicaciones que se ejecutan en un conjunto
de Pods a través de una dirección IP virtual única a nivel de clúster, facilitando la
comunicación y balanceo de carga entre Pods.

#### Node Port

Node Port crea un puerto en cada nodo que va a recibir el tráfico y lo va a mandar a los
servicios (Pods) necesarios²⁶. Esto permite que la aplicación sea accesible desde fuera
del clúster. Suele utilizar puertos dentro del rango 30000-32767.

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

#### Load Balancer

Load Balancer está más enfocado a proveedores de la nube para redireccionar el tráfico en
los Pods. Crea un balanceador de carga proporcionando una IP estable para el servidor, lo
que facilita su acceso desde internet.

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




## **Docker**
### Trabajando con imágenes del container registry

- **Descargar una imagen desde Docker Hub:**
```shell 
#docker pull nombre_de_la_imagen
docker run -d -p 80:80 docker/getting-started
```
- **Listar imágenes locales:**
```shell 
docker image ls
```
- **Crear y ejecutar un contenedor a partir de una imagen:**
```shell 
#docker run [opciones] nombre_del_contenedor nombre_de_la_imagen
docker run -p 80:80 -p 7080:7080 --name containerBilling sotobotero/billingapp
```
- **crear un contenedor de postgres y una base de datos en el mismo comando:**
```shell
docker run --ulimit memlock=-1:-1 -d --name postgres -e POSTGRES_USER=sa -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=product_db -p 5432:5432 postgres:13.3
```
- **Listar contenedores en ejecución:**
```shell 
docker ps
```
- **Listar todos los contenedores (incluso los detenidos):**
```shell 
docker ps -a
```
- **Detener todos los contenedores:**
```shell 
docker stop $(docker ps -q)
```
- **Iniciar todos los contenedores:**
```shell 
docker start $(docker ps -a -q)
```
- **Eliminar todos los contenedores:**
```shell 
docker rm $(docker ps -a -q)
```
### Construyendo Imágenes

- **Construir una imagen desde un Dockerfile:**
 ```shell
 #docker build -t nombre_de_la_imagen [opciones y parametros] .
 docker build -t billingapp --no-cache --build-arg JAR_FILE=target/*.jar .
```
- **Construir una imagen con un contexto específico:**
 ```shell
  docker build -t nombre_de_la_imagen -f ruta/Dockerfile .
```
### Comandos Avanzados para Imágenes

- **Etiquetar una imagen:**
 ```shell
 docker tag nombre_de_la_imagen nueva_etiqueta
```
- **Loguears en un registry:**
 ```shell
docker login # te pedirá usuario y contraseña
 ```
- **Subir una imagen a Docker Hub:**
 ```shell
  docker push nombre_de_la_imagen
```
- **Descargar una imagen con una etiqueta específica:**
 ```shell
  docker pull nombre_de_la_imagen:etiqueta
```
- **Desloguearse de un registry:**
 ```shell
docker logout
 ```
### Comandos para la Gestión Básica de Contenedores

- **Detener un contenedor en ejecución:**
```shell 
docker stop nombre_del_contenedor
```

- **Iniciar un contenedor detenido:**
```shell 
docker start nombre_del_contenedor
```
- **Eliminar un contenedor:**
```shell 
docker rm nombre_del_contenedor
```
- **Eliminar una imagen local:**
```shell
docker image rm nombre_de_la_imagen
```
### Trabajando con Redes y Volúmenes

- **Crear una red personalizada:**
 ```shell 
 docker network create nombre_de_la_red
```
- **Listar redes:**
 ```shell
 docker network ls
```
- **Crear un volumen:**
 ```shell
 docker volume create nombre_del_volumen
```
- **Listar volúmenes:**
 ```shell
 docker volume ls
```
### Interactuando con Contenedores

- **Ejecutar un comando en un contenedor en ejecución:**
 ```shell
 #docker exec -it nombre_del_contenedor comando
docker exec -it localbillingApp sh
```
- **Copiar archivos entre el host y un contenedor:**
 ```shell
  docker cp archivo.txt nombre_del_contenedor:/ruta/destino
  ```
### Docker Compose

- **Iniciar contenedores definidos en un archivo `docker-compose.yml`:**
 ```shell
  docker-compose up
```
- **Escalar servicios en Docker Compose:**
 ```shell
  docker-compose scale servicio=num_instancias
```
- **Detener y eliminar contenedores definidos en Docker Compose:**
 ```shell
  docker-compose down
```
- **Ver logs de servicios en Docker Compose:**
 ```shell
  docker-compose logs servicio
```
### Administración de Redes y Volúmenes

- **Eliminar una red:**
 ```shell
  docker network rm nombre_de_la_red
```
- **Eliminar un volumen:**
 ```shell
  docker volume rm nombre_del_volumen
```
- **Inspeccionar una red:**
 ```shell
 docker network inspect nombre_de_la_red
```
### Comandos para Información y Estadísticas

- **Ver detalles de un contenedor:**
 ```shell
  docker inspect nombre_del_contenedor
```
- **Obtener estadísticas de uso de recursos de un contenedor:**
 ```shell
  docker stats nombre_del_contenedor
```
- **Obtener estadísticas de uso de recursos de todos los contenedores:**
 ```shell
  docker stats
```
### Comandos para Seguridad y Control de Acceso

- **Crear un perfil de control de acceso (se requiere Docker EE):**
 ```shell
  docker trust key generate nombre_de_perfil
```
- **Especificar qué usuarios o equipos pueden o no usar Docker:**
 ```shell
  docker trust key load --alias nombre_de_perfil.pem --pem --root /etc/docker/pki/tls/private
```

- **Inhabilitar Docker para usuarios no autorizados (se requiere Docker EE):**
 ```shell
  docker trust signer remove nombre_de_perfil
```
### Comandos para Configuraciones Avanzadas

- **Crear un contenedor con un archivo de configuración personalizada:**
 ```shell
  docker run -v ruta/local:/ruta/contenedor -e variable_de_entorno=valor nombre_de_la_imagen
```
- **Especificar recursos de sistema para un contenedor (CPU, memoria, etc.):**
 ```shell
 docker run --cpu-shares=512 -m 256m nombre_de_la_imagen
```
- **Elimina todos los contenedores detenidos e imagenes que no esten en uso**
 ```shell
docker system prune --all
 ```
 - **Elimina todos los volumenes que no esten en uso**
 ```shell
docker volume prune
 ```
 - **Elimina todas las redes que no esten en uso, menos las por defecto (bridge, none,host)**
 ```shell
docker network prune
 ```
