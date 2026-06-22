WITH candidate(use_case, target_legitimacy, data_legitimacy, contestability, human_judgment, governance_capacity, repairability, stakes, irreversibility, proxy_illegitimacy) AS (
  VALUES ('automated_benefits_denial', 0.42, 0.48, 0.40, 0.46, 0.44, 0.38, 0.94, 0.78, 0.70)
)
SELECT
  use_case,
  (target_legitimacy + data_legitimacy + contestability + human_judgment + governance_capacity + repairability) / 6.0 AS responsible_use_readiness_score,
  (stakes + irreversibility + (1.0 - governance_capacity) + proxy_illegitimacy) / 4.0 AS non_use_pressure_score,
  CASE
    WHEN ((stakes + irreversibility + (1.0 - governance_capacity) + proxy_illegitimacy) / 4.0) >= 0.70
     AND ((target_legitimacy + data_legitimacy + contestability + human_judgment + governance_capacity + repairability) / 6.0) < 0.65
    THEN 'refuse'
    ELSE 'review_or_allow_with_controls'
  END AS decision
FROM candidate;
