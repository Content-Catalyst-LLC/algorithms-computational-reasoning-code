package main

import "fmt"

func main() {
	scores := []float64{0.98, 0.90, 0.94, 0.88, 0.94, 0.90, 0.96, 0.84, 0.96}
	sum := 0.0
	for _, score := range scores {
		sum += score
	}
	fmt.Printf("transfer_score=%.6f\n", sum/float64(len(scores)))
}
