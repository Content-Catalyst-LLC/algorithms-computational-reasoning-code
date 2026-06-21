# Dependency-light Julia sketch: overlap check for propensity scores.
using Statistics

function overlap_summary(scores::Vector{Float64})
    return Dict(
        "min" => minimum(scores),
        "max" => maximum(scores),
        "mean" => mean(scores),
        "low_overlap_count" => count(x -> x < 0.10 || x > 0.90, scores)
    )
end

scores = [0.12, 0.18, 0.31, 0.44, 0.52, 0.67, 0.78, 0.91]
println(overlap_summary(scores))
