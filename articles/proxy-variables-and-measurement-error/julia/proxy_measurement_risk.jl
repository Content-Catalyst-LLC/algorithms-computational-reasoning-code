validity_gap = 0.42
missingness = 0.12
differential_error = 0.24
label_error = 0.08
score = (validity_gap + missingness + differential_error + label_error) / 4
println("measurement_risk_score=", round(score, digits=4))
