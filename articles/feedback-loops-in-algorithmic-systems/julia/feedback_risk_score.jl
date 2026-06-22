amplification = 0.82
concentration = 0.76
intervention = 0.44
drift = 0.28
recursive_data = 0.31
score = (amplification + concentration + intervention + drift + recursive_data) / 5
println("feedback_risk_score=", round(score, digits=4))
