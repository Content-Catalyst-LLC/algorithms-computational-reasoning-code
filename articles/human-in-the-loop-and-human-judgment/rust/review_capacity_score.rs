fn main() {
    let scores = [0.56_f64, 0.62_f64, 0.58_f64, 0.60_f64, 0.48_f64];
    let total: f64 = scores.iter().sum();
    let capacity = total / scores.len() as f64;
    println!("review_capacity_score={:.4}", capacity);
}
