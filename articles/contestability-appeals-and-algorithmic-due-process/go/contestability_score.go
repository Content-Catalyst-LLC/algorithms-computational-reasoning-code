package main

import "fmt"

func main() {
	notice := 0.70
	reasons := 0.62
	evidenceAccess := 0.48
	humanReview := 0.55
	correction := 0.52
	remedy := 0.44
	score := (notice + reasons + evidenceAccess + humanReview + correction + remedy) / 6.0
	fmt.Printf("contestability_score=%.4f\n", score)
}
