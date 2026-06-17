println("case_name,literacy_support_score,literacy_gap_score,warning")
cases = [
    ("Search ranking", 0.62, 0.54, 0.66, 0.40, 0.38, 0.52, 0.70, 0.68),
    ("Public decision-support workflow", 0.58, 0.62, 0.56, 0.48, 0.70, 0.76, 0.82, 0.74),
    ("Scientific simulation dashboard", 0.76, 0.72, 0.74, 0.78, 0.60, 0.68, 0.70, 0.80),
    ("Recommendation feed", 0.40, 0.42, 0.48, 0.30, 0.32, 0.46, 0.66, 0.50)
]

for c in cases
    name, procedural, data, output, uncertainty, contest, governance, impact, judgment = c
    support = 100 * (0.14*procedural + 0.12*data + 0.14*output + 0.12*uncertainty + 0.12*contest + 0.12*governance + 0.12*impact + 0.12*judgment)
    gap = 100 * mean([1-procedural, 1-data, 1-output, 1-uncertainty, 1-contest, 1-governance, 1-impact, 1-judgment])
    println(join((name, round(support, digits=3), round(gap, digits=3), "Synthetic educational diagnostic only."), ","))
end
