println("case_name,debugging_quality,recurrence_risk,warning")
cases = [
    ("Graph traversal infinite loop", 0.88, 0.84, 0.78, 0.82, 0.80, 0.76, 0.82, 0.78, 0.70, 0.62),
    ("Data pipeline missing-value bug", 0.84, 0.78, 0.74, 0.76, 0.72, 0.80, 0.76, 0.74, 0.68, 0.70),
    ("Simulation instability", 0.80, 0.72, 0.78, 0.74, 0.70, 0.72, 0.74, 0.66, 0.64, 0.68),
    ("Recommendation ranking tie bug", 0.76, 0.70, 0.68, 0.72, 0.70, 0.74, 0.72, 0.70, 0.62, 0.58)
]

for c in cases
    name, reproducibility, expected, trace, hypothesis, isolation, edge, fix, regression, docs, governance = c
    quality = 100 * (0.12*reproducibility + 0.10*expected + 0.10*trace + 0.10*hypothesis + 0.10*isolation + 0.10*edge + 0.12*fix + 0.10*regression + 0.08*docs + 0.08*governance)
    risk = 100 * mean([1-reproducibility, 1-expected, 1-trace, 1-isolation, 1-edge, 1-fix, 1-regression, 1-docs])
    println(join((name, round(quality, digits=3), round(risk, digits=3), "Synthetic educational diagnostic only."), ","))
end
