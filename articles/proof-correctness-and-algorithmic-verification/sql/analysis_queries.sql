.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * specification_clarity +
    0.10 * precondition_definition +
    0.10 * postcondition_definition +
    0.12 * invariant_coverage +
    0.10 * termination_evidence +
    0.10 * test_coverage +
    0.10 * counterexample_handling +
    0.08 * static_check_support +
    0.10 * traceability +
    0.08 * governance_readiness
  ), 2) AS verification_quality
FROM verification_cases
ORDER BY verification_quality DESC;
