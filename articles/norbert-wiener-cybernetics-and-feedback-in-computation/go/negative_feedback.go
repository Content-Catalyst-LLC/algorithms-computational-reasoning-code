package main

import "fmt"

func main() {
	x := 10.0
	target := 0.0
	gain := 0.2
	for i := 0; i < 5; i++ {
		x = x - gain*(x-target)
	}
	fmt.Printf("final_state=%.6f\n", x)
}
