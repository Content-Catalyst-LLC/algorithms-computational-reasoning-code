package main

import (
    "fmt"
    "math"
)

func sigmoid(x float64) float64 { return 1.0 / (1.0 + math.Exp(-x)) }
func representationScore(x1, x2, x3, bias float64) float64 {
    return sigmoid(0.9*x1 - 0.7*x2 + 0.35*x3 + bias)
}
func main() { fmt.Printf("%.6f\n", representationScore(0.5, -0.2, 0.7, 0.0)) }
