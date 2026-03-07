---
authors: Daniel Bazo Correa
description: Introducción al kernel de Linux y a los sistemas operativos basados en él.
title: Linux
---

## Bibliografía

- [NetworkChuck, 60 comandos de Linux que NECESITAS saber (en 10 minutos)](https://www.youtube.com/watch?v=gd7BXuUQ91w)
- [DeciLearn, Linux Para Principiantes - Curso completo](https://youtu.be/jVQKk8IB9pA?si=BdLz0eLehoVxupwF)

## Introducción

<p align="center">
  <img src="../../assets/img/docs/logos/linux-logo.png" height="300" width="300"/>
  <br />
  <em>Mascota de Linux</em>
</p>

**Linux** no es un sistema operativo, se trata de un **_kernel_** de software libre
desarrollado inicialmente por Linus Torvalds. Su código fuente es público y accesible,
permitiendo a cualquier persona examinarlo, modificarlo, contribuir a su desarrollo o
crear su propia distribución.

El _kernel_ de Linux se combina con las utilidades del proyecto **GNU**, que aportan las
herramientas esenciales del entorno de usuario, como compiladores, intérpretes de
comandos y bibliotecas básicas. Por esta razón, la denominación más precisa y adecuada
para referirse al sistema es **GNU/Linux**.

Linux se caracteriza por ser una plataforma robusta, segura y altamente flexible, capaz
de adaptarse tanto a entornos personales como a infraestructuras críticas, incluyendo
servidores y sistemas embebidos. Esta versatilidad lo ha convertido en la base de los
sistemas operativos más utilizados en entornos distribuidos y plataformas en la nube.

El modelo de desarrollo abierto de Linux, sustentado por una comunidad global de
desarrolladores y usuarios, facilita una evolución constante, con mejoras continuas en
rendimiento, estabilidad y seguridad. Esta diversidad se manifiesta en la existencia de
múltiples distribuciones que integran el _kernel_ con diferentes herramientas, entornos
gráficos y gestores de paquetes. Cuando estas componentes se combinan con configuraciones
específicas y, en muchos casos, un entorno gráfico, se obtiene una **distribución**.
Ejemplos representativos como Ubuntu, Debian, Fedora o Arch Linux ilustran cómo un mismo
núcleo puede ajustarse a contextos de uso muy distintos.

### La terminal

La interacción directa con Linux se realiza principalmente a través de la terminal o
**_shell_**, un intérprete de comandos que traduce las órdenes del usuario en acciones
ejecutables por el sistema. Aunque existen alternativas modernas, **Bash** se mantiene
como la _shell_ más extendida y estandarizada.

<p align="center">
  <img src="../../assets/img/docs/shell-example.png"/>
  <br />
  <em>Ejemplo de una ventana de una shell o terminal en PopOS</em>
</p>

Los comandos que podemos utilizar en la terminal presentan una sintaxis basada en un
nombre principal, opciones que modifican el comportamiento de dicho comando y argumentos
que especifican el objetivo de la acción.

???+ example "Ejemplo"

    El comando `ls -l /home/usuario` combina el nombre principal `ls`, que lista los
    archivos y directorios, con la opción `-l`, que indica que la información se muestre en
    formato detallado, y el argumento `/home/usuario`, que especifica la ubicación del
    directorio cuyo contenido se desea visualizar.

El propio sistema facilita la consulta y el aprendizaje mediante documentación integrada.
Para ello, herramientas como `man`, `help` o `type` permiten comprender el funcionamiento
interno de los comandos y distinguir entre utilidades externas, funciones internas o
alias definidos por el usuario.

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
5. **Formatos de archivo y convenciones**: Incluye descripciones de formatos de archivos,
   convenciones de configuración y estructuras de datos. Ejemplo: `/etc/passwd`.
6. **Juegos y diversiones**: Contiene documentación sobre juegos, ejemplos o programas de
   entretenimiento incluidos en el sistema.
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
algunos casos, la información puede encontrarse únicamente mediante otras herramientas de
ayuda o documentación externa.

### Comandos básicos

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
renombrar, y `rm` y `rmdir` para eliminar elementos, comandos que requieren especial
precaución debido a la irreversibilidad de sus efectos.

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
ofrecen. Es por ello que resulta impracticable enumerar todos los comandos de Linux junto
con sus múltiples opciones, debido a la gran cantidad y diversidad que presentan.

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

### Directorios

Linux organiza su almacenamiento siguiendo una estructura jerárquica unificada en forma
de árbol cuyo origen se encuentra en el directorio raíz (`/`).

A diferencia de otros sistemas operativos, no existen unidades identificadas por letras;
todos los dispositivos de almacenamiento se incorporan a esta jerarquía mediante el
proceso de montaje.

<p align="center">
  <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.tecmint.com%2Fwp-content%2Fuploads%2F2012%2F07%2FLinux-File-System.jpg&f=1&nofb=1&ipt=b56b5b1d3ede73ff5f4eeeba1bd0c56bc7573349258800f0aca2cf57fa506845"/>
  <br />
  <em>Jerarquía de los directorios de Linux</em>
</p>

Dentro de esta estructura destacan una serie de directorios esenciales, entre ellos:

- **/boot**: Alberga los componentes necesarios para el arranque del sistema, incluido el
  kernel y el gestor **GRUB** (un programa que aparece al iniciar Linux y permite manejar
  el proceso de inicio, permitiéndote elegir el sistema operativo en caso de que tengas
  varias particiones, por ejemplo).
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

## Gestión de usuarios y grupos

Linux es un sistema multiusuario, en el que la seguridad y el control de acceso se
articulan mediante un modelo basado en usuarios, grupos y permisos. Este enfoque permite
que múltiples personas trabajen simultáneamente en el mismo sistema sin interferir entre
sí, garantizando al mismo tiempo la protección de los recursos y la estabilidad del
entorno.

Los permisos no se asignan únicamente a individuos, sino que se agrupan mediante
**grupos**, que actúan como conjuntos de privilegios compartidos (como una plantilla de
privilegios).

Cada usuario dispone de un **grupo primario**, asociado por defecto a los archivos que
crea, y puede pertenecer a varios **grupos secundarios**, que amplían sus capacidades,
como ocurre con el grupo `sudo`, destinado a la ejecución controlada de tareas
administrativas.

### Seguridad y permisos

Cada archivo o directorio define privilegios de **lectura**, **escritura** y
**ejecución** para tres categorías claramente diferenciadas: a) el **propietario**, b) el
**grupo** asociado y c) el resto de usuarios, denominados **otros**.

