---
authors: Daniel Bazo Correa
description: Infraestructura como código, categorías de herramientas y beneficios.
title: Infraestructura como código
---

## Introducción

La Infraestructura como Código (_Infrastructure as Code_) consiste en definir y
gestionar la infraestructura mediante código versionado. Este enfoque garantiza
reproducibilidad, trazabilidad y coherencia entre entornos, permitiendo crear y destruir
infraestructuras de forma automatizada y predecible.

Docker y plataformas de orquestación como Kubernetes desempeñan un papel central en IaC,
al facilitar la gestión de contenedores, la automatización de despliegues y la
alineación entre los entornos de desarrollo, pruebas y producción. Tratar la
infraestructura como un artefacto más del software refuerza la eficiencia operativa y
reduce la dependencia de configuraciones manuales.

## Categorías de herramientas

Existen cuatro categorías principales de herramientas para gestionar la infraestructura
como código, cada una orientada a un nivel distinto del ciclo de vida de la
infraestructura:

| Categoría                    | Descripción                                                                                                                                                                                                                                                                                       | Ejemplo                                     |
| :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------ |
| **Scripts ad hoc**           | Scripts escritos en Bash, Python u otro lenguaje que ejecutan comandos para configurar servidores. Son el enfoque más básico y directo, pero difíciles de mantener y escalar.                                                                                                                     | Script Bash para instalar paquetes          |
| **Gestión de configuración** | Herramientas diseñadas para instalar y gestionar software en servidores existentes. Ofrecen idempotencia, estructura y convenciones que facilitan la gestión de múltiples servidores.                                                                                                             | Ansible, Chef, Puppet                       |
| **Plantillas de servidor**   | Herramientas que crean imágenes de servidor preconfiguradas (_snapshots_) con todo el software y la configuración necesarios. Promueven la infraestructura inmutable: en lugar de modificar servidores existentes, se reemplazan por nuevas instancias creadas a partir de la imagen actualizada. | Packer                                      |
| **Aprovisionamiento**        | Herramientas que crean y gestionan los propios recursos de infraestructura (servidores, redes, balanceadores de carga, bases de datos). Definen la infraestructura de forma declarativa y gestionan su ciclo de vida completo.                                                                    | OpenTofu, Terraform, Pulumi, CloudFormation |

!!! tip "Complementariedad"

    Estas categorías no son excluyentes. Un flujo típico puede combinar Packer para crear
    imágenes base, Ansible para configurar el software dentro de esas imágenes, y
    OpenTofu/Terraform para aprovisionar los servidores y la red donde se despliegan.

## Beneficios

Cuando la infraestructura se define como código, se habilitan prácticas de ingeniería de
software que mejoran significativamente los procesos de entrega:

| Beneficio                 | Descripción                                                                                                                                                                                                                    |
| :------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Velocidad y seguridad** | Los despliegues automatizados son más rápidos y menos propensos a errores humanos que las configuraciones manuales. Se pueden ejecutar de forma consistente y repetible.                                                       |
| **Documentación**         | El propio código actúa como documentación viva de la infraestructura. Cualquier miembro del equipo puede consultar el estado actual del sistema revisando el repositorio.                                                      |
| **Control de versiones**  | Al almacenar la infraestructura en un sistema de control de versiones (Git), se obtiene un historial completo de cambios, la capacidad de revertir a estados anteriores y la posibilidad de auditar quién cambió qué y cuándo. |
| **Validación**            | Se pueden aplicar revisiones de código, análisis estático, pruebas automatizadas y políticas de cumplimiento sobre la infraestructura antes de desplegarla.                                                                    |
| **Autoservicio**          | Los equipos de desarrollo pueden aprovisionar sus propios entornos sin depender de un equipo de operaciones, utilizando módulos y plantillas predefinidas y validadas.                                                         |
| **Reutilización**         | La infraestructura se puede empaquetar en módulos reutilizables que encapsulan buenas prácticas y se comparten entre equipos y proyectos.                                                                                      |
