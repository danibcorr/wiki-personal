---
authors: Daniel Bazo Correa
description: Automatización de tareas y gestión de red en Linux.
title: Automatización y red
---

## Automatización

En Linux, la eficiencia operativa se potencia mediante la **automatización** de tareas
repetitivas o complejas a través de la shell.

Una herramienta fundamental para este propósito son los **alias**, que funcionan como
atajos para comandos largos o frecuentemente utilizados. Los alias permiten reducir
errores, ahorrar tiempo y estandarizar procedimientos dentro del entorno de trabajo.

Los alias se configuran generalmente en archivos de inicialización de la shell, como
`~/.bashrc` o `~/.zshrc`, lo que asegura que estén disponibles de manera automática en
cada nueva sesión.

???+ example "Ejemplo"

    Un alias como `alias ll='ls -alF'` convierte un comando largo y detallado en una
    instrucción breve y fácil de recordar.

La recarga inmediata de estos archivos mediante `source ~/.bashrc` permite aplicar los
cambios sin necesidad de cerrar la sesión, manteniendo la continuidad del trabajo.

Más allá de los alias, Linux ofrece otras herramientas de automatización, como **scripts
Bash** y **Makefiles**, que permiten ejecutar secuencias de comandos de manera periódica
o en respuesta a eventos específicos.

## Gestión de red y puertos

En entornos de desarrollo y administración de sistemas, es habitual necesitar
inspeccionar el estado de la red, identificar qué puertos están en uso o verificar la
conectividad con servicios remotos. Para ello, Linux dispone de varias herramientas que
pueden instalarse con los siguientes comandos:

???+ example "Ejemplo: Inspección de red y puertos"

    Instalación de las herramientas necesarias:

    ```bash linenums="1"
    sudo apt install net-tools
    sudo apt-get install telnet
    ```

    Una vez instaladas, es posible listar todos los puertos TCP activos en el sistema:

    ```bash linenums="1"
    netstat -n --all --tcp
    ```

    Para localizar el proceso que está utilizando un puerto específico, como el 9000:

    ```bash linenums="1"
    sudo lsof -i -P -n | grep 9000
    ```

    Finalmente, para comprobar la conectividad con un servicio concreto mediante Telnet, indicando la dirección IP y el puerto:

    ```bash linenums="1"
    telnet localhost 5433
    ```