Este esquema limita el acceso indebido a los recursos. Por encima de estas restricciones
se sitúa el **superusuario**, identificado como `root`, que posee control total sobre el
sistema y puede ignorar el modelo de permisos convencional.

La categoría de **otros** representa a cualquier usuario que no sea ni el propietario del
archivo ni miembro del grupo asociado.

El sistema evalúa los permisos siguiendo un orden de prioridad estricto: primero
comprueba si el usuario es el propietario, en cuyo caso aplica los permisos
correspondientes. Si no lo es, verifica si pertenece al grupo, y solo si no cumple
ninguna de estas condiciones, se aplican los permisos definidos para otros.

<p align="center">
  <img src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.purfe.com%2Fwp-content%2Fuploads%2F2021%2F02%2Ffile_permissions.jpg&f=1&nofb=1&ipt=a7ced098cac75da3129b35051830e66669b47212e2784e64a24446e2af131f4c"/>
  <br />
  <em>Registro de permisos de Linux</em>
</p>

Los permisos se visualizan habitualmente mediante el comando `ls -l`, que muestra una
cadena simbólica como `rwxr-xr--`.

Esta notación agrupa los permisos en tres bloques de tres caracteres, cada uno
correspondiente al propietario, al grupo y a otros, respectivamente. Cada carácter indica
si el permiso de lectura (`r`), escritura (`w`) o ejecución (`x`) está concedido o no.

