linear_objective(c, x) = sum(c .* x)
constraint_margin(limit, observed) = limit - observed
penalty_objective(base, penalty, weight) = base + weight * penalty
tradeoff(cost, quality, risk) = 0.35*(1-cost) + 0.40*quality + 0.25*(1-risk)
println("test_name,value")
println("linear_objective,$(linear_objective([4.0,2.0,1.5],[10.0,20.0,5.0]))")
println("constraint_margin,$(constraint_margin(100.0,86.5))")
println("penalty_objective,$(penalty_objective(42.0,8.0,2.5))")
println("normalized_tradeoff_score,$(tradeoff(0.30,0.82,0.25))")
