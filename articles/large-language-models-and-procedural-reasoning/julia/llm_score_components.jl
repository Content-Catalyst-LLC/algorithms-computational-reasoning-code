procedural = 1.0
source = 0.5
risk = 1.0
overall = (procedural + source + risk) / 3
println("overall_score=", round(overall, digits=3))
