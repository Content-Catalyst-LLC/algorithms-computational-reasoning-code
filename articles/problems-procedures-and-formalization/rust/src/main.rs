fn main() {
    println!("case_name,formalization_score,warning");
    let cases = [
        ("Document search", 82.0, 78.0, 70.0, 58.0, 56.0),
        ("Worker scheduling", 72.0, 76.0, 58.0, 54.0, 62.0),
        ("Public service triage", 60.0, 72.0, 52.0, 46.0, 66.0),
        ("Scientific simulation", 86.0, 80.0, 76.0, 84.0, 70.0),
    ];
    for (name, input, output, objective, assumptions, governance) in cases {
        let score = 0.20*input + 0.20*output + 0.25*objective + 0.20*assumptions + 0.15*governance;
        println!("{},{:.3},Synthetic educational diagnostic only.", name, score);
    }
}
