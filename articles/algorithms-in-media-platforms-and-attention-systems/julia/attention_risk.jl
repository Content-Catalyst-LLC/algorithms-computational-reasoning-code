engagement_pressure = 0.92
creator_impact = 0.88
public_knowledge_impact = 0.78
user_control = 0.44
contestability = 0.42
score = (engagement_pressure + creator_impact + public_knowledge_impact + (1 - user_control) + (1 - contestability)) / 5
println("attention_risk_score=", round(score, digits=4))
