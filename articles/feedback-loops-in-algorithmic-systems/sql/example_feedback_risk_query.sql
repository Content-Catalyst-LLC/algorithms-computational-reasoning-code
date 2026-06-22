WITH feedback_case(case_id, amplification, concentration, intervention, drift, recursive_data) AS (
  VALUES ('recommendation_feed', 0.82, 0.76, 0.44, 0.28, 0.31)
)
SELECT
  case_id,
  (amplification + concentration + intervention + drift + recursive_data) / 5.0 AS feedback_risk_score
FROM feedback_case;
