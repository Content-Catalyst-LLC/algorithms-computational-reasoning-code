program harm_risk_score
  implicit none
  real :: error_likelihood, severity, exposure, contestability, harm_risk
  error_likelihood = 0.34
  severity = 0.92
  exposure = 0.78
  contestability = 0.42
  harm_risk = error_likelihood * severity * exposure * (1.0 - contestability)
  print *, "harm_risk_score=", harm_risk
end program harm_risk_score
