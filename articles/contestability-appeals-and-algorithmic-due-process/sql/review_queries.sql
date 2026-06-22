-- Due-process cases requiring review or escalation.
SELECT case_id, domain, stakes, contestability_score, procedural_risk_score, appeal_burden, resolution_days, status
FROM contestability_appeals_audit
WHERE status IN ('review', 'escalate')
ORDER BY procedural_risk_score DESC;

-- High-stakes cases with weak contestability.
SELECT case_id, domain, stakes, contestability_score
FROM contestability_appeals_audit
WHERE stakes >= 0.75 AND contestability_score < 0.70;

-- Appeal burden and timeliness concerns.
SELECT case_id, domain, appeal_burden, resolution_days
FROM contestability_appeals_audit
WHERE appeal_burden >= 0.60 OR resolution_days > 14;

-- Required due-process governance items.
SELECT item, review_question
FROM due_process_governance_register
WHERE status = 'required';
