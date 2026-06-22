-- Use cases that should be refused or reviewed.
SELECT use_case, responsible_use_readiness_score, non_use_pressure_score, recommendation, status
FROM algorithmic_non_use_audit
WHERE status IN ('review', 'refuse')
ORDER BY non_use_pressure_score DESC;

-- High non-use pressure.
SELECT use_case, non_use_pressure_score, recommendation
FROM algorithmic_non_use_audit
WHERE non_use_pressure_score >= 0.70
ORDER BY non_use_pressure_score DESC;

-- Low responsible-use readiness.
SELECT use_case, responsible_use_readiness_score, recommendation
FROM algorithmic_non_use_audit
WHERE responsible_use_readiness_score < 0.65
ORDER BY responsible_use_readiness_score ASC;

-- Required non-use criteria.
SELECT criterion, review_question
FROM algorithmic_non_use_register
WHERE status = 'required';
