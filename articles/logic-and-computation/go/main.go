package main

import "fmt"

type Case struct {
	Name string
	Rule float64
	Predicate float64
	Trace float64
	Test float64
	Governance float64
}

func main() {
	cases := []Case{
		{"Input validation rules", 82, 84, 68, 82, 70},
		{"Database query constraints", 78, 80, 72, 76, 72},
		{"Decision-rule workflow", 74, 70, 68, 72, 78},
		{"Program invariant checks", 80, 78, 74, 80, 66},
	}
	fmt.Println("case_name,logic_quality,warning")
	for _, c := range cases {
		score := 0.24*c.Rule + 0.24*c.Predicate + 0.20*c.Trace + 0.18*c.Test + 0.14*c.Governance
		fmt.Printf("%s,%.3f,Synthetic educational diagnostic only.\n", c.Name, score)
	}
}
