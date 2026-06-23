-- Core computational knowledge transfer threads.
SELECT theme_id, transfer_score, interpretive_status
FROM transfer_map
WHERE interpretive_status = 'core_computational_knowledge_transfer_thread'
ORDER BY transfer_score DESC;

-- Themes with high error-control relevance.
SELECT theme_id, error_control, transfer_score
FROM transfer_map
WHERE error_control >= 0.90
ORDER BY error_control DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
