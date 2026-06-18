fn quorum_size(n:u32)->u32{ n/2 + 1 }
fn crash_fault_tolerance(n:u32)->u32{ (n-1)/2 }
fn availability(replicas:f64,node_availability:f64)->f64{ 1.0 - (1.0-node_availability).powf(replicas) }
fn latency(compute:f64,network:f64,queue:f64)->f64{ compute+network+queue }
fn main(){ println!("test_name,value\nquorum_5_nodes,{}\nfault_tolerance_5_nodes,{}\navailability_3_replicas,{:.6}\ndistributed_latency_ms,{:.3}", quorum_size(5), crash_fault_tolerance(5), availability(3.0,0.99), latency(35.0,80.0,20.0)); }
