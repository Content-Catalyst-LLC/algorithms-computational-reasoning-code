# Data Dictionary

## backus_themes.csv

- `theme_id`: interpretive theme in the Backus/FORTRAN map.
- `high_level_language`: relevance to high-level source expression.
- `scientific_expression`: relevance to formulas, numerical work, and domain expression.
- `compiler_optimization`: relevance to compiler performance and translation quality.
- `numerical_relevance`: relevance to scientific computing, arrays, loops, and numerical methods.
- `portability`: relevance to machine independence and source continuity.
- `performance_credibility`: relevance to adoption through efficient generated code.
- `language_history`: relevance to programming-language history.
- `formal_specification`: relevance to language grammar and Backus-Naur Form.
- `maintainability`: relevance to long-lived scientific software and documentation.
- `governance_caution`: relevance to review, AI-code caution, tests, and accountability.

## backus_fortran_scientific_programming_map.csv

- `birth_score`: average of the theme dimensions.
- `interpretive_status`: core, major, or supporting Backus/FORTRAN scientific-programming thread.

## formula_translation_example.csv

- `x`, `a`, `b`, `c`, `y`: teaching example for y = ax^2 + bx + c.

## vector_formula_example.csv

- `index`, `x`, `sin_x_plus_x_squared`: loop-over-array teaching example.

## interpretation_cautions.csv

- `caution`: interpretive risk to avoid.
- `meaning`: explanation of the caution.
