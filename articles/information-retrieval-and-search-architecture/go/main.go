package main
import "fmt"
func precision(tp, retrieved float64) float64 { if retrieved == 0 { return 0 }; return tp/retrieved }
func recall(tp, relevant float64) float64 { if relevant == 0 { return 0 }; return tp/relevant }
func main(){ fmt.Printf("test_name,value\nprecision,%.4f\nrecall,%.4f\n", precision(2,3), recall(2,2)) }
