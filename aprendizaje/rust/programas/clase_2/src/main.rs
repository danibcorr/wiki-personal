use rand::random_range;
use std::cmp::Ordering;
use std::io;

/*
Aquí definimos las constantes
*/
const VALOR_MINIMO_RANGO: i32 = 0;
const VALOR_MAXIMO_RANGO: i32 = 10;
const NUM_VIDAS: u8 = 3;

fn generar_valor_aleatorio_rango(val_min_rango: i32, val_max_rango: i32) -> i32 {
    return random_range(val_min_rango..val_max_rango);
}

fn solicitar_valor() -> i32 {
    println!("Introduce un valor: ");

    let mut valor_usuario = String::new();
    io::stdin()
        .read_line(&mut valor_usuario)
        .expect("Fallo a leer el input del usuario");

    // trim le quita los espacio en blanco, parse permite parsear de un tipo a otro
    return valor_usuario.trim().parse().expect("No es un valor valido");
}

fn main() {
    println!("Adivina el valor\n");

    let valor_aleatorio: i32 =
        generar_valor_aleatorio_rango(VALOR_MINIMO_RANGO, VALOR_MAXIMO_RANGO);

    let mut contador_vidas: u8 = 0;

    loop {
        let valor_usuario: i32 = solicitar_valor();

        match valor_usuario.cmp(&valor_aleatorio) {
            Ordering::Equal => {
                println!("Has adivinado el valor.");
                break;
            }
            Ordering::Less => {
                println!("Introduce un valor mayor.\n");
            }
            Ordering::Greater => {
                println!("Introduce un valor menor\n");
            }
        }

        contador_vidas += 1;

        if contador_vidas == NUM_VIDAS {
            println!("Has gastado todas las vidas, has perdido.");
            println!("El valor por adivinar era: {}", valor_aleatorio);
            break;
        }
    }
}
