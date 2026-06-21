weights = [0.08,0.10,0.10,0.10,0.08,0.08,0.08,0.08,0.08,0.08,0.06,0.05,0.03]
scenario = fill(0.65, length(weights))
score = 100 * sum(weights .* scenario)
println(round(score, digits=3))
