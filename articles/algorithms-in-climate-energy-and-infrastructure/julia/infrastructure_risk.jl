hazard = 0.80
exposure = 0.75
vulnerability = 0.60
risk = hazard * exposure * vulnerability
println("infrastructure_risk=", round(risk, digits=4))
