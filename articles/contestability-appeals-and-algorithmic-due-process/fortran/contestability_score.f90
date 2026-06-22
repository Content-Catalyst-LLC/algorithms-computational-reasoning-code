program contestability_score
  implicit none
  real :: notice, reasons, evidence_access, human_review, correction, remedy, score
  notice = 0.70
  reasons = 0.62
  evidence_access = 0.48
  human_review = 0.55
  correction = 0.52
  remedy = 0.44
  score = (notice + reasons + evidence_access + human_review + correction + remedy) / 6.0
  print *, "contestability_score=", score
end program contestability_score
