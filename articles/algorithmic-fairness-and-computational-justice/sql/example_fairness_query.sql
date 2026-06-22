WITH group_metrics(group_id, selection_rate, false_positive_rate, false_negative_rate, calibration_gap, justice_capacity_score) AS (
  VALUES
    ('A', 0.42, 0.2667, 0.3500, 0.04, 0.7011),
    ('B', 0.31, 0.1724, 0.5000, 0.12, 0.6100),
    ('C', 0.36, 0.2167, 0.4250, 0.05, 0.6436)
)
SELECT
  MAX(selection_rate) - MIN(selection_rate) AS selection_gap,
  MAX(false_positive_rate) - MIN(false_positive_rate) AS false_positive_gap,
  MAX(false_negative_rate) - MIN(false_negative_rate) AS false_negative_gap,
  MAX(calibration_gap) AS max_calibration_gap,
  AVG(justice_capacity_score) AS mean_justice_capacity_score
FROM group_metrics;
