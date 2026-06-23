fn main() {
    let scores = [0.96, 0.98, 0.96, 0.88, 0.98, 0.90, 0.90, 0.96, 0.98, 0.98];
    let score: f64 = scores.iter().sum::<f64>() / scores.len() as f64;
    println!("origin_care_score={:.6}", score);
}
