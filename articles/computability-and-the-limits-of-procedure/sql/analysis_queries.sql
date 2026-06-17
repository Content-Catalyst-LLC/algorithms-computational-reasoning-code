.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.10 * procedure_definition +
    0.10 * input_domain_clarity +
    0.12 * decision_status_clarity +
    0.12 * termination_guarantee +
    0.10 * recognizability_status +
    0.10 * reduction_awareness +
    0.10 * approximation_honesty +
    0.10 * automation_scope_clarity +
    0.08 * traceability +
    0.08 * governance_readiness
  ), 2) AS computability_boundary_quality
FROM computability_boundary_cases
ORDER BY computability_boundary_quality DESC;
