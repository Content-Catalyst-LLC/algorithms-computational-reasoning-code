# Data Dictionary

## knuth_themes.csv

- `theme_id`: interpretive theme in the Knuth algorithmic-art map.
- `algorithm_analysis`: relevance to algorithm analysis, complexity, and cost models.
- `exposition`: relevance to readable explanation and technical writing.
- `mathematical_rigor`: relevance to proof, notation, and formal reasoning.
- `historical_depth`: relevance to historical scholarship and intellectual context.
- `implementation_relevance`: relevance to executable procedure, machine models, and practice.
- `typography_relevance`: relevance to TeX, METAFONT, and technical presentation.
- `literate_programming`: relevance to WEB, CWEB, and human-readable code.
- `pedagogy`: relevance to exercises, examples, and active learning.
- `maintainability`: relevance to future readers, code durability, and explanation.
- `governance_caution`: relevance to AI code-generation review, trust, tests, and accountability.

## knuth_algorithmic_art_map.csv

- `art_score`: average of the theme dimensions.
- `interpretive_status`: core, major, or supporting Knuth algorithmic-art thread.

## interpretation_cautions.csv

- `caution`: interpretive risk to avoid.
- `meaning`: explanation of the caution.
