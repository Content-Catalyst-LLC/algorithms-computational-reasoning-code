label_rates = Dict("A" => 0.34, "B" => 0.48)
gap = abs(label_rates["A"] - label_rates["B"])
println("absolute_label_rate_gap=", round(gap, digits=4))
