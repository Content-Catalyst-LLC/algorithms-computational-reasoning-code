.headers on
.mode column

SELECT 'LOGIC COMPUTATION CASE SCORES' AS section;

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * rule_clarity +
    0.12 * predicate_definition +
    0.10 * input_validity +
    0.10 * contradiction_control +
    0.12 * inference_traceability +
    0.10 * constraint_coverage +
    0.10 * testability +
    0.08 * verification_readiness +
    0.08 * explainability +
    0.08 * governance_readiness
  ), 2) AS logic_quality
FROM logic_computation_cases
ORDER BY logic_quality DESC;

SELECT 'GOVERNANCE NOTES' AS section;
SELECT note_key, note_text
FROM logic_governance_notes
ORDER BY note_key;
