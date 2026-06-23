fn main() {
    let hazard = 0.80_f64;
    let exposure = 0.75_f64;
    let vulnerability = 0.60_f64;
    let risk = hazard * exposure * vulnerability;
    println!("infrastructure_risk={:.4}", risk);
}
