-- Cases requiring review or escalation.
SELECT case_id, objective, metric, goodhart_risk_score, status
FROM goodhart_risk_audit
WHERE status IN ('review', 'escalate')
ORDER BY goodhart_risk_score DESC;

-- Metrics with weak proxy relationship under strong pressure.
SELECT case_id, objective, metric, proxy_gap, optimization_pressure
FROM goodhart_risk_audit
WHERE proxy_gap >= 0.20 AND optimization_pressure >= 0.70;

-- Cases with weak guardrails.
SELECT case_id, objective, metric, guardrails
FROM goodhart_risk_audit
WHERE guardrails < 2;

-- Required governance items.
SELECT item, review_question
FROM metric_governance_register
WHERE status = 'required';
