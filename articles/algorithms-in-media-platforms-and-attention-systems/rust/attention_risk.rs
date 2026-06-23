fn main() {
    let engagement_pressure = 0.92_f64;
    let creator_impact = 0.88_f64;
    let public_knowledge_impact = 0.78_f64;
    let user_control = 0.44_f64;
    let contestability = 0.42_f64;
    let score = (engagement_pressure + creator_impact + public_knowledge_impact + (1.0 - user_control) + (1.0 - contestability)) / 5.0;
    println!("attention_risk_score={:.4}", score);
}
