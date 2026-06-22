package main

import "fmt"

func main() {
	validityGap := 0.42
	missingness := 0.12
	differentialError := 0.24
	labelError := 0.08
	score := (validityGap + missingness + differentialError + labelError) / 4.0
	fmt.Printf("measurement_risk_score=%.4f\n", score)
}
