WITH proxy_case(case_id, validity_gap, missingness, differential_error, label_error) AS (
  VALUES ('health_spending_as_need', 0.42, 0.12, 0.24, 0.08)
)
SELECT
  case_id,
  (validity_gap + missingness + differential_error + label_error) / 4.0 AS measurement_risk_score
FROM proxy_case;
