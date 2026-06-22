fn main() {
    let scores = [0.94_f64, 0.78_f64, 0.56_f64, 0.70_f64];
    let total: f64 = scores.iter().sum();
    let pressure = total / scores.len() as f64;
    println!("non_use_pressure_score={:.4}", pressure);
}
