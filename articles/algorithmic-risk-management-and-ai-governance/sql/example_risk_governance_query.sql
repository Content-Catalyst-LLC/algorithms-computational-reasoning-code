WITH risk_item(risk_id, severity, likelihood, detectability, ownership, documentation, monitoring, contestability, remediation, stop_authority, control_effectiveness) AS (
  VALUES ('benefits_denial_error', 0.92, 0.44, 0.42, 0.60, 0.62, 0.58, 0.52, 0.46, 0.50, 0.48)
)
SELECT
  risk_id,
  severity * likelihood * (1.0 - detectability) AS inherent_risk_score,
  (ownership + documentation + monitoring + contestability + remediation + stop_authority) / 6.0 AS governance_readiness_score,
  severity * likelihood * (1.0 - detectability) * (1.0 - control_effectiveness) AS residual_risk_score
FROM risk_item;
