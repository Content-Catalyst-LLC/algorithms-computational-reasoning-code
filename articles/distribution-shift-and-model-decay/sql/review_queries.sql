-- Monitoring periods requiring review or escalation.
SELECT period, accuracy, performance_decay, calibration_gap, subgroup_gap, decay_risk_score, status
FROM drift_decay_audit
WHERE status IN ('review', 'escalate')
ORDER BY decay_risk_score DESC;

-- Input and label drift warnings.
SELECT period, input_drift, label_drift
FROM drift_decay_audit
WHERE input_drift >= 0.25 OR label_drift >= 0.15
ORDER BY period;

-- Performance and calibration decay warnings.
SELECT period, performance_decay, calibration_gap
FROM drift_decay_audit
WHERE performance_decay >= 0.08 OR calibration_gap >= 0.10
ORDER BY performance_decay DESC;

-- Required lifecycle governance items.
SELECT item, review_question
FROM drift_decay_governance_register
WHERE status = 'required';
