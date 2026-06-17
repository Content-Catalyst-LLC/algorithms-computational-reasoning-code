.headers on
.mode column

SELECT 'FORMALIZATION CASE SCORES' AS section;

SELECT
  case_name,
  ROUND(100.0 * (
    0.10 * input_clarity +
    0.10 * output_clarity +
    0.10 * constraint_clarity +
    0.08 * state_definition +
    0.14 * objective_alignment +
    0.12 * assumption_documentation +
    0.10 * edge_case_handling +
    0.08 * stopping_condition_clarity +
    0.10 * evaluation_quality +
    0.08 * governance_readiness
  ), 2) AS formalization_score
FROM formalization_cases
ORDER BY formalization_score DESC;

SELECT 'GOVERNANCE NOTES' AS section;
SELECT note_key, note_text
FROM formalization_governance_notes
ORDER BY note_key;
