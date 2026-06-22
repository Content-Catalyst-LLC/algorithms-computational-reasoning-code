package main

import "fmt"

func main() {
	provenanceRisk := 0.66
	measurementWeakness := 0.58
	proxyRisk := 0.62
	remediation := 0.42
	score := (provenanceRisk + measurementWeakness + proxyRisk + (1.0 - remediation)) / 4.0
	fmt.Printf("historical_risk_score=%.4f\n", score)
}
