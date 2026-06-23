function delegation_risk(decision_severity, automation_level, opacity)
    clamp(decision_severity * automation_level * opacity, 0.0, 1.0)
end

println(delegation_risk(0.95, 0.95, 0.80))
