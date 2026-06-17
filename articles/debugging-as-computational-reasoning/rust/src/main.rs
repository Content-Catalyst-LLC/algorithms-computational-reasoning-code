fn main() {
    println!("case_name,debugging_quality,warning");
    let cases = [
        ("Graph traversal infinite loop", 88.0, 78.0, 80.0, 82.0, 78.0),
        ("Data pipeline missing-value bug", 84.0, 74.0, 72.0, 76.0, 74.0),
        ("Simulation instability", 80.0, 78.0, 70.0, 74.0, 66.0),
        ("Recommendation ranking tie bug", 76.0, 68.0, 70.0, 72.0, 70.0),
    ];
    for (name, reproduce, trace, isolate, verify, regression) in cases {
        let score = 0.22*reproduce + 0.20*trace + 0.18*isolate + 0.22*verify + 0.18*regression;
        println!("{},{:.3},Synthetic educational diagnostic only.", name, score);
    }
}
