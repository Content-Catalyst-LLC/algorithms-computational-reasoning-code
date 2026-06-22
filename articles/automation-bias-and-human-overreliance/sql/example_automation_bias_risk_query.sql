WITH oversight_case(case_id, acceptance, quality, uncertainty, review_deficit, override_friction, weak_contestability) AS (
  VALUES ('content_moderation_queue', 0.93, 0.71, 0.29, 0.65, 0.72, 0.0)
)
SELECT
  case_id,
  (acceptance + MAX(0, acceptance - quality) + uncertainty + review_deficit + override_friction + weak_contestability) / 6.0 AS automation_bias_risk_score
FROM oversight_case;
