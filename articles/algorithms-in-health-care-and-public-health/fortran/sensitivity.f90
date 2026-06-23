program sensitivity_example
  implicit none
  real :: tp, fn_cases, sensitivity
  tp = 86.0
  fn_cases = 14.0
  sensitivity = tp / (tp + fn_cases)
  print *, "sensitivity=", sensitivity
end program sensitivity_example
