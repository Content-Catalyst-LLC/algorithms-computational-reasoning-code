-- Simulation as Computational Reasoning: lightweight schema for scenario outputs.

CREATE TABLE IF NOT EXISTS simulation_scenarios (
  scenario_name TEXT PRIMARY KEY,
  initial_stock REAL NOT NULL,
  growth_rate REAL NOT NULL,
  loss_rate REAL NOT NULL,
  intervention_strength REAL NOT NULL,
  shock_probability REAL NOT NULL,
  shock_size REAL NOT NULL,
  time_steps INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS simulation_outputs (
  scenario_name TEXT NOT NULL,
  time_step INTEGER NOT NULL,
  stock REAL NOT NULL,
  stochastic BOOLEAN NOT NULL,
  PRIMARY KEY (scenario_name, time_step, stochastic)
);
