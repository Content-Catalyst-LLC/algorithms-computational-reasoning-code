fn main() {
    let pace = 0.84_f64;
    let hours = 0.72_f64;
    let fatigue = 0.70_f64;
    let schedule_volatility = 0.78_f64;
    let burden = (pace + hours + fatigue + schedule_volatility) / 4.0;
    println!("workload_burden_score={:.4}", burden);
}
