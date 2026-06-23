fn main() {
    let mut x = 10.0;
    let target = 0.0;
    let gain = 0.2;
    for _ in 0..5 {
        x = x - gain * (x - target);
    }
    println!("final_state={:.6}", x);
}
