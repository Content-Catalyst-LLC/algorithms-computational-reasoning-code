WITH failure_case(failure_id, likelihood, severity, detectability, controllability, monitoring, fallback, rollback, escalation, repair) AS (
  VALUES ('schema_drift_in_eligibility_pipeline', 0.42, 0.86, 0.38, 0.44, 0.42, 0.36, 0.50, 0.46, 0.40)
)
SELECT
  failure_id,
  likelihood * severity * (1.0 - detectability) * (1.0 - controllability) AS failure_risk_score,
  likelihood * severity * (1.0 - detectability) AS priority_score,
  (monitoring + fallback + rollback + escalation + repair) / 5.0 AS resilience_capacity
FROM failure_case;
