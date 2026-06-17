.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * operation_fit +
    0.12 * structural_fidelity +
    0.10 * invariant_clarity +
    0.10 * complexity_awareness +
    0.08 * memory_awareness +
    0.10 * interpretability +
    0.10 * retrieval_support +
    0.08 * transformation_support +
    0.10 * representation_risk_documentation +
    0.10 * governance_readiness
  ), 2) AS structure_reasoning_quality
FROM data_structure_cases
ORDER BY structure_reasoning_quality DESC;
