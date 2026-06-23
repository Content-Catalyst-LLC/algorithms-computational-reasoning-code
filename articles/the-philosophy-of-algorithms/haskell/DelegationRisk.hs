module Main where

delegationRisk :: Double -> Double -> Double -> Double
delegationRisk severity automation opacity = max 0.0 (min 1.0 (severity * automation * opacity))

main :: IO ()
main = print (delegationRisk 0.95 0.95 0.80)
