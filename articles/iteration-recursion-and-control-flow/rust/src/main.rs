fn factorial(n: u64) -> u64 { if n == 0 { 1 } else { n * factorial(n - 1) } }
fn main(){ println!("test_name,value\nfactorial_5,{}\niterative_sum,{}", factorial(5), [1,2,3].iter().sum::<i32>()); }
