fn main() {
    let n = 5;

    {
        // El valor va a ser 6 porque estoy en un scope diferente
        // Esto es lo que se conoce como shadowing
        let mut n = 6;
        println!("Valor de n dentro: {}", n);
        n += 1;
        println!("Valor de n dentro: {}", n);
    }

    // El valor es 5
    println!("Valor de n fuera: {}", n);

    // Ejemplo shadowing
    let numero: i32 = 4;
    println!("{}", numero);
    let numero: &str = "Hola";
    println!("{}", numero);
}
