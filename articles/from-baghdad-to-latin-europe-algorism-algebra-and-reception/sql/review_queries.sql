-- Core algorism, algebra, and reception threads.
SELECT theme_id, reception_score, interpretive_status
FROM reception_map
WHERE interpretive_status = 'core_algorism_algebra_reception_thread'
ORDER BY reception_score DESC;

-- Themes with high trust and verification relevance.
SELECT theme_id, trust_verification, reception_score
FROM reception_map
WHERE trust_verification >= 0.90
ORDER BY trust_verification DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
