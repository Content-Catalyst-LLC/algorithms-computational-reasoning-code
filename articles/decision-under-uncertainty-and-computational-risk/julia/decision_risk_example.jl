# Compact Julia example: expected net value.
function expected_net_value(p, benefit, loss, cost)
    p = clamp(p, 0.0, 1.0)
    return p * benefit - p * loss - cost
end

println(expected_net_value(0.42, 150.0, 80.0, 25.0))
