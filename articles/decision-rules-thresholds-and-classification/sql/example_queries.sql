-- Cases classified positive at threshold 0.50
SELECT case_id, score, actual
FROM classification_cases
WHERE score >= 0.50
ORDER BY score DESC;

-- Borderline review band
SELECT case_id, score, actual
FROM classification_cases
WHERE score BETWEEN 0.45 AND 0.55
ORDER BY score DESC;
