package main

import "fmt"

func decision(score float64, threshold float64) string {
	if score >= threshold { return "act" }
	return "monitor"
}

func main() {
	baseline := 0.42
	intervention := 0.57
	fmt.Printf("estimated_effect=%.6f
", intervention-baseline)
	fmt.Println("baseline_decision=", decision(0.53, 0.55))
	fmt.Println("new_threshold_decision=", decision(0.53, 0.50))
}
