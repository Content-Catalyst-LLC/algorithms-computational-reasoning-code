package main

import "fmt"

func main() {
	total := 1200.0
	weights := []float64{2.0, 1.0, 1.0}
	sum := 0.0
	for _, w := range weights {
		sum += w
	}
	for i, w := range weights {
		fmt.Printf("share_%d=%.4f\n", i+1, total*w/sum)
	}
}
