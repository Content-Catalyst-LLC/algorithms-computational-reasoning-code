-- Core cryptanalysis threads.
SELECT theme_id, cryptanalysis_score, interpretive_status
FROM cryptanalysis_map
WHERE interpretive_status = 'core_cryptanalysis_thread'
ORDER BY cryptanalysis_score DESC;

-- Highest sample symbols.
SELECT symbol, count, relative_frequency, rank
FROM sample_frequency_table
ORDER BY rank ASC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
