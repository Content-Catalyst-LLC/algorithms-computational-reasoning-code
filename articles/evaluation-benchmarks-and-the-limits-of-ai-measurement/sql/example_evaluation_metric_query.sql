WITH counts(tp, tn, fp, fn) AS (
  VALUES (42.0, 38.0, 7.0, 13.0)
)
SELECT
  (tp + tn) / (tp + tn + fp + fn) AS accuracy,
  tp / (tp + fp) AS precision,
  tp / (tp + fn) AS recall
FROM counts;
