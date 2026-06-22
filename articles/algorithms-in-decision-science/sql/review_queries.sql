-- Decisions where automation should not proceed.
SELECT decision_id, predicted_probability, decision_support_readiness_score, stakes, recommendation
FROM decision_science_audit
WHERE recommendation = 'do_not_automate_action'
ORDER BY stakes DESC;

-- High-stakes decisions requiring escalation.
SELECT decision_id, predicted_probability, decision_support_readiness_score, stakes, recommendation
FROM decision_science_audit
WHERE stakes >= 0.80
ORDER BY stakes DESC;

-- Cases where expected loss from no action exceeds expected value of action.
SELECT decision_id, expected_value_of_action, expected_loss_if_no_action, recommendation
FROM decision_science_audit
WHERE expected_loss_if_no_action > expected_value_of_action
ORDER BY expected_loss_if_no_action DESC;

-- Required governance controls.
SELECT control, review_question
FROM decision_governance_register
WHERE status = 'required';
