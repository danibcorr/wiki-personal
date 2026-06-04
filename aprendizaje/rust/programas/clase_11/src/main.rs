fn imprimir_nombre_pantalla(nombre: &str) {
    println!("Hola {}!", nombre);
}

fn sumar_valores(valor_1: i32, valor_2: i32) -> isize {
    // Con el 'as' estamos haciendo un casting de tipos
    return (valor_1 + valor_2) as isize;
}

fn main() {
    let nombre = "Dani";
    imprimir_nombre_pantalla(nombre);

    let nombre = "Jorge";
    imprimir_nombre_pantalla(nombre);

    let resultado_suma = sumar_valores(1, 2);

    // Esta es otra forma de hacer un debug, para ver los resultados obtenidos
    // sin utilizar prints
    dbg!(resultado_suma);
}