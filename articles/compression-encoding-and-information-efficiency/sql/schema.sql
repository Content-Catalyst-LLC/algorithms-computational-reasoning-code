DROP TABLE IF EXISTS compression_encoding_cases;
DROP TABLE IF EXISTS encoding_samples;

CREATE TABLE compression_encoding_cases (
  case_name TEXT PRIMARY KEY,
  problem_context TEXT NOT NULL,
  representation_choice TEXT NOT NULL,
  fidelity_requirement REAL NOT NULL,
  encoding_clarity REAL NOT NULL,
  compression_suitability REAL NOT NULL,
  metadata_preservation REAL NOT NULL,
  interoperability REAL NOT NULL,
  integrity_checks REAL NOT NULL,
  storage_efficiency REAL NOT NULL,
  transmission_efficiency REAL NOT NULL,
  accessibility_preservation REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

CREATE TABLE encoding_samples (
  sample_id TEXT PRIMARY KEY,
  sample_text TEXT NOT NULL,
  encoding TEXT NOT NULL,
  use_case TEXT NOT NULL
);

INSERT INTO compression_encoding_cases VALUES
('Institutional archive records','Long-term records require durable storage and exact recovery','Open documented formats with lossless compression checksums schema source metadata and migration plan',0.96,0.90,0.82,0.92,0.90,0.94,0.78,0.74,0.92,0.94),
('Web media delivery','Images and media are optimized for web display and bandwidth','Purpose-specific lossy and lossless formats with alt text source retention responsive sizes and quality thresholds',0.78,0.84,0.90,0.78,0.86,0.78,0.92,0.94,0.86,0.82),
('Scientific simulation outputs','Large model outputs need storage efficiency without losing reproducibility','Typed binary or columnar formats with lossless compression units schema checksums and provenance',0.94,0.88,0.86,0.92,0.82,0.92,0.86,0.78,0.76,0.90),
('AI context packing','Documents are tokenized chunked summarized and packed into limited model context','Token-aware chunking with source links summaries retrieval metadata and loss warnings',0.82,0.82,0.84,0.86,0.78,0.72,0.80,0.82,0.80,0.86);

INSERT INTO encoding_samples VALUES
('sample-1','aaaaabbbbccccccccddddeeeeeeeee','utf-8','run_length_demo'),
('sample-2','Compression uses repeated structure','utf-8','text_entropy_demo'),
('sample-3','Metadata keeps compressed information interpretable','utf-8','governance_demo');
