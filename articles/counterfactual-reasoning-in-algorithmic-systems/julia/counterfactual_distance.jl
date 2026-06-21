# Dependency-light Julia example: counterfactual distance.
function recourse_distance(current::Float64, target::Float64, unit_cost::Float64)
    delta = target - current
    cost = abs(delta) * unit_cost
    return (delta=delta, cost=cost)
end

result = recourse_distance(0.48, 0.70, 0.75)
println(result)
