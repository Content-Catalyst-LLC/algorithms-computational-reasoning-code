fn ski_rental(rent: f64, buy: f64, days: i32) -> (f64, f64, f64) {
    let break_even = (buy / rent).floor() as i32;
    let rent_only = days as f64 * rent;
    let threshold = (days.min(break_even) as f64 * rent) + if days > break_even { buy } else { 0.0 };
    let offline = rent_only.min(buy);
    (threshold, offline, threshold / offline)
}
fn main(){
    let (t,o,r)=ski_rental(10.0,50.0,8);
    println!("test_name,value\nthreshold_strategy,{:.3}\noffline_optimum,{:.3}\nratio,{:.3}", t,o,r);
}
