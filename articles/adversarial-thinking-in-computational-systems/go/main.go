package main

import "fmt"

func readiness(threat, surface, monitoring, defense, incident, governance float64) float64 {
	return 100 * (0.18*threat + 0.18*surface + 0.18*monitoring + 0.18*defense + 0.14*incident + 0.14*governance)
}

func attackSuccess(capability, exposure, control float64) float64 {
	return 100 * capability * exposure * (1 - control)
}

func main() {
	fmt.Printf("adversarial readiness=%.3f\n", readiness(0.86, 0.82, 0.88, 0.82, 0.80, 0.78))
	fmt.Printf("attack success probability=%.3f\n", attackSuccess(0.72, 0.62, 0.82))
}
