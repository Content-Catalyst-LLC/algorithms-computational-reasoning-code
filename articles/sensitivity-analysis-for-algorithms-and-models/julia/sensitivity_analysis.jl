# Minimal Julia example for sensitivity-analysis parameter sweeps.
model(demand, capacity, failure, adaptation) = clamp(0.5 + 0.3demand + 0.25failure - 0.2capacity - 0.15adaptation, 0.0, 1.0)
base = Dict(:demand => 0.45, :capacity => 0.35, :failure => 0.25, :adaptation => 0.30)
println("baseline_risk=", model(base[:demand], base[:capacity], base[:failure], base[:adaptation]))
