fn generalization_gap(train: f64, test: f64) -> f64 { train - test }
fn main() { println!("generalization_gap={:.4}", generalization_gap(0.88, 0.81)); }
