-- Core practical calculation threads.
SELECT theme_id, practical_score, interpretive_status
FROM practical_calculation_procedure_map
WHERE interpretive_status = 'core_practical_calculation_thread'
ORDER BY practical_score DESC;

-- Themes with high verification importance.
SELECT theme_id, verification, practical_score
FROM practical_calculation_procedure_map
WHERE verification >= 0.90
ORDER BY verification DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
