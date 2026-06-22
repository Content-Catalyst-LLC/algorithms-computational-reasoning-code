fn main() {
    let scores = [0.62_f64, 0.58_f64, 0.46_f64, 0.52_f64, 0.60_f64, 0.58_f64];
    let total: f64 = scores.iter().sum();
    let readiness = total / scores.len() as f64;
    println!("delegation_readiness_score={:.4}", readiness);
}
