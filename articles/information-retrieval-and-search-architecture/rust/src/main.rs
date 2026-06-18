fn precision(tp:f64, retrieved:f64) -> f64 { if retrieved == 0.0 {0.0} else {tp/retrieved} }
fn recall(tp:f64, relevant:f64) -> f64 { if relevant == 0.0 {0.0} else {tp/relevant} }
fn main(){ println!("test_name,value\nprecision,{:.4}\nrecall,{:.4}", precision(2.0,3.0), recall(2.0,2.0)); }
