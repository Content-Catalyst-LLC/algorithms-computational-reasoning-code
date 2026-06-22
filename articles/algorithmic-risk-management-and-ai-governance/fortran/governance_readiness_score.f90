program governance_readiness_score
  implicit none
  real, dimension(6) :: scores
  real :: readiness
  scores = (/0.60, 0.62, 0.58, 0.52, 0.46, 0.50/)
  readiness = sum(scores) / 6.0
  print *, "governance_readiness_score=", readiness
end program governance_readiness_score
