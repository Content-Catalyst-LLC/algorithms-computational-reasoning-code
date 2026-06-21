CREATE TABLE IF NOT EXISTS prior_scenarios (scenario TEXT PRIMARY KEY, alpha REAL NOT NULL, beta REAL NOT NULL, rationale TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS evidence_batches (batch_id INTEGER PRIMARY KEY, observations INTEGER NOT NULL, successes INTEGER NOT NULL, evidence_note TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS posterior_summaries (scenario TEXT NOT NULL, stage TEXT NOT NULL, alpha REAL NOT NULL, beta REAL NOT NULL, posterior_mean REAL NOT NULL, p05 REAL NOT NULL, posterior_median REAL NOT NULL, p95 REAL NOT NULL, threshold REAL NOT NULL, probability_above_threshold REAL NOT NULL, PRIMARY KEY (scenario, stage));
CREATE TABLE IF NOT EXISTS bayesian_review_checklist (check_name TEXT PRIMARY KEY, status TEXT NOT NULL, question TEXT NOT NULL);
