module Main where

main :: IO ()
main = do
  let likelihood = 0.42
      severity = 0.86
      detectability = 0.38
      controllability = 0.44
      failureRisk = likelihood * severity * (1 - detectability) * (1 - controllability)
  putStrLn ("failure_risk_score=" ++ show failureRisk)
