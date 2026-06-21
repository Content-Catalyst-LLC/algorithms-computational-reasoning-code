module Main where

riskModel :: Double -> Double -> Double -> Double -> Double -> Double
riskModel demand capacity failureRate adaptationRate noise =
  max 0.0 (min 1.0 (0.42 + 0.38*demand - 0.31*capacity + 0.27*failureRate - 0.18*adaptationRate + noise))

main :: IO ()
main = do
  let score = riskModel 0.55 0.50 0.22 0.30 0.0
  putStrLn ("risk_score=" ++ show score)
