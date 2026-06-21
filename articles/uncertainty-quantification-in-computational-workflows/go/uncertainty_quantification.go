package main

import "fmt"

func clamp(v, lo, hi float64) float64 {
	if v < lo { return lo }
	if v > hi { return hi }
	return v
}

func riskModel(demand, capacity, failureRate, adaptationRate, noise float64) float64 {
	return clamp(0.42+0.38*demand-0.31*capacity+0.27*failureRate-0.18*adaptationRate+noise, 0.0, 1.0)
}

func main() {
	fmt.Printf("risk_score=%.6f\n", riskModel(0.55, 0.50, 0.22, 0.30, 0.0))
}
