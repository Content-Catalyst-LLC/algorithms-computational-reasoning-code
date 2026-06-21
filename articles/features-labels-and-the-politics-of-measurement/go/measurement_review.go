package main
import "fmt"
func rate(num float64, den float64) float64 { if den == 0 { return 0 }; return num / den }
func main() { fmt.Printf("missingness_rate=%.4f\n", rate(171, 900)) }
