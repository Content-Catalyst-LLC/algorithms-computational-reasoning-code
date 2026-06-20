fn identity_access_score(values: &[f64]) -> f64 {
    let weights = [0.10,0.11,0.11,0.09,0.09,0.10,0.09,0.09,0.08,0.06,0.06,0.02];
    values.iter().zip(weights.iter()).map(|(v,w)| v*w).sum::<f64>() * 100.0
}

fn main() {
    let values = [0.75; 12];
    println!("{:.3}", identity_access_score(&values));
}
