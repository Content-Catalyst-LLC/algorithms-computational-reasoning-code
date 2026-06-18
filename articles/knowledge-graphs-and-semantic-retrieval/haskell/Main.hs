module Main where
hybridScore :: Double -> Double -> Double -> Double -> Double
hybridScore l v g p = 100 * (0.25*l + 0.25*v + 0.25*g + 0.25*p)
pathScore :: Double -> Double -> Double -> Double -> Double
pathScore pathLength confidence provenance review =
  100 * (0.25 * (1 / (1 + max (pathLength - 1) 0)) + 0.30*confidence + 0.30*provenance + 0.15*review)
main :: IO ()
main = putStrLn ("test_name,value\nhybrid_score," ++ show (hybridScore 0.82 0.78 0.88 0.90) ++ "\ngraph_path_score," ++ show (pathScore 3 0.90 0.92 0.95))
