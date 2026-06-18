module Main where
relativeImprovement :: Double -> Double -> Double
relativeImprovement baseline heuristic = (baseline - heuristic) / baseline
main :: IO ()
main = putStrLn ("test_name,value\nroute_improvement," ++ show (relativeImprovement 34 27) ++ "\nannealing_improvement," ++ show (relativeImprovement 18.5 12.2))
