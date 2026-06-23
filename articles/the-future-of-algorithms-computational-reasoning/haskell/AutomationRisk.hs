module Main where

automationRisk :: Double -> Double -> Double -> Double -> Double
automationRisk stakes opacity delegation irreversibility =
  max 0.0 (min 1.0 (stakes * opacity * delegation * irreversibility))

main :: IO ()
main = print (automationRisk 0.95 0.85 0.90 0.80)
