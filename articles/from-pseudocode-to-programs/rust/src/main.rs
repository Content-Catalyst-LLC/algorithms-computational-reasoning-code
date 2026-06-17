fn main() {
    println!("case_name,translation_quality,warning");
    let cases = [
        ("Search ranking prototype", 82.0, 80.0, 64.0, 68.0, 72.0),
        ("Decision-rule implementation", 76.0, 74.0, 66.0, 62.0, 68.0),
        ("Simulation loop", 84.0, 82.0, 72.0, 70.0, 74.0),
        ("Data-cleaning procedure", 78.0, 76.0, 70.0, 66.0, 72.0),
    ];
    for (name, intent, control, edge, tests, maintain) in cases {
        let score = 0.22*intent + 0.22*control + 0.18*edge + 0.18*tests + 0.20*maintain;
        println!("{},{:.3},Synthetic educational diagnostic only.", name, score);
    }
}
