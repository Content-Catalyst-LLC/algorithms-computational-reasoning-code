function relative_improvement(baseline, heuristic, direction)
    if direction == "minimize"
        return (baseline - heuristic) / baseline
    else
        return (heuristic - baseline) / baseline
    end
end
println("test_name,value")
println("route_improvement,$(relative_improvement(34.0,27.0,"minimize"))")
println("annealing_improvement,$(relative_improvement(18.5,12.2,"minimize"))")
