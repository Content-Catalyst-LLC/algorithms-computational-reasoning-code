-- Core unknown-variable philosophy threads.
SELECT theme_id, unknown_variable_score, interpretive_status
FROM unknown_variable_map
WHERE interpretive_status = 'core_unknown_variable_philosophy_thread'
ORDER BY unknown_variable_score DESC;

-- Themes with high proof relation.
SELECT theme_id, proof_relation, unknown_variable_score
FROM unknown_variable_map
WHERE proof_relation >= 0.90
ORDER BY proof_relation DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
