violations(assign, constraints) = sum(assign[l] == assign[r] for (l,r) in constraints)
constraints = [("A","B"), ("B","C")]
candidate = Dict("A"=>"red", "B"=>"blue", "C"=>"red")
invalid = Dict("A"=>"red", "B"=>"red", "C"=>"blue")
println("test_name,value")
println("candidate_violation_count,$(violations(candidate,constraints))")
println("invalid_violation_count,$(violations(invalid,constraints))")
