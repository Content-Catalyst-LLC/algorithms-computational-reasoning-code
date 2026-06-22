program documentation_quality_score
  implicit none
  real, dimension(6) :: scores
  real :: quality
  scores = (/0.62, 0.6875, 0.58, 0.50, 0.56, 0.52/)
  quality = sum(scores) / 6.0
  print *, "documentation_quality_score=", quality
end program documentation_quality_score
