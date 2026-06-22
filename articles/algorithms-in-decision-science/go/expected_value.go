package main

import "fmt"

func main() {
	probability := 0.82
	benefitIfAct := 0.88
	costIfAct := 0.30
	expectedValue := probability*benefitIfAct - costIfAct
	fmt.Printf("expected_value_of_action=%.4f\n", expectedValue)
}
