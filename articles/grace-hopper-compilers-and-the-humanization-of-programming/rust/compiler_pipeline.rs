fn main() {
    let source = "ADD PAYROLL-TOTAL TO TAX-BASE";
    let tokens: Vec<&str> = source.split_whitespace().collect();
    println!("source={}", source);
    println!("tokens={:?}", tokens);
    println!("target_code=machine-specific instruction sequence");
}
