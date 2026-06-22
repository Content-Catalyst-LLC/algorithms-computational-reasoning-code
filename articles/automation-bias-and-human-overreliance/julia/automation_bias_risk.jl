acceptance = 0.93
quality = 0.71
uncertainty = 0.29
review_deficit = 0.65
override_friction = 0.72
weak_contestability = 0.0
score = (acceptance + max(0, acceptance - quality) + uncertainty + review_deficit + override_friction + weak_contestability) / 6
println("automation_bias_risk_score=", round(score, digits=4))
