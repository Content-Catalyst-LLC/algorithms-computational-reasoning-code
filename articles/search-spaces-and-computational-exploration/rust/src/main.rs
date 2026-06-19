fn branching_state_count(b:u64,d:u64)->u64{(0..=d).map(|i| b.pow(i as u32)).sum()}
fn path_cost(xs:&[f64])->f64{xs.iter().sum()}
fn ratio(n:f64,d:f64)->f64{if d==0.0{0.0}else{n/d}}
fn main(){ println!("test_name,value\nbranching_state_count,{}\npath_cost,{:.3}\nheuristic_score,{:.3}\ncoverage_ratio,{:.6}\npruning_ratio,{:.6}",branching_state_count(3,5),path_cost(&[2.5,3.0,1.25,4.75]),8.0+5.5,ratio(850.0,5000.0),ratio(1200.0,4200.0)); }
