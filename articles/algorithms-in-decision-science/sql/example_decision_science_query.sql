WITH candidate(decision_id, predicted_probability, benefit_if_act, cost_if_act, loss_if_miss, calibration, uncertainty_communication, human_review, contestability, governance, stakes) AS (
  VALUES ('clinical_triage_review', 0.82, 0.88, 0.30, 0.92, 0.78, 0.74, 0.82, 0.70, 0.76, 0.94)
)
SELECT
  decision_id,
  predicted_probability * benefit_if_act - cost_if_act AS expected_value_of_action,
  predicted_probability * loss_if_miss AS expected_loss_if_no_action,
  CASE WHEN predicted_probability >= 0.70 THEN 1 ELSE 0 END AS threshold_action,
  (calibration + uncertainty_communication + human_review + contestability + governance) / 5.0 AS decision_support_readiness_score
FROM candidate;
