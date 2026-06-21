program intervention_effect
  implicit none
  real :: baseline, intervention, effect
  baseline = 0.42
  intervention = 0.57
  effect = intervention - baseline
  print '(A,F8.6)', 'estimated_effect=', effect
end program intervention_effect
