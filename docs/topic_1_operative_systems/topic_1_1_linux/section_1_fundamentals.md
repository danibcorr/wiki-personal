---
authors: Daniel Bazo Correa
description: Conceptos esenciales de Linux, la terminal y comandos fundamentales.
title: Fundamentos y terminal
---

## Referencias

- [NetworkChuck, 60 comandos de Linux que NECESITAS saber (en 10 minutos)](https://www.youtube.com/watch?v=gd7BXuUQ91w)
- [DeciLearn, Linux Para Principiantes - Curso completo](https://youtu.be/jVQKk8IB9pA?si=BdLz0eLehoVxupwF)

## Introducción

<figure markdown="span">
  ![Mascota de Linux](../../assets/img/docs/logos/linux-logo.png){ width="300" }
  <figcaption>Mascota de Linux</figcaption>
</figure>

**Linux** no es un sistema operativo, se trata de un **_kernel_** de software libre
desarrollado inicialmente por Linus Torvalds. Su código fuente es público y accesible,
permitiendo a cualquier persona examinarlo, modificarlo, contribuir a su desarrollo o
crear su propia distribución.

El _kernel_ de Linux se combina con las utilidades del proyecto **GNU**, que aportan las
herramientas esenciales del entorno de usuario, como compiladores, intérpretes de
comandos y bibliotecas básicas. Por esta razón, la denominación más precisa y adecuada
para referirse al sistema es **GNU/Linux**.

Linux se caracteriza por ser una plataforma robusta, segura y flexible, capaz de
adaptarse tanto a entornos personales como a infraestructuras críticas, incluyendo
servidores y sistemas embebidos. Esta versatilidad lo ha convertido en la base de los
sistemas operativos más utilizados en entornos distribuidos y plataformas en la nube,
aunque también encuentra un lugar destacado en el ámbito doméstico.

El modelo de desarrollo abierto de Linux, sustentado por una comunidad global de
desarrolladores y usuarios, facilita una evolución constante, con mejoras continuas en
rendimiento, estabilidad y seguridad. Esta diversidad se manifiesta en la existencia de
múltiples distribuciones que integran el _kernel_ con diferentes herramientas, entornos
gráficos y gestores de paquetes. Cuando estas componentes se combinan con
configuraciones específicas y, en muchos casos, un entorno gráfico, se obtiene una
**distribución**. Ejemplos representativos como Ubuntu, Debian, Fedora o Arch Linux
ilustran cómo un mismo núcleo puede ajustarse a contextos de uso muy distintos.

## La terminal

La interacción directa con Linux se realiza principalmente a través de la terminal o
**_shell_**, un intérprete de comandos que traduce las órdenes del usuario en acciones
ejecutables por el sistema. Aunque existen alternativas modernas, **Bash** se mantiene
como la _shell_ más extendida y estandarizada.

<figure markdown="span">
  ![Ejemplo de una ventana de una shell o terminal en PopOS](../../assets/img/docs/shell-example.png)
  <figcaption>Ejemplo de una ventana de una shell o terminal en PopOS</figcaption>
</figure>

Los comandos que podemos utilizar en la terminal presentan una sintaxis basada en un
nombre principal, opciones que modifican el comportamiento de dicho comando y argumentos
que especifican el objetivo de la acción.

???+ example "Ejemplo"

    El comando `ls -l /home/usuario` combina el nombre principal `ls`, que lista los
    archivos y directorios, con la opción `-l`, que indica que la información se muestre en
    formato detallado, y el argumento `/home/usuario`, que especifica la ubicación del
    directorio cuyo contenido se desea visualizar.

El propio sistema facilita la consulta y el aprendizaje mediante documentación
integrada. Para ello, herramientas como `man`, `help` o `type` permiten comprender el
funcionamiento interno de los comandos y distinguir entre utilidades externas, funciones
internas o alias definidos por el usuario.

Los manuales se encuentran organizados en secciones que agrupan la información según su
naturaleza, lo que permite acceder de manera más precisa a la documentación. Las
secciones más comunes son las siguientes:

1. **Comandos de usuario**: Incluye programas ejecutables y comandos que los usuarios
   pueden ejecutar desde la _shell_. Ejemplo: `ls`, `cp`.
2. **Llamadas al sistema**: Documenta las funciones proporcionadas por el kernel que
   permiten a los programas interactuar con el sistema operativo. Ejemplo: `open()`,
   `read()`.
3. **Funciones de biblioteca**: Contiene funciones disponibles en bibliotecas estándar,
   como la biblioteca C (`libc`). Ejemplo: `printf()`, `malloc()`.
4. **Archivos especiales y dispositivos**: Describe archivos del sistema y dispositivos
   especiales ubicados en `/dev` u otras rutas del sistema de archivos. Ejemplo:
   `/dev/null`.
5. **Formatos de archivo y convenciones**: Incluye descripciones de formatos de
   archivos, convenciones de configuración y estructuras de datos. Ejemplo:
   `/etc/passwd`.
6. **Juegos y diversiones**: Contiene documentación sobre juegos, ejemplos o programas
   de entretenimiento incluidos en el sistema.
7. **Miscelánea**: Agrupa temas varios, convenciones, estándares o programas que no
   encajan en otras secciones.
8. **Comandos de administración del sistema**: Incluye comandos reservados para la
   administración y configuración del sistema, normalmente accesibles solo por el
   superusuario (`root`). Ejemplo: `mount`, `passwd`.

Al consultar un manual, es posible especificar la sección deseada para acceder
directamente a la información relevante.

???+ example "Ejemplo"

    `man 2 open` muestra la documentación de la llamada al sistema `open()`, mientras que
    `man 1 open` podría referirse a un comando de usuario llamado `open`.

No todos los comandos necesariamente cuentan con una sección específica en el manual, en
algunos casos, la información puede encontrarse únicamente mediante otras herramientas
de ayuda o documentación externa.

## Comandos básicos

La interacción cotidiana con Linux se apoya en un conjunto de comandos fundamentales que
permiten administrar el sistema, navegar por su estructura de archivos (directorios) y
manipular información.

Entre ellos, `pwd` indica el directorio de trabajo actual, `ls` permite explorar el
contenido de los directorios mostrando información detallada, permisos o archivos
ocultos, y `cd` posibilita el desplazamiento entre directorios.

La creación de elementos básicos se realiza con `touch` para archivos y `mkdir` para
directorios. La lectura de archivos puede efectuarse mediante `cat`, adecuada para
contenidos breves, o `less`, que permite una navegación paginada en textos extensos. La
gestión de archivos y directorios se completa con `cp` para copiar, `mv` para mover o
renombrar, y `rm` y `rmdir` para eliminar elementos.

La administración básica también incluye utilidades como `whoami` para identificar al
usuario activo, `useradd` para crear cuentas, `man` para consultar la documentación
integrada de cada comando y `wget` para la descarga de recursos desde la red.

Además, uno de los flujos de trabajo que más se utilizan en entornos corporativos, o si
tienes tu propio servidor en casa, es el acceso remoto a otros equipos. Este se realiza
habitualmente mediante el protocolo **SSH (_Secure Shell_)**, que permite establecer
sesiones seguras desde la línea de comandos, integrando de manera fluida la
administración de sistemas locales y remotos.

Estos son algunos de los comandos más utilizados para el día a día. Sin embargo, existen
aún más comandos cuyo comportamiento puede verse alterado gracias a las opciones que
ofrecen. Es por ello que resulta impracticable enumerar todos los comandos de Linux
junto con sus múltiples opciones, debido a la gran cantidad y diversidad que presentan.

Por esta razón, es posible utilizar la opción `--help` en cualquier comando para obtener
información detallada sobre su uso, incluyendo las opciones disponibles y una breve
descripción de su funcionalidad. También existen recursos externos como la documentación
oficial o motores de búsqueda, aunque explorar el propio sistema resulta igualmente
enriquecedor, preferiblemente en un entorno controlado como una máquina virtual.

En cualquier caso, aquí tienes una recopilación de los comandos más utilizados:

| Comando   | Función resumida                                                                       | Ejemplo de uso                          |
| --------- | -------------------------------------------------------------------------------------- | --------------------------------------- |
| `pwd`     | Muestra el directorio de trabajo actual.                                               | `pwd`                                   |
| `ls`      | Lista el contenido de directorios, mostrando información detallada y archivos ocultos. | `ls -la /home/usuario`                  |
| `cd`      | Permite cambiar de directorio.                                                         | `cd /var/log`                           |
| `touch`   | Crea archivos vacíos.                                                                  | `touch archivo.txt`                     |
| `mkdir`   | Crea nuevos directorios.                                                               | `mkdir proyecto`                        |
| `cat`     | Muestra el contenido de archivos pequeños.                                             | `cat archivo.txt`                       |
| `less`    | Permite visualizar archivos largos de forma paginada.                                  | `less archivo_grande.txt`               |
| `cp`      | Copia archivos o directorios.                                                          | `cp archivo.txt /home/usuario/backup/`  |
| `mv`      | Mueve o renombra archivos o directorios.                                               | `mv archivo.txt documento.txt`          |
| `rm`      | Elimina archivos.                                                                      | `rm archivo.txt`                        |
| `rmdir`   | Elimina directorios vacíos.                                                            | `rmdir carpeta_vacia`                   |
| `whoami`  | Muestra el usuario activo.                                                             | `whoami` → `usuario`                    |
| `useradd` | Crea nuevas cuentas de usuario.                                                        | `sudo useradd nuevo_usuario`            |
| `passwd`  | Cambia la contraseña de un usuario.                                                    | `passwd usuario`                        |
| `man`     | Accede a la documentación integrada de comandos.                                       | `man ls`                                |
| `wget`    | Descarga archivos desde la red.                                                        | `wget https://ejemplo.com/archivo.zip`  |
| `ssh`     | Permite el acceso remoto seguro a otros equipos.                                       | `ssh usuario@192.168.1.10`              |
| `chmod`   | Modifica permisos de archivos y directorios.                                           | `chmod 755 script.sh`                   |
| `chown`   | Cambia el propietario de archivos o directorios.                                       | `chown usuario:grupo archivo.txt`       |
| `find`    | Busca archivos y directorios según criterios específicos.                              | `find /home -name "*.txt"`              |
| `grep`    | Busca cadenas de texto dentro de archivos.                                             | `grep "error" log.txt`                  |
| `tar`     | Comprime o descomprime archivos y directorios.                                         | `tar -czvf backup.tar.gz /home/usuario` |
| `df`      | Muestra el espacio disponible en sistemas de archivos.                                 | `df -h`                                 |
| `du`      | Muestra el tamaño de archivos y directorios.                                           | `du -sh /home/usuario`                  |
| `top`     | Muestra los procesos en ejecución y uso de recursos en tiempo real.                    | `top`                                   |
| `ps`      | Lista los procesos en ejecución.                                                       | `ps aux`                                |

## Estructura de directorios

Linux organiza su almacenamiento siguiendo una estructura jerárquica unificada en forma
de árbol cuyo origen se encuentra en el directorio raíz (`/`).

A diferencia de otros sistemas operativos, no existen unidades identificadas por letras,
todos los dispositivos de almacenamiento se incorporan a esta jerarquía mediante el
proceso de montaje.

<figure markdown="span">
  ![Jerarquía de los directorios de Linux](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.tecmint.com%2Fwp-content%2Fuploads%2F2012%2F07%2FLinux-File-System.jpg&f=1&nofb=1&ipt=b56b5b1d3ede73ff5f4eeeba1bd0c56bc7573349258800f0aca2cf57fa506845)
  <figcaption>Jerarquía de los directorios de Linux</figcaption>
</figure>

Dentro de esta estructura destacan una serie de directorios esenciales, entre ellos:

- **/boot**: Alberga los componentes necesarios para el arranque del sistema, incluido
  el kernel y el gestor **GRUB** (un programa que aparece al iniciar Linux y permite
  manejar el proceso de inicio, permitiéndote elegir el sistema operativo en caso de que
  tengas varias particiones, por ejemplo).
- **/etc**: Concentra los archivos de configuración en formato de texto plano,
  determinando el comportamiento del sistema y sus servicios.
- **/bin** y **/sbin**: Contienen ejecutables imprescindibles para la operación básica y
  la administración del sistema.
- **/home**: Localiza los espacios de trabajo de los usuarios, mientras que **/root** se
  reserva exclusivamente para el superusuario.
- **/var**: Almacena datos variables como registros (logs), colas y bases de datos.
- **/dev**, **/proc** y **/sys**: Proporcionan representaciones virtuales del hardware y
  del estado interno del kernel, permitiendo un acceso sistemático y controlado a los
  recursos del sistema.
