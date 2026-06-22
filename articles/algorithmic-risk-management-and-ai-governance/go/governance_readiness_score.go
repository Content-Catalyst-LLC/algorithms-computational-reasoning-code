package main

import "fmt"

func main() {
	scores := []float64{0.60, 0.62, 0.58, 0.52, 0.46, 0.50}
	total := 0.0
	for _, score := range scores {
		total += score
	}
	fmt.Printf("governance_readiness_score=%.4f\n", total/float64(len(scores)))
}
