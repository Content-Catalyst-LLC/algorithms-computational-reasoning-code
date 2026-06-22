package main

import "fmt"

func main() {
	proxyGap := 0.38
	pressure := 0.88
	gaming := 0.72
	guardrailPenalty := 1.0
	score := (proxyGap + pressure + gaming + guardrailPenalty) / 4.0
	fmt.Printf("goodhart_risk_score=%.4f\n", score)
}
