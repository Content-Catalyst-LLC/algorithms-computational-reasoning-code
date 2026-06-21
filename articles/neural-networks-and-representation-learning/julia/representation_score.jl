sigmoid(x) = 1 / (1 + exp(-x))
function representation_score(x1, x2, x3; bias=0.0)
    linear = 0.9*x1 - 0.7*x2 + 0.35*x3 + bias
    return sigmoid(linear)
end
println(representation_score(0.5, -0.2, 0.7))
