package main
import "fmt"
func fib(n int) int { dp := make([]int, n+2); dp[1]=1; for i:=2;i<=n;i++{ dp[i]=dp[i-1]+dp[i-2] }; return dp[n] }
func main(){ fmt.Printf("test_name,value\nfibonacci_10,%d\nstate_space_size,100000\n", fib(10)) }
