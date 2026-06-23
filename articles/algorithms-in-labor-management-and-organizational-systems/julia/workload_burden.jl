pace = 0.84
hours = 0.72
fatigue = 0.70
schedule_volatility = 0.78
burden = (pace + hours + fatigue + schedule_volatility) / 4
println("workload_burden_score=", round(burden, digits=4))
