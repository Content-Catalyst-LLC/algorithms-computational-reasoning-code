package main

import "fmt"

func main() {
	hazard := 0.80
	exposure := 0.75
	vulnerability := 0.60
	risk := hazard * exposure * vulnerability
	fmt.Printf("infrastructure_risk=%.4f\n", risk)
}
