-- Feedback cases requiring review or escalation.
SELECT case_id, system, feedback_path, feedback_risk_score, status
FROM feedback_loop_audit
WHERE status IN ('review', 'escalate')
ORDER BY feedback_risk_score DESC;

-- High amplification and exposure concentration.
SELECT case_id, system, amplification, exposure_concentration
FROM feedback_loop_audit
WHERE amplification >= 0.70 OR exposure_concentration >= 0.65
ORDER BY amplification DESC;

-- Drift and recursive data risks.
SELECT case_id, system, drift, recursive_data
FROM feedback_loop_audit
WHERE drift >= 0.25 OR recursive_data >= 0.30
ORDER BY drift DESC;

-- Required governance items.
SELECT item, review_question
FROM feedback_governance_register
WHERE status = 'required';
