fn formula(x: f64, a: f64, b: f64, c: f64) -> f64 {
    a * x * x + b * x + c
}

fn main() {
    for x in [-2.0, -1.0, 0.0, 1.0, 2.0, 3.0] {
        println!("x={:.1}, y={:.6}", x, formula(x, 2.0, -3.0, 1.0));
    }
}
