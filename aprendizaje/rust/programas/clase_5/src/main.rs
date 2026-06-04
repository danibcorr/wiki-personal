const MULTIPLICADOR: u32 = 2;

fn main() {
    let user_input = "100";
    println!("User input: {}", user_input);

    let converted: i32 = user_input
        .parse()
        .expect("Error al convertir de str a numero");
    // Podemos realizar castings de tipos con el keyword 'as'
    println!(
        "Conversion + multiplicador: {}",
        converted * MULTIPLICADOR as i32
    );

    let caracter: char = 'A';
    let valor_ascci: u32 = caracter as u32;
    println!("Caracter ASCII: {}", valor_ascci);

    // También tenemos tipos de datos compuestos como las listas
    // tuplas, etc
    let coordenadas: (f32, f32) = (1.05, 6.089);
    println!("Coordenadas: {:?}", coordenadas);

    let lista_valores: [&str; 3] = ["Dani", "Jorge", "Fran"];
    println!("Lista de valores: {:?}", lista_valores);

    let mut vector_valores: Vec<&str> = vec!["Dani", "Jorge", "Fran"];
    println!("Lista de valores: {:?}", vector_valores);
    vector_valores.push("Paco");
    println!("Lista de valores: {:?}", vector_valores);
}
