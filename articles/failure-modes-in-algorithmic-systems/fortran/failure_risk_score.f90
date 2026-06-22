program failure_risk_score
  implicit none
  real :: likelihood, severity, detectability, controllability, failure_risk
  likelihood = 0.42
  severity = 0.86
  detectability = 0.38
  controllability = 0.44
  failure_risk = likelihood * severity * (1.0 - detectability) * (1.0 - controllability)
  print *, "failure_risk_score=", failure_risk
end program failure_risk_score
