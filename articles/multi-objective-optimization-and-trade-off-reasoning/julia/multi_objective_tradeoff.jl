# Dependency-light Julia example for weighted multi-objective scores.

alternatives = [
    (name="A", cost=72.0, risk=34.0, quality=82.0),
    (name="B", cost=64.0, risk=41.0, quality=76.0),
    (name="C", cost=81.0, risk=26.0, quality=88.0),
    (name="D", cost=58.0, risk=52.0, quality=69.0)
]

function norm_min(x, xs)
    maximum(xs) == minimum(xs) && return 1.0
    return (maximum(xs) - x) / (maximum(xs) - minimum(xs))
end

function norm_max(x, xs)
    maximum(xs) == minimum(xs) && return 1.0
    return (x - minimum(xs)) / (maximum(xs) - minimum(xs))
end

costs = [a.cost for a in alternatives]
risks = [a.risk for a in alternatives]
qualities = [a.quality for a in alternatives]

scores = [(a.name, 0.35 * norm_min(a.cost, costs) + 0.30 * norm_min(a.risk, risks) + 0.35 * norm_max(a.quality, qualities)) for a in alternatives]
println(sort(scores, by=x -> x[2], rev=true))
