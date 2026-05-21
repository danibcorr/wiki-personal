---
authors: Daniel Bazo Correa
description: Herramientas necesarias para DevOps.
title: Contenedores
---

## Bibliografía

- [Aprende Docker ahora! Curso completo gratis desde cero](https://youtu.be/4Dko5W96WHg?si=pOAHHRxpPkqpQ2go)
- [Docker Docs](https://docs.docker.com/)
- [DevOps con Docker, Jenkins, Kubernetes, Git, GitFlow CI y CD](https://www.udemy.com/course/devops-con-dockers-kubernetes-jenkins-y-gitflow-cicd/)
- [Minikube Docs](https://minikube.sigs.k8s.io/docs/)
- [Kubernetes Tutorials](https://youtube.com/playlist?list=PLiMWaCMwGJXnHmccp2xlBENZ1xr4FpjXF&si=mxLcHpXxnZUhSGu3)
- [Kubernetes: De novato a pro! (Curso completo en español)](https://youtu.be/DCoBcpOA7W4?si=KioSNJrOkZp-Dx5K)

## Docker

<figure markdown="span">
  ![Logo de Docker](../../assets/img/docs/logos/docker-logo.png){ width="500" }
  <figcaption>Logo de Docker</figcaption>
</figure>

Docker es una plataforma de código abierto que facilita la creación, implementación y
ejecución de aplicaciones mediante contenedores. Un contenedor empaqueta una aplicación
junto con todas sus dependencias y configuraciones en una unidad estandarizada, lo que
simplifica el desarrollo de _software_ y garantiza la consistencia entre distintos
entornos. Cabe mencionar que también existen alternativas de código abierto como Podman,
que están ganando relevancia debido a los últimos cambios de licencia y uso de Docker en
entornos empresariales.

<figure markdown="span">
  ![Sistema basado en Microservicios](https://media.geeksforgeeks.org/wp-content/uploads/20240715174859/Microservices-with-Docker-Containers.webp)
  <figcaption>Sistema basado en Microservicios</figcaption>
</figure>

Este tipo de arquitectura se basa en el concepto de **microservicios**, ya que permite
empaquetar cada servicio de forma independiente con sus propias dependencias, evitando
así conflictos entre ellas. La comunicación entre contenedores, es decir, entre cada
microservicio, se realiza habitualmente mediante APIs.

Entre sus características principales destacan la **portabilidad**, puesto que los
contenedores se ejecutan en cualquier sistema que soporte Docker independientemente del
sistema operativo del _host_. También destaca la **ligereza**, dado que comparten el
_kernel_ del sistema operativo del _host_, lo que los hace más rápidos de iniciar que
las máquinas virtuales. La **consistencia** asegura que una aplicación se ejecute de la
misma manera en cualquier entorno. El **aislamiento** garantiza que cada contenedor
opera de manera independiente, mejorando la seguridad y evitando conflictos entre
aplicaciones. Por último, la **escalabilidad** facilita la creación y eliminación rápida
de instancias.

### Contenedores frente a máquinas virtuales

Los contenedores y las máquinas virtuales son tecnologías de virtualización que permiten
ejecutar múltiples aplicaciones en un solo servidor físico, lo que se conoce como
_host_. Aunque comparten objetivos similares, como optimizar el uso de recursos y
asegurar el aislamiento, difieren significativamente en su implementación y arquitectura
subyacente.

<figure markdown="span">
  ![Pasos para la creación de un contenedor en Docker](https://profile.es/wp-content/media/image-1-1024x266.png)
  <figcaption>Pasos para la creación de un contenedor en Docker</figcaption>
</figure>

Los contenedores constituyen una forma de virtualización a nivel del sistema operativo,
también conocida como virtualización ligera. A diferencia de las máquinas virtuales, que
virtualizan un sistema operativo completo, los contenedores comparten el núcleo
(_kernel_) del sistema operativo del _host_ y ejecutan aplicaciones dentro de espacios
de usuario completamente aislados.

Cada contenedor contiene únicamente la aplicación y sus dependencias (bibliotecas,
archivos de configuración y variables de entorno), lo que lo hace extremadamente
portátil y fácil de desplegar en diferentes entornos, desde la máquina local de un
desarrollador hasta un clúster en la nube.

El aislamiento de los contenedores se logra mediante diferentes técnicas. Los
_namespaces_ (espacios de nombres) aíslan recursos del sistema operativo: `pid` aísla
los identificadores de procesos, `net` proporciona pilas de red separadas, `mnt` aísla
los puntos de montaje del sistema de archivos, `ipc` aísla recursos de comunicación
entre procesos, `uts` aísla nombres de _host_ y dominios, y `user` aísla identificadores
de usuarios y grupos.

Por otra parte, los _cgroups_ (grupos de control) gestionan el uso de recursos como CPU,
memoria y disco, garantizando que los contenedores no consuman más recursos de los
asignados. Además, el _Union Filesystem_ (UFS) permite que los contenedores se
construyan en capas. Las capas de solo lectura contienen archivos del sistema, mientras
que las capas de escritura se mantienen en la parte superior, minimizando el uso de
almacenamiento y facilitando el desarrollo iterativo.

Las máquinas virtuales, por su parte, representan una tecnología de virtualización más
tradicional que permite ejecutar múltiples sistemas operativos en un servidor físico
mediante un hipervisor, como VMware o VirtualBox. Un hipervisor puede ejecutarse
directamente en el _hardware_ del servidor (virtualización tipo 1) o sobre un sistema
operativo (virtualización tipo 2), gestionando la creación y ejecución de múltiples
máquinas virtuales y asignando recursos de _hardware_ de forma eficiente. Cada máquina
virtual dispone de su propio sistema operativo completo, lo que proporciona un
aislamiento más fuerte que los contenedores, pero a costa de un mayor consumo de CPU,
memoria y almacenamiento, así como tiempos de inicio más prolongados.

Los contenedores resultan ideales para desarrollo y pruebas, arquitecturas de
microservicios y despliegue continuo (por ejemplo, en herramientas de CI/CD que ofrecen
GitLab, GitHub o similares), mientras que las máquinas virtuales son más adecuadas para
aplicaciones monolíticas que requieren aislamiento completo del sistema operativo,
entornos con múltiples sistemas operativos y cargas de trabajo heredadas.

En la nube, proveedores como Amazon Web Services (AWS), Google Cloud Platform (GCP) y
Microsoft Azure ofrecen servicios tanto de contenedores (AWS ECS/Fargate, EKS, Azure
Kubernetes Service (AKS) y Google Kubernetes Engine (GKE)) como de máquinas virtuales
(EC2 en AWS, VM _Instances_ en GCP y Azure Virtual Machines). Para la gestión local de
contenedores, herramientas como Docker Desktop o Docker CLI permiten desarrollar,
gestionar y desplegar contenedores.

### Arquitectura de Docker Engine

Docker Engine se compone de tres elementos fundamentales. El primero es **Docker CLI**,
una interfaz de línea de comandos que puede ejecutarse incluso en una máquina remota. El
segundo es la **REST API**, que actúa como canal de comunicación entre el CLI y el
_daemon_. El tercero es el **Docker Daemon**, que gestiona imágenes, contenedores, redes
y volúmenes. El CLI puede comunicarse con un _daemon_ remoto a través de la REST API, lo
que permite gestionar contenedores en servidores remotos de forma transparente.

!!! info

    Un ***daemon*** es un tipo de programa que se ejecuta en segundo plano, en lugar de bajo
    el control directo de un usuario. Son procesos autónomos que inician durante el
    arranque del sistema y gestionan tareas recurrentes como servicios de red, impresión
    o sincronización.

Hay que tener en cuenta que los contenedores **comparten el _kernel_ del _host_**. Si el
_host_ tiene un _kernel_ Linux, no se pueden ejecutar contenedores Windows de forma
nativa, y viceversa. Sin embargo, al instalar Docker en Windows, se crea una instancia
de Linux mediante WSL sobre la que Docker ejecuta los contenedores.

### _Tags_ e imágenes

Las imágenes utilizan **_tags_** para identificar variantes según el sistema operativo
base (Alpine, Debian, Ubuntu), la versión del paquete y otros criterios. Si no se
especifica un _tag_, Docker utiliza `latest` por defecto, lo cual **no se considera
buena práctica**, ya que no se tiene control sobre las versiones utilizadas y podrían
aparecer nuevos problemas no contemplados previamente. Por ello, se recomienda fijar
siempre la versión y actualizarla de forma controlada, por ejemplo, ante problemas de
seguridad.

Las propias imágenes públicas en Docker Hub suelen disponer de un sistema de alertas que
notifica cuando una imagen se ve comprometida o se detecta algún tipo de fallo o mejora
relevante en el servicio al que corresponde.

???+ example "Ejemplo"

    ```bash linenums="1"
    # Especificar versión con tag
    docker run redis:4.0
    ```

    Los *tags* soportados se consultan en la documentación de cada imagen en Docker Hub.

### Recopilación de comandos

A continuación se muestra una tabla que recopila los comandos más utilizados para la
gestión de contenedores con Docker:

|                          Comando                          |                                                                                   Uso/función                                                                                   |
| :-------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                      `docker images`                      |                                                      Devuelve un listado de todas las imágenes descargadas en la máquina.                                                       |
|                `docker pull nombre_imagen`                |                                                   Descarga una imagen de Docker desde [Docker Hub](https://hub.docker.com/).                                                    |
|            `docker image rm nombre_imagen:tag`            |                                                                          Elimina una imagen de Docker.                                                                          |
|               `docker create nombre_imagen`               |                                                Crea un contenedor a partir de una imagen y devuelve el ID del contenedor creado.                                                |
|  `docker create --name nombre_contenedor nombre_imagen`   |                                                       Crea un contenedor con un nombre específico a partir de una imagen.                                                       |
|               `docker start ID_contenedor`                |                                                                      Inicia un contenedor mediante su ID.                                                                       |
|             `docker start nombre_contenedor`              |                                                                    Inicia un contenedor mediante su nombre.                                                                     |
|                        `docker ps`                        |                                               Muestra los contenedores activos con información sobre ID, imagen, estado y nombre.                                               |
|                      `docker ps -a`                       |                                                          Muestra todos los contenedores, tanto activos como detenidos.                                                          |
|              `docker stop nombre_contenedor`              |                                                                     Detiene un contenedor usando su nombre.                                                                     |
|                `docker stop ID_contenedor`                |                                                                       Detiene un contenedor usando su ID.                                                                       |
|               `docker rm nombre_contenedor`               |                                                                        Elimina un contenedor de Docker.                                                                         |
| `docker run -d -p 8080:80 -i --name Debian debian:latest` | Crea y ejecuta un contenedor mapeando puertos. `-d`: Ejecuta el contenedor en segundo plano. `-p`: Mapeo de puertos. `-i`: Acceso al terminal. `--name`: Nombre del contenedor. |
|         `docker exec -it nombre_contenedor bash`          |                                  Ejecuta un comando en el contenedor, en este caso, accede al terminal del contenedor para interactuar con él.                                  |
|  `docker cp ruta_host nombre_contenedor:ruta_contenedor`  |                                                                    Copia archivos del _host_ al contenedor.                                                                     |
|             `docker stats nombre_contenedor`              |                                                       Monitorea el uso de CPU, memoria y ancho de banda de un contenedor.                                                       |
|                      `docker stats`                       |                                                      Monitorea el uso de recursos de todos los contenedores en ejecución.                                                       |
|                    `docker network ls`                    |                                                                 Muestra todas las redes configuradas en Docker.                                                                 |
|            `docker network inspect nombre_red`            |                                         Obtiene detalles sobre una red específica, incluyendo direcciones IP y contenedores conectados.                                         |
|            `docker network create nombre_red`             |                                                                           Crea una red personalizada.                                                                           |
|              `docker network rm nombre_red`               |                                                                                Elimina una red.                                                                                 |
|           `docker volume create nombre_volumen`           |                                                                                Crea un volumen.                                                                                 |
|                    `docker volume ls`                     |                                                                           Lista todos los volúmenes.                                                                            |
|             `docker volume rm nombre_volumen`             |                                                                               Elimina un volumen.                                                                               |
|            `docker inspect nombre_contenedor`             |                                                                       Muestra detalles de un contenedor.                                                                        |
|              `docker logs nombre_contenedor`              |                                                                      Muestra los registros del contenedor.                                                                      |
|            `docker logs -f nombre_contenedor`             |                                                            Muestra los registros del contenedor de manera continua.                                                             |
|         `docker tag nombre_imagen nueva_etiqueta`         |                                                                              Etiqueta una imagen.                                                                               |
|                      `docker login`                       |                                                                         Inicia sesión en un _registry_.                                                                         |
|                `docker push nombre_imagen`                |                                                                          Sube una imagen a Docker Hub.                                                                          |
|                      `docker logout`                      |                                                                         Cierra sesión en un _registry_.                                                                         |
|                `docker system prune --all`                |                                                    Elimina todos los contenedores detenidos e imágenes que no estén en uso.                                                     |
|                   `docker volume prune`                   |                                                                Elimina todos los volúmenes que no estén en uso.                                                                 |
|                  `docker network prune`                   |                                      Elimina todas las redes que no estén en uso, excepto las predeterminadas (_bridge_, _none_, _host_).                                       |
|    `docker update [OPTIONS] CONTAINER [CONTAINER...]`     |                     Actualiza la configuración de uno o varios contenedores. [Documentación](https://docs.docker.com/engine/reference/commandline/update/)                      |
|    `docker run --cpu-shares=512 -m 256m nombre_imagen`    |                                                        Especifica recursos de sistema (CPU, memoria) para un contenedor.                                                        |
|               `docker stop $(docker ps -q)`               |                                                                  Detiene todos los contenedores en ejecución.                                                                   |
|             `docker start $(docker ps -a -q)`             |                                                                         Inicia todos los contenedores.                                                                          |
|              `docker rm $(docker ps -a -q)`               |                                                                         Elimina todos los contenedores.                                                                         |

### Modo interactivo y _attach_/_detach_

Es importante tener en cuenta que un contenedor **no es un sistema operativo completo**,
sino que está pensado para alojar servicios y aplicaciones. Si se ejecuta una imagen
como Ubuntu sin ningún proceso activo, el contenedor se detiene inmediatamente al no
tener ninguna tarea que mantener.

Los contenedores de Docker no leen la entrada estándar (_stdin_) de forma
predeterminada. Para interactuar con un contenedor se utilizan las opciones `-i` (modo
interactivo, que mapea _stdin_) y `-t` (que crea un pseudoterminal).

???+ example "Ejemplo"

    ```bash linenums="1"
    # Modo interactivo con pseudoterminal
    docker run -it <imagen> bash

    # Ejemplo: acceder al bash de una imagen con uv preinstalado
    docker run -it ghcr.io/astral-sh/uv:debian bash
    ```

Cuando se ejecuta un contenedor sin la opción `-d`, el terminal queda en modo _attach_
(primer plano). Para ejecutar en segundo plano se utiliza `-d` (modo _detached_). Si se
desea volver al primer plano de un contenedor que se encuentra en segundo plano debemos
utilizar el comando `attach` junto con el ID del contenedor.

???+ example "Ejemplo"

    ```bash linenums="1"
    # Obtener el ID del contenedor
    docker ps

    # Volver al primer plano
    docker attach <id>
    ```

### Acceso a contenedores mediante mapeo de puertos

<figure markdown="span">
  ![Mapeo de puertos](https://cdn.hashnode.com/res/hashnode/image/upload/v1691510841387/a2a15178-1cb1-4fc3-8c38-9c5e5da38c40.png)
  <figcaption>Mapeo de puertos</figcaption>
</figure>

El mapeo de puertos, o _port mapping_, asigna un puerto específico del _host_ al puerto
de un contenedor, lo que permite que una aplicación dentro del contenedor sea accesible
desde el _host_ o desde otros contenedores.

???+ example "Ejemplo"

    El siguiente comando crea un contenedor de MongoDB y mapea el puerto 27017 del *host* al puerto 27017 del contenedor:

    ```bash linenums="1"
    docker container create -p 27017:27017 --name mongodb mongo
    ```

    En este comando, `-p` mapea un puerto del *host* al puerto del contenedor, `mongodb` es el nombre del contenedor y `mongo` es la imagen utilizada.

### Crear e iniciar un contenedor

El comando `docker run` combina los comandos `docker create` y `docker start`,
realizando los siguientes pasos:

1. Busca la imagen especificada. Si no está disponible localmente, la descarga del
   repositorio.
2. Crea un contenedor a partir de la imagen e inicia el contenedor.

???+ example "Ejemplo"

    El siguiente ejemplo ejecuta un contenedor de MongoDB en segundo plano mapeando el puerto 27017:

    ```bash linenums="1"
    docker run -d -p 27017:27017 --name mongodb mongo
    ```

### Variables de entorno

Para conectar una base de datos con una aplicación dentro de Docker, se utilizan
variables de entorno específicas para la imagen del contenedor.

???+ example "Ejemplo"

    El siguiente ejemplo crea un contenedor de MongoDB con credenciales de administrador:

    ```bash linenums="1"
    docker create -e MONGO_INITDB_ROOT_USERNAME=<usuario> -e MONGO_INITDB_ROOT_PASSWORD=<contraseña> mongo
    ```

Estas variables configuran el usuario y la contraseña del administrador de la base de
datos durante la inicialización del contenedor. Es importante revisar la documentación
de cada imagen, ya que las variables de entorno varían según la imagen utilizada.

### _Dockerfile_

Un `Dockerfile` es un archivo de texto con instrucciones que permiten construir una
imagen Docker personalizada. Cada imagen se construye sobre una imagen previa, que puede
ser oficial de Docker o una personalizada.

???+ example "Ejemplo"

    ```dockerfile linenums="1"
    # Imagen base
    FROM node:18

    # Crear un directorio para el código
    RUN mkdir -p /home/app

    # Copiar los archivos del host al contenedor
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

#### ENTRYPOINT y CMD

`ENTRYPOINT` define el comando base del contenedor, mientras que `CMD` proporciona
argumentos por defecto que pueden sobreescribirse al ejecutar el contenedor.

???+ example "Ejemplo"

    Teniendo el siguiente `Dockerfile`:

    ```dockerfile linenums="1"
    FROM ubuntu
    ENTRYPOINT ["sleep"]
    CMD ["5"]
    ```

    Podemos utilizar el siguiente comando para hacer un sleep de 5 segundos, que es el
    valor por defecto definido en la imagen:

    ```bash linenums="1"
    docker run <imagen>
    ```

    O podemos modificar el valor:

    ```bash linenums="1"
    docker run <imagen> 10
    ```

### Redes en Docker

Para permitir la comunicación entre contenedores, es necesario configurar una red
interna. Docker permite crear redes personalizadas con el comando
`docker network create mi-nueva-red`, y los contenedores que pertenecen a la misma red
pueden comunicarse entre sí utilizando su nombre como dominio. Para crear un contenedor
en una red específica podemos utilizar el siguiente comando:

```bash linenums="1"
docker create -p 27017:27017 --name mongodb --network mi-nueva-red mongo
```

Docker ofrece diferentes modos de red:

|     Tipo     | Descripción                                                                                                                                                        |
| :----------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **_bridge_** | Red por defecto. Docker asigna IPs internas a cada contenedor. Los contenedores pueden comunicarse entre sí y se accede desde el _host_ mediante mapeo de puertos. |
|  **_host_**  | El contenedor usa directamente la red del _host_, sin aislamiento de red.                                                                                          |
|  **_none_**  | Sin conectividad de red, completamente aislado.                                                                                                                    |

Además, se pueden crear **redes personalizadas** que permiten especificar el rango de
direcciones IP y otros parámetros. En lugar de usar `--link` (considerado _legacy_), se
recomienda crear redes definidas por el usuario, que proporcionan **resolución de
nombres interna** (los contenedores se referencian por nombre en lugar de por IP) y
conectividad automática entre todos los contenedores de la misma red.

### Docker Compose

Docker Compose es una herramienta que permite definir y gestionar múltiples contenedores
como un conjunto de servicios interconectados. Utiliza un archivo de configuración
`docker-compose.yml` en formato YAML para especificar la configuración de los servicios,
redes, volúmenes y otros aspectos relacionados con los contenedores, simplificando la
gestión de aplicaciones complejas compuestas por varios contenedores.

???+ example "Ejemplo"

    En este ejemplo se definen dos servicios: uno para la aplicación (`mi-app`), que se
    construye a partir del contexto del directorio actual y mapea el puerto 3000, y otro
    para MongoDB (`mongodb`), que utiliza una imagen preexistente, mapea el puerto 27017
    y establece las credenciales de acceso mediante variables de entorno.

    ```yaml linenums="1"
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

Para iniciar los servicios definidos en el archivo se ejecuta `docker compose up`, que
descarga las imágenes necesarias, crea los contenedores y los pone en funcionamiento.

Para detener y eliminar los servicios, incluidos los contenedores, redes y volúmenes
asociados, se utiliza `docker compose down`. Otros comandos útiles son
`docker-compose scale servicio=num_instancias` para escalar servicios y
`docker-compose logs servicio` para consultar los registros.

Se recomienda consultar el
[historial de versiones de Docker Compose](https://docs.docker.com/compose/intro/history/)
para conocer las diferencias de sintaxis y mejoras entre versiones.

### Persistencia de datos con volúmenes

En Docker, los volúmenes permiten la persistencia de datos en los contenedores. Esto
significa que, incluso si un contenedor se elimina, los datos asociados a los volúmenes
permanecen disponibles, lo cual resulta especialmente útil cuando se desea mantener
información a través de reinicios o actualizaciones de contenedores.

Los volúmenes pueden ser de diferentes tipos. Los **volúmenes anónimos** carecen de
nombre y no pueden referenciarse explícitamente desde otros contenedores. Los
**volúmenes de _host_** permiten especificar qué carpeta del sistema anfitrión se monta
dentro del contenedor. Los **volúmenes nombrados** disponen de un nombre y pueden
referenciarse en otros contenedores o en múltiples servicios.

Para montar un volumen directamente desde la línea de comandos se utiliza la opción
`-v`.

???+ example "Ejemplo"

    Para mapear el directorio del _host_ al directorio del contenedor, podemos utilizar
    el comando:

    ```bash linenums="1"
    docker run -v ./Disco:/home/disco -it ghcr.io/astral-sh/uv:debian bash
    ```

!!!warning

    Para añadir un volumen a un contenedor existente, es necesario **recrear el contenedor**
    con el comando del volumen.

También podemos definir `docker-compose.yml` con volúmenes.

???+ example "Ejemplo"

    En este ejemplo, el servicio `mongodb` utiliza un volumen nombrado llamado
    `mongo-data` para almacenar los datos persistentes de la base de datos. Este volumen
    se monta en el directorio `/data/db` del contenedor, lo que asegura que los datos de
    MongoDB se conserven incluso si el contenedor es detenido o eliminado. Docker se
    encarga de gestionar la creación y almacenamiento de dicho volumen de forma
    completamente automatizada.

    ```yaml linenums="1"
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

Todos los ficheros de Docker se encuentran en `/var/lib/docker`. Docker **cachea las
capas intermedias** de las imágenes, incluso entre diferentes _Dockerfiles_, lo que
ahorra espacio y tiempo de construcción. En ese mismo directorio podemos ver los
volumenes disponibles.

### Registros de imágenes

Existen registros públicos y privados para almacenar y gestionar imágenes de Docker:

| Registro                  | Tipo               | Características clave                                             |
| :------------------------ | :----------------- | :---------------------------------------------------------------- |
| Docker Hub                | Público/Privado    | El más grande, con imágenes oficiales y despliegues automatizados |
| Amazon ECR                | Gestionado (AWS)   | Integración con ECS, EKS y Fargate, con pago por uso              |
| Azure Container Registry  | Gestionado (Azure) | Geo-replicación y soporte de _Helm charts_                        |
| Google Artifact Registry  | Gestionado (GCP)   | Sucesor de GCR, con escaneo de vulnerabilidades y gestión IAM     |
| GitHub Container Registry | Gestionado         | Integrado con GitHub Actions para CI/CD                           |
| Harbor                    | _Open source_      | RBAC y firmado de imágenes                                        |
| JFrog Artifactory         | Universal          | Soporta Docker, Helm y otros formatos                             |

### Optimización del tamaño de imágenes

El tamaño de una imagen Docker influye directamente en los tiempos de descarga,
despliegue y almacenamiento. Reducir el tamaño de las imágenes es una práctica
recomendada que mejora la eficiencia del flujo de trabajo y disminuye los costes de
infraestructura. Existen varias estrategias complementarias para lograrlo.

#### Selección de imágenes base ligeras

La elección de la imagen base es el factor que más impacto tiene en el tamaño final.
Imágenes como Alpine o las variantes Debian Slim ofrecen un sistema operativo mínimo que
reduce significativamente el peso de la imagen resultante en comparación con las
distribuciones completas.

#### Limpieza de caché y metadatos

Cuando se instalan paquetes del sistema operativo dentro de una imagen, los gestores de
paquetes almacenan caché y metadatos que no son necesarios en tiempo de ejecución.
Eliminar estos ficheros temporales tras la instalación reduce el tamaño de la capa
resultante. Es importante encadenar los comandos de instalación y limpieza en una única
instrucción `RUN` para que la caché no persista en capas intermedias.

???+ example "Ejemplo: Instalación con limpieza de caché"

    En este ejemplo se instalan las dependencias del sistema y se eliminan los ficheros
    temporales en la misma instrucción `RUN`, evitando que la caché de `apt` persista
    en la imagen final:

    ```dockerfile linenums="1"
    FROM python:3.13-slim-bookworm

    RUN apt-get update && apt-get install --no-install-recommends -y \
            build-essential \
            curl \
            ca-certificates && \
        apt-get clean && rm -rf /var/lib/apt/lists/*
    ```

#### Gestión de dependencias por grupos

Los gestores de dependencias como uv o Poetry permiten definir grupos diferenciados de
dependencias (producción, desarrollo, documentación, pruebas). Al construir la imagen de
producción, se instalan únicamente las dependencias necesarias para la ejecución,
excluyendo herramientas de desarrollo, _linters_ o _frameworks_ de pruebas que
incrementarían el tamaño de la imagen sin aportar valor en el entorno de despliegue.

#### Copiar solo lo necesario

Es recomendable copiar exclusivamente los ficheros que la aplicación necesita para
ejecutarse, en lugar de copiar todo el directorio del proyecto. Esto evita incluir
ficheros de configuración local, documentación, pruebas o directorios como `.git` que no
son necesarios en la imagen final. El uso de un fichero `.dockerignore` complementa esta
práctica al excluir automáticamente ficheros y directorios no deseados durante el
proceso de construcción.

#### _Multi-stage builds_

Las construcciones multietapa permiten dividir el proceso de creación de una imagen en
varias fases, cada una con su propia imagen base. Una primera etapa, más pesada, se
encarga de compilar el proyecto e instalar las dependencias, mientras que una segunda
etapa, basada en una imagen ligera, recibe únicamente los artefactos necesarios para la
ejecución. De este modo, las herramientas de compilación y las dependencias de
desarrollo no forman parte de la imagen final.

???+ example "Ejemplo: _Multi-stage build_ con uv"

    En este ejemplo, la etapa `builder` utiliza una imagen completa de Python para
    instalar las dependencias del proyecto con uv. La etapa `production` parte de una
    imagen Slim y copia únicamente el entorno virtual generado en la etapa anterior,
    obteniendo una imagen final significativamente más ligera:

    ```dockerfile linenums="1"
    ## Builder Stage
    FROM python:3.13-bookworm AS builder

    RUN apt-get update && apt-get install --no-install-recommends -y \
            build-essential && \
        apt-get clean && rm -rf /var/lib/apt/lists/*

    ADD https://astral.sh/uv/install.sh /install.sh
    RUN chmod -R 655 /install.sh && /install.sh && rm /install.sh

    ENV PATH="/root/.local/bin:$PATH"

    WORKDIR /app
    COPY ./pyproject.toml .
    RUN uv sync

    ## Production Stage
    FROM python:3.13-slim-bookworm AS production

    WORKDIR /app
    COPY . .
    COPY --from=builder /app/.venv .venv

    ENV PATH="/app/.venv/bin:$PATH"

    EXPOSE $PORT

    CMD ["uvicorn", "src.main:app", "--log-level", "info", \
         "--host", "0.0.0.0", "--port", "8080"]
    ```

### Seguridad en contenedores

Por defecto, los procesos dentro de un contenedor Docker se ejecutan como usuario
`root`. Aunque el aislamiento proporcionado por los _namespaces_ limita el alcance de
este usuario, ejecutar aplicaciones como `root` dentro del contenedor sigue
representando un riesgo de seguridad, especialmente si se produce una vulnerabilidad que
permita escapar del contenedor. La práctica recomendada consiste en crear un usuario sin
privilegios y ejecutar la aplicación con dicho usuario.

#### Ejecución con usuario no privilegiado

La instrucción `RUN useradd` permite crear un usuario dentro de la imagen, y la
directiva `USER` establece que todos los comandos posteriores se ejecuten con ese
usuario en lugar de `root`. Esta configuración se aplica habitualmente en la etapa de
producción de un _multi-stage build_.

#### Gestión de secretos en tiempo de construcción

Las variables de entorno definidas con `ENV` en un `Dockerfile` quedan almacenadas en
las capas de la imagen y son visibles mediante `docker inspect`. Para información
sensible como contraseñas o claves de acceso, Docker proporciona el mecanismo de _build
secrets_ mediante `--mount=type=secret`, que permite acceder a los secretos durante la
construcción sin que estos persistan en la imagen final.

???+ example "Ejemplo: Imagen segura con usuario no privilegiado y _build secrets_"

    En este ejemplo, la etapa de producción crea un usuario `appuser` sin privilegios, monta los secretos de forma temporal durante la construcción y copia únicamente el código fuente necesario:

    ```dockerfile linenums="1"
    ## Builder Stage
    FROM python:3.13-bookworm AS builder

    RUN apt-get update && apt-get install --no-install-recommends -y \
            build-essential && \
        apt-get clean && rm -rf /var/lib/apt/lists/*

    ADD https://astral.sh/uv/install.sh /install.sh
    RUN chmod -R 655 /install.sh && /install.sh && rm /install.sh

    ENV PATH="/root/.local/bin:$PATH"

    WORKDIR /app
    COPY ./pyproject.toml .
    RUN uv sync

    ## Production Stage
    FROM python:3.13-slim-bookworm AS production

    RUN --mount=type=secret,id=DB_PASSWORD \
        --mount=type=secret,id=DB_USER \
        --mount=type=secret,id=DB_NAME \
        --mount=type=secret,id=DB_HOST \
        --mount=type=secret,id=ACCESS_TOKEN_SECRET_KEY \
        echo "Secrets available during build"

    RUN useradd --create-home appuser
    USER appuser

    WORKDIR /app
    COPY /src src
    COPY --from=builder /app/.venv .venv

    ENV PATH="/app/.venv/bin:$PATH"

    EXPOSE $PORT

    CMD ["uvicorn", "src.main:app", "--log-level", "info", \
         "--host", "0.0.0.0", "--port", "8080"]
    ```

## Arquitectura de microservicios

### Aplicaciones monolíticas frente a microservicios

En una arquitectura monolítica, todas las funcionalidades están integradas en un único
bloque de código. A medida que el sistema crece, esto genera conflictos de dependencias,
desarrollo más lento y _releases_ más arriesgadas.

La arquitectura de microservicios divide la aplicación en servicios pequeños, autónomos
y sin estado, cada uno con su propia lógica y base de datos independiente. Cada servicio
se corresponde con una funcionalidad de negocio y es _self-contained_. Esta separación
favorece la resiliencia (un fallo en un servicio no compromete al resto) y la
escalabilidad horizontal (se escalan instancias de un servicio concreto según la
demanda).

### Comunicación entre microservicios

La comunicación se realiza habitualmente mediante **APIs REST** a través de HTTP.
Mecanismos complementarios:

- **_Message Broker_**: Intermediario que gestiona el envío y recepción de mensajes
  entre servicios. Permite desacoplar emisor y receptor, procesar mensajes en cola de
  forma paralela y proteger servicios de sobrecargas.
- **_Service Mesh_**: Capa de infraestructura que gestiona la comunicación entre
  microservicios (enrutamiento, seguridad, observabilidad). Se compone de un **plano de
  datos** (_proxys_ junto a cada microservicio) y un **plano de control** (administra y
  coordina los _proxys_).

### Organización del código: monorepo frente a polirepo

| Estrategia   | Descripción                                                                           |
| :----------- | :------------------------------------------------------------------------------------ |
| **Monorepo** | Todos los microservicios en un único repositorio. Facilita la visibilidad global.     |
| **Polirepo** | Cada microservicio en su propio repositorio. Favorece la independencia entre equipos. |

## Infraestructura como Código (IaC)

La Infraestructura como Código (_Infrastructure as Code_) consiste en definir y
gestionar la infraestructura mediante código versionado. Este enfoque garantiza
reproducibilidad, trazabilidad y coherencia entre entornos, permitiendo crear y destruir
infraestructuras de forma automatizada y predecible.

Docker y plataformas de orquestación como Kubernetes desempeñan un papel central en IaC,
al facilitar la gestión de contenedores, la automatización de despliegues y la
alineación entre los entornos de desarrollo, pruebas y producción. Tratar la
infraestructura como un artefacto más del software refuerza la eficiencia operativa y
reduce la dependencia de configuraciones manuales.
