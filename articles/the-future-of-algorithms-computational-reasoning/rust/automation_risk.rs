fn automation_risk(stakes: f64, opacity: f64, delegation: f64, irreversibility: f64) -> f64 {
    (stakes * opacity * delegation * irreversibility).clamp(0.0, 1.0)
}

fn main() {
    println!("{:.6}", automation_risk(0.95, 0.85, 0.90, 0.80));
}
