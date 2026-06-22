program historical_risk_score
  implicit none
  real :: provenance_risk, measurement_weakness, proxy_risk, remediation, score
  provenance_risk = 0.66
  measurement_weakness = 0.58
  proxy_risk = 0.62
  remediation = 0.42
  score = (provenance_risk + measurement_weakness + proxy_risk + (1.0 - remediation)) / 4.0
  print *, "historical_risk_score=", score
end program historical_risk_score
