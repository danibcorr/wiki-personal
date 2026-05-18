---
authors: Daniel Bazo Correa
description: Introducción al desarrollo web.
title: Fundamentos
---

# Introducción al desarrollo web

El desarrollo web se articula en torno a tres tecnologías fundamentales que operan de
forma conjunta. HTML (_HyperText Markup Language_) define la estructura y disposición de
los elementos en la página, tales como títulos, botones, formularios o párrafos. El
término _hypertext_ hace referencia a texto que contiene enlaces a otros textos, lo que
constituye la base de la navegación web. CSS (_Cascading Style Sheets_) se encarga del
estilo visual de esos elementos, controlando colores, tipografías, márgenes y
disposición espacial. JavaScript, por su parte, gestiona la interacción con el usuario,
abarcando desde el procesamiento de entradas hasta la comunicación con APIs externas o
la actualización dinámica del contenido sin necesidad de recargar la página.

A estas tres tecnologías se las denomina colectivamente _front end_, es decir, la parte
de la aplicación que el usuario ve y con la que interactúa directamente. En
contraposición, el _back end_ se ocupa de la lógica del servidor, la gestión de bases de
datos, la autenticación y la exposición de APIs. Un desarrollador _full stack_ es aquel
que posee conocimientos en ambas capas, abarcando todo el ciclo de vida del producto:
planificación, arquitectura, diseño, desarrollo, despliegue y mantenimiento.

La especificación de HTML está mantenida por el W3C (_World Wide Web Consortium_),
organismo que define los cambios y particularidades de cada versión del estándar.

## El modelo cliente-servidor

El modelo fundamental sobre el que se sustenta la web es el modelo **cliente-servidor**.
En este esquema, múltiples clientes (ordenadores, dispositivos móviles, entre otros) se
comunican a través de Internet con un servidor centralizado, habitualmente alojado en un
centro de datos. El flujo de comunicación sigue un patrón definido: el cliente realiza
una petición (_request_) al servidor, este la procesa y devuelve una respuesta
(_response_) que el cliente recibe y presenta al usuario.

Este intercambio se rige por el protocolo **HTTP** (_HyperText Transfer Protocol_), que
define cómo se estructuran y transmiten los mensajes entre ambas partes. Para
comunicaciones seguras se utiliza **HTTPS**, que añade una capa de cifrado antes de
transmitir el contenido. Una petición HTTP presenta la siguiente forma básica:

???+ example "Ejemplo: Petición HTTP"

    ```bash linenums="1"
    GET / HTTP/1.1
    Host: ejemplo.com
    ```

En esta petición, `GET` es el método utilizado, `/` es la ruta del recurso solicitado,
`HTTP/1.1` indica la versión del protocolo y `Host` es una cabecera (_header_) que
especifica el servidor de destino. Los métodos HTTP más comunes son:

- `GET`: Obtiene información de un recurso.
- `POST`: Envía información al servidor, como datos de un formulario.
- `PUT`: Actualiza un recurso existente.
- `DELETE`: Elimina un recurso.

Las respuestas del servidor incluyen códigos de estado que indican el resultado de la
petición. Estos códigos se agrupan por rangos: los códigos 1xx corresponden a respuestas
informativas, los 2xx indican éxito, los 3xx señalan redirecciones, los 4xx reflejan
errores del cliente (como el conocido `404 Not Found`) y los 5xx indican errores del
servidor.

Cuando el navegador recibe la respuesta, procesa el contenido de forma secuencial. Cada
línea de HTML es interpretada y renderizada progresivamente, proceso que se conoce como
_page rendering_.

## Tipos de recursos web

Dentro del ecosistema web conviene distinguir entre distintos tipos de recursos. Una
_webpage_ es una única página web. Un _website_ es un conjunto de _webpages_
interrelacionadas. Una **aplicación web**, como Spotify o Gmail, ofrece una experiencia
dinámica e interactiva, con contenido que se genera y actualiza en tiempo real.

En cuanto al contenido, existe una distinción importante entre páginas **estáticas** y
**dinámicas**. En las páginas estáticas, el contenido permanece invariable y se sirve
tal cual está almacenado en el servidor. En las páginas dinámicas, el contenido se
genera en el servidor en el momento de la petición y se envía al navegador adaptado al
contexto. Para reducir el número de peticiones y mejorar el rendimiento se recurre a la
**caché**, un mecanismo que almacena temporalmente recursos ya descargados para evitar
solicitarlos de nuevo.

## _Hosting_

El _hosting_ es el servicio que permite alojar una aplicación o sitio web en un servidor
accesible a través de Internet. Existen principalmente dos modalidades.

