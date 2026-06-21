program sensitivity_analysis
  implicit none
  real :: risk
  risk = min(1.0, max(0.0, 0.5 + 0.30*0.45 + 0.25*0.25 - 0.20*0.35 - 0.15*0.30))
  print *, "baseline_risk=", risk
end program sensitivity_analysis
