CREATE TABLE IF NOT EXISTS data_structure_traditions (
  tradition_id TEXT PRIMARY KEY,
  representation_centrality REAL NOT NULL,
  operation_clarity REAL NOT NULL,
  memory_awareness REAL NOT NULL,
  time_analysis REAL NOT NULL,
  space_analysis REAL NOT NULL,
  scale_sensitivity REAL NOT NULL,
  abstraction_maturity REAL NOT NULL,
  systems_relevance REAL NOT NULL,
  historical_influence REAL NOT NULL,
  governance_caution REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS data_structure_algorithm_analysis_history_map (
  tradition_id TEXT PRIMARY KEY,
  representation_centrality REAL NOT NULL,
  operation_clarity REAL NOT NULL,
  memory_awareness REAL NOT NULL,
  time_analysis REAL NOT NULL,
  space_analysis REAL NOT NULL,
  scale_sensitivity REAL NOT NULL,
  abstraction_maturity REAL NOT NULL,
  systems_relevance REAL NOT NULL,
  historical_influence REAL NOT NULL,
  governance_caution REAL NOT NULL,
  history_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS growth_rate_examples (
  n INTEGER PRIMARY KEY,
  constant REAL NOT NULL,
  log2_n REAL NOT NULL,
  linear REAL NOT NULL,
  n_log2_n REAL NOT NULL,
  quadratic REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS binary_search_steps (
  n INTEGER PRIMARY KEY,
  binary_search_steps INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS graph_representation_memory (
  nodes INTEGER NOT NULL,
  edges INTEGER NOT NULL,
  adjacency_matrix_cells INTEGER NOT NULL,
  adjacency_list_units INTEGER NOT NULL,
  PRIMARY KEY (nodes, edges)
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
