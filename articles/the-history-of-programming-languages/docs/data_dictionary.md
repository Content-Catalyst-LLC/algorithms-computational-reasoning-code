# Data Dictionary

## programming_language_traditions.csv

- `tradition_id`: interpretive language tradition or layer.
- `abstraction`: degree of distance from machine-level detail.
- `performance_orientation`: importance of runtime performance and machine efficiency.
- `readability`: emphasis on human-readable source.
- `formal_specification`: relevance to formal syntax, semantics, type systems, and language definition.
- `ecosystem_depth`: strength of tools, libraries, packages, compilers, runtimes, and communities.
- `domain_fit`: fit to the target domain or user community.
- `safety_orientation`: emphasis on preventing or exposing errors.
- `institutional_adoption`: adoption by businesses, governments, science, education, platforms, or infrastructure.
- `historical_influence`: lasting influence on language design and software practice.
- `governance_caution`: relevance to dependency governance, code review, AI-generated code, and operational responsibility.

## programming_language_history_map.csv

- `history_score`: average of the tradition dimensions.
- `interpretive_status`: core, major, or supporting programming-language history thread.

## interpretation_cautions.csv

- `caution`: interpretive risk to avoid.
- `meaning`: explanation of the caution.
