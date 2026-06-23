WITH system(system_id, patient_impact, population_impact, clinical_validation, equity_readiness, privacy_readiness, human_review, workflow_integration, monitoring, governance) AS (
  VALUES ('sepsis_alert_model', 0.92, 0.54, 0.70, 0.58, 0.72, 0.66, 0.62, 0.64, 0.60)
)
SELECT
  system_id,
  (patient_impact + population_impact) / 2.0 AS impact_score,
  (clinical_validation + equity_readiness + privacy_readiness + human_review + workflow_integration + monitoring + governance) / 7.0 AS governance_readiness_score,
  (((patient_impact + population_impact) / 2.0) + (1.0 - clinical_validation) + (1.0 - equity_readiness) + (1.0 - ((clinical_validation + equity_readiness + privacy_readiness + human_review + workflow_integration + monitoring + governance) / 7.0))) / 4.0 AS health_algorithm_risk_score
FROM system;
