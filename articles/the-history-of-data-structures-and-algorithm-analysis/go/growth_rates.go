package main

import (
	"fmt"
	"math"
)

func main() {
	for _, n := range []float64{10, 100, 1000, 10000} {
		fmt.Printf("n=%.0f, log2=%.6f, nlogn=%.6f, n2=%.0f\n", n, math.Log2(n), n*math.Log2(n), n*n)
	}
}
