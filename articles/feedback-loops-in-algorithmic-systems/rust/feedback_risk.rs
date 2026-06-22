fn main() {
    let amplification = 0.82;
    let concentration = 0.76;
    let intervention = 0.44;
    let drift = 0.28;
    let recursive_data = 0.31;
    let score = (amplification + concentration + intervention + drift + recursive_data) / 5.0;
    println!("feedback_risk_score={:.4}", score);
}
