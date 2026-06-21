-- Rules without provenance should be blocked before deployment.
SELECT rule_id, conclusion
FROM symbolic_rules
WHERE provenance IS NULL OR TRIM(provenance) = '';

-- Constraints that failed review require escalation.
SELECT constraint_name, interpretation
FROM symbolic_constraint_review
WHERE satisfied = 0;

-- Hybrid interface risks should be reviewed by system owners.
SELECT interface_item, review_question, risk
FROM symbolic_hybrid_interface_register
ORDER BY interface_item;
