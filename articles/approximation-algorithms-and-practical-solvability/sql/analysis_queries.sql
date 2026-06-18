.headers on
.mode column
SELECT case_name, ROUND(100.0*(0.12*objective_clarity+0.12*feasibility_preservation+0.12*guarantee_clarity+0.10*assumption_validity+0.10*bound_evidence+0.10*runtime_practicality+0.08*gap_reporting+0.08*edge_case_coverage+0.08*traceability+0.10*governance_readiness),2) AS approximation_quality
FROM approximation_cases ORDER BY approximation_quality DESC;

SELECT record_id, case_name, algorithm_value, bound_value, problem_type, reported_gap, acceptable_gap, decision
FROM gap_records
ORDER BY record_id ASC;
