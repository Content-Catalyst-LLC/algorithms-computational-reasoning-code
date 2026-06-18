.headers on
.mode column
SELECT case_name, ROUND(100.0*(0.12*purpose_clarity+0.12*rule_transparency+0.12*benchmark_evidence+0.10*parameter_documentation+0.10*robustness_testing+0.10*edge_case_coverage+0.08*fairness_review+0.08*traceability+0.08*monitoring_readiness+0.10*governance_readiness),2) AS heuristic_quality
FROM heuristic_cases ORDER BY heuristic_quality DESC;

SELECT record_id, case_name, baseline_score, heuristic_score, score_direction, seed, notes
FROM benchmark_records
ORDER BY record_id ASC;
