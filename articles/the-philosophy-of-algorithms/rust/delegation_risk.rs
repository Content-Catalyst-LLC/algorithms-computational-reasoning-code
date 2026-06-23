fn delegation_risk(decision_severity: f64, automation_level: f64, opacity: f64) -> f64 {
    (decision_severity * automation_level * opacity).clamp(0.0, 1.0)
}

fn main() { println!("{:.6}", delegation_risk(0.95, 0.95, 0.80)); }
