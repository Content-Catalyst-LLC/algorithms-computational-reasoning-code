package main

import "fmt"

func main() {
	acceptance := 0.93
	quality := 0.71
	uncertainty := 0.29
	reviewDeficit := 0.65
	overrideFriction := 0.72
	weakContestability := 0.0
	overrelianceGap := acceptance - quality
	if overrelianceGap < 0 {
		overrelianceGap = 0
	}
	score := (acceptance + overrelianceGap + uncertainty + reviewDeficit + overrideFriction + weakContestability) / 6.0
	fmt.Printf("automation_bias_risk_score=%.4f\n", score)
}
