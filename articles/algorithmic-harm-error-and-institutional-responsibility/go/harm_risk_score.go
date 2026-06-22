package main

import "fmt"

func main() {
	errorLikelihood := 0.34
	severity := 0.92
	exposure := 0.78
	contestability := 0.42
	harmRisk := errorLikelihood * severity * exposure * (1.0 - contestability)
	fmt.Printf("harm_risk_score=%.4f\n", harmRisk)
}