???+ example "Ejemplo"

    Supongamos que al ejecutar `ls -l` obtenemos la siguiente salida:

    ```bash linenums="1"
    -rwxr-xr--
    ```

    Este conjunto de caracteres puede interpretarse de la siguiente manera, dividiéndolo en
    bloques de tres caracteres que representan los permisos del propietario, del grupo y de
    los demás usuarios:

    | Permiso       | Propietario | Grupo | Otros |
    | ------------- | ----------- | ----- | ----- |
    | Lectura (r)   | ✔           | ✔     | ✔     |
    | Escritura (w) | ✔           | ✖     | ✖     |
    | Ejecución (x) | ✔           | ✔     | ✖     |

    En este contexto:

    - **Propietario:** Tiene permisos completos sobre el archivo, lo que significa que puede
      leer su contenido, modificarlo y ejecutarlo si se trata de un archivo ejecutable.
    - **Grupo:** Posee permisos de lectura y ejecución, lo que le permite abrir y ejecutar
      el archivo, pero no modificarlo.
    - **Otros:** Solo cuentan con permiso de lectura, por lo que pueden consultar el
      contenido del archivo, pero no ejecutarlo ni realizar cambios sobre él.

    Es importante destacar que cada bloque de tres caracteres sigue siempre el orden `rwx`.

Cuando un permiso no está habilitado, se reemplaza con un guion (`-`). Por ejemplo, `r--`
indica que únicamente se permite la lectura, mientras que `rw-` permite lectura y
escritura, pero no ejecución.

### Modificación de permisos

Podemos modificar los permisos de los archivos y directorios utilizando el comando
`chmod` mediante dos notaciones principales, la **octal** y la **simbólica**.

En la **notación octal**, cada permiso tiene un valor numérico fijo, donde la lectura
equivale a 4, la escritura a 2 y la ejecución a 1. La suma de estos valores determina el
permiso final para cada categoría. El comando recibe siempre tres dígitos que representan
de izquierda a derecha los permisos del propietario, del grupo y de otros.

???+ example "Ejemplo"

    Al aplicar `chmod 754 archivo`, el propietario obtiene todos los permisos, el grupo
    puede leer y ejecutar, y el resto de usuarios solo puede leer.

Por otra parte, la **notación simbólica** utiliza letras para identificar a los sujetos,
`u` para el propietario, `g` para el grupo, `o` para otros y `a` para todos, además de
emplear operadores para añadir, quitar o asignar permisos.

???+ example "Ejemplos"

    - **Añadir permisos de ejecución a todos:** `chmod a+x backup.sh`, en este caso, el
      operador `+` suma el permiso de ejecución (`x`) a todas las categorías (`a` de _all_).
    - **Dar acceso de lectura al grupo:** `chmod g+r backup.sh`, aquí se especifica que
      únicamente el sujeto grupo (`g`) reciba el atributo de lectura (`r`).
    - **Retirar permisos de escritura accidental a otros:** `chmod o-w backup.sh`, el
      operador `-` garantiza que cualquier permiso de escritura previo para terceros sea
      revocado, sin alterar los permisos del dueño o del grupo.
    - **Asignación exacta de permisos:** `chmod g=rx backup.sh`, el operador `=` establece
      que el grupo tenga lectura y ejecución, eliminando cualquier otro permiso previo
      que pudiera tener ese grupo (como el de escritura) de una sola vez.

El sistema emplea el comando `umask` para definir los permisos **por defecto** de los
nuevos archivos y directorios. Mientras que `chmod` modifica permisos existentes, `umask`
actúa como una máscara que restringe los permisos máximos iniciales.

Para los archivos, el sistema parte de un valor máximo de lectura y escritura para todos,
y para los directorios, de permisos completos. El valor de `umask` indica qué permisos
deben eliminarse automáticamente, de modo que cuanto más restrictiva sea la máscara, más
limitados serán los permisos resultantes.

???+ example "Ejemplo"

    Supongamos que un usuario tiene configurada una **máscara `umask` de 022**:

    - Para un **archivo nuevo**, el sistema parte de los permisos máximos `rw-rw-rw-`
      (lectura y escritura para todos). La máscara 022 elimina los permisos de escritura
      para **grupo** y **otros**, por lo que el archivo se crea con permisos finales
      `rw-r--r--`.
    - Para un **directorio nuevo**, el sistema parte de permisos máximos `rwxrwxrwx`
      (lectura, escritura y ejecución para todos). Aplicando la misma máscara 022, se
      eliminan los permisos de escritura para **grupo** y **otros**, resultando en permisos
      finales `rwxr-xr-x`.

### Propiedad y gestión de archivos

Además de los permisos, cada archivo y directorio posee un **propietario** y un
**grupo**, que determinan quién ejerce la autoridad principal sobre él.

