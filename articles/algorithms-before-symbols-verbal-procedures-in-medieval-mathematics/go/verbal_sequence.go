package main

import "fmt"

func main() {
	steps := []string{"take the number", "double it", "add the adjustment", "check the result"}
	for i, step := range steps {
		fmt.Printf("%d: %s\n", i+1, step)
	}
}
