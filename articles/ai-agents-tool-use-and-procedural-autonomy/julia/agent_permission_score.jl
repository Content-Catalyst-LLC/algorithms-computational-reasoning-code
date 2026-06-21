risk = 0.85
approval_required = true
approved = false
status = approval_required && !approved ? "blocked" : (risk >= 0.65 ? "escalate" : "pass")
println("agent_action_status=", status)
