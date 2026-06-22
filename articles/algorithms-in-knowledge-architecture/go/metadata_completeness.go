package main

import "fmt"

func main() {
	presentFields := 11.0
	requiredFields := 12.0
	score := presentFields / requiredFields
	fmt.Printf("metadata_completeness_score=%.4f\n", score)
}
