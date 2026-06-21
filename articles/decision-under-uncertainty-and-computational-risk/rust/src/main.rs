fn expected_net_value(p: f64, benefit: f64, loss: f64, cost: f64) -> f64 {
    let bounded = p.clamp(0.0, 1.0);
    bounded * benefit - bounded * loss - cost
}

fn main() {
    println!("{:.6}", expected_net_value(0.42, 150.0, 80.0, 25.0));
}
