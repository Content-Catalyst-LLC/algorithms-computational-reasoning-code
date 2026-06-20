package main

import "fmt"

type ClientUpdate struct {
	Name     string
	Examples int
	Weight   float64
}

func federatedAverage(updates []ClientUpdate) float64 {
	totalExamples := 0
	weighted := 0.0
	for _, u := range updates {
		totalExamples += u.Examples
		weighted += float64(u.Examples) * u.Weight
	}
	if totalExamples == 0 {
		return 0
	}
	return weighted / float64(totalExamples)
}

func main() {
	updates := []ClientUpdate{
		{"client_a", 100, 0.42},
		{"client_b", 240, 0.55},
		{"client_c", 160, 0.49},
	}
	fmt.Printf("federated average weight=%.6f\n", federatedAverage(updates))
}
