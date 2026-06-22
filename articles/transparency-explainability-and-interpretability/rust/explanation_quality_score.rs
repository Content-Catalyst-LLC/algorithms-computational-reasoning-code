fn main() {
    let scores = [0.70_f64, 0.74_f64, 0.62_f64, 0.58_f64, 0.46_f64];
    let total: f64 = scores.iter().sum();
    let quality = total / scores.len() as f64;
    println!("explanation_quality_score={:.4}", quality);
}
