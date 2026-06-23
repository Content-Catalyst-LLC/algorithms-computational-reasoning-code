-- Systems requiring redesign before scaling.
SELECT system_id, governance_readiness_score, attention_risk_score, platform_risk_score, recommendation
FROM attention_system_audit
WHERE recommendation = 'redesign_before_scaling'
ORDER BY platform_risk_score DESC;

-- Systems requiring public-interest or governance review.
SELECT system_id, governance_readiness_score, attention_risk_score, platform_risk_score, recommendation
FROM attention_system_audit
WHERE recommendation IN ('independent_public_interest_review_required', 'governance_review_required', 'use_with_strong_attention_guardrails')
ORDER BY platform_risk_score DESC;

-- Required attention-system governance controls.
SELECT control, review_question
FROM platform_governance_register
WHERE status = 'required';