El comando `chown` permite modificar esta propiedad, definiendo quién es el dueño y a qué
grupo pertenece un recurso. A diferencia de `chmod`, que puede ser utilizado por el
propietario del archivo para ajustar sus permisos, `chown` requiere privilegios
administrativos, ya que cambiar la propiedad implica transferir el control efectivo del
recurso.

`chown` permite modificar únicamente el usuario propietario, solo el grupo o ambos
simultáneamente, y puede aplicarse de forma recursiva a directorios completos.

???+ example "Ejemplo"

    Supongamos que un administrador desea **cambiar el propietario y el grupo de un
    directorio** llamado `proyecto` un usuario llamado `ana`:

    ```bash linenums="1"
    sudo chown ana proyecto
    ```

    Después de ejecutar este comando, `ana` será la propietaria del directorio, mientras que
    el grupo permanece sin cambios. Para **cambiar solo el grupo** a `desarrolladores`:

    ```bash linenums="1"
    sudo chown :desarrolladores proyecto
    ```

    El propietario actual se mantiene, pero ahora el grupo asociado es `desarrolladores`.
    Para **cambiar tanto propietario como grupo simultáneamente**:

    ```bash linenums="1"
    sudo chown ana:desarrolladores proyecto
    ```

    Con esto, `ana` se convierte en la propietaria y `desarrolladores` en el grupo asociado
    al directorio. Para **aplicar los cambios de manera recursiva** a todos los archivos y
    subdirectorios dentro de `proyecto`:

    ```bash linenums="1"
    sudo chown -R ana:desarrolladores proyecto
    ```

### Administración de cuentas de usuario

La gestión de usuarios se completa con comandos orientados a la creación y mantenimiento
de cuentas. Herramientas como `adduser` permiten crear nuevos usuarios de forma
interactiva, mientras que `passwd` se utiliza para establecer o modificar contraseñas. La
pertenencia a grupos puede consultarse mediante `groups`, tanto para el usuario actual
como para cualquier otro usuario del sistema, y modificarse añadiendo usuarios a grupos
específicos, como `sudo`, para concederles capacidades administrativas controladas.

???+ example "Ejemplos"

    - **Creación interactiva de la cuenta:** `sudo adduser pedro`, a diferencia de `useradd`,
      el comando `adduser` es un script de alto nivel que, de forma asistida, crea el
      directorio personal en `/home/pedro`, asigna un intérprete de comandos (Shell) y
      solicita la información básica del usuario.
    - **Gestión de la seguridad de acceso:** `sudo passwd pedro`, aunque el comando anterior
      solicita una clave inicial, `passwd` permite al administrador forzar un cambio de
      contraseña o actualizarla en cualquier momento, garantizando la integridad del acceso.
    - **Concesión de privilegios administrativos:** `sudo adduser pedro sudo`, para que el
      usuario pueda ejecutar tareas de mantenimiento que requieren privilegios de raíz
      (root), se le añade al grupo secundario `sudo`. Esta acción aplica la "plantilla" de
      permisos necesaria para que el sistema le permita utilizar dicho comando.
    - **Auditoría y verificación de pertenencia:** `groups pedro`, este comando permite
      verificar que los cambios se han aplicado correctamente. La salida mostrará una lista
      similar a `pedro : pedro sudo`, confirmando que el usuario pertenece a su grupo
      primario y al grupo de administradores.

## Gestión de procesos, señales y servicios

En Linux, un **proceso** se define como un **programa en ejecución**. Cuando un usuario
inicia un programa, el sistema operativo carga el archivo binario en memoria, asigna los
recursos necesarios y lo transforma en un proceso activo.

Cada proceso es gestionado por el kernel y recibe un identificador único denominado
**PID** (_Process ID_). Todos los procesos forman una jerarquía cuyo origen es el proceso
con PID 1, gestionado actualmente por **`systemd`**.

A lo largo de su ciclo de vida, un proceso puede encontrarse en distintos estados, que
van desde ejecución activa hasta espera o finalización, y puede supervisarse mediante
herramientas como `ps`, `top` o `htop`, las cuales permiten analizar su consumo de
recursos y comportamiento.

Linux organiza los procesos en forma de árbol genealógico. Cada proceso nace de otro
proceso padre:

- **`systemd` (PID 1):** Es el proceso inicial que arranca con el kernel y actúa como
  ancestro de todos los demás.
- **Parent/Child:** Cuando un programa lanza otro (por ejemplo, cuando la terminal
  ejecuta `ls`), el primero actúa como padre y el segundo como hijo.

