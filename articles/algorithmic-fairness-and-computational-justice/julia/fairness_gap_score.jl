rates = [0.42, 0.31, 0.36]
selection_gap = maximum(rates) - minimum(rates)
println("selection_gap=", round(selection_gap, digits=4))
