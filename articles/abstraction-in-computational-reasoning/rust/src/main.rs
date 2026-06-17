fn main() {
    println!("case_name,abstraction_score,warning");
    let cases = [
        ("Search ranking", 82.0, 70.0, 62.0, 60.0, 56.0),
        ("Transit model", 78.0, 72.0, 66.0, 72.0, 66.0),
        ("Database schema", 84.0, 78.0, 70.0, 74.0, 70.0),
        ("Decision-support score", 70.0, 60.0, 48.0, 52.0, 66.0),
    ];
    for (name, clarity, scope, detail, interpretation, governance) in cases {
        let score = 0.22*clarity + 0.20*scope + 0.20*detail + 0.23*interpretation + 0.15*governance;
        println!("{},{:.3},Synthetic educational diagnostic only.", name, score);
    }
}
