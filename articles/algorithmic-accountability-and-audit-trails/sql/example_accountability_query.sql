WITH system_record(system_id, required_records, available_records, documentation, provenance, reviewability, contestability, remediation, governance, stakes) AS (
  VALUES ('benefits_eligibility_model', 12, 9, 0.72, 0.68, 0.64, 0.58, 0.52, 0.66, 0.90)
)
SELECT
  system_id,
  CAST(available_records AS REAL) / required_records AS audit_completeness_score,
  (documentation + provenance + reviewability + contestability + remediation + governance) / 6.0 AS accountability_capacity_score,
  stakes * (1.0 - (CAST(available_records AS REAL) / required_records)) AS reconstruction_risk_score
FROM system_record;
