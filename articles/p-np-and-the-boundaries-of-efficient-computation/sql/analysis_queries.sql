.headers on
.mode column
SELECT case_name, claimed_class,
ROUND(100.0*(0.09*problem_form_clarity+0.09*input_definition_clarity+0.10*certificate_clarity+0.10*verifier_clarity+0.10*reduction_evidence+0.12*class_claim_evidence+0.10*exact_method_feasibility+0.08*approximation_readiness+0.08*benchmark_support+0.07*governance_readiness+0.07*communication_clarity),2) AS claim_quality
FROM p_np_cases ORDER BY claim_quality DESC;
