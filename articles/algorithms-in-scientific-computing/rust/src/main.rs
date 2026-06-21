fn f(x: f64) -> f64 { x.sin() }
fn central_difference(x: f64, h: f64) -> f64 { (f(x + h) - f(x - h)) / (2.0 * h) }
fn trapezoid(n: usize) -> f64 {
    let a = 0.0_f64;
    let b = std::f64::consts::PI;
    let h = (b - a) / n as f64;
    let mut total = 0.5 * (f(a) + f(b));
    for i in 1..n { total += f(a + i as f64 * h); }
    h * total
}
fn main() {
    println!("central_difference={:.12}", central_difference(1.0, 1e-4));
    println!("trapezoid_integral={:.12}", trapezoid(200));
}
