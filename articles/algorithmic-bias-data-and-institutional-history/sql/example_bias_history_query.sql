WITH group_metrics(group_id, data_share, deployment_share, selection_rate, label_positive_rate, verified_positive_rate, provenance_risk, measurement_weakness, proxy_risk, remediation) AS (
  VALUES
    ('A', 0.42, 0.38, 0.46, 0.44, 0.41, 0.38, 0.30, 0.36, 0.68),
    ('B', 0.28, 0.36, 0.31, 0.33, 0.43, 0.66, 0.58, 0.62, 0.42),
    ('C', 0.30, 0.26, 0.37, 0.39, 0.42, 0.50, 0.44, 0.48, 0.54)
)
SELECT
  group_id,
  ABS(data_share - deployment_share) AS representation_gap,
  ABS(label_positive_rate - verified_positive_rate) AS label_gap,
  (provenance_risk + measurement_weakness + proxy_risk + (1.0 - remediation)) / 4.0 AS historical_risk_score
FROM group_metrics
ORDER BY historical_risk_score DESC;
