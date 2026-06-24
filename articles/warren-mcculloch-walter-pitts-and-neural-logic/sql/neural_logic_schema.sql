CREATE TABLE IF NOT EXISTS neural_logic_concepts (
  concept_id TEXT PRIMARY KEY,
  logical_clarity REAL NOT NULL,
  neural_abstraction REAL NOT NULL,
  computational_relevance REAL NOT NULL,
  cybernetic_connection REAL NOT NULL,
  ai_lineage REAL NOT NULL,
  biological_caution REAL NOT NULL,
  historical_influence REAL NOT NULL,
  interpretability REAL NOT NULL,
  formal_tractability REAL NOT NULL,
  responsible_use_relevance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS mcculloch_pitts_neural_logic_map (
  concept_id TEXT PRIMARY KEY,
  logical_clarity REAL NOT NULL,
  neural_abstraction REAL NOT NULL,
  computational_relevance REAL NOT NULL,
  cybernetic_connection REAL NOT NULL,
  ai_lineage REAL NOT NULL,
  biological_caution REAL NOT NULL,
  historical_influence REAL NOT NULL,
  interpretability REAL NOT NULL,
  formal_tractability REAL NOT NULL,
  responsible_use_relevance REAL NOT NULL,
  neural_logic_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS threshold_logic_examples (
  gate TEXT NOT NULL,
  x1 INTEGER NOT NULL,
  x2 INTEGER NOT NULL,
  threshold INTEGER NOT NULL,
  output INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
