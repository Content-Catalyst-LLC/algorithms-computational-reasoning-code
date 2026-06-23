CREATE TABLE IF NOT EXISTS shannon_themes (
  theme_id TEXT PRIMARY KEY,
  entropy_centrality REAL NOT NULL,
  coding_relevance REAL NOT NULL,
  channel_capacity REAL NOT NULL,
  noise_awareness REAL NOT NULL,
  redundancy_design REAL NOT NULL,
  computation_relevance REAL NOT NULL,
  cryptography_relevance REAL NOT NULL,
  ai_relevance REAL NOT NULL,
  semantic_boundary REAL NOT NULL,
  governance_caution REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS shannon_information_map (
  theme_id TEXT PRIMARY KEY,
  entropy_centrality REAL NOT NULL,
  coding_relevance REAL NOT NULL,
  channel_capacity REAL NOT NULL,
  noise_awareness REAL NOT NULL,
  redundancy_design REAL NOT NULL,
  computation_relevance REAL NOT NULL,
  cryptography_relevance REAL NOT NULL,
  ai_relevance REAL NOT NULL,
  semantic_boundary REAL NOT NULL,
  governance_caution REAL NOT NULL,
  information_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS entropy_examples (
  source TEXT PRIMARY KEY,
  probabilities TEXT NOT NULL,
  entropy_bits REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
