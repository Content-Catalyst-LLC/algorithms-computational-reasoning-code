.headers on
.mode column

-- Missingness profile
SELECT field,
       ROUND(1.0 * missing_count / total_count, 4) AS missingness_rate,
       ROUND(1.0 - 1.0 * missing_count / total_count, 4) AS completeness_score,
       missingness_reason,
       handling_policy
FROM missingness_profiles
ORDER BY missingness_rate DESC;

-- Quality gate status
SELECT check_id, dimension,
       ROUND(1.0 * passed / total, 4) AS pass_rate,
       threshold,
       CASE WHEN 1.0 * passed / total >= threshold THEN 'pass' ELSE gate_action END AS status
FROM quality_checks
ORDER BY status, dimension;

-- Quality score for cases
SELECT case_name, computational_use,
       ROUND(100.0 * (0.22*completeness + 0.18*validity + 0.14*freshness + 0.22*provenance + 0.14*representativeness + 0.10*uncertainty_communication), 2) AS quality_score
FROM data_quality_cases
ORDER BY quality_score DESC;
