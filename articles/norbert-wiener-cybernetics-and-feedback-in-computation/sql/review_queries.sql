-- Core Wiener cybernetic-feedback threads.
SELECT theme_id, cybernetic_score, interpretive_status
FROM wiener_cybernetic_feedback_map
WHERE interpretive_status = 'core_wiener_cybernetic_feedback_thread'
ORDER BY cybernetic_score DESC;

-- High-risk amplification and governance themes.
SELECT theme_id, amplification_risk, governance_caution, cybernetic_score
FROM wiener_cybernetic_feedback_map
WHERE amplification_risk >= 0.90 AND governance_caution >= 0.90
ORDER BY cybernetic_score DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
