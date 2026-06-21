module Main where

expectedNetValue :: Double -> Double -> Double -> Double -> Double
expectedNetValue probability benefit loss cost = bounded * benefit - bounded * loss - cost
  where bounded = max 0.0 (min 1.0 probability)

main :: IO ()
main = print (expectedNetValue 0.42 150.0 80.0 25.0)
