DROP TABLE IF EXISTS execution_model_cases;
DROP TABLE IF EXISTS compiler_pipeline_taxonomy;

CREATE TABLE execution_model_cases (
  case_name TEXT PRIMARY KEY,
  problem_context TEXT NOT NULL,
  execution_model_choice TEXT NOT NULL,
  translation_clarity REAL NOT NULL,
  semantic_checking REAL NOT NULL,
  optimization_traceability REAL NOT NULL,
  runtime_visibility REAL NOT NULL,
  diagnostics_quality REAL NOT NULL,
  portability REAL NOT NULL,
  reproducibility REAL NOT NULL,
  security_boundaries REAL NOT NULL,
  performance_fit REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

CREATE TABLE compiler_pipeline_taxonomy (
  stage TEXT PRIMARY KEY,
  representation TEXT NOT NULL,
  purpose TEXT NOT NULL,
  example TEXT NOT NULL
);

INSERT INTO execution_model_cases VALUES
('Ahead-of-time systems binary','A performance-sensitive tool is compiled for a specific operating system and hardware architecture','Ahead-of-time compiler with explicit target optimization settings static analysis tests and signed release artifact',0.90,0.88,0.82,0.78,0.84,0.76,0.88,0.86,0.94,0.88),
('Bytecode virtual machine','A cross-platform service runs compiled bytecode on a managed runtime','Source compiled to bytecode and executed by a virtual machine with runtime checks profiling and managed memory',0.86,0.88,0.80,0.86,0.88,0.92,0.86,0.88,0.86,0.88),
('Interactive interpreted workflow','A research notebook supports exploratory data analysis and reproducible teaching workflows','Interpreter-driven execution with notebook logs dependency lockfile explicit runtime version and generated outputs',0.82,0.76,0.72,0.88,0.86,0.82,0.80,0.76,0.78,0.82),
('Browser transpilation pipeline','A web interface compiles and bundles typed source into browser-executable JavaScript','Typed source transpiled bundled minified source-mapped tested and deployed with artifact hashes',0.84,0.86,0.76,0.80,0.84,0.88,0.84,0.84,0.84,0.86);

INSERT INTO compiler_pipeline_taxonomy VALUES
('source_code','human-readable text','Express program intent and structure','Python or C source file'),
('lexing','tokens','Recognize vocabulary of language','identifier keyword operator literal'),
('parsing','parse tree or AST','Build syntactic structure','expression tree'),
('semantic_analysis','symbols scopes types','Check meaning beyond grammar','name resolution and type checking'),
('intermediate_representation','compiler-friendly form','Support analysis optimization and code generation','SSA or bytecode-like IR'),
('optimization','transformed IR','Improve performance while preserving meaning','inlining or dead-code elimination'),
('code_generation','target code','Produce executable or lower-level representation','machine code bytecode or JS bundle'),
('linking','artifact graph','Resolve external symbols and libraries','shared library linkage'),
('loading','runtime image','Prepare program for execution','process image in memory'),
('execution','runtime state','Run instructions and effects','stack heap I/O scheduler');
