.headers on
.mode column

SELECT 'BOUNDARY STATE CASE SCORES' AS section;

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * input_clarity +
    0.12 * output_clarity +
    0.12 * state_definition +
    0.10 * transition_clarity +
    0.12 * stopping_condition_clarity +
    0.10 * validation_quality +
    0.08 * edge_case_handling +
    0.08 * failure_reporting +
    0.08 * interpretability +
    0.08 * governance_readiness
  ), 2) AS boundary_score
FROM boundary_state_cases
ORDER BY boundary_score DESC;

SELECT 'GOVERNANCE NOTES' AS section;
SELECT note_key, note_text
FROM boundary_governance_notes
ORDER BY note_key;
