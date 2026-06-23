WITH system(system_id, learner_impact, instructional_impact, equity_readiness, privacy_readiness, pedagogical_validity, human_review, accessibility_readiness, monitoring, governance) AS (
  VALUES ('adaptive_math_learning_pathway', 0.78, 0.86, 0.62, 0.72, 0.70, 0.66, 0.68, 0.64, 0.62)
)
SELECT
  system_id,
  (learner_impact + instructional_impact) / 2.0 AS impact_score,
  (equity_readiness + privacy_readiness + pedagogical_validity + human_review + accessibility_readiness + monitoring + governance) / 7.0 AS governance_readiness_score,
  (((learner_impact + instructional_impact) / 2.0) + (1.0 - equity_readiness) + (1.0 - pedagogical_validity) + (1.0 - ((equity_readiness + privacy_readiness + pedagogical_validity + human_review + accessibility_readiness + monitoring + governance) / 7.0))) / 4.0 AS learning_system_risk_score
FROM system;
