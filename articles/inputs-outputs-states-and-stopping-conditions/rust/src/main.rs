fn main() {
    println!("case_name,boundary_score,warning");
    let cases = [
        ("Graph traversal", 84.0, 80.0, 86.0, 80.0, 70.0),
        ("Decision-support workflow", 68.0, 70.0, 74.0, 62.0, 60.0),
        ("Numerical simulation", 82.0, 78.0, 84.0, 78.0, 66.0),
        ("Recommendation ranking", 74.0, 72.0, 70.0, 60.0, 52.0),
    ];
    for (name, input, output, state, stopping, failure) in cases {
        let score = 0.22*input + 0.22*output + 0.22*state + 0.20*stopping + 0.14*failure;
        println!("{},{:.3},Synthetic educational diagnostic only.", name, score);
    }
}
