package main

import (
	"fmt"
	"math"
)

func f(x float64) float64 { return math.Sin(x) }
func centralDifference(x, h float64) float64 { return (f(x+h) - f(x-h)) / (2 * h) }
func trapezoid(n int) float64 {
	a, b := 0.0, math.Pi
	h := (b - a) / float64(n)
	total := 0.5 * (f(a) + f(b))
	for i := 1; i < n; i++ { total += f(a + float64(i)*h) }
	return h * total
}
func main() {
	fmt.Printf("central_difference=%.12f\n", centralDifference(1.0, 1e-4))
	fmt.Printf("trapezoid_integral=%.12f\n", trapezoid(200))
}
