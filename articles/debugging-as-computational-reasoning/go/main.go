package main

import "fmt"

type Case struct {
	Name string
	Reproduce float64
	Trace float64
	Isolate float64
	Verify float64
	Regression float64
}

func main() {
	cases := []Case{
		{"Graph traversal infinite loop", 88, 78, 80, 82, 78},
		{"Data pipeline missing-value bug", 84, 74, 72, 76, 74},
		{"Simulation instability", 80, 78, 70, 74, 66},
		{"Recommendation ranking tie bug", 76, 68, 70, 72, 70},
	}
	fmt.Println("case_name,debugging_quality,warning")
	for _, c := range cases {
		score := 0.22*c.Reproduce + 0.20*c.Trace + 0.18*c.Isolate + 0.22*c.Verify + 0.18*c.Regression
		fmt.Printf("%s,%.3f,Synthetic educational diagnostic only.\n", c.Name, score)
	}
}
