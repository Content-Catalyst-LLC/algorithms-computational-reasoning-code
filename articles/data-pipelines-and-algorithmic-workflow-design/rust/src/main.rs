fn freshness(days:f64, decay:f64) -> f64 { (-decay*days).exp() }
fn quality(v:f64, f:f64, c:f64, l:f64, m:f64) -> f64 { 100.0*(0.25*v + 0.18*f + 0.20*c + 0.22*l + 0.15*m) }
fn main(){ println!("test_name,value\nfreshness_3_days,{:.4}\npipeline_quality_score,{:.3}", freshness(3.0,0.025), quality(.92,.86,.90,.88,.82)); }
