package main

import "fmt"

type Case struct {
	Name string
	Clarity float64
	Scope float64
	Detail float64
	Interpretation float64
	Governance float64
}

func main() {
	cases := []Case{
		{"Search ranking", 82, 70, 62, 60, 56},
		{"Transit model", 78, 72, 66, 72, 66},
		{"Database schema", 84, 78, 70, 74, 70},
		{"Decision-support score", 70, 60, 48, 52, 66},
	}
	fmt.Println("case_name,abstraction_score,warning")
	for _, c := range cases {
		score := 0.22*c.Clarity + 0.20*c.Scope + 0.20*c.Detail + 0.23*c.Interpretation + 0.15*c.Governance
		fmt.Printf("%s,%.3f,Synthetic educational diagnostic only.\n", c.Name, score)
	}
}
