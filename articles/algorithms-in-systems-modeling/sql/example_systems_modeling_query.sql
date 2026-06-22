WITH scenario(scenario_id, feedback_strength, network_dependency, scenario_uncertainty, resilience, calibration, documentation, governance, stakes) AS (
  VALUES ('urban_congestion_intervention', 0.72, 0.68, 0.54, 0.62, 0.70, 0.74, 0.70, 0.76)
)
SELECT
  scenario_id,
  (feedback_strength + network_dependency + scenario_uncertainty + (1.0 - resilience)) / 4.0 AS system_vulnerability_score,
  (calibration + documentation + governance + resilience) / 4.0 AS model_readiness_score,
  stakes *
    ((feedback_strength + network_dependency + scenario_uncertainty + (1.0 - resilience)) / 4.0) *
    (1.0 - ((calibration + documentation + governance + resilience) / 4.0)) AS system_modeling_risk_score
FROM scenario;
