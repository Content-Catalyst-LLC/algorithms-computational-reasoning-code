package main

import "fmt"

func main() {
	dueProcess := 0.58
	transparency := 0.52
	humanReview := 0.60
	appealReadiness := 0.54
	score := (dueProcess + transparency + humanReview + appealReadiness) / 4.0
	fmt.Printf("procedural_readiness_score=%.4f\n", score)
}
