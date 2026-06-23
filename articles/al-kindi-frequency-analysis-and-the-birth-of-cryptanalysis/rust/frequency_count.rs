use std::collections::HashMap;

fn main() {
    let text = "THIS IS A TOY CLASSICAL CIPHER EXAMPLE";
    let mut counts: HashMap<char, usize> = HashMap::new();
    for ch in text.to_lowercase().chars().filter(|c| c.is_alphabetic()) {
        *counts.entry(ch).or_insert(0) += 1;
    }
    println!("{:?}", counts);
}
