-- Workplace systems requiring special review.
SELECT system_id, impact_score, governance_readiness_score, workplace_algorithm_risk_score, recommendation
FROM workplace_algorithm_governance_audit
WHERE recommendation <> 'governed_use_with_monitoring'
ORDER BY workplace_algorithm_risk_score DESC;

-- Systems requiring contestability and appeal review.
SELECT system_id, impact_score, governance_readiness_score, workplace_algorithm_risk_score
FROM workplace_algorithm_governance_audit
WHERE recommendation = 'contestability_and_appeal_review_required';

-- Systems requiring workplace privacy review.
SELECT system_id, impact_score, governance_readiness_score, workplace_algorithm_risk_score
FROM workplace_algorithm_governance_audit
WHERE recommendation = 'workplace_privacy_review_required';

-- Required workplace governance controls.
SELECT control, review_question
FROM workplace_governance_register
WHERE status = 'required';
