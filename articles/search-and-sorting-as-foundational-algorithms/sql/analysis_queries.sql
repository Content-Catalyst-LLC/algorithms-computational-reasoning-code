.headers on
.mode column
SELECT case_name, ROUND(100.0*(0.12*search_space_clarity+0.12*predicate_or_key_clarity+0.10*ordering_rule_quality+0.10*data_structure_fit+0.10*complexity_awareness+0.10*edge_case_coverage+0.10*stability_or_tie_breaking+0.08*traceability+0.10*robustness+0.08*governance_readiness),2) AS search_sorting_quality
FROM search_sorting_cases ORDER BY search_sorting_quality DESC;

SELECT record_id, category, primary_score, secondary_priority
FROM ranked_records
ORDER BY primary_score DESC, secondary_priority ASC, created_at ASC;
