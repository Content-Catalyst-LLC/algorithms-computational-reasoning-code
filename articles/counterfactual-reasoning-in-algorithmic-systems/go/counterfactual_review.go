package main

import "fmt"

func label(score float64, threshold float64) string {
	if score >= threshold {
		return "favorable"
	}
	return "not_favorable"
}

func main() {
	original := label(0.57, 0.62)
	counterfactual := label(0.65, 0.62)
	fmt.Printf("original_label=%s\n", original)
	fmt.Printf("counterfactual_label=%s\n", counterfactual)
	fmt.Printf("decision_flipped=%t\n", original != counterfactual)
}
