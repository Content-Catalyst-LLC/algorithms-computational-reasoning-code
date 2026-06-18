module Tractability where
withinBudget :: Integer -> Integer -> Bool
withinBudget cost budget = cost <= budget
