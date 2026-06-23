-- Core historical algorithmic-reasoning threads.
SELECT theme_id, significance_score, interpretive_status
FROM historical_algorithmic_reasoning_map
WHERE interpretive_status = 'core_algorithmic_reasoning_thread'
ORDER BY significance_score DESC;

-- Themes with high practical application.
SELECT theme_id, practical_application, significance_score
FROM historical_algorithmic_reasoning_map
WHERE practical_application >= 0.85
ORDER BY practical_application DESC;

-- Historical cautions.
SELECT caution, meaning
FROM historical_cautions
ORDER BY caution;
