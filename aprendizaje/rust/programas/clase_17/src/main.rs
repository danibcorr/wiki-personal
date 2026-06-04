fn main() {
    // Esto está en el stack
    let palabra = "Bob";
    println!("palabra: {}", palabra);

    // Esto está una parte en el heap y otra en el stack
    // en el stack está la referencia de la variable, ocupación en memoria y longitud
    // en el heap está el contenido en si
    let otra_palabra = String::from("Bob");
    println!("otra_palabra: {}", otra_palabra);

    {
        // Este scope es el dueño de la variable, que al salir del scope
        // hace un drop, liberando los recursos
        let texto = String::from("Bob");
        println!("Hola {}!", texto);
    }

    let a = 1;
    let b = a;
    println!("a: {}, b: {}", a, b);

    let a = 1;
    let b = a.clone();
    println!("a: {}, b: {}", a, b);

    // Para los Strings, una asignación simple (let b = a) hace un "move":
    // la propiedad se transfiere y la variable original queda invalidada.
    // Si queremos conservar ambas variables usables, necesitamos .clone()
    // que hace una copia profunda (deep copy) del contenido en el heap.
    // Rust previene que dos variables apuntando al mismo dato realicen
    // modificaciones que afecten al otro, esto se consigue con
    // con el sistema de ownership y moves
    let palabra: String = String::from("Prueba");
    let copia_palabra: String = palabra.clone();
    println!("palabra: {}, copia_palabra: {}", palabra, copia_palabra);

    // Realmente podemos hacer:
    let a: String = String::from("Prueba");
    let b: String = a;
    println!("b = {}", b);
    // Lo que no podemos utilizar es la variable `a`, Rust hace un move
    // del contenido de la variable `a` a la variable `b` e invalida `a`.

    // La macro dbg!, toma ownership, por lo que no podremos reutilizar
    // variables complejas que no tengan Copy
    let a = "Hola";
    dbg!(a);
    println!("{a}");

    let a = String::from("Hola");
    dbg!(a);
    // Esto no va a funcionar:
    //println!("{a}");
}