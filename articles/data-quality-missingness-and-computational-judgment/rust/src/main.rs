fn missingness_rate(missing:f64,total:f64)->f64{ if total==0.0 {0.0} else {missing/total} }
fn quality(c:f64,v:f64,t:f64,p:f64,val:f64)->f64{ 100.0*(0.25*c+0.20*v+0.15*t+0.22*p+0.18*val) }
fn main(){ let mr=missingness_rate(45.0,1000.0); println!("test_name,value\nmissingness_rate_45_of_1000,{:.4}\ncompleteness_score_45_of_1000,{:.4}\ndata_quality_score,{:.3}", mr, 1.0-mr, quality(.92,.88,.86,.90,.89)); }
