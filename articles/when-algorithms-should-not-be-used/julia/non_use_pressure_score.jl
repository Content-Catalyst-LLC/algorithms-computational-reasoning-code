scores = [0.94, 0.78, 0.56, 0.70]
pressure = sum(scores) / length(scores)
println("non_use_pressure_score=", round(pressure, digits=4))
