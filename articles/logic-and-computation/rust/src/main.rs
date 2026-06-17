fn main() {
    println!("case_name,logic_quality,warning");
    let cases = [
        ("Input validation rules", 82.0, 84.0, 68.0, 82.0, 70.0),
        ("Database query constraints", 78.0, 80.0, 72.0, 76.0, 72.0),
        ("Decision-rule workflow", 74.0, 70.0, 68.0, 72.0, 78.0),
        ("Program invariant checks", 80.0, 78.0, 74.0, 80.0, 66.0),
    ];
    for (name, rule, pred, trace, test, govern) in cases {
        let score = 0.24*rule + 0.24*pred + 0.20*trace + 0.18*test + 0.14*govern;
        println!("{},{:.3},Synthetic educational diagnostic only.", name, score);
    }
}
