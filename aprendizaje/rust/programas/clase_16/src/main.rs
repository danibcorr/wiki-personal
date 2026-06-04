use std::io;

const MAX_NUMBER_ITERATIONS: u8 = 10;

fn input_usuario() -> String {
    let mut input_user: String = String::new();

    println!("Introduce un valor: ");
    io::stdin().read_line(&mut input_user).expect("Error lectura usuario.");

    if input_user.ends_with("\n") {
        return input_user[..input_user.chars().count() - 1].to_string();
    }

    return input_user;
}

fn main() {
    let mut contador: u8 = 0;
    
    loop {
        if contador < MAX_NUMBER_ITERATIONS {
            contador += 1;
            println!("Sigue contando...");
        } else{
            println!("Has llegado al final :)");
            break;
        }
    }

    println!("Con el `break` salimos del loop infinito :)");

    let mut input_user: String = input_usuario();
    while input_user.to_lowercase() != "hola" {
        println!("El único mensaje que puedo aceptar es `hola`");
        input_user = input_usuario();
    }

    println!("El mensaje es correcto");

    let vector: Vec<i32> = vec![1,2,3,4,5,6,7,8,9];
    for (index, elemn) in vector.iter().enumerate() {
        println!("Elemento: {}, Indice: {}", elemn, index);
    }

    let numbers: [i32; 5] = [1,2,3,4,5];
    let mut mut_power_total: i32 = 0;
    for number in numbers {
        mut_power_total += number.pow(2);
    }
    println!("mut_power_total: {}", mut_power_total);

    
    println!("\nUso de labels en loops :)");
    let mut contador_principal: u8 = 0;

    'loop_principal: loop {
        contador_principal += 1;
        println!("Loop principal, iteracion: {}", contador_principal);

        let mut contador_interno: u8 = 0;

        'loop_interno: loop {
            contador_interno += 1;
            println!("Loop interno, iteracion: {}", contador_interno);
            
            if contador_interno == MAX_NUMBER_ITERATIONS {
                println!("Has llegado al maximo de iteraciones del loop interno.");
                break 'loop_interno;
            }

            if contador_principal == MAX_NUMBER_ITERATIONS {
                println!("Has llegado al maximo de iteraciones del loop principal.");
                break 'loop_principal
            }
        }
    }
}