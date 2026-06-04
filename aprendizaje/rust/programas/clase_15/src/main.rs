use std::io;

const MIN_LENGHT_REQUIRED: u8 = 10;

fn lectura_usuario() -> String {
    let mut user_input: String = String::new();

    println!("Introduce un valor: ");

    io::stdin()
        .read_line(&mut user_input)
        .expect("Error al leer el input del usuario.");

    if user_input.ends_with("\n") {
        user_input = user_input[..user_input.chars().count()-1].to_string();
    }

    return user_input;
}

fn word_lenght_checker(user_input: &String) -> bool {
    // Al igual que en otros lenguajes las evaluaciones devuelven booleanos
    return user_input.chars().count() >= MIN_LENGHT_REQUIRED as usize;
}

fn main() {
    let user_input: String = lectura_usuario();
    println!("{}", user_input.chars().count());

    let word_checker: bool = word_lenght_checker(&user_input);

    if word_checker {
        println!(
            "`user_input` es mayor o igual que MIN_LENGHT_REQUIRED={}",
            MIN_LENGHT_REQUIRED
        );
    } else {
        println!(
            "`user_input` es más pequeño que MIN_LENGHT_REQUIRED={}",
            MIN_LENGHT_REQUIRED
        );
    }

    let palabra_par: bool = if user_input.chars().count() % 2 == 0 {true} else {false};
    println!("La palabra tiene un número de caracteres par?: {}", if palabra_par {"Sí"} else {"No"});
}
