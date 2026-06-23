-- Core algorithm history layers.
SELECT layer_id, history_score, interpretive_status
FROM algorithm_history_map
WHERE interpretive_status = 'core_algorithm_history_layer'
ORDER BY history_score DESC;

-- Layers where governance is especially important.
SELECT layer_id, governance_relevance, history_score
FROM algorithm_history_map
WHERE governance_relevance >= 0.80
ORDER BY governance_relevance DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
