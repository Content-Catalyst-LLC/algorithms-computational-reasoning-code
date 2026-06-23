-- Core astronomical prediction threads.
SELECT theme_id, prediction_score, interpretive_status
FROM astronomical_prediction_map
WHERE interpretive_status = 'core_astronomical_prediction_thread'
ORDER BY prediction_score DESC;

-- Themes with high correction awareness.
SELECT theme_id, correction_awareness, prediction_score
FROM astronomical_prediction_map
WHERE correction_awareness >= 0.90
ORDER BY correction_awareness DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
