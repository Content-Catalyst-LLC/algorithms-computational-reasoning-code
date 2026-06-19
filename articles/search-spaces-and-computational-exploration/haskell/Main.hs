module Main where
branchingStateCount b d = sum [b ^ i | i <- [0..d]]
pathCost xs = sum xs
heuristicScore g h = g + h
ratio n d = if d == 0 then 0 else n / d
main :: IO ()
main = putStrLn ("test_name,value\nbranching_state_count," ++ show (branchingStateCount 3 5) ++ "\npath_cost," ++ show (pathCost [2.5,3.0,1.25,4.75]) ++ "\nheuristic_score," ++ show (heuristicScore 8.0 5.5) ++ "\ncoverage_ratio," ++ show (ratio 850 5000) ++ "\npruning_ratio," ++ show (ratio 1200 4200))
