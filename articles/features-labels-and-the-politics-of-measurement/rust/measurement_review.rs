fn disagreement_rate(errors: f64, total: f64) -> f64 {
    if total == 0.0 { 0.0 } else { errors / total }
}
fn main() {
    println!("label_disagreement_rate={:.4}", disagreement_rate(180.0, 900.0));
}
