-- Core Hopper compiler-humanization threads.
SELECT theme_id, humanization_score, interpretive_status
FROM hopper_compiler_humanization_map
WHERE interpretive_status = 'core_hopper_compiler_humanization_thread'
ORDER BY humanization_score DESC;

-- High-governance caution themes.
SELECT theme_id, standards, debugging, governance_caution, humanization_score
FROM hopper_compiler_humanization_map
WHERE governance_caution >= 0.90
ORDER BY humanization_score DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
