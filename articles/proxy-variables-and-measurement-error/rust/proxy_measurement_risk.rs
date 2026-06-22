fn main() {
    let validity_gap = 0.42;
    let missingness = 0.12;
    let differential_error = 0.24;
    let label_error = 0.08;
    let score = (validity_gap + missingness + differential_error + label_error) / 4.0;
    println!("measurement_risk_score={:.4}", score);
}
