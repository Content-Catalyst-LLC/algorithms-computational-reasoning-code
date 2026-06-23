package main

import "fmt"

func churchApply(n int, f func(int) int, x int) int {
	for i := 0; i < n; i++ {
		x = f(x)
	}
	return x
}

func main() {
	fmt.Printf("church_3_successor_0=%d\n", churchApply(3, func(x int) int { return x + 1 }, 0))
}
