fn data() -> Vec<(f64, f64)> {
    vec![(-2.0, -2.85), (-1.0, -0.67), (0.0, 1.47), (1.0, 3.63), (2.0, 5.82)]
}

fn mse(w: f64, b: f64) -> f64 {
    let rows = data();
    rows.iter().map(|(x, y)| (y - (w * x + b)).powi(2)).sum::<f64>() / rows.len() as f64
}

fn step(w: f64, b: f64, eta: f64) -> (f64, f64) {
    let rows = data();
    let n = rows.len() as f64;
    let grad_w = rows.iter().map(|(x, y)| (2.0 / n) * ((w * x + b) - y) * x).sum::<f64>();
    let grad_b = rows.iter().map(|(x, y)| (2.0 / n) * ((w * x + b) - y)).sum::<f64>();
    (w - eta * grad_w, b - eta * grad_b)
}

fn main() {
    let (mut w, mut b) = (0.0, 0.0);
    for _ in 0..80 {
        let updated = step(w, b, 0.08);
        w = updated.0;
        b = updated.1;
    }
    println!("weight={:.6}, bias={:.6}, loss={:.6}", w, b, mse(w, b));
}
