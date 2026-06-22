scores = [0.62, 0.6875, 0.58, 0.50, 0.56, 0.52]
quality = sum(scores) / length(scores)
println("documentation_quality_score=", round(quality, digits=4))
