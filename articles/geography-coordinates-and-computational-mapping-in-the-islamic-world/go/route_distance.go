package main

import "fmt"

func main() {
	segments := []float64{12.0, 20.0, 7.5}
	total := 0.0
	for _, s := range segments {
		total += s
	}
	fmt.Printf("segments=%d\n", len(segments))
	fmt.Printf("total_distance=%.6f\n", total)
}
