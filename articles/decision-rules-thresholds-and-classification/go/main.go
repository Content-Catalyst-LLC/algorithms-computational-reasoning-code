package main

import "fmt"

func classify(score float64, threshold float64) int {
	if score >= threshold {
		return 1
	}
	return 0
}

func main() {
	fmt.Println(classify(0.72, 0.50))
}
