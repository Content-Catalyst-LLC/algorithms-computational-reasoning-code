module Main where

rankingScore :: Double -> Double -> Double -> Double -> Double -> Double
rankingScore textMatch quality freshness diversityBonus riskPenalty =
  0.36 * textMatch + 0.30 * quality + 0.16 * freshness + 0.14 * diversityBonus - 0.20 * riskPenalty

main :: IO ()
main = print (rankingScore 0.92 0.88 0.60 0.35 0.04)
