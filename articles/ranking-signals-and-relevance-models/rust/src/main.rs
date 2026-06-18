fn precision_at_k(tp:f64, k:f64) -> f64 { if k == 0.0 {0.0} else {tp/k} }
fn ranking_score(l:f64,m:f64,f:f64,a:f64,s:f64,p:f64) -> f64 { 100.0*(0.22*l + 0.18*m + 0.12*f + 0.16*a + 0.17*s + 0.15*p) }
fn main(){ println!("test_name,value\nprecision_at_3,{:.4}\nranking_signal_score,{:.3}", precision_at_k(2.0,3.0), ranking_score(.84,.88,.76,.82,.78,.86)); }
