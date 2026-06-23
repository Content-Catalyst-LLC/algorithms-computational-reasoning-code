fn main() {
    let steps = ["take the number", "double it", "add the adjustment", "check the result"];
    for (idx, step) in steps.iter().enumerate() {
        println!("{}: {}", idx + 1, step);
    }
}
