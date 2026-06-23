# Data Dictionary

## hopper_themes.csv

- `theme_id`: interpretive theme in the Hopper compiler-humanization map.
- `compiler_centrality`: importance of compilers, translation, and automatic programming.
- `human_readability`: degree to which human-facing syntax, diagnostics, and comprehension matter.
- `portability`: relevance to machine independence and cross-system use.
- `documentation`: relevance to manuals, examples, teaching, and maintainability.
- `standards`: relevance to language standards and conformance.
- `debugging`: relevance to diagnostic culture, repair, and correctness.
- `business_relevance`: relevance to business data processing and institutional procedure.
- `institutional_scale`: relevance to organizations, governments, enterprises, and long-lived systems.
- `abstraction`: relevance to hiding machine detail while preserving executable rigor.
- `governance_caution`: relevance to testing, validation, review, accountability, and AI coding caution.

## hopper_compiler_humanization_map.csv

- `humanization_score`: average of the theme dimensions.
- `interpretive_status`: core, major, or supporting Hopper compiler-humanization thread.

## interpretation_cautions.csv

- `caution`: interpretive risk to avoid.
- `meaning`: explanation of the caution.
