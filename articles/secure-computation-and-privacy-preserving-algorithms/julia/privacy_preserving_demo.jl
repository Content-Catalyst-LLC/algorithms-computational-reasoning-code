weights = [0.42, 0.55, 0.49]
counts = [100, 240, 160]
weighted = sum(weights .* counts) / sum(counts)
println("federated average weight=$(round(weighted, digits=6))")
