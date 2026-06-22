package main

import "fmt"

func main() {
	amplification := 0.82
	concentration := 0.76
	intervention := 0.44
	drift := 0.28
	recursiveData := 0.31
	score := (amplification + concentration + intervention + drift + recursiveData) / 5.0
	fmt.Printf("feedback_risk_score=%.4f\n", score)
}
