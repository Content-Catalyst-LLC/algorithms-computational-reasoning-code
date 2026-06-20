-- Algorithmic trust, verification, and security teaching schema.

CREATE TABLE IF NOT EXISTS trust_cases (
  case_id INTEGER PRIMARY KEY,
  case_name TEXT NOT NULL,
  trust_claim TEXT NOT NULL,
  verification_score REAL NOT NULL,
  validation_score REAL NOT NULL,
  security_score REAL NOT NULL,
  provenance_score REAL NOT NULL,
  monitoring_score REAL NOT NULL,
  governance_score REAL NOT NULL
);

INSERT INTO trust_cases VALUES
  (1, 'Signed release and model registry', 'deployed artifact matches reviewed version', 0.88, 0.82, 0.88, 0.90, 0.84, 0.82),
  (2, 'Public eligibility decision support', 'consistent triage with appeal and review', 0.74, 0.76, 0.70, 0.78, 0.70, 0.76),
  (3, 'Research computation pipeline', 'outputs can be reconstructed', 0.76, 0.72, 0.62, 0.88, 0.60, 0.66);

SELECT
  case_name,
  ROUND(100 * (0.18 * verification_score + 0.18 * validation_score + 0.18 * security_score + 0.16 * provenance_score + 0.15 * monitoring_score + 0.15 * governance_score), 3) AS trust_quality_score
FROM trust_cases;
