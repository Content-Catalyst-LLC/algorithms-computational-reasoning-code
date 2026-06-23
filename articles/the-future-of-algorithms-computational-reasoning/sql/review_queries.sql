-- High-risk governance gaps.
SELECT domain_id, risk_score, readiness_score, future_status
FROM future_algorithmic_systems_map
WHERE future_status = 'high_risk_governance_gap'
ORDER BY risk_score DESC;

-- Systems where cautious deployment may be possible.
SELECT domain_id, risk_score, readiness_score, future_status
FROM future_algorithmic_systems_map
WHERE future_status = 'cautious_deployment_possible'
ORDER BY readiness_score DESC;

-- No-go examples.
SELECT case_id, poor_fit, invalid_data, high_opacity, no_appeal, no_governance, no_go
FROM no_go_examples
ORDER BY no_go DESC, case_id;

-- Future cautions.
SELECT caution, meaning
FROM future_algorithmic_cautions
ORDER BY caution;
