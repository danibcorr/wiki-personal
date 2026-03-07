---
authors: Daniel Bazo Correa
description: Introducción al desarrollo web.
title: Desarrollo Web
---

# Introducción al desarrollo web

El desarrollo web se articula en torno a tres tecnologías fundamentales que operan de
forma conjunta. HTML (_HyperText Markup Language_) define la estructura y disposición de
los elementos en la página: títulos, botones, formularios, párrafos, etc. El término
_hypertext_ hace referencia a texto que contiene enlaces a otros textos, lo que
constituye la base de la navegación web. CSS se encarga del estilo visual de esos
elementos, controlando colores, tipografías, márgenes y disposición. JavaScript gestiona
la interacción con el usuario, como el procesamiento de entradas, la comunicación con
APIs externas o la actualización dinámica del contenido sin necesidad de recargar la
página.

A estas tres tecnologías se les denomina colectivamente el **front end**, es decir, la
parte de la aplicación que el usuario ve y con la que interactúa directamente. En
contraposición, el **back end** se ocupa de la lógica del servidor, la gestión de bases
de datos, la autenticación y la exposición de APIs. Un desarrollador **full stack** es
aquel que posee conocimientos en ambas capas, abarcando todo el ciclo de vida del
producto: planificación, arquitectura, diseño, desarrollo, despliegue y mantenimiento.

La especificación de HTML está mantenida por el W3C (_World Wide Web Consortium_),
organismo que define los cambios y particularidades de cada versión del estándar.

## El modelo cliente-servidor

El modelo fundamental sobre el que se sustenta la web es el modelo **cliente-servidor**.
En este esquema, múltiples clientes (ordenadores, dispositivos móviles, etc.) se
comunican a través de Internet con un servidor centralizado, habitualmente alojado en un
centro de datos. El flujo es el siguiente: el cliente realiza una petición (_request_) al
servidor, este la procesa y devuelve una respuesta (_response_) que el cliente recibe y
muestra al usuario.

Este intercambio se rige por el protocolo **HTTP** (_HyperText Transfer Protocol_), que
define cómo se estructuran y transmiten los mensajes entre ambas partes. Para
comunicaciones seguras, se utiliza **HTTPS**, que añade una capa de encriptación antes de
transmitir el contenido. Una petición HTTP tiene la siguiente forma básica:

```
GET / HTTP/1.1
Host: ejemplo.com
```

Donde `GET` es el método utilizado, `/` es la ruta del recurso solicitado, `HTTP/1.1`
indica la versión del protocolo y `Host` es una cabecera (_header_) que especifica el
servidor de destino. Los métodos HTTP más comunes son:

- `GET`: Para obtener información de un recurso.
- `POST`: Para enviar información al servidor, como datos de un formulario.
- `PUT`: Para actualizar un recurso existente.
- `DELETE`: Para eliminar un recurso.

Las respuestas del servidor incluyen códigos de estado que indican el resultado de la
petición. Estos códigos se agrupan por rangos: los códigos 1xx corresponden a respuestas
informativas, los 2xx indican éxito; los 3xx señalan redirecciones, los 4xx reflejan
errores del cliente (como el conocido `404 Not Found`), y los 5xx indican errores del
servidor.

Cuando el navegador recibe la respuesta, procesa el contenido de forma secuencial y en
orden. Cada línea de HTML es interpretada y renderizada progresivamente, lo que se conoce
como **_page rendering_**.

## Tipos de recursos web

Dentro del ecosistema web conviene distinguir entre distintos tipos de recursos. Una
**webpage** es una única página web. Un **website** es un conjunto de webpages
interrelacionadas. Una **aplicación web**, como Spotify o Gmail, ofrece una experiencia
dinámica e interactiva, con contenido que se genera y actualiza en tiempo real.

En cuanto al contenido, existe una distinción entre páginas **estáticas** y
**dinámicas**. En las páginas dinámicas, el contenido se genera en el servidor en el
momento de la petición y se envía al navegador. Para reducir el número de peticiones y
mejorar el rendimiento, se recurre a la **caché**, que almacena temporalmente recursos ya
descargados.

## Hosting

El **hosting** es el servicio que permite alojar una aplicación o sitio web en un
servidor accesible a través de Internet. Existen principalmente dos modalidades.

