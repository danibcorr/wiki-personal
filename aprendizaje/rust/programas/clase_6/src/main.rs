fn main() {
    // El valor es un entero sin signo de 8 bits, va desde 0000 0000
    // hasta el 1111 1111, en este caso el bit más significativo no
    // tiene signo, así que podemos utilizar todo el rango al completo
    // que es desde el 0 hasta el 255
    //let n: u8 = 1000;

    // Cuando compilamos con cargo run, obtenemos el siguiente error:
    // error: this arithmetic operation will overflow
    // --> src/main.rs:10:17
    // |
    // 10 |     let c: u8 = a + b;
    // |                 ^^^^^ attempt to compute `u8::MAX + 100_u8`, which would overflow
    // |
    // = note: `#[deny(arithmetic_overflow)]` on by default
    // error: could not compile `clase_6` (bin "clase_6") due to 1 previous error
    // Pero, si usamos: `cargo run --release` en modo release, va a compilar
    // y se va a producir overflow
    // let a: u8 = 255;
    // let b: u8 = 100;
    // let c: u8 = a + b;
    // print!("{}", c);

    let a: usize = 25;
    println!("Valor de a: {}", a);
    println!("Valor máximo usize: {}", usize::MAX);
    println!("Valor mínimo usize: {}\n", usize::MIN);

    // Aquí vamos a hacer shadowing de la variable anterior
    // obviamente usize va a coger el rango entero positivo desde 0 hasta
    // su valor máximo que, depende de la arquitectura donde se ejecuta el 
    // código, que en este caso es de 64 bits [0, 18446744073709551615]
    // en el caso de isize como es entero, coge el rango negativo por lo
    // que sería la mitad de 18446744073709551615, e iría de 
    // [-9223372036854775808, 9223372036854775807]
    let a: isize = 40;
    println!("Valor de a: {}", a);
    println!("Valor máximo de isize: {}", isize::MAX);
    println!("Valor mínimo de isize: {}\n", isize::MIN);

    // Podemos hacer separaciones de miles
    let variable_millon: i32 = 1_000_000;
    println!("Valor millon: {}", variable_millon);

    // También podríamos hacerlo así, no tiene por qué separar miles
    // ese valor sería 10, pero queda raro
    let numero: i32 = 1_0;
    println!("Valor millon: {}", numero);

    // Incluso podemos hacerlo con valores decimales
    let pi: f32 = 3.141_592_7;
    println!("Numero pi: {}", pi);
}
