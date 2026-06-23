package main

import "fmt"

func main() {
	pace := 0.84
	hours := 0.72
	fatigue := 0.70
	scheduleVolatility := 0.78
	burden := (pace + hours + fatigue + scheduleVolatility) / 4.0
	fmt.Printf("workload_burden_score=%.4f\n", burden)
}
