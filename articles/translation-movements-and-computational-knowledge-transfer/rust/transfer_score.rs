fn main() {
    let scores = [0.98, 0.90, 0.94, 0.88, 0.94, 0.90, 0.96, 0.84, 0.96];
    let score: f64 = scores.iter().sum::<f64>() / scores.len() as f64;
    println!("transfer_score={:.6}", score);
}
