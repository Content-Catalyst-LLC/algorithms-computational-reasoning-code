package main
import "fmt"
func fitness(xs []int) int { s:=0; for _,x:= range xs { s += x }; return s }
func main(){ fmt.Printf("test_name,value\nbinary_fitness,%d\nmutation_rate,0.03\n", fitness([]int{1,0,1,1})) }
