package main

import "fmt"

func thresholdUnit(inputs []int, weights []int, threshold int) int {
	total := 0
	for i := range inputs {
		total += inputs[i] * weights[i]
	}
	if total >= threshold {
		return 1
	}
	return 0
}

func main() {
	fmt.Println(thresholdUnit([]int{1, 1}, []int{1, 1}, 2))
}
