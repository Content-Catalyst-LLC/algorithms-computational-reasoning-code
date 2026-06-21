package main

import (
	"fmt"
	"math"
)

func StandardError(pHat float64, n float64) float64 {
	return math.Sqrt((pHat * (1.0 - pHat)) / n)
}

func main() {
	pHat := 0.57
	n := 1000.0
	se := StandardError(pHat, n)
	fmt.Printf("p_hat=%.3f standard_error=%.6f\n", pHat, se)
}
