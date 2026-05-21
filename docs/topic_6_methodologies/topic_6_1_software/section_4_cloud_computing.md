---
authors: Daniel Bazo Correa
description: Cloud computing y diseño de sistemas distribuidos.
title: Cloud computing
---

## Cloud computing

La computación en la nube proporciona recursos bajo demanda (redes, almacenamiento,
cómputo) a través de Internet. Sus características principales son:

- **Autoservicio bajo demanda**: Provisión de recursos sin intervención humana.
- **Acceso amplio a la red**: Accesible desde cualquier dispositivo con conexión a
  Internet.
- **Elasticidad**: Escalado automático de recursos según la demanda.
- **Pago por uso**: Se factura únicamente por los recursos consumidos.

### Modelos de despliegue

| Modelo           | Descripción                                                              |
| :--------------- | :----------------------------------------------------------------------- |
| **Nube pública** | Infraestructura compartida gestionada por un proveedor (AWS, GCP, Azure) |
| **Nube privada** | Infraestructura dedicada a una única organización                        |
| **Nube híbrida** | Combinación de nube pública y privada                                    |

### Modelos de servicio

| Modelo                                 | Descripción                                         |
| :------------------------------------- | :-------------------------------------------------- |
| **IaaS** (Infrastructure as a Service) | Se gestiona desde el sistema operativo hacia arriba |
| **PaaS** (Platform as a Service)       | Se gestiona solo la aplicación y los datos          |
| **SaaS** (Software as a Service)       | Se consume el software directamente                 |

## Diseño de sistemas distribuidos

Un buen diseño de sistemas debe contemplar escalabilidad, mantenibilidad, eficiencia y
fiabilidad.

### Teorema CAP

En sistemas distribuidos, el teorema CAP establece que solo es posible garantizar dos de
las tres propiedades siguientes simultáneamente:

| Propiedad                                          | Descripción                                                 |
| :------------------------------------------------- | :---------------------------------------------------------- |
| **Consistencia** (Consistency)                     | Todos los nodos reflejan el mismo dato en el mismo instante |
| **Disponibilidad** (Availability)                  | El sistema responde a todas las peticiones                  |
| **Tolerancia a particiones** (Partition Tolerance) | El sistema sigue funcionando ante fallos de red entre nodos |

La clave es encontrar el compromiso adecuado para cada caso de uso.

### SLO y SLA

- **SLO** (_Service Level Objectives_): Objetivos internos de rendimiento (latencia,
  disponibilidad).
- **SLA** (_Service Level Agreements_): Compromisos contractuales con los usuarios sobre
  el nivel de servicio mínimo.

### Rendimiento: _throughput_ y latencia

- **_Throughput_**: Número de peticiones procesadas por segundo.
- **Latencia**: Tiempo de respuesta desde que se recibe una petición hasta que se
  devuelve el resultado.

### Caché

La caché almacena copias de datos frecuentemente solicitados para evitar recalcularlos o
consultar la base de datos. Tipos principales:

- **Caché de navegador**: Almacena recursos estáticos en el cliente.
- **Caché de servidor/aplicación**: Almacena resultados de operaciones costosas.

El problema principal de la caché es la **invalidación**: garantizar que los datos
cacheados estén actualizados respecto a la fuente de verdad.

### CDN (_Content Delivery Network_)

Red de servidores distribuidos geográficamente que cachean contenido estático cerca del
usuario, reduciendo la latencia.

### Proxies

Un servidor proxy actúa como intermediario entre cliente y servidor. Funciones
principales: cacheo, anonimización, balanceo de carga y filtrado de tráfico.

| Tipo              | Descripción                  |
| :---------------- | :--------------------------- |
| **Forward proxy** | Actúa en nombre del cliente  |
| **Reverse proxy** | Actúa en nombre del servidor |

### Balanceadores de carga

Distribuyen el tráfico entre múltiples servidores. Se pueden colocar entre:

- Usuario y servidor web
- Servidor web y aplicación
- Aplicación y base de datos

Algoritmos comunes: _Round Robin_, _Least Connections_, _IP Hash_, _Weighted_,
_Geographic_, _Consistent Hashing_.

Los balanceadores deben ser redundantes (pueden ser un punto único de fallo), monitorear
la salud de los servidores y soportar autoescalado.

### Optimización de bases de datos

- **Índices**: Mejoran el rendimiento de lectura a costa de la escritura. Útiles para
  identificar registros de forma única sin recorrer todas las filas.
- **Particionado**: Divide bases de datos grandes en fragmentos más manejables para
  mejorar rendimiento y escalabilidad.

## Tipos de datos y almacenamiento

Los datos pueden clasificarse según su formato:

- **Texto estructurado**: CSV (delimitadores como comas o tabuladores), JSON (estándar
  abierto para datos estructurados, muy usado en APIs), XML (lenguaje de marcado legible
  por humanos y máquinas).
- **Datos binarios**: Imágenes (JPEG, PNG), audio, vídeo — formatos comprimidos.
- **Datos tabulares/metadatos**: Parquet, JSON, TXT según el caso de uso.

### Data Warehouse vs Data Lake

| Enfoque            | Proceso                        | Uso                                                    |
| :----------------- | :----------------------------- | :----------------------------------------------------- |
| **Data Warehouse** | ETL (Extract, Transform, Load) | Datos ya transformados y listos para análisis          |
| **Data Lake**      | ELT (Extract, Load, Transform) | Datos almacenados en crudo, transformados bajo demanda |

En la práctica ambos conviven, ya que transformar todo un flujo continuo puede ser
costoso y diferentes equipos pueden requerir transformaciones distintas.

Herramientas de orquestación de datos: Prefect, Dagster (alternativas a Airflow).
