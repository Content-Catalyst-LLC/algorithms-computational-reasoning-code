package main

import "fmt"

func main() {
	inputDrift := 0.31
	labelDrift := 0.16
	performanceDecay := 0.10
	calibrationGap := 0.14
	subgroupGap := 0.15
	overrideRate := 0.11
	score := (inputDrift + labelDrift + performanceDecay + calibrationGap + subgroupGap + overrideRate) / 6.0
	fmt.Printf("decay_risk_score=%.4f\n", score)
}
