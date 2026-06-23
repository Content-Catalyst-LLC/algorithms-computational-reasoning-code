-- Core von Neumann architecture threads.
SELECT theme_id, architecture_score, interpretive_status
FROM von_neumann_architecture_map
WHERE interpretive_status = 'core_von_neumann_architecture_thread'
ORDER BY architecture_score DESC;

-- Themes where bottleneck and AI infrastructure are both high.
SELECT theme_id, bottleneck_awareness, ai_infrastructure, architecture_score
FROM von_neumann_architecture_map
WHERE bottleneck_awareness >= 0.90 AND ai_infrastructure >= 0.90
ORDER BY architecture_score DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
