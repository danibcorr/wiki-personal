---
authors: Daniel Bazo Correa
description: Librerías complementarias del ecosistema Rust.
title: Librerías
---

En el desarrollo con Rust, existen numerosas librerías (denominadas _crates_) que
facilitan la implementación de diversas funcionalidades.

A continuación, destaco algunas consideradas especialmente relevantes para crear
utilidades, herramientas de línea de comandos (CLI) o similares.

!!! info

    Se recomienda consultar la documentación oficial de cada librería y sus páginas en
    [crates.io](https://crates.io/) para obtener información detallada sobre la instalación, el
    uso y la compatibilidad de cada uno de los paquetes detallados a continuación, o incluso
    buscar nuevas alternativas, ya que con el tiempo podría ser que algunas de estas
    librerías queden obsoletas.

| Librería      | Descripción                                                                                                                                         | Etiquetas                                    |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| **clap**      | Analiza argumentos de línea de comandos mediante macros derivadas, con generación automática de ayuda, subcomandos, sugerencias y salida coloreada. | cli, argumentos, terminal, comandos, parsing |
| **console**   | Proporciona utilidades de estilización de terminal, incluyendo colores, estilos de texto y control de la salida de forma multiplataforma.           | terminal, colores, estilos, salida, tui      |
| **ctrlc**     | Captura la señal de interrupción (`Ctrl+C`) para ejecutar lógica de limpieza o finalización ordenada antes de terminar el programa.                 | señales, interrupción, ctrl-c, limpieza      |
| **dialoguer** | Crea prompts interactivos en terminal, como selectores, confirmaciones, entradas de texto y menús de selección múltiple.                            | cli, interactivo, prompts, menús, selección  |
