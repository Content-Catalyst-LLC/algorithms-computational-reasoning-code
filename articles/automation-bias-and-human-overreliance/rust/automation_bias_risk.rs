fn main() {
    let acceptance: f64 = 0.93;
    let quality: f64 = 0.71;
    let uncertainty: f64 = 0.29;
    let review_deficit: f64 = 0.65;
    let override_friction: f64 = 0.72;
    let weak_contestability: f64 = 0.0;
    let overreliance_gap = (acceptance - quality).max(0.0);
    let score = (acceptance + overreliance_gap + uncertainty + review_deficit + override_friction + weak_contestability) / 6.0;
    println!("automation_bias_risk_score={:.4}", score);
}
