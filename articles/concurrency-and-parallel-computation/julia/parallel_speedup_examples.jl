speedup(t1,tp) = tp == 0 ? 0 : t1 / tp
amdahl(p,s) = p == 0 ? 0 : 1 / (s + ((1 - s) / p))
efficiency(p,sp) = p == 0 ? 0 : sp / p
println("test_name,value")
println("observed_speedup_120_to_28,$(speedup(120,28))")
println("amdahl_speedup_8_workers,$(amdahl(8,0.12))")
println("efficiency_8_workers,$(efficiency(8, speedup(120,28)))")
