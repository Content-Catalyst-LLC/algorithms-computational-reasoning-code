program explanation_quality_score
  implicit none
  real, dimension(5) :: scores
  real :: quality
  scores = (/0.70, 0.74, 0.62, 0.58, 0.46/)
  quality = sum(scores) / 5.0
  print *, "explanation_quality_score=", quality
end program explanation_quality_score
