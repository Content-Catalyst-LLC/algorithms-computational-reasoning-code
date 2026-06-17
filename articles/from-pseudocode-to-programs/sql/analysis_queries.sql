.headers on
.mode column

SELECT 'PSEUDOCODE TRANSLATION CASE SCORES' AS section;

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * intent_clarity +
    0.10 * input_specification +
    0.10 * output_specification +
    0.10 * state_handling +
    0.12 * control_flow_fidelity +
    0.10 * edge_case_coverage +
    0.10 * error_handling +
    0.10 * test_coverage +
    0.08 * readability +
    0.08 * maintainability
  ), 2) AS translation_quality
FROM pseudocode_translation_cases
ORDER BY translation_quality DESC;

SELECT 'GOVERNANCE NOTES' AS section;
SELECT note_key, note_text
FROM translation_governance_notes
ORDER BY note_key;
