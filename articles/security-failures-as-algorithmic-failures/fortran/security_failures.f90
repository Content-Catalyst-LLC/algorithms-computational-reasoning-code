program security_failures
  implicit none
  real :: weights(13) = (/0.08,0.10,0.10,0.10,0.08,0.08,0.08,0.08,0.08,0.08,0.06,0.05,0.03/)
  real :: score
  score = 100.0 * sum(weights * 0.65)
  print '(F8.3)', score
end program security_failures
