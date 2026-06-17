DROP TABLE IF EXISTS software_architecture_cases;
DROP TABLE IF EXISTS architecture_dependency_edges;

CREATE TABLE software_architecture_cases (
  case_name TEXT PRIMARY KEY, problem_context TEXT, architecture_choice TEXT,
  boundary_clarity REAL, modular_cohesion REAL, dependency_control REAL, interface_discipline REAL,
  state_ownership REAL, failure_containment REAL, scalability_readiness REAL, security_boundaries REAL, observability REAL, governance_readiness REAL
);

CREATE TABLE architecture_dependency_edges (
  source TEXT NOT NULL,
  target TEXT NOT NULL,
  relationship_type TEXT NOT NULL
);

INSERT INTO software_architecture_cases VALUES
('Modular monolith with strong package boundaries','A knowledge platform keeps one deployable application while separating domain logic APIs storage reporting and workflow code','Internal modules with dependency checks explicit interfaces shared observability and architecture decision records',0.88,0.90,0.88,0.86,0.84,0.78,0.78,0.84,0.82,0.88),
('Event-driven data workflow','A data system coordinates ingestion validation feature generation reporting and archival through events','Versioned event contracts idempotent consumers event logs data lineage and dead-letter queues',0.86,0.86,0.84,0.88,0.84,0.86,0.88,0.82,0.88,0.88),
('Model scoring service','A model is deployed behind an API and used by downstream decision-support workflows','Versioned model endpoint model registry input schema validation monitoring human-review boundary and rollback policy',0.88,0.86,0.84,0.90,0.84,0.84,0.86,0.88,0.90,0.90),
('Unstructured script collection','A growing set of scripts shares files credentials global state and manual deployment steps','Minimal structure implicit dependencies inconsistent outputs and limited observability',0.52,0.58,0.50,0.48,0.46,0.44,0.42,0.46,0.44,0.40);

INSERT INTO architecture_dependency_edges VALUES
('api','domain','uses'),('domain','interfaces','depends_on_abstraction'),('infrastructure','interfaces','implements'),('worker','domain','uses'),('worker','queue','consumes'),('reporting','domain','uses'),('reporting','storage','reads'),('api','auth','checks'),('api','observability','emits'),('worker','observability','emits');
