fn slice_lista(lista_valores: &[i32], init_index: usize, end_index: usize) -> &[i32] {
    return &lista_valores[init_index..end_index];
}

fn main() {
    let lista_valores: [i32; 5] = [1, 2, 3, 4, 5];
    let slice_cogido = slice_lista(&lista_valores, 1, 3);
    println!("{:?}", slice_cogido);

    if slice_cogido == [2, 3] {
        println!("Todo correcto :)");
    } else {
        println!("Algo salio mal :(");
    }
}