Cada proceso contiene información esencial para su gestión:

- **PID (Process ID):** Identificador único del proceso.
- **PPID (Parent Process ID):** PID del proceso que lo creó.
- **UID (User ID):** Usuario que ejecuta el proceso, determinando sus permisos sobre
  archivos y recursos del sistema.

Los procesos pueden encontrarse en diferentes estados según su actividad:

- **Running (R):** En ejecución o listo para ejecutarse.
- **Sleeping (S/D):** Esperando un evento, como entrada del usuario o lectura de disco.
- **Stopped (T):** Pausado, por ejemplo mediante `Ctrl+Z`.
- **Zombie (Z):** Ha terminado su ejecución, pero su padre aún no ha registrado su
  finalización. No consume memoria activa.

### Señales y control de procesos

Las **señales** son mecanismos que permiten comunicar eventos a un proceso en ejecución.
Funcionan como mensajes que pueden solicitar la terminación, pausa, reanudación o la
recarga de configuraciones de un proceso. Las señales más utilizadas son:

| Señal       | Nombre    | Número | Función                                                                   |
| ----------- | --------- | ------ | ------------------------------------------------------------------------- |
| **SIGTERM** | Terminate | 15     | Solicita al proceso que cierre de manera ordenada.                        |
| **SIGKILL** | Kill      | 9      | Fuerza la terminación inmediata del proceso, sin posibilidad de reacción. |
| **SIGHUP**  | Hangup    | 1      | Solicita la recarga de la configuración de daemons.                       |
| **SIGSTOP** | Stop      | 19     | Pausa el proceso sin liberarlo de la memoria.                             |
| **SIGCONT** | Continue  | 18     | Reanuda un proceso previamente detenido.                                  |

El comando `kill` permite enviar estas señales a procesos específicos mediante su PID.
Por ejemplo, `kill -15 1234` solicita una terminación ordenada, mientras que
`kill -9 1234` fuerza su cierre.

Si se desconoce el PID, se puede usar `pkill` con el nombre del proceso:
`pkill -9 firefox`. Los usuarios solo pueden enviar señales a sus propios procesos, para
interactuar con procesos de otros usuarios o del sistema se requiere privilegio de
superusuario (`sudo`).

Señales comunes generadas desde el teclado incluyen:

- **Ctrl + C (SIGINT):** Interrumpe la ejecución del proceso activo.
- **Ctrl + Z (SIGTSTP):** Pausa el proceso y lo envía al segundo plano, permitiendo
  reanudarlo con `fg`.

### _Daemons_ y servicios

Los **_daemons_** son procesos diseñados para ejecutarse en segundo plano de manera
continua, sin depender de la sesión de un usuario. Proporcionan servicios permanentes
como servidores web, SSH o tareas programadas.

A diferencia de los procesos interactivos, los _daemons_ se desvinculan de su terminal
original y son adoptados por `systemd` (PID 1), lo que garantiza su ejecución continua
incluso si el usuario que los inició cierra su sesión.

Por convención, muchos _daemons_ tienen nombres terminados en **"d"**, como `sshd`
(gestión de conexiones SSH), `httpd` o `apache2` (servicio web), `crond` (tareas
programadas) y `systemd` (control de servicios y procesos del sistema).

Por razones de seguridad, los _daemons_ no deben ejecutarse como `root` salvo que sea
estrictamente necesario. En entornos web, por ejemplo, se suele asignar un usuario
específico como `www-data` para minimizar riesgos en caso de explotación de
vulnerabilidades.

El control de _daemons_ modernos se realiza mediante `systemctl`, que permite iniciar,
detener, reiniciar y habilitar servicios de manera uniforme:

| Comando                      | Función                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------ |
| `sudo systemctl start sshd`  | Inicia el daemon (crea el proceso).                                            |
| `sudo systemctl stop sshd`   | Detiene el daemon.                                                             |
| `sudo systemctl status sshd` | Muestra el estado, PID y consumo de recursos del daemon.                       |
| `sudo systemctl enable sshd` | Configura el daemon para que se inicie automáticamente al arrancar el sistema. |

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

Finalmente, para comprobar la conectividad con un servicio concreto mediante Telnet,
indicando la dirección IP y el puerto:

```bash linenums="1"
telnet localhost 5433
```
