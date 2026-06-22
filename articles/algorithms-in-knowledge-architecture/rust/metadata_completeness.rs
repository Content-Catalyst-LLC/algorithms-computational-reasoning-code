fn main() {
    let present_fields = 11.0_f64;
    let required_fields = 12.0_f64;
    let score = present_fields / required_fields;
    println!("metadata_completeness_score={:.4}", score);
}
