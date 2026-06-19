branching_state_count(b, d) = sum(b^i for i in 0:d)
path_cost(costs) = sum(costs)
heuristic_score(g, h) = g + h
ratio(n, d) = d == 0 ? 0 : n / d
println("test_name,value")
println("branching_state_count,$(branching_state_count(3,5))")
println("path_cost,$(path_cost([2.5,3.0,1.25,4.75]))")
println("heuristic_score,$(heuristic_score(8.0,5.5))")
println("coverage_ratio,$(ratio(850,5000))")
println("pruning_ratio,$(ratio(1200,4200))")
