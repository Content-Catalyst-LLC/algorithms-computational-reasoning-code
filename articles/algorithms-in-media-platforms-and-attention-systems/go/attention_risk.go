package main

import "fmt"

func main() {
	engagementPressure := 0.92
	creatorImpact := 0.88
	publicKnowledgeImpact := 0.78
	userControl := 0.44
	contestability := 0.42
	score := (engagementPressure + creatorImpact + publicKnowledgeImpact + (1.0 - userControl) + (1.0 - contestability)) / 5.0
	fmt.Printf("attention_risk_score=%.4f\n", score)
}
