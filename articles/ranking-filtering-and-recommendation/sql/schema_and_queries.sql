-- Ranking, filtering, and recommendation synthetic audit schema.
DROP TABLE IF EXISTS ranking_cases;
CREATE TABLE ranking_cases (
  case_name TEXT PRIMARY KEY,
  system_context TEXT NOT NULL,
  ranking_goal TEXT NOT NULL,
  candidate_transparency REAL NOT NULL,
  filter_documentation REAL NOT NULL,
  signal_documentation REAL NOT NULL,
  score_traceability REAL NOT NULL,
  alternative_visibility REAL NOT NULL,
  diversity_review REAL NOT NULL,
  feedback_loop_awareness REAL NOT NULL,
  personalization_clarity REAL NOT NULL,
  fairness_review REAL NOT NULL,
  governance_review REAL NOT NULL,
  communication_clarity REAL NOT NULL
);

DROP TABLE IF EXISTS candidates;
CREATE TABLE candidates (
  candidate_id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  eligible INTEGER NOT NULL,
  text_match REAL NOT NULL,
  quality REAL NOT NULL,
  freshness REAL NOT NULL,
  diversity_bonus REAL NOT NULL,
  risk_penalty REAL NOT NULL,
  source_type TEXT NOT NULL
);

-- Transparent ranking score with explicit weights.
SELECT
  candidate_id,
  title,
  ROUND(0.36 * text_match + 0.30 * quality + 0.16 * freshness + 0.14 * diversity_bonus - 0.20 * risk_penalty, 6) AS ranking_score
FROM candidates
WHERE eligible = 1
ORDER BY ranking_score DESC;
