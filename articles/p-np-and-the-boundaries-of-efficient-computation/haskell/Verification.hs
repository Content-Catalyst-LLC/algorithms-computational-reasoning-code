module Verification where
withinBudget :: Integer -> Integer -> Bool
withinBudget cost budget = cost <= budget
