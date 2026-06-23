-- Learning systems requiring special review.
SELECT system_id, impact_score, governance_readiness_score, learning_system_risk_score, recommendation
FROM learning_system_governance_audit
WHERE recommendation <> 'governed_use_with_monitoring'
ORDER BY learning_system_risk_score DESC;

-- Systems requiring pedagogical validity review.
SELECT system_id, impact_score, governance_readiness_score, learning_system_risk_score
FROM learning_system_governance_audit
WHERE recommendation = 'pedagogical_validity_review_required';

-- Systems requiring student impact review.
SELECT system_id, impact_score, governance_readiness_score, learning_system_risk_score
FROM learning_system_governance_audit
WHERE recommendation = 'student_impact_review_required';

-- Required learning governance controls.
SELECT control, review_question
FROM learning_governance_register
WHERE status = 'required';
