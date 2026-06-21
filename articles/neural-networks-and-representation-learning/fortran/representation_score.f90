program representation_score_example
  implicit none
  real :: x1, x2, x3, bias, linear, score
  x1 = 0.5
  x2 = -0.2
  x3 = 0.7
  bias = 0.0
  linear = 0.9*x1 - 0.7*x2 + 0.35*x3 + bias
  score = 1.0 / (1.0 + exp(-linear))
  print '(F8.6)', score
end program representation_score_example
