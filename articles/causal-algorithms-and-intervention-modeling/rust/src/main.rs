fn decision(score: f64, threshold: f64) -> &'static str {
    if score >= threshold { "act" } else { "monitor" }
}

fn main() {
    let baseline = 0.42;
    let intervention = 0.57;
    let effect = intervention - baseline;
    println!("estimated_effect={:.6}", effect);
    println!("baseline_decision={}", decision(0.53, 0.55));
    println!("new_threshold_decision={}", decision(0.53, 0.50));
}
