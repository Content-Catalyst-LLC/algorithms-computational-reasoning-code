CREATE TABLE IF NOT EXISTS decision_options (
  option_name TEXT PRIMARY KEY,
  risk_reduction REAL,
  benefit_multiplier REAL,
  cost_multiplier REAL,
  governance_burden TEXT
);

CREATE TABLE IF NOT EXISTS decision_metrics (
  case_id INTEGER,
  option_name TEXT,
  baseline_risk REAL,
  post_intervention_risk REAL,
  expected_benefit REAL,
  expected_loss REAL,
  intervention_cost REAL,
  expected_net_value REAL,
  downside_exposure REAL,
  regret REAL,
  governance_burden TEXT,
  PRIMARY KEY (case_id, option_name)
);

CREATE TABLE IF NOT EXISTS threshold_review (
  case_id INTEGER PRIMARY KEY,
  recommended_option TEXT,
  baseline_risk REAL,
  best_expected_net_value REAL,
  confidence_score REAL,
  decision TEXT,
  threshold_rule TEXT,
  review_note TEXT
);

CREATE TABLE IF NOT EXISTS risk_register (
  case_id INTEGER,
  risk_item TEXT,
  recommended_option TEXT,
  downside_exposure REAL,
  confidence_score REAL,
  severity TEXT,
  mitigation TEXT
);
