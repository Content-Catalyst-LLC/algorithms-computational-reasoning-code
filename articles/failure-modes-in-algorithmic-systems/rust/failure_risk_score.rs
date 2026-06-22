fn main() {
    let likelihood = 0.42;
    let severity = 0.86;
    let detectability = 0.38;
    let controllability = 0.44;
    let failure_risk = likelihood * severity * (1.0 - detectability) * (1.0 - controllability);
    println!("failure_risk_score={:.4}", failure_risk);
}
