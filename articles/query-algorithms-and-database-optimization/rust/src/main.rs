fn selection_rows(rows:f64, selectivity:f64) -> f64 { rows * selectivity }
fn join_rows(l:f64, r:f64, ld:f64, rd:f64) -> f64 { (l*r) / ld.max(rd) }
fn main(){ println!("test_name,value\nselection_estimated_rows,{:.3}\njoin_estimated_rows,{:.3}", selection_rows(1000000.0,0.012), join_rows(500000.0,200000.0,50000.0,40000.0)); }
