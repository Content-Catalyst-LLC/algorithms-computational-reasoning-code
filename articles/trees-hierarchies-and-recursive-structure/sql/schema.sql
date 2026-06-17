DROP TABLE IF EXISTS tree_structure_cases;

CREATE TABLE tree_structure_cases (
  case_name TEXT PRIMARY KEY,
  problem_context TEXT NOT NULL,
  tree_structure_choice TEXT NOT NULL,
  hierarchy_fit REAL NOT NULL,
  recursive_clarity REAL NOT NULL,
  invariant_documentation REAL NOT NULL,
  traversal_support REAL NOT NULL,
  balance_awareness REAL NOT NULL,
  path_interpretability REAL NOT NULL,
  relationship_loss_control REAL NOT NULL,
  complexity_awareness REAL NOT NULL,
  representation_risk_documentation REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

INSERT INTO tree_structure_cases VALUES
('Document outline tree','A long article is represented through sections subsections and nested arguments','Rooted document tree with headings anchors path metadata and cross-link notes',0.86,0.84,0.78,0.86,0.76,0.88,0.74,0.76,0.80,0.82),
('Syntax tree','A programming expression is parsed into nested operators and operands','Abstract syntax tree with typed nodes traversal rules and evaluation semantics',0.92,0.92,0.86,0.90,0.72,0.84,0.82,0.84,0.78,0.80),
('Decision classification tree','Cases are routed through conditions toward review approval denial or escalation','Decision tree with condition metadata path explanations uncertainty routing and audit logs',0.78,0.78,0.82,0.84,0.76,0.90,0.70,0.76,0.90,0.90),
('Database B-tree index','Records must support ordered lookup range queries insertion and deletion at scale','Balanced B-tree index with order invariants block-aware layout and maintenance logs',0.88,0.84,0.88,0.86,0.92,0.76,0.80,0.90,0.78,0.82);
