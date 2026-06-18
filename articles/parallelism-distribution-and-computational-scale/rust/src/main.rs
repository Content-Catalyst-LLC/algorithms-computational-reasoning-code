fn speedup(serial_fraction:f64, processors:f64) -> f64 {
    1.0 / (serial_fraction + ((1.0 - serial_fraction) / processors))
}
fn main(){
    let s = speedup(0.10, 16.0);
    println!("test_name,value\nspeedup_p16_s010,{:.6}\nefficiency_p16_s010,{:.6}", s, s/16.0);
}
