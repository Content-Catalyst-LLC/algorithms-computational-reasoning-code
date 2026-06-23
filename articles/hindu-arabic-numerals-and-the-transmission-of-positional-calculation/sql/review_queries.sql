-- Core positional calculation threads.
SELECT theme_id, positional_score, interpretive_status
FROM positional_calculation_transmission_map
WHERE interpretive_status = 'core_positional_calculation_thread'
ORDER BY positional_score DESC;

-- Themes with high representational importance.
SELECT theme_id, representation, positional_score
FROM positional_calculation_transmission_map
WHERE representation >= 0.90
ORDER BY representation DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
