package main
import "fmt"
func main() { train, test := 0.82, 0.74; fmt.Printf("generalization_gap=%.6f\n", train-test) }
