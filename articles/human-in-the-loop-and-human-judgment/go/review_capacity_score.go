package main

import "fmt"

func main() {
	scores := []float64{0.56, 0.62, 0.58, 0.60, 0.48}
	total := 0.0
	for _, score := range scores {
		total += score
	}
	fmt.Printf("review_capacity_score=%.4f\n", total/float64(len(scores)))
}