El **hosting compartido** distribuye los recursos de un mismo servidor físico entre
múltiples clientes, de modo que varias webs comparten CPU, memoria y almacenamiento. Su
principal ventaja es el bajo coste, lo que lo hace adecuado para proyectos pequeños o en
fase de desarrollo con poca demanda.

El **hosting dedicado**, en cambio, reserva los recursos del servidor en exclusiva para
un único cliente. Esto ofrece mayor flexibilidad, rendimiento y control, aunque a un
coste significativamente superior. Es la opción habitual para aplicaciones con alta
demanda o requisitos estrictos de seguridad y disponibilidad.

## Librerías, frameworks y APIs

En el desarrollo web es importante distinguir entre librerías y frameworks. Una
**librería** es un conjunto reducido de funcionalidades que resuelve un problema
específico, como la validación de datos. Un **framework** agrupa un conjunto de librerías
y establece una estructura de trabajo más amplia, pudiendo alterar la forma en que se
desarrolla el proyecto. Ejemplos de frameworks son TypeScript, Astro o Docusaurus. Las
librerías de Node.js se gestionan mediante **npm** (_Node Package Manager_), su gestor de
paquetes oficial.

Las **APIs** (_Application Programming Interface_) actúan como intermediarias entre el
usuario y un servicio, exponiendo funcionalidades de forma controlada. Existen varios
tipos relevantes en el contexto web. Las **Browser APIs** extienden las capacidades del
navegador, como `Fetch` para realizar peticiones HTTP, `Canvas` para renderizado gráfico
o la `History API` para gestionar el historial de navegación. Las **REST APIs** son un
conjunto de principios arquitectónicos para construir APIs eficientes y escalables sobre
HTTP. Por último, las **Sensor-based APIs** permiten interactuar con sensores físicos en
dispositivos IoT.

## HTML: estructura y etiquetas

HTML estructura el contenido mediante **etiquetas** (_tags_) y **elementos**. A
continuación se presentan las etiquetas más habituales:

```html
<!-- Párrafo -->
<p>Texto del párrafo.</p>

<!-- Salto de línea (no requiere etiqueta de cierre) -->
<br />

<!-- Énfasis semántico e importancia -->
<strong>Texto importante</strong>
<em>Texto enfatizado</em>

<!-- Negrita e itálica (estilo visual) -->
<b>Negrita</b>
<i>Itálica</i>

<!-- Lista no ordenada -->
<ul>
  <li>Elemento 1</li>
  <li>Elemento 2</li>
</ul>

<!-- Lista ordenada -->
<ol>
  <li>Elemento 1</li>
  <li>Elemento 2</li>
</ol>

<!-- División sin estilo propio -->
<div>
  <h1>Hola</h1>
</div>

<!-- Enlace -->
<a href="pagina.html">Texto del enlace</a>

<!-- Imagen -->
<img src="image.png" height="300" width="300" />

<!-- Formulario de entrada -->
<input type="text" placeholder="Escribe aquí" />
```

## El DOM

El **DOM** (_Document Object Model_) es una representación en forma de árbol de todos los
elementos de una página HTML. Cuando el navegador carga una página, construye esta
estructura jerárquica a partir del código HTML, donde cada etiqueta se convierte en un
nodo del árbol. Por ejemplo, el nodo raíz sería `<html>`, del que parten `<head>` y
`<body>`, y de estos, sus respectivos elementos hijos.

El DOM es inicialmente estático, pero gracias a JavaScript es posible manipularlo
dinámicamente: añadir, eliminar o modificar elementos sin recargar la página. Este es
precisamente el principio sobre el que se construyen frameworks como React.

Es buena práctica considerar siempre la **accesibilidad** al desarrollar interfaces web.
Para ello, se puede consultar la **WAI** (_Web Accessibility Initiative_) y el estándar
**ARIA** (_Accessible Rich Internet Applications_), que proporcionan guías y atributos
para hacer el contenido web accesible a personas con diversidad funcional.

## CSS: estilos y selectores

CSS (_Cascading Style Sheets_) define el aspecto visual de los elementos HTML. Su
sintaxis básica consiste en un **selector**, que identifica el elemento a estilizar,
seguido de un **bloque de declaración** con pares propiedad-valor:

```css
h1 {
  color: purple;
}
```

Para vincular una hoja de estilos externa a un documento HTML, se incluye la siguiente
etiqueta en el `<head>`:

