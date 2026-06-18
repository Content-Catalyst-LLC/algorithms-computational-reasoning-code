fn subset_count(n: u32) -> u64 { 2_u64.pow(n) }
fn pairs(n: u64) -> u64 { n * (n - 1) / 2 }
fn main(){ println!("test_name,value\nsubsets_20,{}\npairs_100,{}", subset_count(20), pairs(100)); }
