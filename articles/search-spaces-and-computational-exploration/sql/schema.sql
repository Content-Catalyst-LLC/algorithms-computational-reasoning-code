DROP TABLE IF EXISTS search_cases;
CREATE TABLE search_cases (case_name TEXT PRIMARY KEY,state_clarity REAL,transition_clarity REAL,goal_definition REAL,constraint_documentation REAL,heuristic_transparency REAL,pruning_discipline REAL,frontier_discipline REAL,coverage_reporting REAL,stopping_clarity REAL,traceability REAL,governance_review REAL,communication_clarity REAL);
DROP TABLE IF EXISTS search_metrics;
CREATE TABLE search_metrics (case_name TEXT PRIMARY KEY,branching_factor INTEGER,depth INTEGER,path_cost REAL,known_cost REAL,estimated_remaining_cost REAL,explored_states REAL,reachable_states REAL,pruned_states REAL,generated_states REAL);
INSERT INTO search_cases VALUES
('Graph pathfinding audit',0.88,0.86,0.84,0.82,0.78,0.80,0.86,0.76,0.82,0.84,0.76,0.78),
('Shift scheduling exploration',0.82,0.80,0.84,0.86,0.72,0.78,0.76,0.70,0.76,0.80,0.82,0.78),
('AI retrieval candidate search',0.74,0.70,0.76,0.68,0.56,0.62,0.70,0.54,0.62,0.66,0.70,0.68),
('Opaque eligibility search',0.42,0.38,0.52,0.30,0.22,0.28,0.36,0.18,0.32,0.24,0.26,0.34);
INSERT INTO search_metrics VALUES
('small_tree',3,5,11.5,8.0,5.5,850,5000,1200,4200),
('wide_tree',5,4,8.0,6.0,7.0,1200,10000,3600,9000),
('deep_tree',2,10,5.0,4.0,6.0,1500,4096,900,3000),
('retrieval_space',8,3,2.5,2.0,1.4,400,12000,3200,8000);
