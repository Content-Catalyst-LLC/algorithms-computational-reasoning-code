.headers on
.mode column
SELECT case_name, ROUND(100.0*(0.12*search_space_clarity+0.12*candidate_generation_completeness+0.10*constraint_quality+0.10*pruning_soundness+0.10*bound_validity+0.10*objective_clarity+0.10*edge_case_coverage+0.08*traceability+0.10*complexity_awareness+0.08*governance_readiness),2) AS search_strategy_quality
FROM search_strategy_cases ORDER BY search_strategy_quality DESC;

SELECT candidate_id, search_family, depth, feasible, objective_value, pruned, prune_reason
FROM candidate_records
ORDER BY depth ASC, candidate_id ASC;
