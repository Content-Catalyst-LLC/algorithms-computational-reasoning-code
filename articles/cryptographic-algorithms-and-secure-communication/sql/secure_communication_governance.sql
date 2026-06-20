-- Educational schema for cryptographic algorithms and secure communication governance.
-- This is not production security infrastructure.

CREATE TABLE IF NOT EXISTS secure_communication_case (
  case_id INTEGER PRIMARY KEY,
  case_name TEXT NOT NULL,
  system_context TEXT NOT NULL,
  security_goal TEXT NOT NULL,
  threat_model_clarity REAL NOT NULL,
  key_management REAL NOT NULL,
  certificate_validation REAL NOT NULL,
  message_integrity REAL NOT NULL,
  authentication_design REAL NOT NULL,
  implementation_review REAL NOT NULL,
  governance_reviewed INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS cryptographic_asset_inventory (
  asset_id INTEGER PRIMARY KEY,
  asset_name TEXT NOT NULL,
  asset_type TEXT NOT NULL,
  security_property TEXT NOT NULL,
  key_owner TEXT,
  rotation_required INTEGER NOT NULL DEFAULT 1,
  revocation_path_documented INTEGER NOT NULL DEFAULT 0
);
