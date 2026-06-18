efficiency_gain(baseline, optimized) = (baseline - optimized) / baseline
understanding(readability, debuggability, explainability, auditability, maintainability) = 100 * mean([readability, debuggability, explainability, auditability, maintainability])
println("test_name,value")
println("efficiency_gain_percent,$(100*efficiency_gain(100.0,64.0))")
println("understanding_score,$(understanding(0.80,0.75,0.70,0.78,0.82))")