```html
<head>
  <link rel="stylesheet" href="style.css" />
</head>
```

CSS ofrece varios tipos de selectores para aplicar estilos con distintos niveles de
especificidad:

```css
/* Selector de elemento */
p {
  color: blue;
}

/* Selector de ID (único en la página) */
#mi-id {
  color: blue;
}

/* Selector de clase (reutilizable) */
.mi-clase {
  color: blue;
}

/* Elemento con clase específica */
p.mi-clase {
  color: blue;
}

/* Selector descendente */
#blog p {
  color: blue;
}

/* Selector hijo directo */
h2 > span {
  color: blue;
}

/* Pseudo-clase (estado del elemento) */
a:hover {
  color: blue;
}
```

Y su correspondencia en HTML:

```html
<p>Selector de elemento</p>
<p id="mi-id">Selector de ID</p>
<p class="mi-clase">Selector de clase</p>

<div id="blog">
  <p>Selector descendente</p>
</div>

<h2><span>Selector hijo directo</span></h2>
<a href="#">Pseudo-clase hover</a>
```

## El modelo de caja

En CSS, cada elemento HTML se representa como una **caja** (_box model_) compuesta por
cuatro capas concéntricas. La más interna es el **contenido**, cuyo tamaño se controla
con las propiedades `width`, `min-width`, `max-width`, `height`, `min-height` y
`max-height`. Alrededor del contenido se encuentra el **padding** (relleno interno), que
separa el contenido del borde. El **border** rodea el padding y puede ser de tipo
`solid`, `dashed` (discontinuo), `dotted` (punteado) o `double` (doble). Finalmente, el
**margin** es el espacio exterior que separa la caja de otros elementos.

Las dimensiones de la caja se calculan de la siguiente forma:

$$\text{padding-box width} = \text{content width} + \text{padding-left} + \text{padding-right}$$

$$\text{padding-box height} = \text{content height} + \text{padding-top} + \text{padding-bottom}$$

Los elementos HTML se clasifican en dos tipos según su comportamiento en el flujo del
documento. Los **elementos de bloque** (`div`, `form`, `h1`, `h2`, etc.) ocupan todo el
ancho disponible y generan un salto de línea antes y después. Los **elementos de línea**
(`a`, `img`, `input`, `b`, etc.) ocupan únicamente el espacio de su contenido y no
interrumpen el flujo del texto.

## Diseño responsive y Bootstrap

El **diseño responsive** consiste en adaptar la presentación de una web a distintos
tamaños de pantalla y resoluciones. Se apoya en tres pilares: **flexible grids** (mallas
flexibles), **fluid images** (imágenes fluidas) y **media queries** (consultas de medios
que aplican estilos según las características del dispositivo).

**Bootstrap** es una librería de CSS y JavaScript que facilita la creación de interfaces
responsive mediante componentes reutilizables y un sistema de mallas predefinido. Su
sistema de rejilla se basa en una jerarquía de 12 columnas y se estructura siempre con un
contenedor (`container`), filas (`row`) y columnas (`col`):

```html
<div class="container">
  <div class="row">
    <!-- Ocupa 12 columnas en móvil, 6 en pantallas grandes (≥992px) -->
    <div class="col-12 col-lg-6">Contenido</div>
  </div>
</div>
```

Bootstrap sigue el enfoque **mobile first**: los estilos base se aplican a pantallas
pequeñas y los **breakpoints** (como `lg` para pantallas de 992px o más) permiten
sobreescribir el diseño para pantallas mayores. Las herramientas de desarrollo del
navegador permiten simular distintos dispositivos para verificar el comportamiento
responsive.

## React y el Virtual DOM

**React** es una librería de JavaScript, no un framework, diseñada para construir
interfaces de usuario mediante **componentes** reutilizables e independientes. Cada
componente encapsula su propia lógica y presentación, lo que facilita el testing y la
reutilización a lo largo del proyecto.

React introduce el concepto de **Virtual DOM**: una representación en memoria del DOM
real de la página. Cuando el estado de la aplicación cambia, React actualiza primero el
Virtual DOM y lo compara con su versión anterior mediante un proceso de reconciliación
(_diffing_). Solo los nodos que han cambiado se actualizan en el DOM real del navegador,
lo que minimiza las operaciones costosas de manipulación del DOM y mejora
significativamente el rendimiento.
