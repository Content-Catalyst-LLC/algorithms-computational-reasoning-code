package main

import "fmt"

func main() {
	rates := []float64{0.42, 0.31, 0.36}
	minRate := rates[0]
	maxRate := rates[0]
	for _, value := range rates {
		if value < minRate {
			minRate = value
		}
		if value > maxRate {
			maxRate = value
		}
	}
	fmt.Printf("selection_gap=%.4f\n", maxRate-minRate)
}
