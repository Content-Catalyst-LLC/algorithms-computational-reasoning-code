CREATE TABLE IF NOT EXISTS algorithmic_decisions (
  case_id INTEGER PRIMARY KEY,
  baseline_score REAL,
  document_quality REAL,
  timeliness REAL,
  prior_flag REAL,
  access_constraint REAL,
  risk_adjustment REAL,
  decision_score REAL,
  decision TEXT,
  threshold REAL,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS counterfactual_candidates (
  case_id INTEGER,
  original_decision TEXT,
  original_score REAL,
  counterfactual_feature TEXT,
  original_value REAL,
  counterfactual_value REAL,
  delta REAL,
  counterfactual_score REAL,
  counterfactual_decision TEXT,
  score_change REAL,
  flipped_to_favorable BOOLEAN,
  allowed_for_recourse BOOLEAN,
  recourse_cost REAL,
  feasibility_note TEXT
);

CREATE TABLE IF NOT EXISTS recourse_review (
  case_id INTEGER,
  recommended_feature TEXT,
  original_value REAL,
  counterfactual_value REAL,
  delta REAL,
  original_score REAL,
  counterfactual_score REAL,
  recourse_cost REAL,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS feature_change_rules (
  feature TEXT PRIMARY KEY,
  allowed_for_recourse BOOLEAN,
  min_value REAL,
  max_value REAL,
  unit_cost REAL,
  reason TEXT
);
