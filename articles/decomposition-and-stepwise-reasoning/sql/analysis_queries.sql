.headers on
.mode column

SELECT 'DECOMPOSITION CASE SCORES' AS section;

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * subproblem_clarity +
    0.10 * boundary_definition +
    0.10 * input_output_clarity +
    0.10 * sequencing_quality +
    0.10 * dependency_visibility +
    0.12 * testability +
    0.10 * traceability +
    0.10 * recomposition_quality +
    0.08 * governance_readiness +
    0.08 * risk_awareness
  ), 2) AS decomposition_score
FROM decomposition_cases
ORDER BY decomposition_score DESC;

SELECT 'GOVERNANCE NOTES' AS section;
SELECT note_key, note_text
FROM decomposition_governance_notes
ORDER BY note_key;
