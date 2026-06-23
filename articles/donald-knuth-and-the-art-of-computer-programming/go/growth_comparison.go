package main

import (
	"fmt"
	"math"
)

func main() {
	n := 1000.0
	fmt.Printf("log2_n=%.6f\n", math.Log2(n))
	fmt.Printf("n=%.0f\n", n)
	fmt.Printf("n_log2_n=%.6f\n", n*math.Log2(n))
	fmt.Printf("n_squared=%.0f\n", n*n)
}
