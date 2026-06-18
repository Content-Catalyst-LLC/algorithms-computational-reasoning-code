package main
import "fmt"
func factorial(n int) int { if n <= 0 { return 1 }; return n * factorial(n-1) }
func main(){ fmt.Printf("test_name,value\nfactorial_5,%d\niterative_sum,%d\n", factorial(5), 1+2+3) }
