fn trust_quality(verification: f64, validation: f64, security: f64, provenance: f64, monitoring: f64, governance: f64) -> f64 {
    100.0 * (0.18 * verification + 0.18 * validation + 0.18 * security + 0.16 * provenance + 0.15 * monitoring + 0.15 * governance)
}

fn main() {
    println!("trust quality={:.3}", trust_quality(0.88, 0.82, 0.88, 0.90, 0.84, 0.82));
}
