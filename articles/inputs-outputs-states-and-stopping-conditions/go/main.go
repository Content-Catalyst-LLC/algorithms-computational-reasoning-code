package main

import "fmt"

type Case struct {
	Name string
	Input float64
	Output float64
	State float64
	Stopping float64
	Failure float64
}

func main() {
	cases := []Case{
		{"Graph traversal", 84, 80, 86, 80, 70},
		{"Decision-support workflow", 68, 70, 74, 62, 60},
		{"Numerical simulation", 82, 78, 84, 78, 66},
		{"Recommendation ranking", 74, 72, 70, 60, 52},
	}
	fmt.Println("case_name,boundary_score,warning")
	for _, c := range cases {
		score := 0.22*c.Input + 0.22*c.Output + 0.22*c.State + 0.20*c.Stopping + 0.14*c.Failure
		fmt.Printf("%s,%.3f,Synthetic educational diagnostic only.\n", c.Name, score)
	}
}
