.headers on
.mode column
SELECT case_name, ROUND(100.0*(0.12*problem_formulation+0.10*input_output_clarity+0.12*correctness_rationale+0.10*termination_argument+0.10*complexity_analysis+0.10*data_structure_fit+0.10*edge_case_coverage+0.10*robustness+0.08*interpretability+0.08*governance_readiness),2) AS design_quality
FROM algorithm_design_cases ORDER BY design_quality DESC;
