program identity_access
  implicit none
  real :: weights(12) = (/0.10,0.11,0.11,0.09,0.09,0.10,0.09,0.09,0.08,0.06,0.06,0.02/)
  real :: score
  score = sum(0.75 * weights) * 100.0
  print *, score
end program identity_access
