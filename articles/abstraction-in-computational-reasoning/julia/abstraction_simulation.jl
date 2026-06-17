println("case_name,abstraction_score,abstraction_risk,warning")
cases = [
    ("Search ranking", 0.82, 0.70, 0.62, 0.58, 0.72, 0.60, 0.58, 0.50, 0.56, 0.64),
    ("Transit model", 0.78, 0.72, 0.66, 0.68, 0.70, 0.72, 0.64, 0.62, 0.66, 0.74),
    ("Database schema", 0.84, 0.78, 0.70, 0.72, 0.76, 0.74, 0.72, 0.60, 0.70, 0.68),
    ("Decision-support score", 0.70, 0.60, 0.48, 0.50, 0.64, 0.52, 0.46, 0.44, 0.66, 0.78)
]

for c in cases
    name, clarity, scope, detail, assumptions, testability, interpretation, reuse, uncertainty, governance, risk_awareness = c
    score = 100 * (0.12*clarity + 0.10*scope + 0.12*detail + 0.12*assumptions + 0.10*testability + 0.12*interpretation + 0.08*reuse + 0.08*uncertainty + 0.08*governance + 0.08*risk_awareness)
    risk = 100 * mean([1-scope, 1-detail, 1-assumptions, 1-interpretation, 1-reuse, 1-uncertainty, 1-governance, 1-risk_awareness])
    println(join((name, round(score, digits=3), round(risk, digits=3), "Synthetic educational diagnostic only."), ","))
end
