fn main() {
    println!("name,algorithmic_score,computational_score,warning");
    let profiles = [
        ("Recipe-like procedure", 86.0, 72.0, 70.0, 62.0, 42.0, 20.0),
        ("Classroom algorithm exercise", 90.0, 82.0, 84.0, 78.0, 62.0, 32.0),
        ("Search and ranking system", 72.0, 70.0, 76.0, 66.0, 78.0, 70.0),
        ("Public decision-support workflow", 68.0, 66.0, 64.0, 72.0, 80.0, 86.0),
        ("Scientific modeling workflow", 74.0, 78.0, 76.0, 82.0, 86.0, 74.0),
    ];
    for (name, step, decomp, control, test, rep, governance) in profiles {
        let algorithmic = 0.28*step + 0.24*decomp + 0.24*control + 0.24*test;
        let computational = 0.16*step + 0.14*decomp + 0.14*control + 0.14*test + 0.22*rep + 0.20*governance;
        println!("{},{:.3},{:.3},Synthetic educational diagnostic only.", name, algorithmic, computational);
    }
}
