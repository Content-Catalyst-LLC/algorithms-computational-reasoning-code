-- Oversight cases requiring review or escalation.
SELECT case_id, context, acceptance_rate, model_quality, overreliance_gap, automation_bias_risk_score, status
FROM automation_bias_overreliance_audit
WHERE status IN ('review', 'escalate')
ORDER BY automation_bias_risk_score DESC;

-- High acceptance with weak model quality.
SELECT case_id, context, acceptance_rate, model_quality, overreliance_gap
FROM automation_bias_overreliance_audit
WHERE acceptance_rate >= 0.85 AND model_quality <= 0.75;

-- Override and contestability concerns.
SELECT case_id, context, override_friction, appeal_pathway
FROM automation_bias_overreliance_audit
WHERE override_friction >= 0.60 OR appeal_pathway = 0;

-- Required oversight governance items.
SELECT item, review_question
FROM automation_oversight_governance_register
WHERE status = 'required';
