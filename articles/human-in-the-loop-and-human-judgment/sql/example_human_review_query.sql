WITH review_context(context_id, time_score, information, authority, training, protection, accepted, total, overrides, reviewed, escalation, contestability, governance, stakes) AS (
  VALUES ('benefits_case_review', 0.56, 0.62, 0.58, 0.60, 0.48, 920, 1000, 18, 1000, 0.54, 0.52, 0.60, 0.88)
)
SELECT
  context_id,
  (time_score + information + authority + training + protection) / 5.0 AS review_capacity_score,
  CAST(accepted AS REAL) / total AS reliance_score,
  CAST(overrides AS REAL) / reviewed AS override_rate,
  stakes * (1.0 - (((time_score + information + authority + training + protection) / 5.0 + escalation + contestability + governance) / 4.0)) AS review_risk_score
FROM review_context;
