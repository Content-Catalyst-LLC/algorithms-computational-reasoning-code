println("case_name,translation_quality,translation_risk,warning")
cases = [
    ("Search ranking prototype", 0.82, 0.74, 0.78, 0.70, 0.80, 0.64, 0.62, 0.68, 0.78, 0.72),
    ("Decision-rule implementation", 0.76, 0.70, 0.72, 0.78, 0.74, 0.66, 0.70, 0.62, 0.72, 0.68),
    ("Simulation loop", 0.84, 0.82, 0.78, 0.86, 0.82, 0.72, 0.68, 0.70, 0.76, 0.74),
    ("Data-cleaning procedure", 0.78, 0.76, 0.74, 0.68, 0.76, 0.70, 0.64, 0.66, 0.80, 0.72)
]

for c in cases
    name, intent, input, output, state, control, edge, error, test, readable, maintain = c
    quality = 100 * (0.12*intent + 0.10*input + 0.10*output + 0.10*state + 0.12*control + 0.10*edge + 0.10*error + 0.10*test + 0.08*readable + 0.08*maintain)
    risk = 100 * mean([1-intent, 1-input, 1-output, 1-control, 1-edge, 1-error, 1-test, 1-maintain])
    println(join((name, round(quality, digits=3), round(risk, digits=3), "Synthetic educational diagnostic only."), ","))
end
