fn main() {
    let b = 10.0_f64;
    let c = 39.0_f64;
    let completion = (b / 2.0).powi(2);
    println!("completion_term={:.6}", completion);
    println!("completed_rhs={:.6}", c + completion);
}
