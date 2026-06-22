fn main() {
    let provenance_risk = 0.66;
    let measurement_weakness = 0.58;
    let proxy_risk = 0.62;
    let remediation = 0.42;
    let score = (provenance_risk + measurement_weakness + proxy_risk + (1.0 - remediation)) / 4.0;
    println!("historical_risk_score={:.4}", score);
}
