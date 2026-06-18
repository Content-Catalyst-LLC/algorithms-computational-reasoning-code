fn growth(b: u64, d: u64) -> u64 { (0..=d).map(|level| b.pow(level as u32)).sum() }
fn main(){ println!("test_name,value\nsearch_space_growth,{}\npermutation_count,6", growth(2,3)); }
