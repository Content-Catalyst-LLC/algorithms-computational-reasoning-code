fn main() {
    let scores = [0.72_f64, 0.68_f64, 0.64_f64, 0.58_f64, 0.52_f64, 0.66_f64];
    let total: f64 = scores.iter().sum();
    let capacity = total / scores.len() as f64;
    println!("accountability_capacity_score={:.4}", capacity);
}
