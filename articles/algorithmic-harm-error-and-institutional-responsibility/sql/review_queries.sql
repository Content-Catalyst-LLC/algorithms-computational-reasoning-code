-- Harm and responsibility cases requiring review or escalation.
SELECT case_id, domain, harm_risk_score, responsibility_capacity, remediation_gap, status
FROM harm_responsibility_audit
WHERE status IN ('review', 'escalate')
ORDER BY harm_risk_score DESC;

-- High harm with low responsibility capacity.
SELECT case_id, domain, harm_risk_score, responsibility_capacity
FROM harm_responsibility_audit
WHERE harm_risk_score >= 0.30 AND responsibility_capacity < 0.65;

-- High remediation gaps.
SELECT case_id, domain, remediation_gap, status
FROM harm_responsibility_audit
WHERE remediation_gap >= 0.20
ORDER BY remediation_gap DESC;

-- Required incident register fields.
SELECT field, purpose
FROM algorithmic_incident_register
WHERE required = 'yes';
