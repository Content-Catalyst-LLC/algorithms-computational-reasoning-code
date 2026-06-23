package main

import "fmt"

func gcdAlgorithm(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	if a < 0 {
		return -a
	}
	return a
}

func main() {
	fmt.Printf("gcd=%d\n", gcdAlgorithm(252, 105))
}
