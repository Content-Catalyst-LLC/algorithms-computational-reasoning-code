.headers on
.mode column

SELECT case_name,
ROUND(100.0 * (0.16*(1-storage_governance) + 0.16*(1-deployment_reproducibility) + 0.17*(1-observability) + 0.17*(1-identity_access_control) + 0.11*(1-cost_visibility) + 0.11*(1-resilience_design) + 0.07*(1-data_governance) + 0.05*(1-dependency_mapping)),2) AS cloud_risk_score
FROM cloud_cases
ORDER BY cloud_risk_score DESC;

SELECT service_layer, ROUND(SUM(monthly_cost),2) AS monthly_cost
FROM cloud_resources
GROUP BY service_layer
ORDER BY monthly_cost DESC;

SELECT resource_id, resource_type, owner, access_risk, observability_level
FROM cloud_resources
WHERE criticality='high' OR access_risk='high'
ORDER BY access_risk DESC, resource_type;
