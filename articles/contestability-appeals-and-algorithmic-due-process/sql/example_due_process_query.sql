WITH due_process_case(case_id, stakes, notice, reasons, evidence_access, human_review, correction, remedy) AS (
  VALUES ('public_benefits_eligibility', 0.94, 0.70, 0.62, 0.48, 0.55, 0.52, 0.44)
)
SELECT
  case_id,
  (notice + reasons + evidence_access + human_review + correction + remedy) / 6.0 AS contestability_score,
  stakes * (1.0 - ((notice + reasons + evidence_access + human_review + correction + remedy) / 6.0)) AS procedural_risk_score
FROM due_process_case;
