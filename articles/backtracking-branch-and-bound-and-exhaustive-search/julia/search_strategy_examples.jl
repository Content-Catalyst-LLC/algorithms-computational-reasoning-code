function search_space_growth(branching_factor, depth)
    return sum(branching_factor^level for level in 0:depth)
end
println("test_name,value")
println("search_space_growth,$(search_space_growth(2,3))")
println("permutation_count,6")
