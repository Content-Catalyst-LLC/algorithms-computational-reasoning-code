package main

import "fmt"

func automationRisk(stakes, opacity, delegation, irreversibility float64) float64 {
	risk := stakes * opacity * delegation * irreversibility
	if risk < 0 { return 0 }
	if risk > 1 { return 1 }
	return risk
}

func main() {
	fmt.Printf("%.6f\n", automationRisk(0.95, 0.85, 0.90, 0.80))
}
