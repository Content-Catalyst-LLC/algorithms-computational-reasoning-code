.headers on
.mode column

SELECT 'ALGORITHMIC LITERACY CASE SCORES' AS section;

SELECT
  case_name,
  ROUND(100.0 * (
    0.14 * procedural_transparency +
    0.12 * data_visibility +
    0.14 * output_interpretability +
    0.12 * uncertainty_communication +
    0.12 * contestability +
    0.12 * governance_readiness +
    0.12 * impact_awareness +
    0.12 * human_judgment_support
  ), 2) AS literacy_support_score
FROM algorithmic_literacy_cases
ORDER BY literacy_support_score DESC;

SELECT 'GOVERNANCE NOTES' AS section;
SELECT note_key, note_text
FROM algorithmic_literacy_governance_notes
ORDER BY note_key;
