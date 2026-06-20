.headers on
.mode column

SELECT case_name,
ROUND(100.0 * (0.11*objective_clarity + 0.11*constraint_documentation + 0.10*feasible_set_clarity + 0.09*data_quality + 0.09*uncertainty_handling + 0.08*sensitivity_review + 0.10*tradeoff_transparency + 0.09*fairness_review + 0.08*robustness_review + 0.07*traceability + 0.06*governance_review + 0.02*communication_clarity),2) AS optimization_score
FROM optimization_cases
ORDER BY optimization_score DESC;

SELECT case_name,
ROUND((c1*x1 + c2*x2 + c3*x3),4) AS linear_objective,
ROUND(limit_value - observed_value,4) AS constraint_margin,
ROUND(base_objective + penalty_weight * penalty,4) AS penalty_objective,
ROUND((0.35*(1-cost_score)) + (0.40*quality_score) + (0.25*(1-risk_score)),4) AS normalized_tradeoff_score
FROM optimization_metrics
ORDER BY linear_objective DESC;
