.headers on
.mode column

SELECT 'DEBUGGING REASONING CASE SCORES' AS section;

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * reproducibility +
    0.10 * expected_behavior_clarity +
    0.10 * trace_quality +
    0.10 * hypothesis_strength +
    0.10 * isolation_quality +
    0.10 * edge_case_awareness +
    0.12 * fix_verification +
    0.10 * regression_testing +
    0.08 * documentation_quality +
    0.08 * governance_readiness
  ), 2) AS debugging_quality
FROM debugging_reasoning_cases
ORDER BY debugging_quality DESC;

SELECT 'GOVERNANCE NOTES' AS section;
SELECT note_key, note_text
FROM debugging_governance_notes
ORDER BY note_key;
