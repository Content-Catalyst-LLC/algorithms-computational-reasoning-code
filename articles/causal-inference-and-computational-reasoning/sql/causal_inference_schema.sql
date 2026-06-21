CREATE TABLE IF NOT EXISTS causal_effect_estimates (
  estimate_type TEXT PRIMARY KEY,
  estimated_effect REAL,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS causal_assumption_register (
  assumption TEXT PRIMARY KEY,
  description TEXT,
  review_question TEXT,
  status TEXT
);

CREATE TABLE IF NOT EXISTS causal_balance_diagnostics (
  covariate TEXT PRIMARY KEY,
  treated_mean REAL,
  control_mean REAL,
  standardized_difference REAL,
  absolute_standardized_difference REAL,
  interpretation TEXT
);
