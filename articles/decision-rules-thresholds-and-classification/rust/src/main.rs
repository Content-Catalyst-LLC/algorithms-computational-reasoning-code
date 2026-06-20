fn classify(score: f64, threshold: f64) -> i32 {
    if score >= threshold { 1 } else { 0 }
}

fn main() {
    println!("{}", classify(0.72, 0.50));
}
