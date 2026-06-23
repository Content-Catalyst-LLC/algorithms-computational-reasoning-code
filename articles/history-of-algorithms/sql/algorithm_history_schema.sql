CREATE TABLE IF NOT EXISTS algorithm_history_layers (
  layer_id TEXT PRIMARY KEY,
  procedural_explicitness REAL NOT NULL,
  representation REAL NOT NULL,
  proof_correctness REAL NOT NULL,
  portability REAL NOT NULL,
  mechanization REAL NOT NULL,
  formalization REAL NOT NULL,
  programmability REAL NOT NULL,
  institutional_adoption REAL NOT NULL,
  governance_relevance REAL NOT NULL,
  modern_resonance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS algorithm_history_map (
  layer_id TEXT PRIMARY KEY,
  procedural_explicitness REAL NOT NULL,
  representation REAL NOT NULL,
  proof_correctness REAL NOT NULL,
  portability REAL NOT NULL,
  mechanization REAL NOT NULL,
  formalization REAL NOT NULL,
  programmability REAL NOT NULL,
  institutional_adoption REAL NOT NULL,
  governance_relevance REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  history_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
