automation_risk(stakes, opacity, delegation, irreversibility) = clamp(stakes * opacity * delegation * irreversibility, 0.0, 1.0)
println(automation_risk(0.95, 0.85, 0.90, 0.80))
