threshold_unit(inputs, weights, threshold) = sum(inputs .* weights) >= threshold ? 1 : 0
println(threshold_unit([1, 1], [1, 1], 2))
