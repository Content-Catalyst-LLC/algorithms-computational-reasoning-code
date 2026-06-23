-- Core Shannon information threads.
SELECT theme_id, information_score, interpretive_status
FROM shannon_information_map
WHERE interpretive_status = 'core_shannon_information_thread'
ORDER BY information_score DESC;

-- Themes where semantic boundary and governance caution are both high.
SELECT theme_id, semantic_boundary, governance_caution, information_score
FROM shannon_information_map
WHERE semantic_boundary >= 0.90 AND governance_caution >= 0.90
ORDER BY information_score DESC;

-- Entropy examples.
SELECT source, probabilities, entropy_bits
FROM entropy_examples
ORDER BY entropy_bits DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
