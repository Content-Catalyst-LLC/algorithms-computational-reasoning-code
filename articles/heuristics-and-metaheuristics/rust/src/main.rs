fn relative_improvement(baseline: f64, heuristic: f64) -> f64 { (baseline - heuristic) / baseline }
fn main(){ println!("test_name,value\nroute_improvement,{}\nannealing_improvement,{}", relative_improvement(34.0,27.0), relative_improvement(18.5,12.2)); }
