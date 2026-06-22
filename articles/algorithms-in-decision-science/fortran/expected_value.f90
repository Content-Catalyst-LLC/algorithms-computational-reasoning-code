program expected_value
  implicit none
  real :: probability, benefit_if_act, cost_if_act, ev
  probability = 0.82
  benefit_if_act = 0.88
  cost_if_act = 0.30
  ev = probability * benefit_if_act - cost_if_act
  print *, "expected_value_of_action=", ev
end program expected_value
