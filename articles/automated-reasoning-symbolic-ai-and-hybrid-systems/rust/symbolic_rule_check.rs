use std::collections::HashSet;

fn main() {
    let facts: HashSet<&str> = ["has_documentation", "logs_decisions"].iter().copied().collect();
    let premises = ["has_documentation", "logs_decisions"];
    let fires = premises.iter().all(|p| facts.contains(p));
    println!("rule_fires={}", fires);
}
