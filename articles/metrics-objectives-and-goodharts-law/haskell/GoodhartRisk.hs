module Main where

main :: IO ()
main = do
  let proxyGap = 0.38
      pressure = 0.88
      gaming = 0.72
      guardrailPenalty = 1.0
      score = (proxyGap + pressure + gaming + guardrailPenalty) / 4
  putStrLn ("goodhart_risk_score=" ++ show score)
