program probability_calculator
  implicit none
  real :: p_hat, n, se
  p_hat = 0.57
  n = 1000.0
  se = sqrt((p_hat * (1.0 - p_hat)) / n)
  print *, "p_hat=", p_hat, " standard_error=", se
end program probability_calculator
