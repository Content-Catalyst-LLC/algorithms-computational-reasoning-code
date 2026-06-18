.headers on
.mode column
SELECT case_name, problem_form,
ROUND(100.0*(0.10*input_definition_clarity+0.12*complexity_evidence+0.10*structure_exploitation+0.10*exact_method_feasibility+0.10*approximation_readiness+0.10*heuristic_validation+0.12*benchmark_evidence+0.08*timeout_handling+0.10*governance_readiness+0.08*communication_clarity),2) AS tractability_quality
FROM tractability_cases ORDER BY tractability_quality DESC;
