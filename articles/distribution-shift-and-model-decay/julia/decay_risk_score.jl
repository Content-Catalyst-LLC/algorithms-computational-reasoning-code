input_drift = 0.31
label_drift = 0.16
performance_decay = 0.10
calibration_gap = 0.14
subgroup_gap = 0.15
override_rate = 0.11
score = (input_drift + label_drift + performance_decay + calibration_gap + subgroup_gap + override_rate) / 6
println("decay_risk_score=", round(score, digits=4))
