package main

import "fmt"

func main() {
	facts := map[string]bool{"has_documentation": true, "logs_decisions": true}
	premises := []string{"has_documentation", "logs_decisions"}
	fires := true
	for _, premise := range premises {
		if !facts[premise] {
			fires = false
		}
	}
	fmt.Printf("rule_fires=%v\n", fires)
}
