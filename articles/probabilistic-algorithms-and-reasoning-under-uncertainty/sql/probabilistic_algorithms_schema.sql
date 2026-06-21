-- SQL schema for probabilistic algorithm audit outputs.
CREATE TABLE IF NOT EXISTS probabilistic_sampling_trials (
  experiment_name TEXT,
  sample_size INTEGER,
  batch INTEGER,
  seed INTEGER,
  true_probability REAL,
  estimate REAL,
  standard_error REAL,
  interval_lower REAL,
  interval_upper REAL,
  threshold REAL,
  decision INTEGER,
  absolute_error REAL,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS expected_loss_decisions (
  event_probability REAL,
  loss_false_positive REAL,
  loss_false_negative REAL,
  expected_loss_if_act REAL,
  expected_loss_if_do_not_act REAL,
  choose_action INTEGER,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS probability_review_checklist (
  check_name TEXT PRIMARY KEY,
  status TEXT,
  question TEXT
);
