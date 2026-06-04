fn main() {
    // El principal punto aquí está en que en algunos casos los decimales o se
    // pueden redondear o se pueden truncar, eso es debido a la representación
    // binaria del valor (perdiendo precisión), donde a veces la aproximación
    // queda ligeramente por encima del valor decimal esperado y a veces 
    // queda ligeramente por debajo
    let a: f64 = 0.1;
    let b: f64 = 0.2;
    let c: f64 = a + b;
    const EXPECTED_VALUE: f64 = 0.3;
    
    // El resultado no será 0.3, da 0.30000000000000004
    println!("a={}, b={}, c=a+b={}", a, b, c);

    // Por ejemplo, para comparar valores, esto dará False
    println!("¿c == 0.3?: {}", c == EXPECTED_VALUE);

    // Por lo que tenemos que calcular la diferencia en valor absoluto 
    // y ver que no supere un error
    println!("¿c ≈ 0.3?: {}", (c - EXPECTED_VALUE).abs() < f64::EPSILON);
}