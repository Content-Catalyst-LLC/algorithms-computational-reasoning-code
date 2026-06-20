fn score(threat_model: f64, keys: f64, validation: f64, integrity: f64, authentication: f64) -> f64 {
    100.0 * (0.22 * threat_model + 0.24 * keys + 0.18 * validation + 0.18 * integrity + 0.18 * authentication)
}

fn main() {
    println!("standard secure channel score={:.2}", score(0.86, 0.82, 0.90, 0.86, 0.84));
    println!("legacy manual transfer score={:.2}", score(0.36, 0.24, 0.18, 0.34, 0.28));
}
