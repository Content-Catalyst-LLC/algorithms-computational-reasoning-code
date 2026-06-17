.headers on
.mode column
SELECT case_name, ROUND(100.0*(0.12*state_visibility+0.12*mutation_control+0.10*aliasing_risk_control+0.10*side_effect_boundaries+0.10*lifecycle_clarity+0.10*concurrency_safety+0.10*reproducibility_support+0.10*auditability+0.08*rollback_support+0.08*governance_readiness),2) AS state_quality
FROM state_mutation_cases ORDER BY state_quality DESC;
