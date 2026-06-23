program transfer_score_example
  implicit none
  real :: scores(9)
  scores = (/0.98, 0.90, 0.94, 0.88, 0.94, 0.90, 0.96, 0.84, 0.96/)
  print *, "transfer_score=", sum(scores) / size(scores)
end program transfer_score_example
