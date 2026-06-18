fn fib(n: usize) -> usize { let mut dp=vec![0; n+2]; dp[1]=1; for i in 2..=n { dp[i]=dp[i-1]+dp[i-2]; } dp[n] }
fn main(){ println!("test_name,value\nfibonacci_10,{}\nstate_space_size,100000", fib(10)); }
