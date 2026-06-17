fn main() {
    println!("case_name,literacy_support_score,warning");
    let cases = [
        ("Search ranking", 62.0, 66.0, 38.0, 52.0, 68.0),
        ("Public decision-support workflow", 58.0, 56.0, 70.0, 76.0, 74.0),
        ("Scientific simulation dashboard", 76.0, 74.0, 60.0, 68.0, 80.0),
        ("Recommendation feed", 40.0, 48.0, 32.0, 46.0, 50.0),
    ];
    for (name, transparency, interpretability, contestability, governance, judgment) in cases {
        let score = 0.22*transparency + 0.22*interpretability + 0.18*contestability + 0.18*governance + 0.20*judgment;
        println!("{},{:.3},Synthetic educational diagnostic only.", name, score);
    }
}
