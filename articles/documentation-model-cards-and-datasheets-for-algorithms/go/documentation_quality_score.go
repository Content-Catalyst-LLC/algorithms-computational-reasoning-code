package main

import "fmt"

func main() {
	scores := []float64{0.62, 0.6875, 0.58, 0.50, 0.56, 0.52}
	total := 0.0
	for _, score := range scores {
		total += score
	}
	fmt.Printf("documentation_quality_score=%.4f\n", total/float64(len(scores)))
}
