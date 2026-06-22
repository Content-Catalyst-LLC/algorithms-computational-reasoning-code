package main

import "fmt"

func main() {
	scores := []float64{0.94, 0.78, 0.56, 0.70}
	total := 0.0
	for _, score := range scores {
		total += score
	}
	fmt.Printf("non_use_pressure_score=%.4f\n", total/float64(len(scores)))
}
