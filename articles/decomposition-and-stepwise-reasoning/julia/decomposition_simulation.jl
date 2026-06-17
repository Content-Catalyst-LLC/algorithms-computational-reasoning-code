println("case_name,decomposition_score,decomposition_risk,warning")
cases = [
    ("Search system", 0.82, 0.78, 0.80, 0.82, 0.72, 0.76, 0.68, 0.72, 0.58, 0.62),
    ("Public decision-support workflow", 0.74, 0.66, 0.70, 0.68, 0.60, 0.66, 0.72, 0.58, 0.76, 0.80),
    ("Scientific simulation", 0.86, 0.82, 0.84, 0.80, 0.78, 0.76, 0.78, 0.82, 0.70, 0.76),
    ("Knowledge architecture", 0.80, 0.76, 0.72, 0.74, 0.70, 0.64, 0.72, 0.80, 0.68, 0.70)
]

for c in cases
    name, subproblem, boundary, input_output, sequencing, dependencies, testability, traceability, recomposition, governance, risk_awareness = c
    score = 100 * (0.12*subproblem + 0.10*boundary + 0.10*input_output + 0.10*sequencing + 0.10*dependencies + 0.12*testability + 0.10*traceability + 0.10*recomposition + 0.08*governance + 0.08*risk_awareness)
    risk = 100 * mean([1-boundary, 1-dependencies, 1-traceability, 1-recomposition, 1-governance, 1-risk_awareness])
    println(join((name, round(score, digits=3), round(risk, digits=3), "Synthetic educational diagnostic only."), ","))
end
