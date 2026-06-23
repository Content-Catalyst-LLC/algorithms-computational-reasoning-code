fn main() {
    let total = 1200.0_f64;
    let weights = [2.0_f64, 1.0, 1.0];
    let sum: f64 = weights.iter().sum();
    for (idx, weight) in weights.iter().enumerate() {
        println!("share_{}={:.4}", idx + 1, total * weight / sum);
    }
}
