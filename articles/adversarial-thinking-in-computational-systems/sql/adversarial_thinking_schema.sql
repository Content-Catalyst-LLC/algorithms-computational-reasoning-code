-- Schema for adversarial thinking review records.

CREATE TABLE adversarial_case (
    case_id INTEGER PRIMARY KEY,
    case_name TEXT NOT NULL,
    system_context TEXT NOT NULL,
    primary_adversary TEXT NOT NULL,
    threat_model_clarity REAL NOT NULL,
    attack_surface_mapping REAL NOT NULL,
    trust_boundary_review REAL NOT NULL,
    abuse_case_coverage REAL NOT NULL,
    monitoring_detection REAL NOT NULL,
    defense_in_depth REAL NOT NULL,
    incident_response REAL NOT NULL,
    governance_ownership REAL NOT NULL
);

CREATE TABLE attack_surface (
    surface_id INTEGER PRIMARY KEY,
    surface_name TEXT NOT NULL,
    possible_attack TEXT NOT NULL,
    control TEXT NOT NULL,
    risk_level TEXT NOT NULL
);

CREATE TABLE threshold_evasion_test (
    test_id INTEGER PRIMARY KEY,
    case_id TEXT NOT NULL,
    original_score REAL NOT NULL,
    shifted_score REAL NOT NULL,
    threshold REAL NOT NULL,
    evasion_success INTEGER NOT NULL
);
