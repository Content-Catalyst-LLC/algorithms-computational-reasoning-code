fn classify(score: f64, stakes: &str) -> &'static str {
    if stakes == "high" && score < 1.0 { "escalate" }
    else if score >= 0.8 { "pass" }
    else { "review" }
}
fn main() { println!("{}", classify(0.67, "medium")); }
