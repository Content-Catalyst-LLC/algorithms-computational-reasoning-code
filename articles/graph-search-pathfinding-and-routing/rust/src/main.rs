fn density(nodes:f64, edges:f64)->f64{ if nodes <= 1.0 {0.0} else { edges/(nodes*(nodes-1.0)) } }
fn main(){ println!("test_name,value\nnode_count,5\nedge_count,7\ndensity,{:.6}\nmanual_shortest_path_cost,5.5", density(5.0,7.0)); }
