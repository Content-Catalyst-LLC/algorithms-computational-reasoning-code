DROP TABLE IF EXISTS automated_reasoning_cases;

CREATE TABLE automated_reasoning_cases (
  case_name TEXT PRIMARY KEY,
  reasoning_context TEXT NOT NULL,
  inference_claim TEXT NOT NULL,
  formalization_clarity REAL NOT NULL,
  premise_quality REAL NOT NULL,
  rule_soundness REAL NOT NULL,
  inference_traceability REAL NOT NULL,
  proof_or_model_evidence REAL NOT NULL,
  satisfiability_handling REAL NOT NULL,
  counterexample_handling REAL NOT NULL,
  unknown_status_handling REAL NOT NULL,
  human_review_pathway REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

INSERT INTO automated_reasoning_cases VALUES
('SAT solver workflow','Boolean satisfiability solver checks whether formal constraints can be jointly true','The solver reports satisfiable unsatisfiable or bounded unknown for encoded constraints',0.86,0.80,0.86,0.78,0.82,0.90,0.78,0.74,0.70,0.74),
('Model checking workflow','State-space model checker verifies safety properties for a formal system model','The checker verifies modeled safety properties or returns counterexample traces',0.82,0.78,0.84,0.84,0.86,0.76,0.88,0.76,0.78,0.82),
('Institutional rule engine','Rule engine applies documented policy rules to structured case facts','The system classifies clear in-scope cases and routes ambiguous cases for review',0.78,0.74,0.76,0.86,0.70,0.66,0.72,0.84,0.88,0.88),
('AI-assisted theorem proving','AI suggests proof steps while a formal checker validates accepted proof objects','AI proposes candidate steps but the proof assistant determines formal validity',0.80,0.76,0.88,0.78,0.86,0.70,0.74,0.76,0.84,0.82);
