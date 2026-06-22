package main

import "fmt"

func main() {
	scores := []float64{0.70, 0.74, 0.62, 0.58, 0.46}
	total := 0.0
	for _, score := range scores {
		total += score
	}
	fmt.Printf("explanation_quality_score=%.4f\n", total/float64(len(scores)))
}
