# Data Dictionary

## dijkstra_themes.csv

- `theme_id`: interpretive theme in the Dijkstra structured-programming map.
- `structured_control`: importance of structured control flow.
- `correctness`: relevance to specifications, proof, and correctness.
- `invariants`: relevance to preserved properties and loop reasoning.
- `proof_relevance`: importance of proof obligations and derivation.
- `formal_methods`: relevance to program logic, predicate transformers, and verification.
- `readability`: human readability and reasoning clarity.
- `maintainability`: maintainability and long-term software discipline.
- `algorithmic_relevance`: relevance to algorithm design and analysis.
- `system_design`: relevance to operating systems, layers, concurrency, and architecture.
- `governance_caution`: relevance to review, accountability, AI code generation, and responsible software.

## dijkstra_structured_programming_map.csv

- `discipline_score`: average of the theme dimensions.
- `interpretive_status`: core, major, or supporting Dijkstra structured-programming thread.

## interpretation_cautions.csv

- `caution`: interpretive risk to avoid.
- `meaning`: explanation of the caution.
