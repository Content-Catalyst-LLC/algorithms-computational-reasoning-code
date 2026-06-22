fn main() {
    let input_drift = 0.31;
    let label_drift = 0.16;
    let performance_decay = 0.10;
    let calibration_gap = 0.14;
    let subgroup_gap = 0.15;
    let override_rate = 0.11;
    let score = (input_drift + label_drift + performance_decay + calibration_gap + subgroup_gap + override_rate) / 6.0;
    println!("decay_risk_score={:.4}", score);
}
