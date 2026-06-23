# Data Dictionary

## data_structure_traditions.csv

- `tradition_id`: interpretive data-structure or analysis tradition.
- `representation_centrality`: importance of representation choice.
- `operation_clarity`: clarity of supported operations and access discipline.
- `memory_awareness`: relevance to memory layout, storage, pointers, locality, or I/O.
- `time_analysis`: relevance to runtime, comparisons, traversal, or operation cost.
- `space_analysis`: relevance to memory or storage growth.
- `scale_sensitivity`: relevance to input-size growth and system scaling.
- `abstraction_maturity`: degree to which interface and implementation are separated.
- `systems_relevance`: relevance to operating systems, databases, compilers, search, distributed systems, AI, or infrastructure.
- `historical_influence`: influence on computer science education and practice.
- `governance_caution`: relevance to documentation, auditability, AI infrastructure, and operational responsibility.

## data_structure_algorithm_analysis_history_map.csv

- `history_score`: average of the tradition dimensions.
- `interpretive_status`: core, major, or supporting data-structure/analysis history thread.

## growth_rate_examples.csv

- `n`: input size.
- `constant`, `log2_n`, `linear`, `n_log2_n`, `quadratic`: teaching growth-rate values.

## binary_search_steps.csv

- `n`: sorted collection size.
- `binary_search_steps`: approximate maximum number of halving steps.

## graph_representation_memory.csv

- `nodes`: number of nodes.
- `edges`: number of edges.
- `adjacency_matrix_cells`: matrix storage units.
- `adjacency_list_units`: list-style storage units.

## interpretation_cautions.csv

- `caution`: interpretive risk to avoid.
- `meaning`: explanation of the caution.
