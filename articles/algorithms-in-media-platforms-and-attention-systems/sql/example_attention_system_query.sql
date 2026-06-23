WITH system(system_id, engagement_pressure, transparency, contestability, moderation_readiness, creator_impact, public_knowledge_impact, user_control, governance, monitoring) AS (
  VALUES ('short_video_recommendation', 0.92, 0.48, 0.42, 0.66, 0.88, 0.78, 0.44, 0.54, 0.60)
)
SELECT
  system_id,
  (transparency + contestability + moderation_readiness + user_control + governance + monitoring) / 6.0 AS governance_readiness_score,
  (engagement_pressure + creator_impact + public_knowledge_impact + (1.0 - user_control) + (1.0 - contestability)) / 5.0 AS attention_risk_score,
  ((engagement_pressure + creator_impact + public_knowledge_impact + (1.0 - user_control) + (1.0 - contestability)) / 5.0) *
  (1.0 - ((transparency + contestability + moderation_readiness + user_control + governance + monitoring) / 6.0)) AS platform_risk_score
FROM system;
