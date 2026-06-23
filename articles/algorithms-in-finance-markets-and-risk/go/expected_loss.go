package main

import "fmt"

func main() {
	pd := 0.035
	lgd := 0.45
	ead := 100000.0
	expectedLoss := pd * lgd * ead
	fmt.Printf("expected_loss=%.4f\n", expectedLoss)
}
