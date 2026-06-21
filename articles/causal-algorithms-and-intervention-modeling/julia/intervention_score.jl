# Compact Julia example: intervention effect and net benefit.
function net_benefit(effect, implementation_cost; cost_weight=0.35, governance_risk=0.08, risk_weight=0.15)
    return effect - cost_weight * implementation_cost - risk_weight * governance_risk
end

baseline = 0.42
intervention = 0.57
effect = intervention - baseline
println("estimated_effect=", round(effect, digits=6))
println("net_benefit=", round(net_benefit(effect, 0.20), digits=6))
