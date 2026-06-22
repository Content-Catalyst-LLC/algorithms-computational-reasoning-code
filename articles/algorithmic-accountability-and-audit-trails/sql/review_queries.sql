-- Systems requiring accountability review or escalation.
SELECT system_id, audit_completeness_score, accountability_capacity_score, reconstruction_risk_score, status
FROM accountability_audit
WHERE status IN ('review', 'escalate')
ORDER BY reconstruction_risk_score DESC;

-- Systems with incomplete audit trails.
SELECT system_id, audit_completeness_score
FROM accountability_audit
WHERE audit_completeness_score < 0.75
ORDER BY audit_completeness_score ASC;

-- Systems with weak accountability capacity.
SELECT system_id, accountability_capacity_score
FROM accountability_audit
WHERE accountability_capacity_score < 0.70
ORDER BY accountability_capacity_score ASC;

-- Required governance items.
SELECT item, review_question
FROM accountability_governance_register
WHERE status = 'required';
