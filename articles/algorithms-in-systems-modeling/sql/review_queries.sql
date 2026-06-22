-- Scenarios requiring escalation or governance review.
SELECT scenario_id, system_vulnerability_score, model_readiness_score, system_modeling_risk_score, recommendation
FROM systems_modeling_audit
WHERE recommendation IN ('stress_test_and_escalate', 'governance_review_required', 'do_not_use_for_decision_without_redesign')
ORDER BY system_modeling_risk_score DESC;

-- High vulnerability scenarios.
SELECT scenario_id, system_vulnerability_score, recommendation
FROM systems_modeling_audit
WHERE system_vulnerability_score >= 0.70
ORDER BY system_vulnerability_score DESC;

-- Weak readiness scenarios.
SELECT scenario_id, model_readiness_score, recommendation
FROM systems_modeling_audit
WHERE model_readiness_score < 0.65
ORDER BY model_readiness_score ASC;

-- Required systems-modeling governance controls.
SELECT control, review_question
FROM systems_modeling_register
WHERE status = 'required';
