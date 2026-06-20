CREATE TABLE IF NOT EXISTS payoff_profiles (
  player_one_strategy TEXT,
  player_two_strategy TEXT,
  player_one_payoff REAL,
  player_two_payoff REAL,
  total_welfare REAL,
  pure_nash_equilibrium BOOLEAN
);
CREATE TABLE IF NOT EXISTS incentive_sensitivity (
  base_reward REAL,
  manipulation_cost REAL,
  penalty REAL,
  net_gain_from_manipulation REAL,
  manipulation_attractive BOOLEAN
);
