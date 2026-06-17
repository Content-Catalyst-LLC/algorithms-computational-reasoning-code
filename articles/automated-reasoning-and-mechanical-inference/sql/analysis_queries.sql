.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * formalization_clarity +
    0.10 * premise_quality +
    0.12 * rule_soundness +
    0.12 * inference_traceability +
    0.10 * proof_or_model_evidence +
    0.08 * satisfiability_handling +
    0.10 * counterexample_handling +
    0.08 * unknown_status_handling +
    0.08 * human_review_pathway +
    0.10 * governance_readiness
  ), 2) AS automated_reasoning_quality
FROM automated_reasoning_cases
ORDER BY automated_reasoning_quality DESC;
