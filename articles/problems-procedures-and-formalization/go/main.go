package main

import "fmt"

type Case struct {
	Name string
	Input float64
	Output float64
	Objective float64
	Assumptions float64
	Governance float64
}

func main() {
	cases := []Case{
		{"Document search", 82, 78, 70, 58, 56},
		{"Worker scheduling", 72, 76, 58, 54, 62},
		{"Public service triage", 60, 72, 52, 46, 66},
		{"Scientific simulation", 86, 80, 76, 84, 70},
	}
	fmt.Println("case_name,formalization_score,warning")
	for _, c := range cases {
		score := 0.20*c.Input + 0.20*c.Output + 0.25*c.Objective + 0.20*c.Assumptions + 0.15*c.Governance
		fmt.Printf("%s,%.3f,Synthetic educational diagnostic only.\n", c.Name, score)
	}
}
