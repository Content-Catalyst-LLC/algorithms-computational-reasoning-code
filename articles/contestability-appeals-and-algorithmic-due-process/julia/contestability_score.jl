notice = 0.70
reasons = 0.62
evidence_access = 0.48
human_review = 0.55
correction = 0.52
remedy = 0.44
score = (notice + reasons + evidence_access + human_review + correction + remedy) / 6
println("contestability_score=", round(score, digits=4))
