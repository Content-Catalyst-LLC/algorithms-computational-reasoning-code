package main

import "fmt"

func sumTo(n int) int {
	acc := 0
	for i := 0; i <= n; i++ {
		acc += i
	}
	return acc
}

func main() {
	fmt.Printf("sum_to_5=%d\n", sumTo(5))
}
