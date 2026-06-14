fn factorial(n: u64) -> u64 {
    match n {
        0 => 1,
        _ => n * factorial(n - 1),
    }
}

fn main() {
    let values: Vec<u64> = (0..=6).map(factorial).collect();
    println!("{:?}", values);
}
