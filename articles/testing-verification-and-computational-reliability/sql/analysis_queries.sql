.headers on
.mode column
SELECT case_name, ROUND(100.0*(0.12*specification_clarity+0.10*test_coverage_rationale+0.12*oracle_quality+0.10*edge_case_testing+0.10*regression_discipline+0.10*property_checks+0.10*reproducibility_evidence+0.10*observability+0.08*security_testing+0.08*governance_readiness),2) AS reliability_quality
FROM reliability_cases ORDER BY reliability_quality DESC;

SELECT status, COUNT(*) AS test_count FROM test_results GROUP BY status;
