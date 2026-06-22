-- Explanation artifacts requiring review or escalation.
SELECT case_id, audience, explanation_quality_score, transparency_capacity_score, contestability, explanation_risk_score, status
FROM explanation_audit
WHERE status IN ('review', 'escalate')
ORDER BY explanation_risk_score DESC;

-- Explanations with weak contestability.
SELECT case_id, audience, contestability, status
FROM explanation_audit
WHERE contestability < 0.65;

-- High-stakes explanations with low transparency capacity.
SELECT case_id, audience, transparency_capacity_score, explanation_risk_score
FROM explanation_audit
WHERE transparency_capacity_score < 0.70
ORDER BY explanation_risk_score DESC;

-- Required governance items.
SELECT item, review_question
FROM explanation_governance_register
WHERE status = 'required';
