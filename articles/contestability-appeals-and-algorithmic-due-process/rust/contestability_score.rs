fn main() {
    let notice = 0.70;
    let reasons = 0.62;
    let evidence_access = 0.48;
    let human_review = 0.55;
    let correction = 0.52;
    let remedy = 0.44;
    let score = (notice + reasons + evidence_access + human_review + correction + remedy) / 6.0;
    println!("contestability_score={:.4}", score);
}
