module Metaheuristics where
acceptanceProbability :: Double -> Double -> Double
acceptanceProbability delta temperature = exp ((-delta) / temperature)
