fn threshold_unit(inputs: &[i32], weights: &[i32], threshold: i32) -> i32 {
    let total: i32 = inputs.iter().zip(weights.iter()).map(|(x, w)| x * w).sum();
    if total >= threshold { 1 } else { 0 }
}

fn main() {
    println!("{}", threshold_unit(&[1, 1], &[1, 1], 2));
}
