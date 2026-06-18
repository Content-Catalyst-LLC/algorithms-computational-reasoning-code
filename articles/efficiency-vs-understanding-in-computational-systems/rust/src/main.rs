fn efficiency_gain(baseline:f64, optimized:f64) -> f64 { (baseline - optimized) / baseline }
fn main(){
    let gain = efficiency_gain(100.0,64.0);
    println!("test_name,value\nefficiency_gain_percent,{:.3}\nunderstanding_floor,{}", 100.0*gain, "review_required");
}
