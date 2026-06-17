DROP TABLE IF EXISTS halting_boundary_cases;

CREATE TABLE halting_boundary_cases (
  case_name TEXT PRIMARY KEY,
  automation_context TEXT NOT NULL,
  automation_claim TEXT NOT NULL,
  program_scope_clarity REAL NOT NULL,
  termination_claim_clarity REAL NOT NULL,
  undecidability_awareness REAL NOT NULL,
  bounded_analysis_honesty REAL NOT NULL,
  unknown_status_handling REAL NOT NULL,
  timeout_policy REAL NOT NULL,
  false_certainty_risk_control REAL NOT NULL,
  human_review_pathway REAL NOT NULL,
  traceability REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

INSERT INTO halting_boundary_cases VALUES
('Static analyzer','Tool checks source code for selected error classes','Analyzer detects scoped patterns and reports unknown status when analysis is incomplete',0.86,0.78,0.80,0.84,0.82,0.76,0.80,0.74,0.80,0.76),
('AI code review assistant','Generative model explains code and suggests possible issues','Assistant supports review but does not decide arbitrary termination or correctness',0.66,0.62,0.58,0.68,0.60,0.64,0.62,0.78,0.60,0.72),
('Formal verification workflow','Verifier checks specified properties under formal assumptions','Workflow proves bounded or specified properties not universal behavior of all programs',0.82,0.80,0.84,0.82,0.78,0.72,0.80,0.80,0.84,0.82),
('Institutional automation workflow','Rule engine routes cases through automated checks and human review','Clear cases are automated while ambiguous or unresolved cases are escalated',0.80,0.76,0.64,0.78,0.84,0.82,0.78,0.88,0.86,0.88);
