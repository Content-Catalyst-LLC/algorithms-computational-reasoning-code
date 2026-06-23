package main

import "fmt"

func delegationRisk(decisionSeverity, automationLevel, opacity float64) float64 { risk := decisionSeverity * automationLevel * opacity; if risk < 0 { return 0 }; if risk > 1 { return 1 }; return risk }
func main() { fmt.Printf("%.6f\n", delegationRisk(0.95, 0.95, 0.80)) }
