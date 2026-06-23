CREATE TABLE IF NOT EXISTS dijkstra_themes (
  theme_id TEXT PRIMARY KEY,
  structured_control REAL NOT NULL,
  correctness REAL NOT NULL,
  invariants REAL NOT NULL,
  proof_relevance REAL NOT NULL,
  formal_methods REAL NOT NULL,
  readability REAL NOT NULL,
  maintainability REAL NOT NULL,
  algorithmic_relevance REAL NOT NULL,
  system_design REAL NOT NULL,
  governance_caution REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS dijkstra_structured_programming_map (
  theme_id TEXT PRIMARY KEY,
  structured_control REAL NOT NULL,
  correctness REAL NOT NULL,
  invariants REAL NOT NULL,
  proof_relevance REAL NOT NULL,
  formal_methods REAL NOT NULL,
  readability REAL NOT NULL,
  maintainability REAL NOT NULL,
  algorithmic_relevance REAL NOT NULL,
  system_design REAL NOT NULL,
  governance_caution REAL NOT NULL,
  discipline_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS dijkstra_shortest_path_example (
  source TEXT NOT NULL,
  node TEXT NOT NULL,
  distance REAL NOT NULL,
  PRIMARY KEY (source, node)
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
