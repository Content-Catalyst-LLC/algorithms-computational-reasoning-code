-- Core programming-language history threads.
SELECT tradition_id, history_score, interpretive_status
FROM programming_language_history_map
WHERE interpretive_status = 'core_programming_language_history_thread'
ORDER BY history_score DESC;

-- High ecosystem / high governance traditions.
SELECT tradition_id, ecosystem_depth, institutional_adoption, governance_caution, history_score
FROM programming_language_history_map
WHERE ecosystem_depth >= 0.90 AND governance_caution >= 0.90
ORDER BY history_score DESC;

-- Language lineage edges.
SELECT source, target, relation
FROM language_family_edges
ORDER BY source, target;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
