-- Core Backus/FORTRAN high-level scientific-programming threads.
SELECT theme_id, birth_score, interpretive_status
FROM backus_fortran_scientific_programming_map
WHERE interpretive_status = 'core_backus_fortran_scientific_programming_thread'
ORDER BY birth_score DESC;

-- High-optimization, high-performance themes.
SELECT theme_id, compiler_optimization, performance_credibility, numerical_relevance, birth_score
FROM backus_fortran_scientific_programming_map
WHERE compiler_optimization >= 0.90 AND performance_credibility >= 0.90
ORDER BY birth_score DESC;

-- Formula-translation teaching example.
SELECT x, y
FROM formula_translation_example
ORDER BY x;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
