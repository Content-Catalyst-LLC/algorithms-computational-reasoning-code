score_in_range(x) = 0 <= x <= 100
println("test_name,status")
println("score_72,$(score_in_range(72) ? "pass" : "fail")")
println("score_150,$(score_in_range(150) ? "pass" : "fail")")
