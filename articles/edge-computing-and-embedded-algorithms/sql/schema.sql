DROP TABLE IF EXISTS edge_cases;
CREATE TABLE edge_cases (
  case_name TEXT PRIMARY KEY,
  latency_discipline REAL,
  power_awareness REAL,
  memory_awareness REAL,
  sensor_validation REAL,
  offline_behavior REAL,
  update_safety REAL,
  security_design REAL,
  observability REAL,
  fail_safe_design REAL,
  data_minimization REAL,
  governance_review REAL
);

DROP TABLE IF EXISTS edge_timing_power;
CREATE TABLE edge_timing_power (
  case_name TEXT PRIMARY KEY,
  sense_ms REAL,
  filter_ms REAL,
  compute_ms REAL,
  actuate_ms REAL,
  deadline_ms REAL,
  uplink_ms REAL,
  cloud_compute_ms REAL,
  downlink_ms REAL,
  battery_wh REAL,
  average_power_w REAL,
  signal_value REAL,
  threshold REAL
);

INSERT INTO edge_cases VALUES
('Environmental sensor node',0.74,0.86,0.78,0.82,0.84,0.70,0.72,0.76,0.78,0.86,0.76),
('Industrial vibration monitor',0.82,0.74,0.76,0.84,0.78,0.74,0.76,0.80,0.82,0.72,0.78),
('Medical wearable signal filter',0.86,0.82,0.78,0.86,0.80,0.82,0.84,0.78,0.86,0.88,0.84),
('Unreviewed smart controller',0.58,0.52,0.62,0.28,0.34,0.22,0.24,0.26,0.20,0.48,0.18);

INSERT INTO edge_timing_power VALUES
('environmental_sensor',8,6,14,5,50,90,60,90,12,0.08,0.82,0.75),
('industrial_vibration',4,8,18,6,45,65,80,65,24,0.65,0.68,0.70),
('medical_wearable',3,7,16,4,35,80,75,80,4.8,0.06,0.91,0.86),
('traffic_signal',5,6,20,8,60,55,70,55,120,7.5,0.74,0.80),
('smart_controller',10,4,8,7,40,100,50,100,8,0.20,0.60,0.55);
