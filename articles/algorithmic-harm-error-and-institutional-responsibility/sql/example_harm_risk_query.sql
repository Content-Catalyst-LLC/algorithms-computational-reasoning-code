WITH harm_case(case_id, error_likelihood, severity, exposure, contestability, ownership, monitoring, appeals, repair, governance) AS (
  VALUES ('public_benefits_denial', 0.34, 0.92, 0.78, 0.42, 0.48, 0.45, 0.40, 0.35, 0.50)
)
SELECT
  case_id,
  error_likelihood * severity * exposure * (1.0 - contestability) AS harm_risk_score,
  (ownership + monitoring + appeals + repair + governance) / 5.0 AS responsibility_capacity,
  MAX(0, severity - repair) AS remediation_gap
FROM harm_case;
