-- Group-level bias and history metrics.
SELECT group_id, representation_gap, selection_rate, label_gap, proxy_risk, historical_risk_score
FROM bias_history_group_metrics
ORDER BY historical_risk_score DESC;

-- High historical-risk groups.
SELECT group_id, historical_risk_score
FROM bias_history_group_metrics
WHERE historical_risk_score >= 0.55;

-- High label-gap groups.
SELECT group_id, label_gap
FROM bias_history_group_metrics
WHERE label_gap >= 0.08;

-- Required governance items.
SELECT item, review_question
FROM bias_history_governance_register
WHERE status = 'required';
