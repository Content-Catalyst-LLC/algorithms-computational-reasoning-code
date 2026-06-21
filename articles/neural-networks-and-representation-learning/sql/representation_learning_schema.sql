CREATE TABLE IF NOT EXISTS representation_audit_summary (
  article TEXT PRIMARY KEY,
  timestamp_utc TEXT,
  n INTEGER,
  train_n INTEGER,
  test_n INTEGER,
  train_accuracy REAL,
  test_accuracy REAL,
  train_loss REAL,
  test_loss REAL,
  generalization_gap_loss REAL,
  representation_gap REAL,
  governance_items_needing_review INTEGER,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS model_evaluation_summary (
  split TEXT PRIMARY KEY,
  n INTEGER,
  accuracy REAL,
  mean_loss REAL,
  threshold REAL,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS representation_governance_register (
  item TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);

CREATE TABLE IF NOT EXISTS embedding_similarity_examples (
  left_item TEXT,
  right_item TEXT,
  cosine_similarity REAL,
  interpretation TEXT
);
