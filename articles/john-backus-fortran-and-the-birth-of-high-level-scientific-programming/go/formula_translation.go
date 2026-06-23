package main

import "fmt"

func formula(x, a, b, c float64) float64 {
	return a*x*x + b*x + c
}

func main() {
	for _, x := range []float64{-2, -1, 0, 1, 2, 3} {
		fmt.Printf("x=%.1f, y=%.6f\n", x, formula(x, 2, -3, 1))
	}
}
