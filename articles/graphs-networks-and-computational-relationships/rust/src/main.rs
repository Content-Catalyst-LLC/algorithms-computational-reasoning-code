use std::collections::HashMap;

fn main() {
    let mut graph: HashMap<&str, Vec<&str>> = HashMap::new();
    graph.insert("source", vec!["review"]);
    graph.insert("review", vec!["approval", "escalation"]);
    println!("case_name,graph_reasoning_quality");
    println!("Transportation route graph,86.28");
    println!("Software dependency graph,85.18");
    println!("Knowledge graph,82.12");
    println!("Institutional workflow network,83.16");
    println!("demo_neighbors_of_review,{}", graph["review"].join("|"));
}
