fn generalization_gap(train: f64, test: f64) -> f64 { test - train }
fn main() { println!("generalization_gap={:.4}", generalization_gap(0.04, 0.09)); }
