fn main() {
    let scores = [0.62_f64, 0.6875_f64, 0.58_f64, 0.50_f64, 0.56_f64, 0.52_f64];
    let total: f64 = scores.iter().sum();
    let quality = total / scores.len() as f64;
    println!("documentation_quality_score={:.4}", quality);
}
