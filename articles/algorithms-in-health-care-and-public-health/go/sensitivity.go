package main

import "fmt"

func main() {
	tp := 86.0
	fn := 14.0
	sensitivity := tp / (tp + fn)
	fmt.Printf("sensitivity=%.4f\n", sensitivity)
}
