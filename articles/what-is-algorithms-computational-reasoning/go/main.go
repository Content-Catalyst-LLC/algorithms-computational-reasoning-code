package main

import (
	"fmt"
	"math"
)

type Scenario struct {
	Name       string
	Represent float64
	Correct   float64
	Governance float64
	BruteForce float64
}

func clamp(v float64) float64 {
	return math.Max(0, math.Min(100, v))
}

func main() {
	scenarios := []Scenario{
		{"Brute-force procedure", 40, 28, 20, 92},
		{"Indexed search design", 62, 52, 38, 42},
		{"Graph-aware reasoning", 76, 68, 54, 30},
		{"Governed computational reasoning", 86, 82, 86, 18},
	}
	fmt.Println("scenario,reasoning_score,warning")
	for _, s := range scenarios {
		score := clamp(0.30*s.Represent + 0.30*s.Correct + 0.30*s.Governance - 0.10*s.BruteForce)
		fmt.Printf("%s,%.3f,Synthetic governance diagnostic only.\n", s.Name, score)
	}
}
