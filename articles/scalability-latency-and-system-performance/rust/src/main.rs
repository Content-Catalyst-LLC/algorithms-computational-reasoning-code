fn response_time(n:f64,q:f64,c:f64,s:f64,o:f64)->f64{n+q+c+s+o}
fn throughput(completed:f64,seconds:f64)->f64{if seconds==0.0{0.0}else{completed/seconds}}
fn utilization(arrival:f64,service:f64)->f64{if service==0.0{0.0}else{arrival/service}}
fn little_law(arrival:f64,time:f64)->f64{arrival*time}
fn main(){ println!("test_name,value\nresponse_time_ms,{:.3}\nthroughput,{:.3}\nutilization,{:.3}\nlittle_law_items,{:.3}",response_time(45.0,20.0,85.0,35.0,15.0),throughput(12000.0,60.0),utilization(180.0,200.0),little_law(180.0,0.45)); }
