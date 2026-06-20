CREATE TABLE classification_cases (
  case_id TEXT PRIMARY KEY,
  score REAL NOT NULL,
  actual INTEGER NOT NULL,
  group_id TEXT,
  notes TEXT
);

CREATE TABLE threshold_metrics (
  threshold REAL NOT NULL,
  true_positive INTEGER NOT NULL,
  false_positive INTEGER NOT NULL,
  true_negative INTEGER NOT NULL,
  false_negative INTEGER NOT NULL,
  precision REAL,
  recall REAL,
  specificity REAL
);
