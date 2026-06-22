fn main() {
    let rates = [0.42_f64, 0.31_f64, 0.36_f64];
    let max_rate = rates.iter().cloned().fold(f64::NEG_INFINITY, f64::max);
    let min_rate = rates.iter().cloned().fold(f64::INFINITY, f64::min);
    let gap = max_rate - min_rate;
    println!("selection_gap={:.4}", gap);
}
