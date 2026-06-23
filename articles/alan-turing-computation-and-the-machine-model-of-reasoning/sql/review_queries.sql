-- Core Turing machine reasoning threads.
SELECT theme_id, reasoning_score, interpretive_status
FROM turing_machine_reasoning_map
WHERE interpretive_status = 'core_turing_machine_reasoning_thread'
ORDER BY reasoning_score DESC;

-- Themes where limit awareness and governance caution are both high.
SELECT theme_id, limit_awareness, governance_caution, reasoning_score
FROM turing_machine_reasoning_map
WHERE limit_awareness >= 0.90 AND governance_caution >= 0.90
ORDER BY reasoning_score DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
