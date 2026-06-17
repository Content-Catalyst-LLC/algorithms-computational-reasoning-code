println("case_name,boundary_score,boundary_risk,warning")
cases = [
    ("Graph traversal", 0.84, 0.80, 0.86, 0.82, 0.80, 0.76, 0.74, 0.70, 0.72, 0.58),
    ("Decision-support workflow", 0.68, 0.70, 0.74, 0.66, 0.62, 0.66, 0.58, 0.60, 0.64, 0.78),
    ("Numerical simulation", 0.82, 0.78, 0.84, 0.80, 0.78, 0.74, 0.70, 0.66, 0.70, 0.68),
    ("Recommendation ranking", 0.74, 0.72, 0.70, 0.64, 0.60, 0.66, 0.58, 0.52, 0.54, 0.56)
]

for c in cases
    name, input, output, state, transition, stopping, validation, edge, failure, interp, governance = c
    score = 100 * (0.12*input + 0.12*output + 0.12*state + 0.10*transition + 0.12*stopping + 0.10*validation + 0.08*edge + 0.08*failure + 0.08*interp + 0.08*governance)
    risk = 100 * mean([1-input, 1-output, 1-state, 1-stopping, 1-edge, 1-failure, 1-interp, 1-governance])
    println(join((name, round(score, digits=3), round(risk, digits=3), "Synthetic educational diagnostic only."), ","))
end
