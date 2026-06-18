subset_count(n) = 2^n
quadratic_pairs(n) = div(n*(n-1), 2)
println("test_name,value")
println("subsets_20,$(subset_count(20))")
println("pairs_100,$(quadratic_pairs(100))")
