CREATE TABLE IF NOT EXISTS supervised_metrics (
  paradigm TEXT,
  split TEXT,
  threshold REAL,
  n INTEGER,
  tp INTEGER,
  fp INTEGER,
  tn INTEGER,
  fn INTEGER,
  accuracy REAL,
  precision REAL,
  recall REAL,
  f1 REAL,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS unsupervised_cluster_summary (
  paradigm TEXT,
  cluster INTEGER,
  n INTEGER,
  centroid_access REAL,
  centroid_risk REAL,
  mean_distance_to_centroid REAL,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS reinforcement_learning_summary (
  paradigm TEXT,
  arm TEXT,
  true_reward_probability REAL,
  times_selected INTEGER,
  observed_mean_reward REAL,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS learning_paradigm_governance_register (
  paradigm TEXT,
  governance_item TEXT,
  review_question TEXT,
  status TEXT
);
