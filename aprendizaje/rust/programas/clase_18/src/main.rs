fn normalize_text(text: String) -> String {
    return text.to_lowercase();
}

fn normalize_text_reference(text: &String) -> String {
    return text.to_lowercase();
}

fn sumar_uno(valor: i32) -> i32 {
    return valor + 1;
}

fn contar_numero_caracteres(text: String) -> (String, usize) {
    let text_length: usize = text.chars().count();
    return (text, text_length);
}

fn contar_numero_caracteres_reference(text: &String) -> usize {
    return text.chars().count();
}

fn agregar_texto(text: &mut String) {
    return text.push_str("!");
}

fn main() {
    let text: String = String::from("Hola");
    println!("Llamada función `normalize_text`: {}", normalize_text(text));

    // Como normalize text se le pasa como parámetro text que es un String
    // y no una referencia, normalize_text coge el ownership de text, que
    // al salir del scope de normalize_text deja de estar disponible y
    // no podemos hacer:
    // println!("{text}");

    // Lo que tendríamos que hacer es pasarlo por referencia:
    let text: String = String::from("Hola");
    println!(
        "Llamada función `normalize_text_reference`: {}",
        normalize_text_reference(&text)
    );
    println!("Valor de `text`: {text}");

    // Pero tener de nuevo en cuenta que lo anterior solo ocurre por el tipo
    // complejo de los datos (una parte se guarda en el stack y otra en el heap)
    // para tipos simples si funciona porque se hace una copia completa porque están
    // en el stack
    let n: i32 = 200;
    println!("Llamada función `sumar_uno`: {}", sumar_uno(n));
    println!("Valor de `n`: {n}");

    // Si queremos recuperar el ownership lo que debemos hacer es hacer
    // que la función devuelva la variable que le pasamos como parámetro
    // por ejemplo:
    let texto: String = String::from("Hola");
    let (texto, size_texto) = contar_numero_caracteres(texto);
    println!("El texto: `{texto}`, tiene {size_texto} caracteres.");

    // O directamente pasarlo por referencia
    let texto: String = String::from("Prueba");
    let size_texto: usize = contar_numero_caracteres_reference(&texto);
    println!("El texto: `{texto}`, tiene {size_texto} caracteres.");

    // Podemos hacer modificaciones de un valor pasado por referencia
    // utilizando variables mutables
    let mut texto: String = String::from("Bob");
    // Realizamos una modificación en la función del valor pasado como
    // referencia ya que es mutable
    agregar_texto(&mut texto);
    // El valor se verá modificado
    println!("Añadir texto: {texto}");

    // Podemos crear una variable utilizar el valor de referencia mutable
    let texto_2 = &mut texto;

    // Pero solo podemos hacerlo 1 vez, en el caso de tener otra variable
    // que se defina a partir de la referencia mutable de la misma variable
    // tendríamos 2 variables apuntando al mismo lugar que pueden ser
    // de escritura/lectura y que no existe mecanismo de sincronización
    // para solucionarlo
    let texto_3 = &mut texto;

    // Esto no lo podríamos a hacer por la explicación anterior
    // dbg!(texto_2, texto_3);

    // Pero podemos hacer:
    let texto_2 = &texto;
    let texto_3 = &texto;
    dbg!(texto_2, texto_3);
}
