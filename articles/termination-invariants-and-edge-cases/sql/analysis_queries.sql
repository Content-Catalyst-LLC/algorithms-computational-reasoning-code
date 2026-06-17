.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * stopping_condition_clarity +
    0.12 * progress_measure_definition +
    0.12 * invariant_coverage +
    0.10 * boundary_case_coverage +
    0.10 * invalid_input_handling +
    0.08 * recursion_safety +
    0.08 * numerical_edge_handling +
    0.08 * concurrency_edge_awareness +
    0.10 * counterexample_traceability +
    0.10 * governance_readiness
  ), 2) AS reliability_quality
FROM boundary_reliability_cases
ORDER BY reliability_quality DESC;
