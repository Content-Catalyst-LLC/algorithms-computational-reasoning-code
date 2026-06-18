.headers on
.mode column

-- Validation pass rates
SELECT check_id, dimension, ROUND(1.0 * passed / total, 4) AS pass_rate, threshold,
       CASE WHEN 1.0 * passed / total >= threshold THEN 'pass' ELSE 'review' END AS status
FROM pipeline_quality_checks
ORDER BY status, dimension;

-- Governance-gated tasks
SELECT task_id, task_name, task_type, expected_output
FROM pipeline_tasks
WHERE governance_gate = 1
ORDER BY task_id;

-- Pipeline run risk review
SELECT run_id, run_label, validation_pass_rate, freshness_score, lineage_coverage, monitoring_status,
       ROUND(100.0 * (0.35*validation_pass_rate + 0.25*freshness_score + 0.25*lineage_coverage + CASE WHEN monitoring_status = 'healthy' THEN 0.15 ELSE 0.05 END), 2) AS run_quality_score
FROM pipeline_runs
ORDER BY run_quality_score DESC;
