fn main() {
    // Las listas se guardan en el stack (pila), porque en tiempo de compilación
    // conocemos el tamaño de la lista, 3 elementos de 32 bits = 96 bits/8 = 12 bytes
    let lista_numeros: [i32; 3] = [1,2,3];
    println!("Contenido de la lista: {:?}", lista_numeros);

    let lista_char: [char; 4] = ['a', 'b', 'c', 'd'];
    println!("Contenido de la lista de char: {:?}", lista_char);

    let lista_strings: [&str; 4] = ["hola", "adios", "hello", "bye"];
    println!("Contenido de la lista de strings: {:?}", lista_strings);
    println!("Primer elemento de la lista: {}", lista_strings[0]);
    println!("Último elemento de la lista: {}", lista_strings[lista_strings.len() - 1]);

    let lista_repetida_nombre = ["Dani"; 5];
    println!("Mi nombre repetido 5 veces: {:?}", lista_repetida_nombre);
}