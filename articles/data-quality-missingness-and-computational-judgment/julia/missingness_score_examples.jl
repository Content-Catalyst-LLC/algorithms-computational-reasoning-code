missingness_rate(missing, total) = total == 0 ? 0 : missing / total
completeness_score(missing, total) = 1 - missingness_rate(missing, total)
quality(c, v, t, p, val) = 100 * (0.25*c + 0.20*v + 0.15*t + 0.22*p + 0.18*val)
println("test_name,value")
println("missingness_rate_45_of_1000,$(missingness_rate(45,1000))")
println("completeness_score_45_of_1000,$(completeness_score(45,1000))")
println("data_quality_score,$(quality(.92,.88,.86,.90,.89))")
