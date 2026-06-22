probability = 0.82
benefit_if_act = 0.88
cost_if_act = 0.30
expected_value = probability * benefit_if_act - cost_if_act
println("expected_value_of_action=", round(expected_value, digits=4))
