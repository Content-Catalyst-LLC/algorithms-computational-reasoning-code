program automation_risk_example
  implicit none
  real :: risk
  risk = max(0.0, min(1.0, 0.95 * 0.85 * 0.90 * 0.80))
  print *, risk
end program automation_risk_example