El **_hosting_ compartido** distribuye los recursos de un mismo servidor físico entre
múltiples clientes, de modo que varias webs comparten CPU, memoria y almacenamiento. Su
principal ventaja es el bajo coste, lo que lo hace adecuado para proyectos pequeños o en
fase de desarrollo con poca demanda de tráfico.

El **_hosting_ dedicado**, en cambio, reserva los recursos del servidor en exclusiva
para un único cliente. Esto ofrece mayor flexibilidad, rendimiento y control, aunque a
un coste significativamente superior. Es la opción habitual para aplicaciones con alta
demanda o requisitos estrictos de seguridad y disponibilidad.

## Librerías, _frameworks_ y APIs

En el desarrollo web es importante distinguir entre librerías y _frameworks_. Una
**librería** es un conjunto reducido de funcionalidades que resuelve un problema
específico, como la validación de datos. Un **_framework_** agrupa un conjunto de
librerías y establece una estructura de trabajo más amplia, pudiendo alterar la forma en
que se desarrolla el proyecto. Ejemplos de _frameworks_ son TypeScript, Astro o
Docusaurus. Las librerías de Node.js se gestionan mediante **npm** (_Node Package
Manager_), su gestor de paquetes oficial.

Las **APIs** (_Application Programming Interface_) actúan como intermediarias entre el
usuario y un servicio, exponiendo funcionalidades de forma controlada. Existen varios
tipos relevantes en el contexto web. Las _Browser APIs_ extienden las capacidades del
navegador, como `Fetch` para realizar peticiones HTTP, `Canvas` para renderizado gráfico
o la _History API_ para gestionar el historial de navegación. Las _REST APIs_
constituyen un conjunto de principios arquitectónicos para construir APIs eficientes y
escalables sobre HTTP. Por último, las _Sensor-based APIs_ permiten interactuar con
sensores físicos en dispositivos IoT.

## HTML: estructura y etiquetas

HTML estructura el contenido mediante **etiquetas** (_tags_) y **elementos**. Cada
etiqueta define un tipo de contenido o comportamiento dentro del documento. Las
etiquetas pueden ser de apertura y cierre (como `<p>...</p>`) o autocontenidas (como
`<br />`). A continuación se presentan las etiquetas más habituales:

