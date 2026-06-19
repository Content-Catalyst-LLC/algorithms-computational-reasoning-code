module Main where
dependencyScore a v c s e = 100 * (0.22*a + 0.22*v + 0.18*c + 0.24*s + 0.14*e)
switchingCost m r t d l = m + r + t + d + l
ratio n d = if d == 0 then 0 else n / d
main :: IO ()
main = putStrLn ("test_name,value\ndependency_score," ++ show (dependencyScore 0.80 0.90 0.70 0.85 0.65) ++ "\nswitching_cost," ++ show (switchingCost 45000 120000 18000 24000 75000) ++ "\napi_dependency_ratio," ++ show (ratio 850000 1000000) ++ "\nvisibility_share," ++ show (ratio 250000 5000000))
