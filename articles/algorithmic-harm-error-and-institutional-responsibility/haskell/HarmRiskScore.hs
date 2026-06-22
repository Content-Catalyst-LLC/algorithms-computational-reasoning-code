module Main where

main :: IO ()
main = do
  let errorLikelihood = 0.34
      severity = 0.92
      exposure = 0.78
      contestability = 0.42
      harmRisk = errorLikelihood * severity * exposure * (1 - contestability)
  putStrLn ("harm_risk_score=" ++ show harmRisk)
