fn main() {
    let tp = 86.0_f64;
    let fn_cases = 14.0_f64;
    let sensitivity = tp / (tp + fn_cases);
    println!("sensitivity={:.4}", sensitivity);
}
