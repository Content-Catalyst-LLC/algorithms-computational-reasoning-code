CREATE TABLE IF NOT EXISTS intervention_cases (
  case_id INTEGER PRIMARY KEY,
  baseline_need REAL,
  access_barrier REAL,
  service_quality REAL,
  support_intensity REAL,
  baseline_outcome REAL,
  baseline_decision_score REAL,
  baseline_decision TEXT
);

CREATE TABLE IF NOT EXISTS intervention_effect_estimates (
  intervention_name TEXT PRIMARY KEY,
  mean_estimated_effect REAL,
  min_estimated_effect REAL,
  max_estimated_effect REAL,
  mean_net_benefit REAL,
  decision_change_rate REAL,
  cases_evaluated INTEGER,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS adjustment_set_review (
  target_effect TEXT PRIMARY KEY,
  candidate_adjustment TEXT,
  blocks_confounding TEXT,
  collider_warning TEXT,
  mediator_warning TEXT,
  review_status TEXT
);

CREATE TABLE IF NOT EXISTS intervention_feasibility_review (
  intervention_name TEXT PRIMARY KEY,
  mean_estimated_effect REAL,
  mean_net_benefit REAL,
  decision_change_rate REAL,
  feasibility_status TEXT,
  review_question TEXT
);
