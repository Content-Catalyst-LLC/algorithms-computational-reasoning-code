DROP TABLE IF EXISTS algorithmic_literacy_cases;
DROP TABLE IF EXISTS algorithmic_literacy_governance_notes;

CREATE TABLE algorithmic_literacy_cases (
  case_name TEXT PRIMARY KEY,
  system_context TEXT NOT NULL,
  user_group TEXT NOT NULL,
  procedural_transparency REAL NOT NULL,
  data_visibility REAL NOT NULL,
  output_interpretability REAL NOT NULL,
  uncertainty_communication REAL NOT NULL,
  contestability REAL NOT NULL,
  governance_readiness REAL NOT NULL,
  impact_awareness REAL NOT NULL,
  human_judgment_support REAL NOT NULL
);

INSERT INTO algorithmic_literacy_cases VALUES
('Search ranking','Ranked information retrieval system','general public',0.62,0.54,0.66,0.40,0.38,0.52,0.70,0.68),
('Public decision-support workflow','Eligibility or prioritization tool used in an institutional setting','affected public and case reviewers',0.58,0.62,0.56,0.48,0.70,0.76,0.82,0.74),
('Scientific simulation dashboard','Scenario model used to compare possible system futures','researchers policy analysts and educators',0.76,0.72,0.74,0.78,0.60,0.68,0.70,0.80),
('Recommendation feed','Personalized content ranking and recommendation system','platform users',0.40,0.42,0.48,0.30,0.32,0.46,0.66,0.50);

CREATE TABLE algorithmic_literacy_governance_notes (
  note_key TEXT PRIMARY KEY,
  note_text TEXT NOT NULL
);

INSERT INTO algorithmic_literacy_governance_notes VALUES
('problem','Name the problem being formalized.'),
('inputs','Identify data signals rules and parameters.'),
('outputs','Explain scores labels rankings forecasts or recommendations.'),
('optimization','Name what the system optimizes rewards or suppresses.'),
('contestability','Provide correction appeal review or escalation paths where consequences matter.'),
('judgment','Keep human judgment active when stakes uncertainty or values require it.');
