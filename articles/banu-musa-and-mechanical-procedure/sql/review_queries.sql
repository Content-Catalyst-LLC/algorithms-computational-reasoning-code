-- Core mechanical procedure threads.
SELECT theme_id, mechanical_score, interpretive_status
FROM mechanical_procedure_map
WHERE interpretive_status = 'core_mechanical_procedure_thread'
ORDER BY mechanical_score DESC;

-- Themes with high conditional control.
SELECT theme_id, conditional_control, mechanical_score
FROM mechanical_procedure_map
WHERE conditional_control >= 0.90
ORDER BY conditional_control DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
