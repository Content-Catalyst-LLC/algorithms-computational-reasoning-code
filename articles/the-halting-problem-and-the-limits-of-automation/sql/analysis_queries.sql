.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.10 * program_scope_clarity +
    0.12 * termination_claim_clarity +
    0.12 * undecidability_awareness +
    0.10 * bounded_analysis_honesty +
    0.10 * unknown_status_handling +
    0.08 * timeout_policy +
    0.12 * false_certainty_risk_control +
    0.10 * human_review_pathway +
    0.08 * traceability +
    0.08 * governance_readiness
  ), 2) AS halting_boundary_quality
FROM halting_boundary_cases
ORDER BY halting_boundary_quality DESC;
