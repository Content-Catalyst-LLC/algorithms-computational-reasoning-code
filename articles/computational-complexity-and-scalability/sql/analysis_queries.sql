.headers on
.mode column
SELECT case_name, ROUND(100.0*(0.12*input_definition_clarity+0.12*time_complexity_clarity+0.10*space_complexity_clarity+0.12*benchmark_evidence+0.10*bottleneck_identification+0.10*threshold_reporting+0.08*degradation_planning+0.08*monitoring_readiness+0.10*governance_readiness+0.08*equity_under_scale_review),2) AS scalability_quality
FROM scalability_cases ORDER BY scalability_quality DESC;
