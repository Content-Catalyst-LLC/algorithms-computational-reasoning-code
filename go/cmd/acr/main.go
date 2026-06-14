package main

import "fmt"

func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

func main() {
	for i := 0; i <= 6; i++ {
		fmt.Println(i, factorial(i))
	}
}
