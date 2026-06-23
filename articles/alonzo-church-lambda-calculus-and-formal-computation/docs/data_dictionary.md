# Data Dictionary

## church_themes.csv

- `theme_id`: interpretive theme in the Church formal-computation map.
- `formalization`: degree to which the theme clarifies computation as a formal system.
- `functional_abstraction`: degree to which functions and higher-order abstraction matter.
- `symbolic_transformation`: degree to which computation is represented as expression transformation.
- `substitution`: importance of substitution and variable handling.
- `reduction`: importance of beta reduction, evaluation, and normal forms.
- `computability`: relevance to effective calculability and computable functions.
- `undecidability`: relevance to decision-procedure limits.
- `type_influence`: relevance to type theory and proof systems.
- `programming_relevance`: relevance to functional programming and language semantics.
- `ai_caution`: relevance to formal reasoning and AI-era overclaiming.

## church_formal_computation_map.csv

- `formal_score`: average of the theme dimensions.
- `interpretive_status`: core, major, or supporting Church formal-computation thread.

## interpretation_cautions.csv

- `caution`: interpretive risk to avoid.
- `meaning`: explanation of the caution.
