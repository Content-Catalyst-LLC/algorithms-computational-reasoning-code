println("case_name,formalization_score,formalization_risk,warning")
cases = [
    ("Document search", 0.82, 0.78, 0.62, 0.60, 0.70, 0.58, 0.62, 0.74, 0.70, 0.56),
    ("Worker scheduling", 0.72, 0.76, 0.82, 0.70, 0.58, 0.54, 0.56, 0.68, 0.60, 0.62),
    ("Public service triage", 0.60, 0.72, 0.68, 0.58, 0.52, 0.46, 0.48, 0.60, 0.54, 0.66),
    ("Scientific simulation", 0.86, 0.80, 0.78, 0.88, 0.76, 0.84, 0.72, 0.82, 0.78, 0.70)
]

for c in cases
    name, input, output, constraint, state, objective, assumptions, edges, stopping, evaluation, governance = c
    score = 100 * (0.10*input + 0.10*output + 0.10*constraint + 0.08*state + 0.14*objective + 0.12*assumptions + 0.10*edges + 0.08*stopping + 0.10*evaluation + 0.08*governance)
    risk = 100 * mean([1-input, 1-output, 1-constraint, 1-objective, 1-assumptions, 1-edges, 1-evaluation, 1-governance])
    println(join((name, round(score, digits=3), round(risk, digits=3), "Synthetic educational diagnostic only."), ","))
end
