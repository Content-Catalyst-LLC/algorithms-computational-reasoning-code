WITH explanation_case(case_id, faithfulness, stability, understandability, actionability, uncertainty, documentation, contestability, governance, stakes) AS (
  VALUES ('benefits_eligibility_notice', 0.70, 0.74, 0.62, 0.58, 0.46, 0.68, 0.55, 0.60, 0.88)
)
SELECT
  case_id,
  (faithfulness + stability + understandability + actionability + uncertainty) / 5.0 AS explanation_quality_score,
  (documentation + governance + uncertainty) / 3.0 AS transparency_capacity_score,
  stakes * (1.0 - (((faithfulness + stability + understandability + actionability + uncertainty) / 5.0 + (documentation + governance + uncertainty) / 3.0 + contestability + governance) / 4.0)) AS explanation_risk_score
FROM explanation_case;
