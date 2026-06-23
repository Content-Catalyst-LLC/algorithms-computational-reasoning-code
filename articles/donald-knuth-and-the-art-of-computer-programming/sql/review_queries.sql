-- Core Knuth algorithmic-art threads.
SELECT theme_id, art_score, interpretive_status
FROM knuth_algorithmic_art_map
WHERE interpretive_status = 'core_knuth_algorithmic_art_thread'
ORDER BY art_score DESC;

-- High-exposition and high-governance themes.
SELECT theme_id, exposition, maintainability, governance_caution, art_score
FROM knuth_algorithmic_art_map
WHERE exposition >= 0.94 AND governance_caution >= 0.90
ORDER BY art_score DESC;

-- Comparison-sorting lower-bound examples.
SELECT n, comparison_sort_lower_bound_log2_factorial
FROM comparison_sort_lower_bounds
ORDER BY n;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
