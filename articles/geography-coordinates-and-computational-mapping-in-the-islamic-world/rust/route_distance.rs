fn main() {
    let segments = [12.0_f64, 20.0, 7.5];
    let total: f64 = segments.iter().sum();
    println!("segments={}", segments.len());
    println!("total_distance={:.6}", total);
}
