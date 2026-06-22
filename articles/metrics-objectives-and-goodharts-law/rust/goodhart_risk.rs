fn main() {
    let proxy_gap = 0.38;
    let pressure = 0.88;
    let gaming = 0.72;
    let guardrail_penalty = 1.0;
    let score = (proxy_gap + pressure + gaming + guardrail_penalty) / 4.0;
    println!("goodhart_risk_score={:.4}", score);
}
