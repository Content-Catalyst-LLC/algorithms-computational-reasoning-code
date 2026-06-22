proxy_gap = 0.38
pressure = 0.88
gaming = 0.72
guardrail_penalty = 1.0
score = (proxy_gap + pressure + gaming + guardrail_penalty) / 4
println("goodhart_risk_score=", round(score, digits=4))
