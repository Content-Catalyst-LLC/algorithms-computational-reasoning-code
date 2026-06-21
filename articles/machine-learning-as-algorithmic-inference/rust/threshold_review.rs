fn main() {
    let tp = 80.0;
    let fp = 25.0;
    let tn = 140.0;
    let fn_count = 35.0;
    let total = tp + fp + tn + fn_count;
    let accuracy = (tp + tn) / total;
    let precision = tp / (tp + fp).max(1.0);
    let recall = tp / (tp + fn_count).max(1.0);
    println!("accuracy={:.6}", accuracy);
    println!("precision={:.6}", precision);
    println!("recall={:.6}", recall);
}
