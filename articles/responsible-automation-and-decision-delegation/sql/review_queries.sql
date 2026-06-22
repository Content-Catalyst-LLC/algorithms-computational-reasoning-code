-- Delegation contexts requiring review or escalation.
SELECT context_id, delegation_readiness_score, automation_reliance_score, delegation_risk_score, recommendation, status
FROM delegation_readiness_audit
WHERE status IN ('review', 'escalate')
ORDER BY delegation_risk_score DESC;

-- High automation reliance contexts.
SELECT context_id, automation_reliance_score, recommendation
FROM delegation_readiness_audit
WHERE automation_reliance_score >= 0.85
ORDER BY automation_reliance_score DESC;

-- Weak delegation readiness contexts.
SELECT context_id, delegation_readiness_score, delegation_risk_score
FROM delegation_readiness_audit
WHERE delegation_readiness_score < 0.70
ORDER BY delegation_readiness_score ASC;

-- Required governance controls.
SELECT item, review_question
FROM delegation_governance_register
WHERE status = 'required';
