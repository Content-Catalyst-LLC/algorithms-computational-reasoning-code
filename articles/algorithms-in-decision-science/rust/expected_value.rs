fn main() {
    let probability = 0.82_f64;
    let benefit_if_act = 0.88_f64;
    let cost_if_act = 0.30_f64;
    let expected_value = probability * benefit_if_act - cost_if_act;
    println!("expected_value_of_action={:.4}", expected_value);
}
