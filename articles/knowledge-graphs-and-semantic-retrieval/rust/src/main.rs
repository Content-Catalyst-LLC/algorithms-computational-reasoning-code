fn hybrid_score(l:f64, v:f64, g:f64, p:f64) -> f64 { 100.0*(0.25*l + 0.25*v + 0.25*g + 0.25*p) }
fn path_score(path_length:f64, confidence:f64, provenance:f64, review:f64) -> f64 {
    100.0*(0.25*(1.0/(1.0+(path_length-1.0).max(0.0))) + 0.30*confidence + 0.30*provenance + 0.15*review)
}
fn main(){ println!("test_name,value\nhybrid_score,{:.3}\ngraph_path_score,{:.3}", hybrid_score(.82,.78,.88,.90), path_score(3.0,.90,.92,.95)); }
