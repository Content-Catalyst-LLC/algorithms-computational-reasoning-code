provenance_risk = 0.66
measurement_weakness = 0.58
proxy_risk = 0.62
remediation = 0.42
historical_risk = (provenance_risk + measurement_weakness + proxy_risk + (1 - remediation)) / 4
println("historical_risk_score=", round(historical_risk, digits=4))
