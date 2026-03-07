---
sidebar_position: 9
authors:
Daniel Bazo Correa
description: Fundamentos de Software.
title: Fundamentos de Software.
---

## Versionado de código, SemVer

El semantic versioning consiste en un sistema para controlar el software y estandarizar
como la versión refleja el cambio del código. Este viene representado por tres letras
principales que son la X, la I y la Z donde la X significan versiones grandes la y
versiones medias y la Z son Patch son soluciones arreglos de box y se van realizando
incrementos de uno.

El inicio de un proyecto empieza con una versión Millor en cero el valor del pack es
decir de la Z. Se incrementa cuando se arreglan fallos de código que sean compatibles con
todo lo existente una versión menor la Y, pues se incrementa cuando se añade una nueva
funcionalidad compatible con el resto del código existente y una versión mayor pues
incrementa cuando un nuevo cambio o nueva funcionalidad rompe con algo existente.

Podemos añadir incluso etiquetas adicionales como pre Release, que al final pues tienen
John lo que se conocen como identificadores por ejemplo una versión que es 3.1.4 es mayor
que la versión 3.1.4-pre-release.

## Diseño sistemas

Un buen diseño debe incluir escalabilidad, mantenibilidad, eficiencia y fiabilidad. Es lo
que se conoce como el teorema Cap C a P para crear sistemas distribuidos donde uno la
consistencia es un un cambio un dato en uno de un sistema distribuido debe estar
reflejado en el resto de nodos como fichero compartido de Google Dox por ejemplo la
disponibilidad tiene que ser que el servicio esté disponible para ser usado no tiene que
ser tolerable a particiones, es decir que tiene éxito tiene que existir redundancia.
Según este teorema solo podemos conseguir dos de tres haciendo compromisos la idea es
encontrar la mejor solución posible para nuestro caso en particular. Para ello tenemos en
cuenta los S Leo y ese lea los S.L. o son los service Level Objectif que son definiciones
objetivos como niveles de latencia disponibilidad requerida y las S.L.A. son los service
Level Agreement es ver si se cumple con los objetivos que es lo mínimo para cumplir decir
que la velocidad de un sistema pues al final vienen en medido por dos parámetros o que
veáis principales que son el truco de la latencia, el throughput se puede medir como el
número de respuestas por segundo, que serían las peticiones de los usuarios en el número
de acuerdos por segundo o las peticiones que sean las peticiones de la base de datos y la
latencia, pues se mide en el tiempo de respuesta.

Podemos utilizar mecanismos de cacheo para almacenar copias de datos para devolverla sin
rehacerlas para ello podemos utilizar la caché del navegador utilizando pases datos
cacheadas o podemos utilizar server caché por ejemplo para escribir para Right round
Right True Out Right veis que es lo que se llama como se ve en ese también podemos
calcular tener un radio de caché podemos utilizar por Isis para borrar caché como el

tenemos que un servidor Proxy permite cachear recursos Anonim izar peticiones, hacer
balanceo de carga, recibe peticiones del usuario y lo manda al servidor oportuno. Para
ello tenemos el forward proxy, reverse, open, transparent, anonymous, distorting y high
aanonimity proxy.

Tenemos balanceadores de carga, por ejemplo round robbin, least connection, least
responde time ip hash, weighted algorithms, geographic, cosisten hashing. Los
balanceadores de carga, pues lo que te van a hacer es medir la salud continuamente del
sistema luego también tiene que existir cierta redundancia para estos balanceadores de
carga tienen que permitir el auto escalado y luego también la autogestión de fallos, lo
que se conoce como el self healing,

- CAP theorem para sistemas distribuidos.

- Los load balancer se pueden colocar entre el usuario y el servidor, entre servidores y
  aplicaciones y entre aplicaciones y bases de datos. Existen varios algoritmos para los
  balanceadores de carga. Podemos poner varios load balancer por redundancia, ya que
  pueden ser tambien un punto de fallo.

- Para reducir el compute/coste de operaciones petitivas utilizamos caché que suele ser
  más rápida de acceder que a una base de datos. Eso se conoce como caché de
  aplicaciones.

- Content Delivery Network (CDN) es muy útil para servir contenido estático, cachea
  información cerca del usuario, lo que permite reducir latencia.

- El problema de la caché es cuando la información que almacena no corresponde con la
  información (la última información más actual) de la base de datos. Para solventarlo,
  existen sistemas de invalidación de caché. También existen mecanismos para eliminar
  información de la caché.

- En SQL podemos mejorar rendimiento de queries utilizando indices, p.ej. para
  identificar personas de manera única, en vez de recorrer todas las filas. Esto mejora
  el rendimiento de lectura pero empeora el rendimiento de escritura.

- Podemos dividir bases de datos grandes, creando particiones. Para ello existen técnicas
  de partición.
