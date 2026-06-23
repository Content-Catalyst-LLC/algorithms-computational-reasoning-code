package main

import "fmt"

func main() {
	digits := []int{1, 2, 3, 0}
	value := 0
	for _, digit := range digits {
		value = value*10 + digit
	}
	fmt.Printf("place_value_result=%d\n", value)
}
