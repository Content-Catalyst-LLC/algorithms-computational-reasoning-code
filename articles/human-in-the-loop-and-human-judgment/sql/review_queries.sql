-- Review contexts requiring review or escalation.
SELECT context_id, review_capacity_score, reliance_score, override_rate, judgment_capacity_score, review_risk_score, status
FROM human_review_audit
WHERE status IN ('review', 'escalate')
ORDER BY review_risk_score DESC;

-- High reliance contexts.
SELECT context_id, reliance_score, override_rate
FROM human_review_audit
WHERE reliance_score >= 0.90
ORDER BY reliance_score DESC;

-- Low override contexts.
SELECT context_id, reliance_score, override_rate
FROM human_review_audit
WHERE override_rate <= 0.02
ORDER BY override_rate ASC;

-- Required governance items.
SELECT item, review_question
FROM human_review_governance_register
WHERE status = 'required';
