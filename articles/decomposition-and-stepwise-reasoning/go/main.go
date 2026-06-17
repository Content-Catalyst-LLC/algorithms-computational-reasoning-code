package main

import "fmt"

type Case struct {
	Name string
	Subproblem float64
	Boundary float64
	Sequencing float64
	Dependencies float64
	Recomposition float64
}

func main() {
	cases := []Case{
		{"Search system", 82, 78, 82, 72, 72},
		{"Public decision-support workflow", 74, 66, 68, 60, 58},
		{"Scientific simulation", 86, 82, 80, 78, 82},
		{"Knowledge architecture", 80, 76, 74, 70, 80},
	}
	fmt.Println("case_name,decomposition_score,warning")
	for _, c := range cases {
		score := 0.22*c.Subproblem + 0.20*c.Boundary + 0.18*c.Sequencing + 0.20*c.Dependencies + 0.20*c.Recomposition
		fmt.Printf("%s,%.3f,Synthetic educational diagnostic only.\n", c.Name, score)
	}
}
