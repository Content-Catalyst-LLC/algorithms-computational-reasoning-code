package main

import "fmt"

type Profile struct {
	Name       string
	Step       float64
	Decomp     float64
	Control    float64
	Test       float64
	Represent  float64
	Governance float64
}

func main() {
	profiles := []Profile{
		{"Recipe-like procedure", 86, 72, 70, 62, 42, 20},
		{"Classroom algorithm exercise", 90, 82, 84, 78, 62, 32},
		{"Search and ranking system", 72, 70, 76, 66, 78, 70},
		{"Public decision-support workflow", 68, 66, 64, 72, 80, 86},
		{"Scientific modeling workflow", 74, 78, 76, 82, 86, 74},
	}
	fmt.Println("name,algorithmic_score,computational_score,warning")
	for _, p := range profiles {
		algorithmic := 0.28*p.Step + 0.24*p.Decomp + 0.24*p.Control + 0.24*p.Test
		computational := 0.16*p.Step + 0.14*p.Decomp + 0.14*p.Control + 0.14*p.Test + 0.22*p.Represent + 0.20*p.Governance
		fmt.Printf("%s,%.3f,%.3f,Synthetic educational diagnostic only.\n", p.Name, algorithmic, computational)
	}
}
