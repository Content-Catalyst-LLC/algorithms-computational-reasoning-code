total = 1200.0
weights = [2.0, 1.0, 1.0]
shares = total .* weights ./ sum(weights)
println(shares)
