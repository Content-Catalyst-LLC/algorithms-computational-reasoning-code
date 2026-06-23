-- Core procedural legacy threads.
SELECT theme_id, legacy_score, interpretive_status
FROM al_khwarizmi_procedural_legacy_map
WHERE interpretive_status = 'core_procedural_legacy'
ORDER BY legacy_score DESC;

-- Themes with high representation importance.
SELECT theme_id, representation, legacy_score
FROM al_khwarizmi_procedural_legacy_map
WHERE representation >= 0.85
ORDER BY representation DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
