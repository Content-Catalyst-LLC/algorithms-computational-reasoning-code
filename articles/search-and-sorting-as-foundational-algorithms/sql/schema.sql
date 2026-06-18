DROP TABLE IF EXISTS search_sorting_cases;
DROP TABLE IF EXISTS ranked_records;

CREATE TABLE search_sorting_cases (
  case_name TEXT PRIMARY KEY, problem_context TEXT, algorithmic_choice TEXT,
  search_space_clarity REAL, predicate_or_key_clarity REAL, ordering_rule_quality REAL,
  data_structure_fit REAL, complexity_awareness REAL, edge_case_coverage REAL,
  stability_or_tie_breaking REAL, traceability REAL, robustness REAL, governance_readiness REAL
);

CREATE TABLE ranked_records (
  record_id TEXT PRIMARY KEY,
  category TEXT,
  primary_score REAL,
  secondary_priority INTEGER,
  created_at TEXT
);

INSERT INTO search_sorting_cases VALUES
('Binary search over sorted records','A lookup workflow searches a sorted table of versioned records','Binary search with sortedness precondition duplicate-handling rule and traceable bounds',0.90,0.90,0.88,0.90,0.88,0.84,0.82,0.84,0.82,0.82),
('Stable multi-key sorting','A data pipeline sorts records by department date and priority','Stable sort with explicit primary and secondary keys',0.84,0.92,0.90,0.86,0.82,0.86,0.92,0.86,0.84,0.86),
('Document retrieval and ranking','A knowledge system retrieves and ranks source documents for research support','Indexed search with ranking signals source metadata freshness checks and audit logs',0.86,0.84,0.82,0.88,0.84,0.78,0.80,0.90,0.82,0.90),
('Opaque priority queue','A review queue sorts cases by an undocumented risk score','Hidden ranking function with limited tie-breaking documentation',0.66,0.48,0.42,0.72,0.70,0.46,0.34,0.40,0.44,0.36);

INSERT INTO ranked_records VALUES
('A-001','Research',92,2,'2026-06-01'),
('A-002','Research',92,1,'2026-06-02'),
('B-001','Library',88,1,'2026-06-03'),
('C-001','Platform',77,3,'2026-06-04'),
('D-001','Governance',88,2,'2026-06-05');
