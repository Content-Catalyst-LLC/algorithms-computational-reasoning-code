likelihood = 0.42
severity = 0.86
detectability = 0.38
controllability = 0.44
failure_risk = likelihood * severity * (1 - detectability) * (1 - controllability)
println("failure_risk_score=", round(failure_risk, digits=4))