???+ example "Ejemplo: Etiquetas HTML básicas"

    ```html linenums="1"
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

### Ejemplo práctico: sitio web multipágina

El siguiente ejemplo ilustra un sitio web sencillo con navegación entre páginas, uso de
imágenes y listas. La página principal actúa como punto de entrada y enlaza con páginas
secundarias:

???+ example "Ejemplo: Página principal con enlaces y listas"

    ```html linenums="1"
    <!doctype html>
    <html>
      <head>
        <title>Titulo pestaña</title>
      </head>
      <body>
        <h1>Titulo en H1</h1>
        <h2>Esto es un titulo con el tag H2</h2>
        <p>Nah de locos de aqui a ser full stack data scientist</p>
        <ul>
          <li>Como nos gustan los bullet points</li>
          <li>Aquí tienes uno</li>
          <li>Aquí tienes otro</li>
          <ul>
            <li>Aquí lo tienes dentro</li>
          </ul>
        </ul>
        <a href="./pages/pagina_1.html">Pincha aqui</a>
        <p>Si quieres ver tablas, <a href="./pages/pagina_2.html">Pulsa aqui</a></p>
      </body>
    </html>
    ```

???+ example "Ejemplo: Página con imagen"

    ```html linenums="1"
    <!doctype html>
    <html>
      <head>
        <title>Pagina 1</title>
      </head>
      <body>
        <h1>Eres un crack</h1>
        <p>Por pulsar el boton<br />venga antes de irte, una fotito</p>
        <p>
          <img
            src="../assets/imagen.jpg"
            height="200"
            width="500"
            alt="Imagen de un mono riendo."
          />
          <br />
          <em>No te preocupes, no eres tú :)</em>
        </p>
        <p>Ahora vuelve pa' tras, <a href="../index.html">pulsame</a></p>
      </body>
    </html>
    ```

???+ example "Ejemplo: Formulario de registro"

    ```html linenums="1"
    <!doctype html>
    <html>
      <head>
        <title>Formulario</title>
      </head>
      <body>
        <h1>Registro</h1>
        <form action="/registration" method="POST">
          <label for="username">Introduce tu nombre de usuario:</label><br />
          <input type="text" name="username" /><br /><br />
          <label for="password">Introduce tu contraseña:</label><br />
          <input type="password" />
          <input type="submit" />
        </form>
      </body>
    </html>
    ```

## El DOM

El **DOM** (_Document Object Model_) es una representación en forma de árbol de todos
los elementos de una página HTML. Cuando el navegador carga una página, construye esta
estructura jerárquica a partir del código fuente, donde cada etiqueta se convierte en un
nodo del árbol. El nodo raíz es `<html>`, del que parten `<head>` y `<body>`, y de
estos, sus respectivos elementos hijos.

El DOM es inicialmente estático, pero gracias a JavaScript es posible manipularlo
dinámicamente: añadir, eliminar o modificar elementos sin recargar la página. Este es
precisamente el principio sobre el que se construyen _frameworks_ como React.

Es buena práctica considerar siempre la **accesibilidad** al desarrollar interfaces web.
Para ello se puede consultar la **WAI** (_Web Accessibility Initiative_) y el estándar
**ARIA** (_Accessible Rich Internet Applications_), que proporcionan guías y atributos
para hacer el contenido web accesible a personas con diversidad funcional.

## CSS: estilos y selectores

CSS (_Cascading Style Sheets_) define el aspecto visual de los elementos HTML. Su
sintaxis básica consiste en un **selector**, que identifica el elemento a estilizar,
seguido de un **bloque de declaración** con pares propiedad-valor:

???+ example "Ejemplo: Sintaxis básica de CSS"

    ```css linenums="1"
    h1 {
      color: purple;
    }
    ```

Para vincular una hoja de estilos externa a un documento HTML se incluye la siguiente
etiqueta en el `<head>`:

???+ example "Ejemplo: Vincular hoja de estilos"

    ```html linenums="1"
    <head>
      <link rel="stylesheet" href="style.css" />
    </head>
    ```

CSS ofrece varios tipos de selectores para aplicar estilos con distintos niveles de
especificidad. El **selector de elemento** aplica estilos a todas las instancias de una
etiqueta. El **selector de ID** (precedido por `#`) identifica un elemento único en la
página. El **selector de clase** (precedido por `.`) permite reutilizar estilos en
múltiples elementos. Además, existen selectores descendentes, selectores de hijo directo
y pseudo-clases que permiten aplicar estilos según el estado del elemento:

