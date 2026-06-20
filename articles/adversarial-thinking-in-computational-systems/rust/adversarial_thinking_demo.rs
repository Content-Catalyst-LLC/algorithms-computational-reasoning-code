fn readiness(threat: f64, surface: f64, monitoring: f64, defense: f64, incident: f64, governance: f64) -> f64 {
    100.0 * (0.18 * threat + 0.18 * surface + 0.18 * monitoring + 0.18 * defense + 0.14 * incident + 0.14 * governance)
}

fn main() {
    println!("adversarial readiness={:.3}", readiness(0.86, 0.82, 0.88, 0.82, 0.80, 0.78));
}
