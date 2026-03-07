---
sidebar_position: 9
authors:
Daniel Bazo Correa
description: Cloud computing.
title: Cloud computing.
---

pues al final la computación en la nube, lo que permite es proporcionar recursos bajo
demanda ya sean redes, servicio de almacenamiento todo utilizando Internet. Inicialmente
es menos costoso, existe menor fricción y será permitir la colaboración como
características, pues es bajo demanda lo que se conoce como autoservicio sin
intervención humana tiene un acceso amplio a la red, es decir, que es accesible
independientemente del dispositivo con conexión a Internet y es Resource Pouring, es
decir, que hace una gestión dinámica de recursos donde se paga por lo que se usa y es
elástico, es decir que es escalable. Al final aquí se utiliza tecnología como servicio
donde tenemos nubes públicas, nubes, privadas y Y nubes híbridas, que al final es el lo
que se conoce como el tipo de modelo de despliegue de la nube, y luego tenemos modelos
de servicios donde existe el la infraestructura como servicio, la plataforma como
servicio o el software como servicio.

## Tipos de datos

pues tenemos ficheros de texto generalmente los datos se separan con delimitadores como
comas, tabuladores o cosas. Así luego tenemos el lenguaje XML, que es un lenguaje de
marcado leíble por humanos y máquinas que puede parecerse a HTML y es independiente de
la plataforma independiente del lenguaje. luego también tenemos el JSON que es un
estándar abierto para transmitir datos estructurados sobre la web independiente del
lenguaje es compatible con navegadores y muy usado en Apis.

- Formatos de datos: para datos binarios como imagenes, audio o similar podemos usar
  formatos como JPEG que estan comprimidos.
- Para metadaos (labels), datos tabulares, texto, utilizar parquets, json, txt esta bien

Podemos usar data warehouse para ETL (datos ta transformados) o Data Lakes para ELT
(datos almacenados para transformar). En la práctica ambos conviven. Yo supongo que es
porque transformar todo un flujo de datos continuo puede ser costro en el tiempo,
recursos y puede no ser requerido o quedar obsoleto, o equipos pueden requerir diferentes
tipos de transformaciones.

Existe herramientas de orquestacion con Prefect, Dogster que son alternativas a Airflow.
