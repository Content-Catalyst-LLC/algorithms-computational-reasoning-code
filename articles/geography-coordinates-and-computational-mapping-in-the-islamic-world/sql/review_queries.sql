-- Core computational mapping threads.
SELECT theme_id, mapping_score, interpretive_status
FROM computational_mapping_map
WHERE interpretive_status = 'core_computational_mapping_thread'
ORDER BY mapping_score DESC;

-- Themes with high coordinate structure.
SELECT theme_id, coordinate_structure, mapping_score
FROM computational_mapping_map
WHERE coordinate_structure >= 0.90
ORDER BY coordinate_structure DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
