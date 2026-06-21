fn f(x: f64) -> f64 { x.sin() + 0.25 * x * x }
fn central_difference(x: f64, h: f64) -> f64 { (f(x + h) - f(x - h)) / (2.0 * h) }
fn main() { println!("{:.12}", central_difference(1.0, 0.01)); }
