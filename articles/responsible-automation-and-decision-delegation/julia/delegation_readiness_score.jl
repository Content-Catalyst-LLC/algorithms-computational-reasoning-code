scores = [0.62, 0.58, 0.46, 0.52, 0.60, 0.58]
readiness = sum(scores) / length(scores)
println("delegation_readiness_score=", round(readiness, digits=4))
