scores = [0.56, 0.62, 0.58, 0.60, 0.48]
capacity = sum(scores) / length(scores)
println("review_capacity_score=", round(capacity, digits=4))
