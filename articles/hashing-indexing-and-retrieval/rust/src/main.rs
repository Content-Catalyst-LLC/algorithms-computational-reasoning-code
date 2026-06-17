use std::collections::HashMap;

fn main() {
    let mut index = HashMap::new();
    index.insert("hashing", "doc-1|doc-4");
    index.insert("retrieval", "doc-2|doc-3|doc-4");
    println!("case_name,retrieval_quality");
    println!("Article metadata dictionary,84.24");
    println!("Case status database index,84.20");
    println!("Search inverted index,83.24");
    println!("Cache for expensive computations,82.92");
    println!("demo_retrieval_docs_for_hashing,{}", index["hashing"]);
}
