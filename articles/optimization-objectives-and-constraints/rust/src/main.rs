fn linear_objective(c:&[f64], x:&[f64])->f64{c.iter().zip(x.iter()).map(|(a,b)|a*b).sum()}
fn constraint_margin(limit:f64, observed:f64)->f64{limit-observed}
fn penalty_objective(base:f64, penalty:f64, weight:f64)->f64{base+weight*penalty}
fn tradeoff(cost:f64, quality:f64, risk:f64)->f64{0.35*(1.0-cost)+0.40*quality+0.25*(1.0-risk)}
fn main(){ println!("test_name,value\nlinear_objective,{:.3}\nconstraint_margin,{:.3}\npenalty_objective,{:.3}\nnormalized_tradeoff_score,{:.6}",linear_objective(&[4.0,2.0,1.5],&[10.0,20.0,5.0]),constraint_margin(100.0,86.5),penalty_objective(42.0,8.0,2.5),tradeoff(0.30,0.82,0.25)); }
