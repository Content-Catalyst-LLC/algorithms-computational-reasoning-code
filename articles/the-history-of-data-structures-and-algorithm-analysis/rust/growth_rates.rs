fn main() {
    for n in [10.0_f64, 100.0, 1000.0, 10000.0] {
        println!("n={:.0}, log2={:.6}, nlogn={:.6}, n2={:.0}", n, n.log2(), n * n.log2(), n * n);
    }
}
