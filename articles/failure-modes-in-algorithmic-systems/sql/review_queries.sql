SELECT failure_id, category, failure_risk_score, priority_score, resilience_capacity, status
FROM failure_mode_audit
WHERE status IN ('review', 'escalate')
ORDER BY priority_score DESC;

SELECT failure_id, category, priority_score, resilience_capacity
FROM failure_mode_audit
WHERE priority_score >= 0.35 AND resilience_capacity < 0.60;

SELECT item, review_question
FROM failure_mode_governance_register
WHERE status = 'required';
