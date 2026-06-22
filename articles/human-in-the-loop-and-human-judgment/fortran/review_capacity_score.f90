program review_capacity_score
  implicit none
  real, dimension(5) :: scores
  real :: capacity
  scores = (/0.56, 0.62, 0.58, 0.60, 0.48/)
  capacity = sum(scores) / 5.0
  print *, "review_capacity_score=", capacity
end program review_capacity_score
