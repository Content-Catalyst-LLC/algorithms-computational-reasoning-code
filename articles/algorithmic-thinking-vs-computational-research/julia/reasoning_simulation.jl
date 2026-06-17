println("name,algorithmic_thinking_score,computational_reasoning_score,reasoning_gap,warning")
profiles = [
    ("Recipe-like procedure", 0.86, 0.72, 0.70, 0.62, 0.42, 0.34, 0.30, 0.48, 0.20, 0.28),
    ("Classroom algorithm exercise", 0.90, 0.82, 0.84, 0.78, 0.62, 0.46, 0.62, 0.58, 0.32, 0.36),
    ("Search and ranking system", 0.72, 0.70, 0.76, 0.66, 0.78, 0.76, 0.72, 0.62, 0.70, 0.72),
    ("Public decision-support workflow", 0.68, 0.66, 0.64, 0.72, 0.80, 0.84, 0.66, 0.78, 0.86, 0.88),
    ("Scientific modeling workflow", 0.74, 0.78, 0.76, 0.82, 0.86, 0.80, 0.84, 0.78, 0.74, 0.68)
]

for p in profiles
    name, step, decomp, control, test, rep, data_context, complexity, interp, governance, stakeholder = p
    algorithmic = 100 * (0.28*step + 0.24*decomp + 0.24*control + 0.24*test)
    computational = 100 * (0.11*step + 0.10*decomp + 0.09*control + 0.10*test + 0.13*rep + 0.12*data_context + 0.11*complexity + 0.12*interp + 0.12*governance + 0.10*stakeholder)
    println(join((name, round(algorithmic, digits=3), round(computational, digits=3), round(computational - algorithmic, digits=3), "Synthetic educational diagnostic only."), ","))
end
