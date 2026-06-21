program uncertainty_quantification
  implicit none
  real :: score
  score = max(0.0, min(1.0, 0.42 + 0.38*0.55 - 0.31*0.50 + 0.27*0.22 - 0.18*0.30))
  print *, 'risk_score=', score
end program uncertainty_quantification
