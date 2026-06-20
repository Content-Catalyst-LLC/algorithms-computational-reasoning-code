fn ranking_score(text_match: f64, quality: f64, freshness: f64, diversity_bonus: f64, risk_penalty: f64) -> f64 {
    0.36 * text_match + 0.30 * quality + 0.16 * freshness + 0.14 * diversity_bonus - 0.20 * risk_penalty
}
fn main() {
    println!("{:.6}", ranking_score(0.92, 0.88, 0.60, 0.35, 0.04));
}
