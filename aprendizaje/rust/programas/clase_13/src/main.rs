fn main() {
    // En rust solo podemos hacer asignaciones si devuelven un valor
    // por ejemplo, al asignar a una variable el resultado de definir una variable
    // con un valor, eso no funciona en rust, la variable que se define no devuelve nada
    // let variable = (let variable = 2);

    // Por ejemplo, dbg! devuelve un resultado, que es la evalución
    // [src/main.rs:8:26] 20 + 30 = 50
    // Resultado de dbg es: 50
    // por tanto dbg es una expresión
    let resultado: i32 = dbg!(20 + 30);
    println!("Resultado de dbg es: {}", resultado);

    // Otra forma de definir una variable
    let suma = {
        let x = 1;
        let y = 2;
        x + y
    };
    println!("La suma es: {}", suma);
}