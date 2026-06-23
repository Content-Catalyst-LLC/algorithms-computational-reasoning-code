-- Core Lovelace computation-imagination threads.
SELECT theme_id, imagination_score, interpretive_status
FROM lovelace_computation_imagination_map
WHERE interpretive_status = 'core_lovelace_computation_thread'
ORDER BY imagination_score DESC;

-- Themes where AI caution and limit awareness are both high.
SELECT theme_id, limit_awareness, ai_caution, imagination_score
FROM lovelace_computation_imagination_map
WHERE limit_awareness >= 0.85 AND ai_caution >= 0.85
ORDER BY imagination_score DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
