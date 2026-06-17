.headers on
.mode column
SELECT case_name, ROUND(100.0*(0.12*boundary_clarity+0.12*modular_cohesion+0.12*dependency_control+0.10*interface_discipline+0.10*state_ownership+0.10*failure_containment+0.08*scalability_readiness+0.10*security_boundaries+0.08*observability+0.08*governance_readiness),2) AS architecture_quality
FROM software_architecture_cases ORDER BY architecture_quality DESC;

SELECT source, target, relationship_type
FROM architecture_dependency_edges
ORDER BY source, target;
