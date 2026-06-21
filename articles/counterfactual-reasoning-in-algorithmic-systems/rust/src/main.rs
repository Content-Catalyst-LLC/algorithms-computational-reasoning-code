fn label(score: f64, threshold: f64) -> &'static str {
    if score >= threshold { "favorable" } else { "not_favorable" }
}

fn main() {
    let original = label(0.57, 0.62);
    let counterfactual = label(0.65, 0.62);
    println!("original_label={}", original);
    println!("counterfactual_label={}", counterfactual);
    println!("decision_flipped={}", original != counterfactual);
}
