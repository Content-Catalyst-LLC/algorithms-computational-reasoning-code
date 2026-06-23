due_process = 0.58
transparency = 0.52
human_review = 0.60
appeal_readiness = 0.54
score = (due_process + transparency + human_review + appeal_readiness) / 4
println("procedural_readiness_score=", round(score, digits=4))
