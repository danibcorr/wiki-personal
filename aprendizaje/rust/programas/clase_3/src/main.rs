fn main() {
    // Las variables por defecto son inmutables, por lo que no
    // podemos modificar su valor una vez creada la variable
    // para ello usamos el key word 'mut'
    let mut contador: i32 = 4;
    contador += 1;
    println!("{}", contador);

    // Las constantes son siempre inmutables y se deben especificar
    // siempre el tipo de la variable
    const CONSTANTE: u8 = 6;
    println!("{}", CONSTANTE);
}
