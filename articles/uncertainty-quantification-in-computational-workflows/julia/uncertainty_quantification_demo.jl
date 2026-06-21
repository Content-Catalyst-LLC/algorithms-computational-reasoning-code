# Minimal Julia demonstration for uncertainty propagation.
using Random, Statistics

function bounded_normal(center, spread)
    return clamp(center + spread * randn(), 0.0, 1.0)
end

function risk_model(demand, capacity, failure_rate, adaptation_rate, noise)
    return clamp(0.42 + 0.38*demand - 0.31*capacity + 0.27*failure_rate - 0.18*adaptation_rate + noise, 0.0, 1.0)
end

Random.seed!(2026)
values = Float64[]
for _ in 1:1000
    push!(values, risk_model(
        bounded_normal(0.55, 0.12),
        bounded_normal(0.50, 0.10),
        bounded_normal(0.22, 0.08),
        bounded_normal(0.30, 0.10),
        0.035 * randn()
    ))
end

println("mean=", mean(values))
println("std=", std(values))
println("exceedance=", mean(values .>= 0.62))
