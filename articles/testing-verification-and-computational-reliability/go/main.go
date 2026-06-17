package main
import "fmt"
func scoreInRange(x float64) bool { return x >= 0 && x <= 100 }
func main(){ fmt.Printf("test_name,status\nscore_72,%s\nscore_150,%s\n", pass(scoreInRange(72)), pass(scoreInRange(150))) }
func pass(ok bool) string { if ok { return "pass" }; return "fail" }
