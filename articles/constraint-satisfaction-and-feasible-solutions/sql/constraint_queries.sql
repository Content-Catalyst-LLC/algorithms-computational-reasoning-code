.headers on
.mode column

SELECT case_name,
ROUND(100.0 * (0.10*variable_clarity + 0.10*domain_clarity + 0.12*constraint_documentation + 0.11*feasibility_logic + 0.09*inconsistency_handling + 0.08*pruning_transparency + 0.08*propagation_transparency + 0.09*traceability + 0.07*exception_handling + 0.06*governance_review + 0.07*fairness_review + 0.03*communication_clarity),2) AS constraint_system_score
FROM constraint_cases
ORDER BY constraint_system_score DESC;
