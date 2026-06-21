# Compact Julia demonstration for Monte Carlo estimation.
using Random, Statistics
rng = MersenneTwister(42)
samples = 10_000
inside = 0
for _ in 1:samples
    x = rand(rng); y = rand(rng)
    if x*x + y*y <= 1.0
        inside += 1
    end
end
println("pi_estimate=", 4 * inside / samples)
