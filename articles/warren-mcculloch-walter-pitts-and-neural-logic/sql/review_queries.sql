-- Core McCulloch-Pitts neural logic threads.
SELECT concept_id, neural_logic_score, interpretive_status
FROM mcculloch_pitts_neural_logic_map
WHERE interpretive_status = 'core_neural_logic_thread'
ORDER BY neural_logic_score DESC;

-- Concepts with high AI lineage and high biological caution.
SELECT concept_id, ai_lineage, biological_caution, responsible_use_relevance
FROM mcculloch_pitts_neural_logic_map
WHERE ai_lineage >= 0.90 AND biological_caution >= 0.90
ORDER BY responsible_use_relevance DESC;

-- Threshold logic examples.
SELECT gate, x1, x2, threshold, output
FROM threshold_logic_examples
ORDER BY gate, x1, x2;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
