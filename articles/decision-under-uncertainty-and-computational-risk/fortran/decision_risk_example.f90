program decision_risk_example
  implicit none
  real :: p, benefit, loss, cost, value
  p = 0.42
  benefit = 150.0
  loss = 80.0
  cost = 25.0
  value = max(0.0, min(1.0, p)) * benefit - max(0.0, min(1.0, p)) * loss - cost
  print *, value
end program decision_risk_example
