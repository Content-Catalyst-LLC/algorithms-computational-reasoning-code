module Main where

main :: IO ()
main = do
  let provenanceRisk = 0.66
      measurementWeakness = 0.58
      proxyRisk = 0.62
      remediation = 0.42
      historicalRisk = (provenanceRisk + measurementWeakness + proxyRisk + (1 - remediation)) / 4
  putStrLn ("historical_risk_score=" ++ show historicalRisk)
