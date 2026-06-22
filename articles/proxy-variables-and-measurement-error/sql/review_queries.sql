-- Proxy cases requiring review or escalation.
SELECT case_id, construct, proxy, measurement_risk_score, status
FROM proxy_measurement_error_audit
WHERE status IN ('review', 'escalate')
ORDER BY measurement_risk_score DESC;

-- Weak proxy validity.
SELECT case_id, construct, proxy, validity_gap
FROM proxy_measurement_error_audit
WHERE validity_gap >= 0.30
ORDER BY validity_gap DESC;

-- Differential measurement error.
SELECT case_id, construct, proxy, differential_error
FROM proxy_measurement_error_audit
WHERE differential_error >= 0.15
ORDER BY differential_error DESC;

-- Required measurement governance items.
SELECT item, review_question
FROM measurement_governance_register
WHERE status = 'required';
