const MAX_ITER: u8 = 5;
const CHANGE_BOOL: u8 = 3;

fn boolean_function() {
    let mut connected_to_internet: bool = false;
    let mut contador: u8 = 0;

    while contador < MAX_ITER {
        contador += 1;

        if contador == CHANGE_BOOL {
            println!("Conectado.");
            connected_to_internet = true;
            break;
        };  

        println!("Conectando...");
    };

    println!("Conectado a internet?: {}", connected_to_internet);
    println!("Numero de intentos restantes: {}", MAX_ITER - CHANGE_BOOL);
}

fn character_function() {
    // Solo puede ser un caracter
    let letter: char = 'z';
    println!("Letra: {}", letter);
}

fn main() {
    boolean_function();
    character_function();
}