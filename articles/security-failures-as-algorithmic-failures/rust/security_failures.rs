fn main() {
    let weights = [0.08,0.10,0.10,0.10,0.08,0.08,0.08,0.08,0.08,0.08,0.06,0.05,0.03];
    let score: f64 = weights.iter().map(|w| w * 0.65).sum::<f64>() * 100.0;
    println!("{:.3}", score);
}
