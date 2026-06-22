program automation_bias_risk
  implicit none
  real :: acceptance, quality, uncertainty, review_deficit, override_friction, weak_contestability, overreliance_gap, score
  acceptance = 0.93
  quality = 0.71
  uncertainty = 0.29
  review_deficit = 0.65
  override_friction = 0.72
  weak_contestability = 0.0
  overreliance_gap = max(0.0, acceptance - quality)
  score = (acceptance + overreliance_gap + uncertainty + review_deficit + override_friction + weak_contestability) / 6.0
  print *, "automation_bias_risk_score=", score
end program automation_bias_risk
