# Optional Julia example for probability estimation.
using Random, Statistics

function estimate_probability(n::Int, p::Float64; seed::Int=2026)
    rng = MersenneTwister(seed)
    trials = rand(rng, n) .< p
    phat = mean(trials)
    se = sqrt(phat * (1 - phat) / n)
    return (estimate = phat, standard_error = se)
end

println(estimate_probability(1000, 0.57))
