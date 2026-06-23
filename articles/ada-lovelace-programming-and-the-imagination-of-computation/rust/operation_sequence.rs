fn main() {
    let operations = ["initialize", "store", "multiply", "subtract", "repeat", "output"];
    println!("operation_count={}", operations.len());
    println!("sequence={}", operations.join(" -> "));
}
