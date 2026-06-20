package main

import "fmt"

func identityAccessScore(values []float64) float64 {
	weights := []float64{0.10, 0.11, 0.11, 0.09, 0.09, 0.10, 0.09, 0.09, 0.08, 0.06, 0.06, 0.02}
	total := 0.0
	for i, value := range values {
		total += value * weights[i]
	}
	return total * 100.0
}

func main() {
	values := []float64{0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75}
	fmt.Printf("%.3f\n", identityAccessScore(values))
}
