fn sigmoid(x: f64) -> f64 { 1.0 / (1.0 + (-x).exp()) }
fn representation_score(x1: f64, x2: f64, x3: f64, bias: f64) -> f64 {
    sigmoid(0.9*x1 - 0.7*x2 + 0.35*x3 + bias)
}
fn main() { println!("{:.6}", representation_score(0.5, -0.2, 0.7, 0.0)); }
