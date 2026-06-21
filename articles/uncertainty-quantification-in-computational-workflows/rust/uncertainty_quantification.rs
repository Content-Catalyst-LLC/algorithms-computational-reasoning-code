fn risk_model(demand: f64, capacity: f64, failure_rate: f64, adaptation_rate: f64, noise: f64) -> f64 {
    (0.42 + 0.38 * demand - 0.31 * capacity + 0.27 * failure_rate - 0.18 * adaptation_rate + noise).clamp(0.0, 1.0)
}

fn main() {
    let score = risk_model(0.55, 0.50, 0.22, 0.30, 0.0);
    println!("risk_score={:.6}", score);
}
