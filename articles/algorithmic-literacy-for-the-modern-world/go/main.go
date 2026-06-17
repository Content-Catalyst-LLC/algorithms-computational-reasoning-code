package main

import "fmt"

type Case struct {
	Name string
	Transparency float64
	Interpretability float64
	Contestability float64
	Governance float64
	Judgment float64
}

func main() {
	cases := []Case{
		{"Search ranking", 62, 66, 38, 52, 68},
		{"Public decision-support workflow", 58, 56, 70, 76, 74},
		{"Scientific simulation dashboard", 76, 74, 60, 68, 80},
		{"Recommendation feed", 40, 48, 32, 46, 50},
	}
	fmt.Println("case_name,literacy_support_score,warning")
	for _, c := range cases {
		score := 0.22*c.Transparency + 0.22*c.Interpretability + 0.18*c.Contestability + 0.18*c.Governance + 0.20*c.Judgment
		fmt.Printf("%s,%.3f,Synthetic educational diagnostic only.\n", c.Name, score)
	}
}
