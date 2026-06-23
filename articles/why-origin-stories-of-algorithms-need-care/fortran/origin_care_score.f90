program origin_care_score_example
  implicit none
  real :: scores(10)
  scores = (/0.96, 0.98, 0.96, 0.88, 0.98, 0.90, 0.90, 0.96, 0.98, 0.98/)
  print *, "origin_care_score=", sum(scores) / size(scores)
end program origin_care_score_example
