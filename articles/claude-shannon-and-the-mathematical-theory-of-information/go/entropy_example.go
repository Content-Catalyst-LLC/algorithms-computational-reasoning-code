package main

import (
	"fmt"
	"math"
)

func entropy(probs []float64) float64 {
	total := 0.0
	for _, p := range probs {
		if p > 0 {
			total += p * math.Log2(p)
		}
	}
	return -total
}

func main() {
	fmt.Printf("entropy_bits=%.9f\n", entropy([]float64{0.5, 0.5}))
}
