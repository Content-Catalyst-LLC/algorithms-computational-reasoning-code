.headers on
.mode column

SELECT 'ABSTRACTION CASE SCORES' AS section;

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * representation_clarity +
    0.10 * scope_definition +
    0.12 * detail_preservation +
    0.12 * assumption_documentation +
    0.10 * testability +
    0.12 * interpretability +
    0.08 * reuse_safety +
    0.08 * uncertainty_visibility +
    0.08 * governance_readiness +
    0.08 * risk_awareness
  ), 2) AS abstraction_score
FROM abstraction_cases
ORDER BY abstraction_score DESC;

SELECT 'GOVERNANCE NOTES' AS section;
SELECT note_key, note_text
FROM abstraction_governance_notes
ORDER BY note_key;
