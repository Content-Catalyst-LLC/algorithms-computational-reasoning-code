module Main where
linearObjective cs xs = sum (zipWith (*) cs xs)
constraintMargin limit observed = limit - observed
penaltyObjective base penalty weight = base + weight * penalty
tradeoff cost quality risk = 0.35*(1-cost) + 0.40*quality + 0.25*(1-risk)
main :: IO ()
main = putStrLn ("test_name,value\nlinear_objective," ++ show (linearObjective [4.0,2.0,1.5] [10.0,20.0,5.0]) ++ "\nconstraint_margin," ++ show (constraintMargin 100.0 86.5) ++ "\npenalty_objective," ++ show (penaltyObjective 42.0 8.0 2.5) ++ "\nnormalized_tradeoff_score," ++ show (tradeoff 0.30 0.82 0.25))
