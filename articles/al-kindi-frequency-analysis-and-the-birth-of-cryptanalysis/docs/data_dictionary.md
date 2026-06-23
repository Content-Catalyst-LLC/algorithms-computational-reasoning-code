# Data Dictionary

## sample_frequency_table.csv

- `symbol`: observed ciphertext symbol.
- `count`: number of times the symbol appears.
- `relative_frequency`: count divided by total alphabetic symbols.
- `rank`: frequency rank among observed symbols.

## cryptanalysis_themes.csv

- `theme_id`: interpretive theme in frequency-analysis cryptanalysis.
- `linguistic_evidence`: importance of language regularity, grammar, word patterns, and textual evidence.
- `counting_procedure`: importance of counting, frequency, normalization, ranking, and comparison.
- `inferential_structure`: importance of hypothesis, testing, conflict detection, and revision.
- `cryptanalytic_relevance`: importance for classical decipherment.
- `historical_significance`: importance for the history of cryptanalysis and algorithmic reasoning.
- `ethical_caution`: importance of responsible boundaries and non-abusive framing.
- `modern_resonance`: degree to which the theme clarifies modern pattern, leakage, and security reasoning.

## cryptanalysis_map.csv

- `cryptanalysis_score`: average of the theme dimensions.
- `interpretive_status`: core, major, or supporting cryptanalysis thread.

## interpretation_cautions.csv

- `caution`: interpretive risk to avoid.
- `meaning`: explanation of the caution.
