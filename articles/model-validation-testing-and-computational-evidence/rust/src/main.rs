fn main() {
    let observed = [33.1, 39.7, 38.8, 39.3, 8.4];
    let predicted = [31.92, 31.58, 36.48, 25.30, 11.30];
    let mut squared = 0.0_f64;
    let mut absolute = 0.0_f64;
    for (y, yhat) in observed.iter().zip(predicted.iter()) {
        let err = y - yhat;
        squared += err * err;
        absolute += err.abs();
    }
    let n = observed.len() as f64;
    println!("rmse={:.4}", (squared / n).sqrt());
    println!("mae={:.4}", absolute / n);
}
