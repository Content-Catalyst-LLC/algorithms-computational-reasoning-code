.headers on
.mode column
SELECT case_name, ROUND(100.0*(0.12*randomness_clarity+0.12*distribution_validity+0.10*seed_control+0.10*error_bound_clarity+0.10*sample_adequacy+0.10*repeatability+0.10*edge_case_coverage+0.10*variance_analysis+0.08*traceability+0.08*governance_readiness),2) AS randomized_algorithm_quality
FROM randomized_algorithm_cases ORDER BY randomized_algorithm_quality DESC;

SELECT trial_id, procedure, seed, sample_size, estimate, error_bound
FROM random_trials
ORDER BY procedure ASC, trial_id ASC;
