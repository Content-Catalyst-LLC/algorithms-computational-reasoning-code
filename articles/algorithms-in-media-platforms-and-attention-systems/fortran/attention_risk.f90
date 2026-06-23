program attention_risk
  implicit none
  real :: engagement_pressure, creator_impact, public_knowledge_impact, user_control, contestability, score
  engagement_pressure = 0.92
  creator_impact = 0.88
  public_knowledge_impact = 0.78
  user_control = 0.44
  contestability = 0.42
  score = (engagement_pressure + creator_impact + public_knowledge_impact + (1.0 - user_control) + (1.0 - contestability)) / 5.0
  print *, "attention_risk_score=", score
end program attention_risk
