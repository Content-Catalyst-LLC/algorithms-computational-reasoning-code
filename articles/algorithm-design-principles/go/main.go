package main
import "fmt"
func nondecreasing(xs []int) bool { for i:=0; i<len(xs)-1; i++ { if xs[i] > xs[i+1] { return false } }; return true }
func pass(ok bool) string { if ok { return "pass" }; return "fail" }
func main(){ fmt.Printf("test_name,status\nsorted_valid,%s\nsorted_invalid,%s\n", pass(nondecreasing([]int{1,2,2,3})), pass(nondecreasing([]int{1,3,2}))) }
