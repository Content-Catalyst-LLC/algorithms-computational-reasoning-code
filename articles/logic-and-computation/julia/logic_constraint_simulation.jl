println("case_name,logic_quality,logic_risk,warning")
cases = [
    ("Input validation rules", 0.82, 0.84, 0.80, 0.76, 0.68, 0.78, 0.82, 0.62, 0.78, 0.70),
    ("Database query constraints", 0.78, 0.80, 0.76, 0.74, 0.72, 0.82, 0.76, 0.66, 0.70, 0.72),
    ("Decision-rule workflow", 0.74, 0.70, 0.72, 0.62, 0.68, 0.66, 0.72, 0.58, 0.76, 0.78),
    ("Program invariant checks", 0.80, 0.78, 0.74, 0.76, 0.74, 0.72, 0.80, 0.76, 0.68, 0.66)
]

for c in cases
    name, rule, pred, input, contradiction, trace, constraint, test, verify, explain, govern = c
    quality = 100 * (0.12*rule + 0.12*pred + 0.10*input + 0.10*contradiction + 0.12*trace + 0.10*constraint + 0.10*test + 0.08*verify + 0.08*explain + 0.08*govern)
    risk = 100 * mean([1-rule, 1-pred, 1-input, 1-contradiction, 1-trace, 1-constraint, 1-test, 1-explain])
    println(join((name, round(quality, digits=3), round(risk, digits=3), "Synthetic educational diagnostic only."), ","))
end
