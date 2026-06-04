fn calcular_distancia_coordenadas(coordenadas_1: (f32, f32), coordenadas_2: (f32, f32)) -> f32 {
    return ((coordenadas_2.0.powi(2) - coordenadas_1.0.powi(2))
        + (coordenadas_2.1.powi(2) - coordenadas_1.1.powi(2)))
    .sqrt();
}

fn main() {
    let tupla: (i32, i32) = (1, 2);
    println!("Valor x: {}, valor y: {}", tupla.0, tupla.1);

    let (a, b) = tupla;
    println!("Valor x: {}, valor y: {}", a, b);

    // Podemos crear tuplas de valores diferentes
    let tupla: (&str, u8, i32) = ("Hola", 1, 6);
    println!("Valores de la tupla: {:?}", tupla);

    // Las tuplas son muy utilizadas para coordenadas por ejemplo
    let coordenadas_1: (f32, f32) = (2.0, 3.0);
    let coordenadas_2: (f32, f32) = (4.5, 6.0);
    let distancia_coordenadas: f32 = calcular_distancia_coordenadas(coordenadas_1, coordenadas_2);
    println!(
        "La distancia entre las coordenadas 1 {:?} y las coordenadas 2 {:?}, es de: {}",
        coordenadas_1, coordenadas_2, distancia_coordenadas
    );

    // Podemos crear tuplas vacias, que en Rust se conocen como unit
    // Su propósito es semántico: es el valor de retorno implícito
    let empty_tuple: () = ();
}
