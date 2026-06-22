program goodhart_risk
  implicit none
  real :: proxy_gap, pressure, gaming, guardrail_penalty, score
  proxy_gap = 0.38
  pressure = 0.88
  gaming = 0.72
  guardrail_penalty = 1.0
  score = (proxy_gap + pressure + gaming + guardrail_penalty) / 4.0
  print *, "goodhart_risk_score=", score
end program goodhart_risk
