package main

import "fmt"

func main() {
	scores := []float64{0.72, 0.68, 0.64, 0.58, 0.52, 0.66}
	total := 0.0
	for _, score := range scores {
		total += score
	}
	fmt.Printf("accountability_capacity_score=%.4f\n", total/float64(len(scores)))
}
