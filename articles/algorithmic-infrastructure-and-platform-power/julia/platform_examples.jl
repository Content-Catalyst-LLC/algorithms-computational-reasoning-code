dependency_score(a,v,c,s,e) = 100 * (0.22a + 0.22v + 0.18c + 0.24s + 0.14e)
switching_cost(m,r,t,d,l) = m + r + t + d + l
ratio(n,d) = d == 0 ? 0 : n / d
println("test_name,value")
println("dependency_score,$(dependency_score(0.80,0.90,0.70,0.85,0.65))")
println("switching_cost,$(switching_cost(45000,120000,18000,24000,75000))")
println("api_dependency_ratio,$(ratio(850000,1000000))")
println("visibility_share,$(ratio(250000,5000000))")
