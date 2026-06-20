struct ClientUpdate {
    examples: f64,
    weight: f64,
}

fn federated_average(updates: &[ClientUpdate]) -> f64 {
    let total: f64 = updates.iter().map(|u| u.examples).sum();
    let weighted: f64 = updates.iter().map(|u| u.examples * u.weight).sum();
    if total == 0.0 { 0.0 } else { weighted / total }
}

fn main() {
    let updates = [
        ClientUpdate { examples: 100.0, weight: 0.42 },
        ClientUpdate { examples: 240.0, weight: 0.55 },
        ClientUpdate { examples: 160.0, weight: 0.49 },
    ];
    println!("federated average weight={:.6}", federated_average(&updates));
}
