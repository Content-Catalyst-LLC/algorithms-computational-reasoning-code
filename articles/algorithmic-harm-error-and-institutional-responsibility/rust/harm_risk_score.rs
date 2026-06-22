fn main() {
    let error_likelihood = 0.34;
    let severity = 0.92;
    let exposure = 0.78;
    let contestability = 0.42;
    let harm_risk = error_likelihood * severity * exposure * (1.0 - contestability);
    println!("harm_risk_score={:.4}", harm_risk);
}
