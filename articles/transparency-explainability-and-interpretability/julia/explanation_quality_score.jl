scores = [0.70, 0.74, 0.62, 0.58, 0.46]
quality = sum(scores) / length(scores)
println("explanation_quality_score=", round(quality, digits=4))
