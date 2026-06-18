.headers on
.mode column
SELECT case_name, ROUND(100.0*(0.12*decomposition_clarity+0.10*base_case_clarity+0.10*subproblem_validity+0.12*progress_toward_termination+0.12*combination_correctness+0.10*recurrence_awareness+0.10*edge_case_coverage+0.08*boundary_handling+0.08*traceability+0.08*governance_readiness),2) AS divide_conquer_quality
FROM divide_conquer_cases ORDER BY divide_conquer_quality DESC;

SELECT partition_id, source_size, subproblem_size, combine_rule, boundary_check
FROM partition_records
ORDER BY source_size DESC, partition_id ASC;
