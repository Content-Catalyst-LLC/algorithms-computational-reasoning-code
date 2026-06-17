.headers on
.mode column
SELECT case_name, ROUND(100.0*(0.10*runtime_documentation+0.12*dependency_control+0.10*configuration_validation+0.10*resource_visibility+0.08*portability_support+0.12*reproducibility_support+0.12*security_boundaries+0.10*observability+0.08*external_service_discipline+0.08*governance_readiness),2) AS runtime_quality
FROM runtime_context_cases ORDER BY runtime_quality DESC;
