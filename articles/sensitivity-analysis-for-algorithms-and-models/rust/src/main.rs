fn model(demand: f64, capacity: f64, failure: f64, adaptation: f64) -> f64 {
    (0.5 + 0.30 * demand + 0.25 * failure - 0.20 * capacity - 0.15 * adaptation).clamp(0.0, 1.0)
}

fn main() {
    let baseline = model(0.45, 0.35, 0.25, 0.30);
    println!("baseline_risk={:.6}", baseline);
}
