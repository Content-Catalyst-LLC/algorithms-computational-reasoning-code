module Heuristics where
relativeImprovement :: Double -> Double -> Double
relativeImprovement baseline heuristic = (baseline - heuristic) / baseline
