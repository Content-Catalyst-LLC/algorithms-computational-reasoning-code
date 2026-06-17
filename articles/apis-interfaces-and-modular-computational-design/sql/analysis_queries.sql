.headers on
.mode column
SELECT case_name, ROUND(100.0*(0.12*contract_clarity+0.12*schema_validation+0.10*error_behavior+0.10*versioning_strategy+0.10*documentation_quality+0.10*testability+0.10*coupling_control+0.08*observability+0.10*security_boundaries+0.08*governance_readiness),2) AS interface_quality
FROM api_interface_cases ORDER BY interface_quality DESC;
