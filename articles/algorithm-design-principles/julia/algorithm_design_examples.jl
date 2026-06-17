sorted_invariant(values) = all(values[i] <= values[i+1] for i in 1:length(values)-1)
println("test_name,status")
println("sorted_valid,$(sorted_invariant([1,2,2,3]) ? "pass" : "fail")")
println("sorted_invalid,$(sorted_invariant([1,3,2]) ? "pass" : "fail")")
