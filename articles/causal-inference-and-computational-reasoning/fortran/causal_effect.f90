program causal_effect
  implicit none
  real :: treated_mean, control_mean, effect
  treated_mean = 0.64
  control_mean = 0.47
  effect = treated_mean - control_mean
  print *, "causal contrast = ", effect
end program causal_effect
