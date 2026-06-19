.headers on
.mode column

SELECT case_name,
ROUND(100.0 * (
  0.11*access_dependence + 0.11*visibility_dependence + 0.10*api_dependence +
  0.10*data_dependence + 0.09*cost_dependence + 0.11*switching_difficulty +
  0.10*(1-interoperability) + 0.09*(1-transparency) + 0.08*(1-auditability) +
  0.06*(1-appeal_mechanism) + 0.04*(1-governance_review) + 0.01*(1-communication_clarity)
),2) AS platform_power_risk
FROM platform_cases
ORDER BY platform_power_risk DESC;

SELECT case_name,
ROUND(100.0 * (0.22*access_dependence + 0.22*visibility_dependence + 0.18*cost_dependence + 0.24*switching_difficulty + 0.14*evidence_dependence),2) AS dependency_score,
ROUND(migration + rebuild + training + downtime + lost_network,2) AS switching_cost,
ROUND(platform_requests / total_requests,4) AS api_dependency_ratio,
ROUND(actor_exposure / total_exposure,4) AS visibility_share
FROM platform_metrics
ORDER BY dependency_score DESC;
