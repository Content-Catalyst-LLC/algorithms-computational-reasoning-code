error_likelihood = 0.34
severity = 0.92
exposure = 0.78
contestability = 0.42
harm_risk = error_likelihood * severity * exposure * (1 - contestability)
println("harm_risk_score=", round(harm_risk, digits=4))
