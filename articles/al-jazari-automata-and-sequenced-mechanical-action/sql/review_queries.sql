-- Core sequenced mechanical action threads.
SELECT theme_id, sequenced_action_score, interpretive_status
FROM sequenced_action_map
WHERE interpretive_status = 'core_sequenced_mechanical_action_thread'
ORDER BY sequenced_action_score DESC;

-- High repeatability themes.
SELECT theme_id, repeatability, sequenced_action_score
FROM sequenced_action_map
WHERE repeatability >= 0.90
ORDER BY repeatability DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
