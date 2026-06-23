program infrastructure_risk_example
  implicit none
  real :: hazard, exposure, vulnerability, risk
  hazard = 0.80
  exposure = 0.75
  vulnerability = 0.60
  risk = hazard * exposure * vulnerability
  print *, "infrastructure_risk=", risk
end program infrastructure_risk_example
