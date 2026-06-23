fn main() {
    let x0 = 10.0_f64;
    let y0 = 1.2_f64;
    let x1 = 20.0_f64;
    let y1 = 2.8_f64;
    let x = 15.0_f64;
    let y = y0 + ((x - x0) / (x1 - x0)) * (y1 - y0);
    println!("interpolated_y={:.6}", y);
}
