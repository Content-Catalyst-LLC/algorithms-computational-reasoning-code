fn main() {
    let pretest = 0.52_f64;
    let posttest = 0.78_f64;
    let gain = posttest - pretest;
    println!("learning_gain={:.4}", gain);
}
