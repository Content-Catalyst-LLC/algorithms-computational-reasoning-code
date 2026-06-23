fn main() {
    let n: f64 = 1000.0;
    println!("log2_n={:.6}", n.log2());
    println!("n={:.0}", n);
    println!("n_log2_n={:.6}", n * n.log2());
    println!("n_squared={:.0}", n * n);
}
