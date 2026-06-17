.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * operation_fit +
    0.12 * order_semantics +
    0.10 * invariant_clarity +
    0.10 * complexity_awareness +
    0.08 * memory_behavior +
    0.08 * overflow_handling +
    0.10 * interpretability +
    0.10 * traversal_support +
    0.10 * representation_risk_documentation +
    0.10 * governance_readiness
  ), 2) AS sequence_structure_quality
FROM sequence_structure_cases
ORDER BY sequence_structure_quality DESC;
