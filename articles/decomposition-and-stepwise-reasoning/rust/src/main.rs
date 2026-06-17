fn main() {
    println!("case_name,decomposition_score,warning");
    let cases = [
        ("Search system", 82.0, 78.0, 82.0, 72.0, 72.0),
        ("Public decision-support workflow", 74.0, 66.0, 68.0, 60.0, 58.0),
        ("Scientific simulation", 86.0, 82.0, 80.0, 78.0, 82.0),
        ("Knowledge architecture", 80.0, 76.0, 74.0, 70.0, 80.0),
    ];
    for (name, subproblem, boundary, sequencing, dependencies, recomposition) in cases {
        let score = 0.22*subproblem + 0.20*boundary + 0.18*sequencing + 0.20*dependencies + 0.20*recomposition;
        println!("{},{:.3},Synthetic educational diagnostic only.", name, score);
    }
}
