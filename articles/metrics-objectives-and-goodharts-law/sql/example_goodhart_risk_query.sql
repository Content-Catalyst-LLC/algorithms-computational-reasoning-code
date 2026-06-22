WITH metric_case(case_id, proxy_gap, pressure, gaming, guardrail_penalty) AS (
  VALUES ('platform_engagement', 0.38, 0.88, 0.72, 1.0)
)
SELECT
  case_id,
  (proxy_gap + pressure + gaming + guardrail_penalty) / 4.0 AS goodhart_risk_score
FROM metric_case;
