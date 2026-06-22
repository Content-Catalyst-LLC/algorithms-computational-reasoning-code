program accountability_capacity_score
  implicit none
  real, dimension(6) :: scores
  real :: capacity
  scores = (/0.72, 0.68, 0.64, 0.58, 0.52, 0.66/)
  capacity = sum(scores) / 6.0
  print *, "accountability_capacity_score=", capacity
end program accountability_capacity_score
