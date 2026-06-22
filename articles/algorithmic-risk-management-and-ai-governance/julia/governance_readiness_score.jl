scores = [0.60, 0.62, 0.58, 0.52, 0.46, 0.50]
readiness = sum(scores) / length(scores)
println("governance_readiness_score=", round(readiness, digits=4))
