---
authors: Daniel Bazo Correa
description: Fundamentos del lenguaje de programación Rust.
title: Fundamentos
---

## Bibliografía

- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
- [Repositorio aprendiendo-rust](https://github.com/danibcorr/aprendiendo-rust)

## Introducción

**Rust** es un lenguaje de programación de sistemas desarrollado originalmente por
Mozilla Research, cuyo diseño persigue tres objetivos fundamentales: seguridad de
memoria, concurrencia libre de _data races_ y rendimiento comparable al de C y C++. A
diferencia de otros lenguajes que dependen de un _garbage collector_ para gestionar la
memoria en tiempo de ejecución, Rust introduce un sistema de _ownership_ (propiedad) que
verifica la corrección del uso de la memoria en tiempo de compilación. Este enfoque
elimina categorías enteras de errores comunes, como los accesos a memoria liberada o las
condiciones de carrera, sin incurrir en penalizaciones de rendimiento.

El lenguaje resulta especialmente adecuado para el desarrollo de software de sistemas,
herramientas de línea de comandos, servicios web de alto rendimiento y cualquier
contexto en el que el control preciso sobre los recursos sea un requisito.

### Primer programa

Todo programa en Rust comienza su ejecución en la función `main`, que actúa como punto
de entrada. La macro `println!` permite imprimir texto en la salida estándar:

```rust linenums="1"
fn main() {
    println!("Hola mundo");
}
```

### Cargo

**Cargo** es la herramienta oficial de Rust que integra la gestión de paquetes, la
compilación del código y la ejecución de pruebas en un único flujo de trabajo. Cuando se
crea un proyecto con Cargo, este genera automáticamente la estructura de directorios
necesaria junto con un archivo `Cargo.toml` que describe las dependencias y la
configuración del proyecto.

```bash linenums="1"
# Crear un nuevo proyecto
cargo new nombre_proyecto

# Compilar y ejecutar en modo debug
cargo run

# Compilar y ejecutar en modo release (con optimizaciones)
cargo run --release
```

La diferencia entre ambos modos de compilación es relevante: el modo _debug_ incluye
comprobaciones adicionales (como la detección de _overflow_ aritmético) y genera código
sin optimizar para facilitar la depuración, mientras que el modo _release_ produce un
binario optimizado destinado a producción.

## Variables y constantes

En Rust, las variables se declaran con la palabra clave `let` y son **inmutables por
defecto**. Esta decisión de diseño fomenta la escritura de código más seguro y
predecible, ya que obliga al programador a ser explícito cuando desea permitir la
modificación de un valor. Para declarar una variable mutable se añade la palabra clave
`mut` tras `let`.

Las **constantes**, por su parte, se declaran con `const` y requieren siempre una
anotación de tipo explícita. A diferencia de las variables inmutables, las constantes se
evalúan en tiempo de compilación y no pueden declararse como mutables bajo ninguna
circunstancia.

```rust linenums="1"
fn main() {
    // Variable mutable: permite modificar su valor
    let mut contador: i32 = 4;
    contador += 1;
    println!("{}", contador);

    // Constante: inmutable, tipo obligatorio, evaluada en compilación
    const CONSTANTE: u8 = 6;
    println!("{}", CONSTANTE);
}
```

### _Shadowing_

El _shadowing_ consiste en redeclarar una variable con el mismo nombre mediante una
nueva sentencia `let`. A diferencia de la mutabilidad, el _shadowing_ crea una variable
completamente nueva que puede incluso tener un tipo distinto al de la original. La
variable anterior deja de ser accesible en el _scope_ actual, aunque conserva su valor
en _scopes_ superiores si la redeclaración ocurre dentro de un bloque anidado.

```rust linenums="1"
fn main() {
    let n = 5;

    {
        // Shadowing dentro de un scope diferente
        let mut n = 6;
        println!("Valor de n dentro: {}", n); // 6
        n += 1;
        println!("Valor de n dentro: {}", n); // 7
    }

    // El valor original permanece inalterado fuera del bloque
    println!("Valor de n fuera: {}", n); // 5

    // Shadowing con cambio de tipo
    let numero: i32 = 4;
    println!("{}", numero);
    let numero: &str = "Hola";
    println!("{}", numero);
}
```

## Tipos de datos

### Tipos numéricos enteros

Rust proporciona tipos enteros con y sin signo en diversos tamaños: `i8`/`u8`,
`i16`/`u16`, `i32`/`u32`, `i64`/`u64`, `i128`/`u128`, además de `isize`/`usize`. Los
tipos `isize` y `usize` tienen un tamaño que depende de la arquitectura del sistema
donde se ejecuta el programa (64 bits en sistemas de 64 bits, 32 bits en sistemas de 32
bits). El tipo `usize` se utiliza habitualmente para indexar colecciones, ya que
representa un valor sin signo del tamaño de un puntero.

En cuanto al comportamiento ante desbordamiento aritmético (_overflow_), Rust adopta una
estrategia diferente según el modo de compilación. En modo _debug_, el compilador
detecta el _overflow_ y genera un error que detiene la ejecución. En modo _release_, se
aplica _wrapping_ (el valor desborda de forma silenciosa y vuelve al inicio del rango),
lo que puede producir resultados inesperados si no se gestiona adecuadamente.

Para mejorar la legibilidad de literales numéricos extensos, Rust permite insertar
guiones bajos como separadores visuales en cualquier posición dentro del número, tanto
en enteros como en decimales.

```rust linenums="1"
fn main() {
    let a: usize = 25;
    println!("Valor máximo usize: {}", usize::MAX);
    println!("Valor mínimo usize: {}", usize::MIN);

    let a: isize = 40;
    println!("Valor máximo isize: {}", isize::MAX);
    println!("Valor mínimo isize: {}", isize::MIN);

    // Separadores visuales para legibilidad
    let variable_millon: i32 = 1_000_000;
    println!("Valor: {}", variable_millon);

    // También aplicable a decimales
    let pi: f32 = 3.141_592_7;
    println!("Pi: {}", pi);
}
```

### Punto flotante

Los tipos de punto flotante `f32` y `f64` siguen el estándar IEEE 754 para la
representación de números reales en formato binario. Debido a las limitaciones
inherentes de esta representación, determinados valores decimales no pueden expresarse
de forma exacta, lo que introduce pequeños errores de precisión. Este comportamiento no
es exclusivo de Rust, sino que afecta a cualquier lenguaje que utilice aritmética de
punto flotante.

Por esta razón, la comparación directa entre valores de punto flotante mediante el
operador `==` resulta poco fiable. La práctica recomendada consiste en calcular la
diferencia absoluta entre ambos valores y verificar que sea inferior a un umbral de
tolerancia, habitualmente representado por la constante `f64::EPSILON`.

```rust linenums="1"
fn main() {
    let a: f64 = 0.1;
    let b: f64 = 0.2;
    let c: f64 = a + b;
    const EXPECTED_VALUE: f64 = 0.3;

    // El resultado no es exactamente 0.3 (produce 0.30000000000000004)
    println!("¿c == 0.3?: {}", c == EXPECTED_VALUE); // false

    // Comparación correcta mediante tolerancia
    println!("¿c ≈ 0.3?: {}", (c - EXPECTED_VALUE).abs() < f64::EPSILON);
}
```

### Booleanos y caracteres

El tipo `bool` representa valores lógicos y admite únicamente dos estados: `true` o
`false`. Se utiliza de forma habitual en expresiones condicionales y bucles.

El tipo `char` representa un único carácter Unicode y ocupa 4 bytes en memoria, lo que
permite almacenar cualquier carácter del estándar Unicode, incluyendo emojis y
caracteres de escrituras no latinas.

```rust linenums="1"
fn main() {
    let connected: bool = false;
    println!("Conectado: {}", connected);

    let letter: char = 'z';
    println!("Letra: {}", letter);
}
```

### Conversión de tipos

La conversión entre tipos numéricos se realiza mediante la palabra clave `as`, que
efectúa un _casting_ explícito. Para convertir cadenas de texto a tipos numéricos se
utiliza el método `.parse()`, que devuelve un `Result` y requiere gestión de errores
(habitualmente mediante `.expect()` o _pattern matching_).

```rust linenums="1"
const MULTIPLICADOR: u32 = 2;

fn main() {
    let user_input = "100";
    let converted: i32 = user_input
        .parse()
        .expect("Error al convertir de str a numero");

    println!("Resultado: {}", converted * MULTIPLICADOR as i32);

    let caracter: char = 'A';
    let valor_ascii: u32 = caracter as u32;
    println!("Valor ASCII de 'A': {}", valor_ascii);
}
```

## Tipos compuestos

### Tuplas

Las tuplas permiten agrupar un número fijo de valores que pueden ser de tipos
diferentes. El acceso a los elementos individuales se realiza mediante notación de punto
seguida del índice posicional (comenzando en cero), o bien mediante _destructuring_, que
asigna cada componente a una variable independiente en una sola sentencia.

Existe un caso especial denominado _unit_ (`()`), que es una tupla vacía. En Rust, la
_unit_ representa la ausencia de valor y constituye el tipo de retorno implícito de las
funciones que no devuelven nada explícitamente.

```rust linenums="1"
fn calcular_distancia(coord_1: (f32, f32), coord_2: (f32, f32)) -> f32 {
    return ((coord_2.0.powi(2) - coord_1.0.powi(2))
        + (coord_2.1.powi(2) - coord_1.1.powi(2)))
    .sqrt();
}

fn main() {
    let tupla: (i32, i32) = (1, 2);
    println!("x: {}, y: {}", tupla.0, tupla.1);

    // Destructuring
    let (a, b) = tupla;
    println!("x: {}, y: {}", a, b);

    // Tuplas con tipos mixtos
    let tupla: (&str, u8, i32) = ("Hola", 1, 6);
    println!("Valores: {:?}", tupla);

    // Unit: tupla vacía
    let _empty: () = ();
}
```

### _Arrays_

Los _arrays_ en Rust tienen un tamaño fijo que debe conocerse en tiempo de compilación.
Se almacenan íntegramente en el _stack_, lo que los hace muy eficientes en términos de
acceso. Todos los elementos de un _array_ deben ser del mismo tipo. La sintaxis de
declaración incluye el tipo y la cantidad de elementos entre corchetes: `[T; N]`.

También es posible inicializar un _array_ con un valor repetido mediante la sintaxis
`[valor; cantidad]`, que resulta útil cuando se necesita una colección de tamaño fijo
con todos sus elementos idénticos.

```rust linenums="1"
fn main() {
    let lista: [i32; 3] = [1, 2, 3];
    println!("Contenido: {:?}", lista);

    let nombres: [&str; 4] = ["hola", "adios", "hello", "bye"];
    println!("Primer elemento: {}", nombres[0]);
    println!("Último elemento: {}", nombres[nombres.len() - 1]);

    // Inicialización con valor repetido
    let repetido = ["Dani"; 5];
    println!("Repetido: {:?}", repetido);
}
```

### Vectores

Los vectores (`Vec<T>`) constituyen la alternativa dinámica a los _arrays_. Su tamaño
puede crecer o decrecer en tiempo de ejecución, ya que almacenan sus datos en el _heap_.
Se crean habitualmente mediante la macro `vec![]` y permiten añadir elementos con el
método `.push()`.

```rust linenums="1"
fn main() {
    let mut vector: Vec<&str> = vec!["Dani", "Jorge", "Fran"];
    vector.push("Paco");
    println!("Vector: {:?}", vector);
}
```

## Funciones

Las funciones se definen con la palabra clave `fn` seguida del nombre, los parámetros
entre paréntesis y, opcionalmente, el tipo de retorno indicado con `->`. Cada parámetro
requiere una anotación de tipo explícita. El valor de retorno puede especificarse
mediante la palabra clave `return` o, de forma idiomática en Rust, omitiendo el punto y
coma en la última expresión del cuerpo de la función.

La macro `dbg!` resulta especialmente útil durante el desarrollo, ya que imprime el
archivo, la línea y el valor de una expresión en la salida de error estándar,
facilitando la depuración sin necesidad de configurar un depurador completo.

```rust linenums="1"
fn imprimir_nombre(nombre: &str) {
    println!("Hola {}!", nombre);
}

fn sumar_valores(valor_1: i32, valor_2: i32) -> isize {
    return (valor_1 + valor_2) as isize;
}

fn main() {
    imprimir_nombre("Dani");

    let resultado = sumar_valores(1, 2);
    dbg!(resultado);
}
```

### Sentencias y expresiones

Rust establece una distinción fundamental entre sentencias y expresiones. Las
**sentencias** realizan una acción pero no devuelven un valor (por ejemplo, una
declaración `let`). Las **expresiones**, en cambio, se evalúan y producen un resultado
que puede asignarse a una variable o utilizarse en otro contexto.

Los bloques delimitados por llaves `{}` actúan como expresiones cuando su última línea
no termina en punto y coma. Esta característica permite construir asignaciones complejas
de forma concisa y legible.

```rust linenums="1"
fn main() {
    // dbg! es una expresión que devuelve el valor evaluado
    let resultado: i32 = dbg!(20 + 30);
    println!("Resultado: {}", resultado); // 50

    // Bloque como expresión (sin punto y coma en la última línea)
    let suma = {
        let x = 1;
        let y = 2;
        x + y
    };
    println!("Suma: {}", suma); // 3
}
```

## Control de flujo

### Condicionales

La estructura `if`/`else` en Rust funciona de manera similar a otros lenguajes, con la
particularidad de que puede utilizarse como expresión para asignar valores directamente
a una variable. Las condiciones no requieren paréntesis, aunque las llaves que delimitan
cada bloque son obligatorias.

```rust linenums="1"
use std::io;

const MIN_LENGTH: u8 = 10;

fn main() {
    let mut input: String = String::new();
    println!("Introduce un valor: ");
    io::stdin().read_line(&mut input).expect("Error de lectura");

    if input.trim().len() >= MIN_LENGTH as usize {
        println!("Longitud suficiente");
    } else {
        println!("Demasiado corto");
    }

    // Uso de if como expresión para asignar un valor
    let es_par: bool = if input.trim().len() % 2 == 0 { true } else { false };
    println!("¿Par?: {}", es_par);
}
```

### Bucles

Rust proporciona tres construcciones para la iteración. El bucle `loop` crea una
repetición infinita que solo se interrumpe mediante `break`. El bucle `while` evalúa una
condición antes de cada iteración y continúa mientras esta sea verdadera. El bucle `for`
itera sobre los elementos de un iterador, siendo la forma más idiomática y segura de
recorrer colecciones.

Cuando se trabaja con bucles anidados, Rust permite asignar etiquetas (_labels_) a cada
bucle mediante la sintaxis `'nombre_etiqueta:`. Estas etiquetas posibilitan el uso de
`break` y `continue` dirigidos a un bucle específico, lo que resulta útil para salir de
múltiples niveles de anidamiento de forma controlada.

```rust linenums="1"
fn main() {
    // loop: bucle infinito con break explícito
    let mut contador: u8 = 0;
    loop {
        if contador >= 10 {
            break;
        }
        contador += 1;
    }

    // while: evalúa la condición antes de cada iteración
    let mut n = 3;
    while n > 0 {
        println!("{}", n);
        n -= 1;
    }

    // for con enumerate para obtener índice y valor
    let vector: Vec<i32> = vec![1, 2, 3, 4, 5];
    for (index, elem) in vector.iter().enumerate() {
        println!("Índice: {}, Elemento: {}", index, elem);
    }

    // Labels en bucles anidados
    let mut contador_principal: u8 = 0;

    'loop_principal: loop {
        contador_principal += 1;
        let mut contador_interno: u8 = 0;

        'loop_interno: loop {
            contador_interno += 1;

            if contador_interno == 10 {
                break 'loop_interno;
            }
            if contador_principal == 10 {
                break 'loop_principal;
            }
        }
    }
}
```

## _Ownership_

El sistema de _ownership_ constituye el mecanismo central mediante el cual Rust gestiona
la memoria sin recurrir a un _garbage collector_. Este sistema se rige por tres reglas
fundamentales que el compilador verifica de forma estática:

1. Cada valor en Rust tiene exactamente una variable que actúa como su **propietario**
   (_owner_).
2. Solo puede existir **un propietario** en cada momento.
3. Cuando el propietario sale del ámbito (_scope_) en el que fue declarado, el valor se
   libera automáticamente mediante la operación _drop_.

### _Stack_ y _heap_

Para comprender el _ownership_ es necesario distinguir entre las dos regiones de memoria
que utiliza un programa. El **_stack_** (pila) almacena datos cuyo tamaño se conoce en
tiempo de compilación, como enteros, referencias `&str` y _arrays_. Las operaciones
sobre el _stack_ son extremadamente rápidas porque consisten en apilar y desapilar
valores de tamaño fijo.

El **_heap_** (montículo) almacena datos cuyo tamaño puede variar en tiempo de
ejecución, como `String` o `Vec`. Cuando se crea un valor en el _heap_, el sistema
reserva un bloque de memoria y devuelve un puntero que se almacena en el _stack_ junto
con la longitud y la capacidad del dato.

### _Move_ y _clone_

Cuando se asigna una variable que contiene datos en el _heap_ a otra variable, Rust no
copia el contenido. En su lugar, transfiere la propiedad (_move_) a la nueva variable e
invalida la original, impidiendo su uso posterior. Este comportamiento previene la
liberación doble de memoria (_double free_), un error común en lenguajes como C.

Para los tipos que residen exclusivamente en el _stack_ (como los enteros), la
asignación realiza una copia completa de los bits, ya que el coste es despreciable. Si
se necesita una copia profunda de un valor en el _heap_, se utiliza el método
`.clone()`, que duplica tanto el puntero como el contenido al que apunta.

```rust linenums="1"
fn main() {
    // Tipos simples (stack): se copian automáticamente
    let a = 1;
    let b = a;
    println!("a: {}, b: {}", a, b); // Ambos válidos

    // Tipos complejos (heap): se produce un move
    let palabra: String = String::from("Hola");
    let otra = palabra; // Move: `palabra` queda invalidada
    println!("otra: {}", otra);
    // println!("{}", palabra); // Error de compilación: valor movido

    // Clone: copia profunda del contenido en el heap
    let texto: String = String::from("Prueba");
    let copia: String = texto.clone();
    println!("texto: {}, copia: {}", texto, copia); // Ambos válidos
}
```

## Referencias y _borrowing_

Las **referencias** permiten acceder al valor de una variable sin adquirir su
_ownership_. Este mecanismo se denomina _borrowing_ (préstamo) y constituye la forma
idiomática de pasar datos a funciones sin transferir la propiedad. Rust distingue dos
tipos de referencias:

- `&T`: Referencia inmutable que permite únicamente la lectura del valor. Se pueden
  mantener múltiples referencias inmutables activas de forma simultánea.
- `&mut T`: Referencia mutable que permite tanto la lectura como la escritura. Solo
  puede existir una referencia mutable activa a la vez para un mismo valor.

El compilador garantiza en tiempo de compilación que nunca coexistan referencias
mutables e inmutables sobre el mismo dato, eliminando así la posibilidad de _data
races_.

```rust linenums="1"
fn normalize_text(text: &String) -> String {
    return text.to_lowercase();
}

fn agregar_texto(text: &mut String) {
    text.push_str("!");
}

fn main() {
    let text: String = String::from("Hola");

    // Referencia inmutable: no adquiere ownership
    println!("Normalizado: {}", normalize_text(&text));
    println!("Original: {}", text); // Sigue disponible

    // Referencia mutable: permite modificar el valor
    let mut texto: String = String::from("Bob");
    agregar_texto(&mut texto);
    println!("Modificado: {}", texto); // "Bob!"

    // Múltiples referencias inmutables simultáneas: permitido
    let ref_1 = &texto;
    let ref_2 = &texto;
    println!("{}, {}", ref_1, ref_2);
}
```

!!!warning "Reglas de _borrowing_"

    El compilador aplica las siguientes restricciones sobre las referencias para garantizar
    la seguridad de memoria:

    - Se pueden mantener **múltiples referencias inmutables** (`&T`) de forma simultánea.
    - Solo se permite **una referencia mutable** (`&mut T`) activa a la vez.
    - No pueden coexistir referencias mutables e inmutables activas sobre el mismo valor.

## _Slices_

Los _slices_ son referencias a una subsecuencia contigua de elementos dentro de una
colección, sin adquirir el _ownership_ de los datos subyacentes. Se representan con el
tipo `&[T]` y se construyen especificando un rango sobre la colección original mediante
la sintaxis `&coleccion[inicio..fin]`, donde `inicio` es inclusivo y `fin` es exclusivo.

Los _slices_ resultan especialmente útiles para trabajar con porciones de _arrays_ o
vectores sin necesidad de copiar los datos, lo que los convierte en una herramienta
eficiente para el procesamiento de secuencias.

```rust linenums="1"
fn slice_lista(lista: &[i32], init: usize, end: usize) -> &[i32] {
    return &lista[init..end];
}

fn main() {
    let lista: [i32; 5] = [1, 2, 3, 4, 5];
    let slice = slice_lista(&lista, 1, 3);
    println!("{:?}", slice); // [2, 3]

    if slice == [2, 3] {
        println!("Todo correcto");
    }
}
```

## Ejemplo práctico: juego de adivinar

El siguiente programa integra varios de los conceptos presentados en este documento:
entrada y salida estándar, constantes, bucles, _pattern matching_ con `match` y gestión
de dependencias externas. El objetivo del juego consiste en adivinar un número aleatorio
dentro de un rango, disponiendo de un número limitado de intentos.

```rust linenums="1"
use rand::random_range;
use std::cmp::Ordering;
use std::io;

const VALOR_MINIMO: i32 = 0;
const VALOR_MAXIMO: i32 = 10;
const NUM_VIDAS: u8 = 3;

fn solicitar_valor() -> i32 {
    println!("Introduce un valor: ");
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Error de lectura");
    return input.trim().parse().expect("No es un valor válido");
}

fn main() {
    let secreto: i32 = random_range(VALOR_MINIMO..VALOR_MAXIMO);
    let mut vidas: u8 = 0;

    loop {
        let intento: i32 = solicitar_valor();

        match intento.cmp(&secreto) {
            Ordering::Equal => {
                println!("¡Has adivinado!");
                break;
            }
            Ordering::Less => println!("Introduce un valor mayor."),
            Ordering::Greater => println!("Introduce un valor menor."),
        }

        vidas += 1;
        if vidas == NUM_VIDAS {
            println!("Sin vidas. El valor era: {}", secreto);
            break;
        }
    }
}
```

!!!note "Dependencia externa"

    Este ejemplo requiere añadir el _crate_ `rand` como dependencia en el archivo
    `Cargo.toml` del proyecto:

    ```toml
    [dependencies]
    rand = "0.9"
    ```
