fn main() {
    let pd = 0.035_f64;
    let lgd = 0.45_f64;
    let ead = 100000.0_f64;
    let expected_loss = pd * lgd * ead;
    println!("expected_loss={:.4}", expected_loss);
}
