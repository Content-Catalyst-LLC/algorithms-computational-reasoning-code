fn step(x: f64) -> f64 {
    (x + 0.08 * x - 0.03 * x - 0.04 * x).max(0.0)
}

fn main() {
    let mut stock = 100.0_f64;
    for t in 0..=30 {
        println!("time_step={},stock={:.6}", t, stock);
        stock = step(stock);
    }
}
