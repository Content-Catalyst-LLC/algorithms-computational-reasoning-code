.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * specification_clarity +
    0.10 * assumption_documentation +
    0.10 * invariant_strength +
    0.12 * proof_obligation_traceability +
    0.12 * machine_check_status +
    0.10 * counterexample_handling +
    0.10 * model_scope_clarity +
    0.08 * refinement_evidence +
    0.08 * unknown_status_handling +
    0.08 * governance_readiness
  ), 2) AS formal_methods_quality
FROM formal_methods_cases
ORDER BY formal_methods_quality DESC;
