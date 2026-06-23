-- Core al-Khwārizmī algorithmic-method threads.
SELECT theme_id, method_score, interpretive_status
FROM khwarizmi_algorithmic_method_map
WHERE interpretive_status = 'core_khwarizmi_algorithmic_method_thread'
ORDER BY method_score DESC;

-- Themes where etymology and transmission are both high.
SELECT theme_id, etymology, transmission, method_score
FROM khwarizmi_algorithmic_method_map
WHERE etymology >= 0.90 AND transmission >= 0.90
ORDER BY method_score DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
