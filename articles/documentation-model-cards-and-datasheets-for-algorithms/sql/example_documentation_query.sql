WITH documentation_record(system_id, required_fields, completed_fields, accuracy, specificity, timeliness, accessibility, actionability, stakes) AS (
  VALUES ('benefits_eligibility_model', 16, 11, 0.62, 0.58, 0.50, 0.56, 0.52, 0.92)
)
SELECT
  system_id,
  CAST(completed_fields AS REAL) / required_fields AS documentation_completeness_score,
  (
    accuracy +
    (CAST(completed_fields AS REAL) / required_fields) +
    specificity +
    timeliness +
    accessibility +
    actionability
  ) / 6.0 AS documentation_quality_score,
  stakes * (
    1.0 - (
      (
        accuracy +
        (CAST(completed_fields AS REAL) / required_fields) +
        specificity +
        timeliness +
        accessibility +
        actionability
      ) / 6.0
    )
  ) AS documentation_risk_score
FROM documentation_record;
