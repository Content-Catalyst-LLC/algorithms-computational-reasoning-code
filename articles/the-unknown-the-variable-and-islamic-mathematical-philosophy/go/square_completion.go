package main

import "fmt"

func main() {
	b := 10.0
	c := 39.0
	completion := (b / 2.0) * (b / 2.0)
	fmt.Printf("completion_term=%.6f\n", completion)
	fmt.Printf("completed_rhs=%.6f\n", c+completion)
}
