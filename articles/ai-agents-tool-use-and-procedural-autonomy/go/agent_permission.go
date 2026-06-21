package main

import "fmt"

func main() {
	risk := 0.85
	approvalRequired := true
	approved := false
	status := "pass"
	if approvalRequired && !approved {
		status = "blocked"
	} else if risk >= 0.65 {
		status = "escalate"
	}
	fmt.Printf("agent_action_status=%s\n", status)
}
