fn average(values: &[f64]) -> f64 {
    if values.is_empty() { 0.0 } else { values.iter().sum::<f64>() / values.len() as f64 }
}

fn main() {
    println!("case_name,style_quality");
    println!("Functional data transformation,88.82");
    println!("Object-oriented domain model,85.78");
    println!("Declarative query layer,85.68");
    println!("Event-driven platform workflow,82.08");
    println!("demo_average,{:.2}", average(&[0.90, 0.82, 0.88, 0.86]));
}
