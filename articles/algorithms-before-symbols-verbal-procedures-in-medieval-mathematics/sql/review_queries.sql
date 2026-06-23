-- Core verbal procedure threads.
SELECT theme_id, verbal_procedure_score, interpretive_status
FROM verbal_procedure_map
WHERE interpretive_status = 'core_verbal_procedure_thread'
ORDER BY verbal_procedure_score DESC;

-- Themes with high pedagogical value.
SELECT theme_id, pedagogical_value, verbal_procedure_score
FROM verbal_procedure_map
WHERE pedagogical_value >= 0.90
ORDER BY pedagogical_value DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
