fn total_latency(c:f64,s:f64,n:f64,q:f64,o:f64)->f64{c+s+n+q+o}
fn nominal_capacity(nodes:f64,cap:f64)->f64{nodes*cap}
fn unit_cost(c:f64,s:f64,n:f64,m:f64,o:f64,completed:f64)->f64{if completed==0.0{0.0}else{(c+s+n+m+o)/completed}}
fn main(){ println!("test_name,value\ncloud_response_latency_ms,{:.3}\nnominal_capacity,{:.3}\nunit_cost,{:.6}",total_latency(80.0,45.0,60.0,25.0,15.0),nominal_capacity(12.0,250.0),unit_cost(120.0,35.0,25.0,90.0,18.0,144000.0)); }
