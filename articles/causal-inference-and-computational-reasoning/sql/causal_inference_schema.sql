CREATE TABLE IF NOT EXISTS causal_effect_estimates (
  estimate_type TEXT PRIMARY KEY,
  estimated_effect REAL NOT NULL,
  identification_warning TEXT
);

CREATE TABLE IF NOT EXISTS causal_assumption_register (
  assumption TEXT PRIMARY KEY,
  description TEXT NOT NULL,
  review_question TEXT NOT NULL,
  status TEXT NOT NULL CHECK (status IN ('complete', 'partial', 'needs_review'))
);

CREATE TABLE IF NOT EXISTS covariate_balance_diagnostics (
  covariate TEXT PRIMARY KEY,
  treated_mean REAL,
  control_mean REAL,
  standardized_difference REAL,
  absolute_standardized_difference REAL,
  review_flag TEXT
);

CREATE TABLE IF NOT EXISTS causal_review_decisions (
  review_id INTEGER PRIMARY KEY,
  article_slug TEXT NOT NULL,
  causal_claim TEXT NOT NULL,
  evidence_status TEXT NOT NULL,
  decision_boundary TEXT NOT NULL,
  reviewer_note TEXT
);
