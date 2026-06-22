WITH monitoring_period(period, input_drift, label_drift, performance_decay, calibration_gap, subgroup_gap, override_rate) AS (
  VALUES ('month_3', 0.31, 0.16, 0.10, 0.14, 0.15, 0.11)
)
SELECT
  period,
  (input_drift + label_drift + performance_decay + calibration_gap + subgroup_gap + override_rate) / 6.0 AS decay_risk_score
FROM monitoring_period;
