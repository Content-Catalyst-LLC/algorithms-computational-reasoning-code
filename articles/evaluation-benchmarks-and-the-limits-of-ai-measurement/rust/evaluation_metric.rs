fn main() {
    let tp = 42.0;
    let tn = 38.0;
    let fp = 7.0;
    let fn_ = 13.0;
    let accuracy = (tp + tn) / (tp + tn + fp + fn_);
    println!("accuracy={:.4}", accuracy);
}
