fn stable_queue(arrival: f64, processing: f64) -> bool { arrival < processing }
fn main(){
    let arrival = 90.0;
    let processing = 100.0;
    println!("test_name,value\nutilization,{:.3}\nstable,{}", arrival/processing, stable_queue(arrival, processing));
}
