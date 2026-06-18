function binary_fitness(candidate)
    return sum(candidate)
end
function hamming_diversity(a, b)
    return sum(a .!= b) / length(a)
end
println("test_name,value")
println("binary_fitness,$(binary_fitness([1,0,1,1]))")
println("hamming_diversity,$(hamming_diversity([1,0,1,1],[0,0,1,0]))")
