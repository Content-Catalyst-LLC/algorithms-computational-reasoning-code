package main

import "fmt"

type Case struct {
	Name string
	Intent float64
	Control float64
	Edge float64
	Tests float64
	Maintain float64
}

func main() {
	cases := []Case{
		{"Search ranking prototype", 82, 80, 64, 68, 72},
		{"Decision-rule implementation", 76, 74, 66, 62, 68},
		{"Simulation loop", 84, 82, 72, 70, 74},
		{"Data-cleaning procedure", 78, 76, 70, 66, 72},
	}
	fmt.Println("case_name,translation_quality,warning")
	for _, c := range cases {
		score := 0.22*c.Intent + 0.22*c.Control + 0.18*c.Edge + 0.18*c.Tests + 0.20*c.Maintain
		fmt.Printf("%s,%.3f,Synthetic educational diagnostic only.\n", c.Name, score)
	}
}
