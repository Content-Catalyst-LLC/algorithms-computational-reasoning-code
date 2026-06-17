.headers on
.mode column

SELECT 'REASONING PROFILE SCORES' AS section;

SELECT
  name,
  ROUND(100.0 * (
    0.28 * step_clarity +
    0.24 * decomposition +
    0.24 * control_flow +
    0.24 * testability
  ), 2) AS algorithmic_score,
  ROUND(100.0 * (
    0.11 * step_clarity +
    0.10 * decomposition +
    0.09 * control_flow +
    0.10 * testability +
    0.13 * representation_quality +
    0.12 * data_context +
    0.11 * complexity_awareness +
    0.12 * interpretability +
    0.12 * governance_readiness +
    0.10 * stakeholder_awareness
  ), 2) AS computational_score
FROM reasoning_profiles
ORDER BY computational_score DESC;

SELECT 'GOVERNANCE NOTES' AS section;
SELECT note_key, note_text
FROM reasoning_governance_notes
ORDER BY note_key;
