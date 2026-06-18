module Scalability where
withinBudget :: Double -> Double -> Bool
withinBudget cost budget = cost <= budget
