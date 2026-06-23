fn entropy(probs: &[f64]) -> f64 {
    -probs.iter().filter(|p| **p > 0.0).map(|p| p * p.log2()).sum::<f64>()
}

fn main() {
    println!("entropy_bits={:.9}", entropy(&[0.5, 0.5]));
}
