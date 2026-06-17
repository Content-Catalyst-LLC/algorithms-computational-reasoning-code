.headers on
.mode column

SELECT 'ALGORITHM SCENARIOS' AS section;
SELECT scenario,
       ROUND((representation_quality + indexing_strength + decomposition_strength + correctness_evidence + interpretability + robustness + governance_readiness + data_quality + objective_alignment + memory_efficiency + monitoring_strength - brute_force_pressure) / 10.0 * 100.0, 2) AS rough_reasoning_score
FROM algorithm_scenarios
ORDER BY rough_reasoning_score DESC;

SELECT 'GOVERNANCE NOTES' AS section;
SELECT note_key, note_text
FROM algorithm_governance_notes
ORDER BY note_key;
