fn edge_response_time(s:f64,f:f64,c:f64,a:f64)->f64{s+f+c+a}
fn cloud_response_time(s:f64,u:f64,c:f64,d:f64,a:f64)->f64{s+u+c+d+a}
fn battery_life(b:f64,p:f64)->f64{if p==0.0{0.0}else{b/p}}
fn local_action(signal:f64,threshold:f64)->&'static str{if signal>=threshold{"alert"}else{"monitor"}}
fn main(){ println!("test_name,value\nedge_response_time_ms,{:.3}\ncloud_response_time_ms,{:.3}\nbattery_life_hours,{:.3}\nlocal_action,{}",edge_response_time(8.0,6.0,14.0,5.0),cloud_response_time(8.0,90.0,60.0,90.0,5.0),battery_life(12.0,0.08),local_action(0.82,0.75)); }
