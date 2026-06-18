function interval_scheduling(intervals)
    selected = []
    current_finish = typemin(Int)
    for interval in sort(intervals, by = x -> x[3])
        if interval[2] >= current_finish
            push!(selected, interval)
            current_finish = interval[3]
        end
    end
    return selected
end
println("test_name,value")
println("interval_count,$(length(interval_scheduling([(\"A\",0,6),(\"B\",1,4),(\"C\",5,7)])))")
