-- Hash verification schema for artifact integrity and provenance records.
CREATE TABLE IF NOT EXISTS hash_manifest (
  artifact_id TEXT PRIMARY KEY,
  file_name TEXT NOT NULL,
  hash_algorithm TEXT NOT NULL,
  digest TEXT NOT NULL,
  reference_source TEXT NOT NULL,
  signed_manifest BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS hash_verification_event (
  event_id TEXT PRIMARY KEY,
  artifact_id TEXT NOT NULL,
  current_digest TEXT NOT NULL,
  verified BOOLEAN NOT NULL,
  checked_at TEXT NOT NULL,
  checker TEXT NOT NULL,
  FOREIGN KEY (artifact_id) REFERENCES hash_manifest(artifact_id)
);

INSERT INTO hash_manifest VALUES
('artifact-001', 'analysis_report.csv', 'sha256', 'demo-reference-digest', 'signed release manifest', TRUE, '2026-06-20T00:00:00Z');
