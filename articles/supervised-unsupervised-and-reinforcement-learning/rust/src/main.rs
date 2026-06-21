fn expected_reward(probability: f64, value: f64, cost: f64) -> f64 { probability * value - cost }
fn main() { println!("expected_reward={:.6}", expected_reward(0.54, 1.0, 0.08)); }
