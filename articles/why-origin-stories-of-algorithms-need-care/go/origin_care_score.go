package main

import "fmt"

func main() {
	scores := []float64{0.96, 0.98, 0.96, 0.88, 0.98, 0.90, 0.90, 0.96, 0.98, 0.98}
	sum := 0.0
	for _, score := range scores {
		sum += score
	}
	fmt.Printf("origin_care_score=%.6f\n", sum/float64(len(scores)))
}
