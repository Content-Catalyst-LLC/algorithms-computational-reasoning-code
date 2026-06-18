.headers on
.mode column
SELECT case_name, ROUND(100.0*(0.12*state_clarity+0.12*recurrence_validity+0.10*base_case_clarity+0.10*overlapping_subproblem_evidence+0.10*optimal_substructure_evidence+0.10*transition_clarity+0.10*storage_strategy_quality+0.10*edge_case_coverage+0.08*traceability+0.08*governance_readiness),2) AS dynamic_programming_quality
FROM dynamic_programming_cases ORDER BY dynamic_programming_quality DESC;

SELECT state_id, state_family, dimension_count, storage_strategy, backpointer_required, staleness_risk
FROM state_tables
ORDER BY staleness_risk DESC, state_id ASC;