???+ example "Ejemplo: Tipos de selectores CSS"

    ```css linenums="1"
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

    ```html linenums="1"
    <p>Selector de elemento</p>
    <p id="mi-id">Selector de ID</p>
    <p class="mi-clase">Selector de clase</p>

    <div id="blog">
      <p>Selector descendente</p>
    </div>

    <h2><span>Selector hijo directo</span></h2>
    <a href="#">Pseudo-clase hover</a>
    ```

### Ejemplo práctico: tabla con estilos CSS

El siguiente ejemplo muestra una página con una tabla estilizada mediante una hoja de
estilos externa. Se observa cómo la etiqueta `<link>` conecta el documento HTML con el
archivo CSS que define las propiedades visuales de la tabla:

???+ example "Ejemplo: Página con tabla"

    ```html linenums="1"
    <!doctype html>
    <html>
      <head>
        <title>Título</title>
        <link rel="stylesheet" href="../css/stylesheet.css" />
      </head>
      <body>
        <table>
          <tr>
            <th>Columna 1</th>
            <th>Columna 2</th>
          </tr>
          <tr>
            <td>Fila 1</td>
            <td>10€</td>
          </tr>
          <tr>
            <td>Fila 2</td>
            <td>10€</td>
          </tr>
        </table>
        <a href="../index.html">Home</a>
      </body>
    </html>
    ```

    Y su hoja de estilos asociada (`stylesheet.css`):

    ```css linenums="1"
    table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
        border-radius: 100px;
    }
    ```

## El modelo de caja

<figure markdown="span">
  ![CSS Padding](https://media.geeksforgeeks.org/wp-content/uploads/20251028152632603398/css_padding.webp)
  <figcaption>CSS Padding</figcaption>
</figure>

En CSS, cada elemento HTML se representa como una **caja** (_box model_) compuesta por
cuatro capas concéntricas. La más interna es el **contenido**, cuyo tamaño se controla
con las propiedades `width`, `min-width`, `max-width`, `height`, `min-height` y
`max-height`. Alrededor del contenido se encuentra el **_padding_** (relleno interno),
que separa el contenido del borde. El **_border_** rodea el _padding_ y puede adoptar
estilos como `solid`, `dashed` (discontinuo), `dotted` (punteado) o `double` (doble).
Finalmente, el **_margin_** es el espacio exterior que separa la caja de otros elementos
adyacentes.

Las dimensiones totales de la caja se calculan de la siguiente forma:

$$\text{padding-box width} = \text{content width} + \text{padding-left} + \text{padding-right}$$

$$\text{padding-box height} = \text{content height} + \text{padding-top} + \text{padding-bottom}$$

Los elementos HTML se clasifican en dos tipos según su comportamiento en el flujo del
documento. Los **elementos de bloque** (`div`, `form`, `h1`, `h2`, entre otros) ocupan
todo el ancho disponible y generan un salto de línea antes y después. Los **elementos de
línea** (`a`, `img`, `input`, `b`, entre otros) ocupan únicamente el espacio de su
contenido y no interrumpen el flujo del texto.

## Diseño _responsive_ y Bootstrap

El **diseño _responsive_** consiste en adaptar la presentación de una web a distintos
tamaños de pantalla y resoluciones. Se apoya en tres pilares: _flexible grids_ (mallas
flexibles), _fluid images_ (imágenes fluidas) y _media queries_ (consultas de medios que
aplican estilos según las características del dispositivo).

**Bootstrap** es una librería de CSS y JavaScript que facilita la creación de interfaces
_responsive_ mediante componentes reutilizables y un sistema de mallas predefinido. Su
sistema de rejilla se basa en una jerarquía de 12 columnas y se estructura siempre con
un contenedor (`container`), filas (`row`) y columnas (`col`):

???+ example "Ejemplo: Sistema de rejilla de Bootstrap"

    ```html linenums="1"
    <div class="container">
      <div class="row">
        <!-- Ocupa 12 columnas en móvil, 6 en pantallas grandes (≥992px) -->
        <div class="col-12 col-lg-6">Contenido</div>
      </div>
    </div>
    ```

Bootstrap sigue el enfoque _mobile first_: los estilos base se aplican a pantallas
pequeñas y los _breakpoints_ (como `lg` para pantallas de 992px o más) permiten
sobreescribir el diseño para pantallas mayores. Las herramientas de desarrollo del
navegador permiten simular distintos dispositivos para verificar el comportamiento
_responsive_.

### Ejemplo práctico: navegación con Bootstrap

El siguiente ejemplo muestra dos páginas con navegación entre ellas utilizando
componentes de Bootstrap. Se observa cómo se incluyen tanto la hoja de estilos como el
_bundle_ de JavaScript de Bootstrap a través de un CDN:

???+ example "Ejemplo: Página principal con Bootstrap"

    ```html linenums="1"
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Bootstrap demo</title>
        <link
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
          rel="stylesheet"
          integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB"
          crossorigin="anonymous"
        />
      </head>
      <body>
        <script
          src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
          integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI"
          crossorigin="anonymous"
        ></script>
        <div>
          <h1>Hello, world!</h1>
          <button
            type="button"
            class="btn btn-primary"
            onclick="location.href = './page2.html'"
          >
            Primary
          </button>
        </div>
      </body>
    </html>
    ```

???+ example "Ejemplo: Segunda página con Bootstrap"

    ```html linenums="1"
    <!doctype html>
    <html lang="en">
      <head>
        <title>Pagina 2</title>
        <link
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
          rel="stylesheet"
          integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB"
          crossorigin="anonymous"
        />
      </head>
      <body>
        <script
          src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
          integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI"
          crossorigin="anonymous"
        ></script>
        <div>
          <h1>Página 2</h1>
          <p>Estas en la página 2.</p>
        </div>
        <div>
          <button
            type="button"
            class="btn btn-primary"
            onclick="location.href = 'index.html'"
          >
            Home
          </button>
        </div>
      </body>
    </html>
    ```

## React y el _Virtual DOM_

**React** es una librería de JavaScript diseñada para construir interfaces de usuario
mediante **componentes** reutilizables e independientes. Es importante señalar que React
no es un _framework_, sino una librería centrada exclusivamente en la capa de
presentación. Cada componente encapsula su propia lógica y presentación, lo que facilita
tanto el _testing_ como la reutilización a lo largo del proyecto.

React introduce el concepto de **_Virtual DOM_**: una representación en memoria del DOM
real de la página. Cuando el estado de la aplicación cambia, React actualiza primero el
_Virtual DOM_ y lo compara con su versión anterior mediante un proceso de reconciliación
denominado _diffing_. Solo los nodos que han cambiado se actualizan en el DOM real del
navegador, lo que minimiza las operaciones costosas de manipulación directa del DOM y
mejora significativamente el rendimiento de la aplicación.
