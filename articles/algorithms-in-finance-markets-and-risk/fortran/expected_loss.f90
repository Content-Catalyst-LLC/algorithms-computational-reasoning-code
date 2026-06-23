program expected_loss
  implicit none
  real :: pd, lgd, ead, result
  pd = 0.035
  lgd = 0.45
  ead = 100000.0
  result = pd * lgd * ead
  print *, "expected_loss=", result
end program expected_loss
