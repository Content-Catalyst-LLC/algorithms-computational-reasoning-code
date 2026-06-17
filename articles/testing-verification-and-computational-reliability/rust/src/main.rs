fn score_in_range(x: f64) -> bool { (0.0..=100.0).contains(&x) }
fn main(){ println!("test_name,status"); println!("score_72,{}", if score_in_range(72.0) {"pass"} else {"fail"}); println!("score_150,{}", if score_in_range(150.0) {"pass"} else {"fail"}); }
