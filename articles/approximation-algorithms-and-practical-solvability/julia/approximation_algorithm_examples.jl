function relative_gap_minimization(algorithm_value, lower_bound)
    return (algorithm_value - lower_bound) / lower_bound
end
println("test_name,value")
println("relative_gap,$(relative_gap_minimization(12,10))")
println("approximation_ratio,$(12/8)")
