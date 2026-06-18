fn nlogn(n: f64) -> f64 { n * n.log2() }
fn main(){ println!("test_name,value\nlinear_1000,1000\nnlogn_1000,{}\nquadratic_1000,1000000", nlogn(1000.0)); }
