package main
import "fmt"
func relativeGap(alg, bound float64) float64 { return (alg - bound) / bound }
func main(){ fmt.Printf("test_name,value\nrelative_gap,%.6f\napproximation_ratio,1.500000\n", relativeGap(12,10)) }
