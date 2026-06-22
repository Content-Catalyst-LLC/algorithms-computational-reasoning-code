fn main() {
    let current_stock = 100.0_f64;
    let inflow = 12.0_f64;
    let outflow = 7.0_f64;
    let next_stock = current_stock + inflow - outflow;
    println!("next_stock={:.4}", next_stock);
}
