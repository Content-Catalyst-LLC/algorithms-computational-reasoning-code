fn relative_gap(alg: f64, bound: f64) -> f64 { (alg - bound) / bound }
fn main(){ println!("test_name,value\nrelative_gap,{}\napproximation_ratio,1.5", relative_gap(12.0,10.0)); }
