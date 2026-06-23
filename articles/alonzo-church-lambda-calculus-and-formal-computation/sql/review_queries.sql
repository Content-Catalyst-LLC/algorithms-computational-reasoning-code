-- Core Church formal-computation threads.
SELECT theme_id, formal_score, interpretive_status
FROM church_formal_computation_map
WHERE interpretive_status = 'core_church_formal_computation_thread'
ORDER BY formal_score DESC;

-- Themes where computability and undecidability are both high.
SELECT theme_id, computability, undecidability, formal_score
FROM church_formal_computation_map
WHERE computability >= 0.90 AND undecidability >= 0.90
ORDER BY formal_score DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
