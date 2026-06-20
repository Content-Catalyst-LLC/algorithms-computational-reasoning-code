-- Educational schema for authentication, authorization, and computational identity review.

CREATE TABLE IF NOT EXISTS identities (
  identity_id TEXT PRIMARY KEY,
  identity_type TEXT NOT NULL,
  owner TEXT,
  active INTEGER NOT NULL,
  last_review_days INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS permissions (
  permission_id TEXT PRIMARY KEY,
  resource TEXT NOT NULL,
  action TEXT NOT NULL,
  sensitivity TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS role_assignments (
  identity_id TEXT NOT NULL,
  role_name TEXT NOT NULL,
  permission_id TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS access_events (
  event_id TEXT PRIMARY KEY,
  identity_id TEXT NOT NULL,
  resource TEXT NOT NULL,
  action TEXT NOT NULL,
  decision TEXT NOT NULL,
  event_time TEXT NOT NULL
);

INSERT INTO identities VALUES
  ('alice', 'human', 'clinical operations', 1, 42),
  ('carol_admin', 'human', 'security', 1, 110),
  ('service_ingest', 'service', 'platform', 1, 210),
  ('legacy_export_job', 'service', 'unknown', 1, 390);

SELECT identity_id, identity_type, owner, last_review_days
FROM identities
WHERE active = 1 AND last_review_days > 90;
