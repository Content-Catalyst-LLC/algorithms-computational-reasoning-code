package main

import "fmt"

func pow(base, exp int) int {
	result := 1
	for i := 0; i < exp; i++ {
		result *= base
	}
	return result
}

func main() {
	digit := 7
	base := 10
	position := 3
	value := digit * pow(base, position)
	fmt.Printf("place_value=%d\n", value)
}
