fn main() {
    println!("scenario,reasoning_score,warning");
    let scenarios = [
        ("Brute-force procedure", 40.0, 28.0, 20.0, 92.0),
        ("Indexed search design", 62.0, 52.0, 38.0, 42.0),
        ("Graph-aware reasoning", 76.0, 68.0, 54.0, 30.0),
        ("Governed computational reasoning", 86.0, 82.0, 86.0, 18.0),
    ];
    for (name, representation, correctness, governance, brute_force) in scenarios {
        let score = (0.30 * representation + 0.30 * correctness + 0.30 * governance - 0.10 * brute_force).clamp(0.0, 100.0);
        println!("{},{:.3},Synthetic governance diagnostic only.", name, score);
    }
}
