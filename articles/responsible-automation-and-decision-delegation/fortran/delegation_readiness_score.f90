program delegation_readiness_score
  implicit none
  real, dimension(6) :: scores
  real :: readiness
  scores = (/0.62, 0.58, 0.46, 0.52, 0.60, 0.58/)
  readiness = sum(scores) / 6.0
  print *, "delegation_readiness_score=", readiness
end program delegation_readiness_score
