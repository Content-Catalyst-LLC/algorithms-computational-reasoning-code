fn standard_error(p_hat: f64, n: f64) -> f64 {
    ((p_hat * (1.0 - p_hat)) / n).sqrt()
}

fn main() {
    let p_hat = 0.57;
    let n = 1000.0;
    println!("p_hat={:.3} standard_error={:.6}", p_hat, standard_error(p_hat, n));
}
