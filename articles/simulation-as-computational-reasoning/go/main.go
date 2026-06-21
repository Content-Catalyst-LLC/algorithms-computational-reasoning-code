package main

import "fmt"

func step(x float64) float64 {
	v := x + 0.08*x - 0.03*x - 0.04*x
	if v < 0 { return 0 }
	return v
}

func main() {
	stock := 100.0
	for t := 0; t <= 30; t++ {
		fmt.Printf("time_step=%d,stock=%.6f\n", t, stock)
		stock = step(stock)
	}
}
