DROP TABLE IF EXISTS boundary_state_cases;
DROP TABLE IF EXISTS boundary_governance_notes;

CREATE TABLE boundary_state_cases (
  case_name TEXT PRIMARY KEY,
  procedure_type TEXT NOT NULL,
  input_description TEXT NOT NULL,
  output_description TEXT NOT NULL,
  state_description TEXT NOT NULL,
  stopping_condition TEXT NOT NULL,
  input_clarity REAL NOT NULL,
  output_clarity REAL NOT NULL,
  state_definition REAL NOT NULL,
  transition_clarity REAL NOT NULL,
  stopping_condition_clarity REAL NOT NULL,
  validation_quality REAL NOT NULL,
  edge_case_handling REAL NOT NULL,
  failure_reporting REAL NOT NULL,
  interpretability REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

INSERT INTO boundary_state_cases VALUES
('Graph traversal','stateful search','Graph starting node optional target node','Path visited set or no-solution result','Current node frontier visited nodes path history','Target found frontier exhausted or limit reached',0.84,0.80,0.86,0.82,0.80,0.76,0.74,0.70,0.72,0.58),
('Decision-support workflow','institutional workflow','Case record evidence fields policy rules review notes','Recommendation escalation decision or appeal path','Submitted under review approved denied appealed closed','Decision made appeal opened or human review required',0.68,0.70,0.74,0.66,0.62,0.66,0.58,0.60,0.64,0.78),
('Numerical simulation','iterative model','Initial conditions parameters time horizon transition equations','Time series scenario comparison summary metrics','Current time step and model-variable values','Time horizon reached convergence reached or invalid state detected',0.82,0.78,0.84,0.80,0.78,0.74,0.70,0.66,0.70,0.68),
('Recommendation ranking','ranking system','User context item catalog interaction history ranking model','Ranked list of recommended items','Session state user profile item scores feedback history','Enough candidates ranked time budget reached or confidence threshold met',0.74,0.72,0.70,0.64,0.60,0.66,0.58,0.52,0.54,0.56);

CREATE TABLE boundary_governance_notes (
  note_key TEXT PRIMARY KEY,
  note_text TEXT NOT NULL
);

INSERT INTO boundary_governance_notes VALUES
('inputs','Define accepted inputs rejected inputs source units type and validity rules.'),
('outputs','Define output meaning uncertainty confidence and interpretation limits.'),
('states','Define valid states invalid states history and memory requirements.'),
('transitions','Define allowed and forbidden state transitions.'),
('stopping','Define halting no-solution escalation and handoff behavior.'),
('failure','Return explicit errors warnings or review requests when completion is not responsible.');
