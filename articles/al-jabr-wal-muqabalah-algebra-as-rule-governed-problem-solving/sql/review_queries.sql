-- Core rule-governed algebra threads.
SELECT theme_id, procedure_score, interpretive_status
FROM rule_governed_algebra_map
WHERE interpretive_status = 'core_rule_governed_algebra_thread'
ORDER BY procedure_score DESC;

-- Themes with high transformation importance.
SELECT theme_id, transformation, procedure_score
FROM rule_governed_algebra_map
WHERE transformation >= 0.90
ORDER BY transformation DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
