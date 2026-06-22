package main

import "fmt"

func main() {
	currentStock := 100.0
	inflow := 12.0
	outflow := 7.0
	nextStock := currentStock + inflow - outflow
	fmt.Printf("next_stock=%.4f\n", nextStock)
}
