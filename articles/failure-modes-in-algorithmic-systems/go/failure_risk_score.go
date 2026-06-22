package main

import "fmt"

func main() {
	likelihood := 0.42
	severity := 0.86
	detectability := 0.38
	controllability := 0.44
	failureRisk := likelihood * severity * (1.0 - detectability) * (1.0 - controllability)
	fmt.Printf("failure_risk_score=%.4f\n", failureRisk)
}
