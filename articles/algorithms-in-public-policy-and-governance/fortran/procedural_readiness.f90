program procedural_readiness
  implicit none
  real :: due_process, transparency, human_review, appeal_readiness, score
  due_process = 0.58
  transparency = 0.52
  human_review = 0.60
  appeal_readiness = 0.54
  score = (due_process + transparency + human_review + appeal_readiness) / 4.0
  print *, "procedural_readiness_score=", score
end program procedural_readiness
