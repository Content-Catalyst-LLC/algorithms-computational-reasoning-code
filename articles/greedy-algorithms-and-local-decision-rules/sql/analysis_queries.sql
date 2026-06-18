.headers on
.mode column
SELECT case_name, ROUND(100.0*(0.12*local_rule_clarity+0.12*global_objective_clarity+0.12*greedy_choice_evidence+0.10*optimal_substructure_evidence+0.10*feasibility_check_quality+0.10*edge_case_coverage+0.10*counterexample_testing+0.08*traceability+0.08*robustness+0.08*governance_readiness),2) AS greedy_quality
FROM greedy_cases ORDER BY greedy_quality DESC;

SELECT case_id, risk_score, urgency_score, eligibility, local_priority
FROM priority_queue_cases
WHERE eligibility='true'
ORDER BY local_priority DESC, case_id ASC;
