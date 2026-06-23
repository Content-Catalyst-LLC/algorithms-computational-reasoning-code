WITH future_domain(domain_id, risk_score, readiness_score) AS (
  VALUES
    ('ai_agents_and_tool_use', 0.922857, 0.686667),
    ('scientific_computing_and_simulation', 0.765714, 0.806667),
    ('public_policy_algorithmic_governance', 0.917143, 0.633333),
    ('platform_attention_systems', 0.914286, 0.666667)
)
SELECT
  domain_id,
  risk_score,
  readiness_score,
  CASE
    WHEN risk_score >= 0.82 AND readiness_score < 0.72 THEN 'high_risk_governance_gap'
    WHEN risk_score >= 0.82 THEN 'high_risk_requires_strong_governance'
    WHEN readiness_score >= 0.72 THEN 'cautious_deployment_possible'
    ELSE 'further_review_needed'
  END AS future_status
FROM future_domain
ORDER BY risk_score DESC;
