package main

import "fmt"

func clamp(x, lo, hi float64) float64 {
	if x < lo { return lo }
	if x > hi { return hi }
	return x
}

func model(demand, capacity, failure, adaptation float64) float64 {
	return clamp(0.5+0.30*demand+0.25*failure-0.20*capacity-0.15*adaptation, 0, 1)
}

func main() {
	fmt.Printf("baseline_risk=%.6f\n", model(0.45, 0.35, 0.25, 0.30))
}
